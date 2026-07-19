#!/usr/bin/env python3
"""
propagate_footer.py
===================

Propagates the restyled <footer> + FOOTER RESTYLE CSS from ``index.html`` to
all 17 sibling HTML pages in this directory.

Re-runnable / idempotent: pages already containing ``footer-tagline`` (the
new footer marker that appears in BOTH the CSS rule and the HTML class)
are treated as already-updated and skipped.

Safety guards added after the first run, per code-review feedback
(Nit Pick Nick):

    Before splicing any destination page, this script asserts:

      * The page contains EXACTLY ONE ``<footer`` opening tag (i.e.
        ``content.count('<footer') == 1``). If a Webflow re-export
        later adds nested ``<footer``-shaped markup (in a comment,
        script string, or SVG, for example), the script logs a
        WARNING and SKIPS the page rather than corrupting the splice.
      * The page's existing ``<footer>...</footer>`` block is bounded
        in size (default 50 KB). Pathological content triggers a skip.

    On the source side, ``index.html`` must also contain EXACTLY ONE
    ``<footer`` opening tag (otherwise extraction aborts entirely).

    A naive substring count is used intentionally — over-counting
    (because of comments/strings containing ``<footer``) is what we
    WANT: it makes the script fail safe.

Usage
-----

From the project directory (where index.html + the 17 sibling pages live)::

    # preview what would change without writing anything
    python propagate_footer.py --dry-run

    # apply (skipping pages already propagated)
    python propagate_footer.py

    # re-propagate even on already-propagated pages, after updating the
    # footer in index.html and wanting to push the new version everywhere
    python propagate_footer.py --force

    # limit to a specific page (debugging)
    python propagate_footer.py --pages about.html
"""

from __future__ import annotations

import argparse
import os
import sys


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE = os.path.dirname(os.path.abspath(__file__))
SOURCE_FILE = 'index.html'

# Marker for the new footer. Appears in:
#   * the CSS rule  (`.footer-tagline { ... }`)
#   * the HTML class (`<p class="footer-tagline">…</p>`)
# Both must be present in a fully-propagated page.
FOOTER_MARKER = 'footer-tagline'

# Comment at the top of the FOOTER RESTYLE CSS block.
STYLE_MARKER = 'FOOTER RESTYLE'

# Default destinations — skip index.html (source) and any other artifact.
DEFAULT_PAGES = [
    'about.html',
    'blog.html',
    'campaign.html',
    'contact.html',
    'copy.html',
    'donation.html',
    'feed.html',
    'home-2.html',
    'issues.html',
    'license.html',
    'login.html',
    'manifesto.html',
    'party-members.html',
    'press-conference.html',
    'register.html',
    'tweets.html',
    'volunteer.html',
    'projects.html',
    'events.html',
    'budget.html',
]

