/**
 * Joan Alobo Constituency Site — Animations
 * Features: page-load fadeInUp, scroll-triggered reveal, animated counters
 *
 * Usage:
 *   class="fade-in-up"        → element fades in on scroll into viewport
 *   class="count-up"          → number text counts up when scrolled into view
 *   data-count-to="1234"      → target value for count-up
 *   data-count-duration="2000"→ animation duration in ms (default 2000)
 */

(function () {
  'use strict';

  // ── 1. Inject animation keyframes ──────────────────────────────────────
  var style = document.createElement('style');
  style.textContent =
    '\n' +
    '/* ── Joan Alobo site animations ── */\n' +
    '@keyframes fadeInUp {\n' +
    '  from {\n' +
    '    opacity: 0;\n' +
    '    transform: translateY(30px);\n' +
    '  }\n' +
    '  to {\n' +
    '    opacity: 1;\n' +
    '    transform: translateY(0);\n' +
    '  }\n' +
    '}\n' +
    '\n' +
    '.fade-in-up {\n' +
    '  opacity: 0;\n' +
    '  transform: translateY(30px);\n' +
    '  transition: opacity 0.6s ease-out, transform 0.6s ease-out;\n' +
    '}\n' +
    '\n' +
    '.fade-in-up.visible {\n' +
    '  opacity: 1;\n' +
    '  transform: translateY(0);\n' +
    '}\n' +
    '\n' +
    '.fade-in-up[data-delay="1"] { transition-delay: 0.1s; }\n' +
    '.fade-in-up[data-delay="2"] { transition-delay: 0.2s; }\n' +
    '.fade-in-up[data-delay="3"] { transition-delay: 0.3s; }\n' +
    '.fade-in-up[data-delay="4"] { transition-delay: 0.4s; }\n' +
    '.fade-in-up[data-delay="5"] { transition-delay: 0.5s; }\n' +
    '\n' +
    '.fade-in-up[data-duration="slow"]  { transition-duration: 1.0s; }\n' +
    '.fade-in-up[data-duration="fast"]  { transition-duration: 0.3s; }\n' +
    '';

  document.head.appendChild(style);

  // ── 2. Scroll-triggered fadeInUp via IntersectionObserver ──────────────
  function initFadeInUp() {
    var els = document.querySelectorAll('.fade-in-up:not(.visible)');
    if (!els.length) return;

    // If IntersectionObserver is not supported, just show everything
    if (!('IntersectionObserver' in window)) {
      for (var i = 0; i < els.length; i++) els[i].classList.add('visible');
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        for (var i = 0; i < entries.length; i++) {
          if (entries[i].isIntersecting) {
            entries[i].target.classList.add('visible');
            observer.unobserve(entries[i].target);
          }
        }
      },
      { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
    );

    for (var i = 0; i < els.length; i++) observer.observe(els[i]);
  }

  // ── 3. Animated number count-up ────────────────────────────────────────
  function initCountUp() {
    var counters = document.querySelectorAll('.count-up');
    if (!counters.length) return;

    // If IntersectionObserver is not supported, just show final values
    if (!('IntersectionObserver' in window)) {
      for (var i = 0; i < counters.length; i++) renderCount(counters[i]);
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        for (var i = 0; i < entries.length; i++) {
          if (entries[i].isIntersecting) {
            animateCount(entries[i].target);
            observer.unobserve(entries[i].target);
          }
        }
      },
      { threshold: 0.3 }
    );

    for (var i = 0; i < counters.length; i++) observer.observe(counters[i]);
  }

  function parseCount(el) {
    // Use data-count-to attribute, or parse the text content
    var target = el.getAttribute('data-count-to');
    if (target) return parseFloat(target.replace(/[^\d.-]/g, ''));

    var text = el.textContent || el.innerText || '';
    return parseFloat(text.replace(/[^\d.-]/g, '')) || 0;
  }

  function getFormat(el) {
    return el.getAttribute('data-count-format') || 'number';
  }

  function getPrefix(el) {
    return el.getAttribute('data-count-prefix') || '';
  }

  function renderCount(el) {
    var val = parseCount(el);
    var prefix = getPrefix(el);
    var fmt = getFormat(el);

    if (fmt === 'currency') {
      el.textContent = prefix + formatCurrency(val);
    } else {
      el.textContent = prefix + val.toLocaleString();
    }
  }

  function formatCurrency(val) {
    return 'UGX ' + Math.round(val).toLocaleString();
  }

  function animateCount(el) {
    var target = parseCount(el);
    var duration = parseInt(el.getAttribute('data-count-duration'), 10) || 2000;
    var prefix = getPrefix(el);
    var fmt = getFormat(el);
    var startTime = null;
    var startVal = 0;

    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      // Ease-out cubic
      var eased = 1 - Math.pow(1 - progress, 3);
      var current = startVal + (target - startVal) * eased;

      if (fmt === 'currency') {
        el.textContent = prefix + formatCurrency(current);
      } else {
        el.textContent = prefix + Math.round(current).toLocaleString();
      }

      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        renderCount(el); // Ensure final value is exact
      }
    }

    requestAnimationFrame(step);
  }

  // ── 4. Initialize on DOM ready ─────────────────────────────────────────
  function init() {
    initFadeInUp();
    initCountUp();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
