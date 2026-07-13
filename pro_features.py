import re

changes_made = 0

# ======= 1. ALL HTML FILES: Replace LinkedIn with WhatsApp in header =======
import glob
html_files = glob.glob('*.html')
whatsapp_svg = '<a href="https://chat.whatsapp.com/INVITE_LINK_HERE" target="_blank" class="header-top-single-social-item w-inline-block"><svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg></a>'

linkedin_pattern = r'<a\s+href="#"\s+class="header-top-single-social-item w-inline-block"><img src="assets/63ec6740e5b15cc3f0559507_linkedin-2\.svg"[^>]*?/></a>'

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    new_content = re.sub(linkedin_pattern, whatsapp_svg, content)
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        changes_made += 1
        print(f'OK: WhatsApp icon replaced LinkedIn in {f}')

# ======= 2. INDEX.HTML: Add Video/Speeches section before client logos =======
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

video_section = '''    <div class="video-section">
        <div class="container w-container">
            <div class="join-our-movement-title-block">
                <div class="section-title-block section-block-center">
                    <h2 class="section-title">Speeches &amp; Videos</h2>
                    <p class="section-summary">Watch Hon. Joan Alobo's parliamentary speeches, community addresses, and campaign highlights from across Soroti City East.</p>
                </div>
            </div>
            <div class="video-grid">
                <div class="video-card">
                    <div class="video-wrapper">
                        <iframe src="https://www.youtube.com/embed/PLACEHOLDER_ID_1" title="Parliamentary Speech" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </div>
                    <h4 class="video-title">Parliamentary Address on Healthcare</h4>
                    <p class="video-date">Parliament of Uganda &bull; June 2026</p>
                </div>
                <div class="video-card">
                    <div class="video-wrapper">
                        <iframe src="https://www.youtube.com/embed/PLACEHOLDER_ID_2" title="Campaign Rally" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </div>
                    <h4 class="video-title">Community Rally in Soroti City East</h4>
                    <p class="video-date">Soroti City &bull; May 2026</p>
                </div>
                <div class="video-card">
                    <div class="video-wrapper">
                        <iframe src="https://www.youtube.com/embed/PLACEHOLDER_ID_3" title="Women Empowerment Speech" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </div>
                    <h4 class="video-title">Women's Economic Empowerment Forum</h4>
                    <p class="video-date">Kampala &bull; April 2026</p>
                </div>
            </div>
        </div>
    </div>
'''

# Insert before client-logo-section
old_section_start = '<section class="client-logo-section">'
if old_section_start in html:
    html = html.replace(old_section_start, video_section + '\n    ' + old_section_start)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    changes_made += 1
    print('OK: Video section added to index.html')
else:
    print('NOT FOUND: client-logo-section in index.html')

# ======= 3. INDEX.HTML: Add WhatsApp floating button next to Donate FAB =======
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add WhatsApp FAB before the Donate FAB
old_fab = '<!-- Floating Donate FAB -->'
whatsapp_fab = '''<!-- Floating WhatsApp FAB -->
    <a href="https://chat.whatsapp.com/INVITE_LINK_HERE" target="_blank" class="mobile-fab-whatsapp" style="text-decoration:none;" aria-label="Join WhatsApp Community">
        <div class="whatsapp-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
        </div>
        <span class="mobile-fab-label">WhatsApp</span>
    </a>

    <!-- Floating Donate FAB -->'''

if old_fab in html:
    html = html.replace(old_fab, whatsapp_fab)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    changes_made += 1
    print('OK: WhatsApp FAB added to index.html')
else:
    print('NOT FOUND: Floating Donate FAB in index.html')

# ======= 4. MANIFESTO.HTML: Update PDF download link =======
with open('manifesto.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_pdf = 'href="#" class="download-pdf-link-block'
new_pdf = 'href="assets/manifesto.pdf" download class="download-pdf-link-block'

if old_pdf in html:
    html = html.replace(old_pdf, new_pdf)
    with open('manifesto.html', 'w', encoding='utf-8') as f:
        f.write(html)
    changes_made += 1
    print('OK: Manifesto PDF download link updated')
else:
    print('NOT FOUND: download-pdf-link-block in manifesto.html')

# ======= 5. CSS: Add styles for video section and WhatsApp FAB =======
with open('assets/css/unio-template.webflow.c4cead615.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* === VIDEO SECTION === */
.video-section {
    padding-top: 40px;
    padding-bottom: 80px;
    background: #f8f9fb;
}
.video-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-top: 40px;
}
.video-card {
    display: flex;
    flex-direction: column;
    gap: 12px;
}
.video-wrapper {
    position: relative;
    padding-bottom: 56.25%;
    height: 0;
    overflow: hidden;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    background: #000;
}
.video-wrapper iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 12px;
}
.video-title {
    font-size: 16px;
    font-weight: 700;
    color: #333;
    line-height: 1.3;
}
.video-date {
    font-size: 13px;
    color: #888;
    line-height: 1;
}
/* === WHATSAPP FAB === */
.mobile-fab-whatsapp {
    position: fixed;
    right: 20px;
    bottom: 130px;
    z-index: 9999;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: #25D366;
    box-shadow: 0 4px 20px rgba(37, 211, 102, 0.5), 0 0 0 4px rgba(255,255,255,0.95);
    display: none;
    align-items: center;
    justify-content: center;
    transition: transform 0.2s ease;
    color: #fff;
}
.mobile-fab-whatsapp:active {
    transform: scale(0.92);
}
.mobile-fab-whatsapp .whatsapp-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
}
.mobile-fab-whatsapp .mobile-fab-label {
    display: none;
}
@media screen and (max-width: 767px) {
    .video-grid {
        grid-template-columns: 1fr;
        gap: 24px;
    }
    .mobile-fab-whatsapp {
        display: flex;
    }
}
@media screen and (max-width: 479px) {
    .mobile-fab-whatsapp {
        bottom: 120px;
    }
}
'''

# Insert before the donatPulse keyframes (near end of file)
insert_marker = '@keyframes donatePulse'
if insert_marker in css:
    css = css.replace(insert_marker, new_css + '\n' + insert_marker)
    with open('assets/css/unio-template.webflow.c4cead615.css', 'w', encoding='utf-8') as f:
        f.write(css)
    changes_made += 1
    print('OK: CSS styles added for video section and WhatsApp FAB')
else:
    print('NOT FOUND: donatePulse keyframes')

print(f'\n=== Total changes: {changes_made} ===')