# Safety bound — if the splice slice is larger than this, we assume
# extraction went wrong (e.g. matched too much) and skip the page.
MAX_FOOTER_BYTES = 50_000


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _read(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def _write_atomic(path: str, content: str) -> None:
    """Write content to *path* via a sibling tempfile + os.replace.

    Makes the write atomic on the same filesystem, so a crash mid-write
    can't leave the destination file half-truncated.
    """
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        f.write(content)
    os.replace(tmp, path)


def _count_open_footer_tags(content: str) -> int:
    """Naive count of ``<footer`` occurrences.

    Intentionally counts every occurrence, including ones inside HTML
    comments, JavaScript string literals, or SVG. Over-counting is the
    safe failure mode for our safety guard — we'd rather skip a page
    than corrupt it.
    """
    return content.count('<footer')


def extract_blocks(src: str, source_label: str) -> tuple[str, str]:
    """Extract (footer_css, footer_html) from the source page.

    Aborts with ``ValueError`` if invariants don't hold — most importantly,
    if the source has != 1 ``<footer`` opening tag (catches re-exported
    index.html with duplicate footer markup).
    """
    open_count = _count_open_footer_tags(src)
    if open_count != 1:
        raise ValueError(
            f'source {source_label!r} has {open_count} <footer opening tags; '
            f'expected exactly 1. Refusing to extract a malformed footer slice. '
            f'Inspect {source_label} manually.'
        )
    if STYLE_MARKER not in src:
        raise ValueError(
            f'source {source_label!r} does not contain the {STYLE_MARKER!r} '
            f'comment. Has the CSS block been renamed?'
        )

    # Extract FOOTER RESTYLE CSS block: from the marker comment to the
    # last `}` before this source's </style> tag.
    style_start = src.index(STYLE_MARKER)
    style_end = src.index('</style>', style_start)
    last_brace = src.rfind('}', style_start, style_end)
    if last_brace == -1:
        raise ValueError(
            f'no closing }} for {STYLE_MARKER!r} CSS block in {source_label}'
        )
    footer_css = src[style_start:last_brace + 1]

    # Extract footer HTML block: <footer…>…</footer>, inclusive.
    f_start = src.index('<footer')
    f_end = src.index('</footer>', f_start) + len('</footer>')
    footer_html = src[f_start:f_end]

    if len(footer_html) > MAX_FOOTER_BYTES:
        raise ValueError(
            f'extracted footer HTML from {source_label!r} is '
            f'{len(footer_html)} bytes (>{MAX_FOOTER_BYTES}). Refusing to '
            f'propagate an oversized slice.'
        )

    return footer_css, footer_html


def is_already_propagated(content: str) -> bool:
    """A page is "already propagated" iff it has BOTH the new CSS marker
    class and the FOOTER RESTYLE CSS comment. Checking both avoids false
    positives where one shows up in a stray comment but the other doesn't.
    """
    return FOOTER_MARKER in content and STYLE_MARKER in content


def propagate_one(
    page_path: str,
    footer_css: str,
    footer_html: str,
    *,
    force: bool,
    dry_run: bool,
) -> tuple[str, str]:
    """Apply both edits to a single page.

    Returns ``(status, message)`` where status is one of
    ``'updated'``, ``'skipped'``, ``'error'``.

    SAFETY CONTRACT (reviewer-flagged): refuses to splice when
    ``count('<footer') != 1`` so future re-exports with nested footer
    markup cannot silently corrupt the document.
    """
    if not os.path.exists(page_path):
        return ('error', f'file does not exist: {page_path}')

    content = _read(page_path)

    if is_already_propagated(content) and not force:
        return ('skipped', 'already propagated (use --force to override)')

    # -- Hardened assertion (the reviewer-flagged guard) -----------------
    open_count = _count_open_footer_tags(content)
    if open_count != 1:
        return (
            'error',
            f'has {open_count} <footer opening tags (expected 1); '
            f'refusing to splice (likely Webflow re-export added nested '
            f'footer markup). Inspect manually.'
        )
    # -------------------------------------------------------------------

    # Inject the FOOTER RESTYLE <style> block immediately before </head>.
    if '</head>' not in content:
        return ('error', 'no </head> tag found')

    style_block = '\n    <style>\n' + footer_css + '\n    </style>\n'
    new_content = content.replace('</head>', style_block + '\n</head>', 1)

    # Splice the footer block: first <footer -> first </footer> after it.
    pf_start = new_content.index('<footer')
    pf_end = new_content.index('</footer>', pf_start) + len('</footer>')
    existing_footer = new_content[pf_start:pf_end]
    if len(existing_footer) > MAX_FOOTER_BYTES:
        return (
            'error',
            f'existing footer block is {len(existing_footer)} bytes '
            f'(>{MAX_FOOTER_BYTES}); refusing to splice an oversized block.'
        )

    new_content = new_content[:pf_start] + footer_html + new_content[pf_end:]

    if dry_run:
        delta = len(new_content) - len(content)
        return ('updated', f'dry-run: would change {len(content)} -> {len(new_content)} bytes (+{delta})')

    _write_atomic(page_path, new_content)
    delta = len(new_content) - len(content)
    return ('updated', f'{len(content)} -> {len(new_content)} bytes (+{delta})')


def verify(page_paths: list[str]) -> bool:
    """Per-page structural checks post-propagation. Logs OK / FAIL rows.

    Returns True iff every page passes every check.
    """
    print()
    print('=== Verification ===')
    all_ok = True
    for page_name in page_paths:
        path = os.path.join(BASE, page_name)
        if not os.path.exists(path):
            print(f'  MISSING: {page_name}')
            all_ok = False
            continue
        c = _read(path)
        n_open = _count_open_footer_tags(c)
        n_close = c.count('</footer>')
        issues = []
        if n_open != 1:
            issues.append(f'<footer count={n_open} (expect 1)')
        if n_close != 1:
            issues.append(f'</footer> count={n_close} (expect 1)')
        if FOOTER_MARKER not in c:
            issues.append(f'missing {FOOTER_MARKER}')
        if STYLE_MARKER not in c:
            issues.append(f'missing {STYLE_MARKER}')
        if c.count('class="footer-inner"') != 1:
            issues.append('footer-inner != 1')
        if c.count('class="footer-bottom"') != 1:
            issues.append('footer-bottom != 1')
        if issues:
            print(f'  FAIL    {page_name}: ' + '; '.join(issues))
            all_ok = False
        else:
            print(f'  OK      {page_name}')
    return all_ok


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='preview changes without writing to files',
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='re-propagate even on already-propagated pages '
             '(use after updating the footer in index.html)',
    )
    parser.add_argument(
        '--pages',
        nargs='*',
        default=None,
        help='limit to specific page filenames (default: all 17)',
    )
    parser.add_argument(
        '--skip-verify',
        action='store_true',
        help='skip the post-propagation structural verification sweep',
    )
    args = parser.parse_args(argv)

    pages = args.pages if args.pages else DEFAULT_PAGES
    source_path = os.path.join(BASE, SOURCE_FILE)
    if not os.path.exists(source_path):
        print(f'FATAL: {SOURCE_FILE} not found in {BASE}', file=sys.stderr)
        return 1

    src = _read(source_path)

    print('### propagate_footer.py ###')
    print(f'  base       : {BASE}')
    print(f'  source     : {SOURCE_FILE} ({len(src)} bytes)')
    print(f'  pages      : {len(pages)} ({"subset" if args.pages else "default 17"})')
    print(f'  mode       : {"dry-run" if args.dry_run else "apply"}'
          f'{" + force" if args.force else ""}')
    print()

    # 1) Extract (with source-side invariants).
    try:
        footer_css, footer_html = extract_blocks(src, SOURCE_FILE)
    except ValueError as exc:
        print(f'FATAL: {exc}', file=sys.stderr)
        return 1

    print(f'  footer CSS : {len(footer_css)} chars  '
          f'({footer_css.count("#6fa8dc")} x #6fa8dc)')
    print(f'  footer HTML: {len(footer_html)} chars  '
          f'({footer_html.count(FOOTER_MARKER)} x {FOOTER_MARKER})')
    print()

    # 2) Propagate.
    print('=== Propagation ===')
    n_updated = n_skipped = n_errors = 0
    error_details: list[tuple[str, str]] = []
    for page_name in pages:
        path = os.path.join(BASE, page_name)
        status, msg = propagate_one(
            path,
            footer_css,
            footer_html,
            force=args.force,
            dry_run=args.dry_run,
        )
        if status == 'updated':
            print(f'  UPDATE  {page_name}: {msg}')
            n_updated += 1
        elif status == 'skipped':
            print(f'  SKIP    {page_name}: {msg}')
            n_skipped += 1
        else:
            print(f'  ERROR   {page_name}: {msg}')
            error_details.append((page_name, msg))
            n_errors += 1

    print()
    print(
        f'Result: {n_updated} updated, {n_skipped} skipped, '
        f'{n_errors} errors out of {len(pages)} pages'
    )

    if error_details:
        print()
        print('ERRORED PAGES (inspect manually):')
        for name, msg in error_details:
            print(f'  - {name}: {msg}')

    # 3) Verify (only when writes happened and the user didn't opt out).
    if args.dry_run or args.skip_verify or n_updated == 0:
        print()
        print('Skipping verification sweep.')
    else:
        if not verify(pages):
            print('\nSome pages failed verification — see above.', file=sys.stderr)
            return 2
        print('\nAll pages verified clean.')

    return 0


if __name__ == '__main__':
    sys.exit(main())
