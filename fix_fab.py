# Wrap both FABs in a container div so they stack naturally with flexbox
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find both FABs and wrap them
old_fabs = '''    <!-- Floating WhatsApp FAB -->
    <a href="https://chat.whatsapp.com/INVITE_LINK_HERE" target="_blank" class="mobile-fab-whatsapp" style="text-decoration:none;" aria-label="Join WhatsApp Community">
        <div class="whatsapp-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
        </div>
        <span class="mobile-fab-label">WhatsApp</span>
    </a>

    <!-- Floating Donate FAB -->
    <a href="donation.html" class="mobile-fab-donate" style="text-decoration:none;">
        <div class="donate-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
        </div>
        <span class="mobile-fab-label">Donate</span>
    </a>'''

new_fabs = '''    <!-- Floating Action Buttons Container -->
    <div class="fab-container">
        <!-- Floating WhatsApp FAB -->
        <a href="https://chat.whatsapp.com/INVITE_LINK_HERE" target="_blank" class="mobile-fab-whatsapp" style="text-decoration:none;" aria-label="Join WhatsApp Community">
            <div class="whatsapp-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
            </div>
            <span class="mobile-fab-label">WhatsApp</span>
        </a>

        <!-- Floating Donate FAB -->
        <a href="donation.html" class="mobile-fab-donate" style="text-decoration:none;">
            <div class="donate-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
            </div>
            <span class="mobile-fab-label">Donate</span>
        </a>
    </div>'''

if old_fabs in html:
    html = html.replace(old_fabs, new_fabs)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('OK: Both FABs wrapped in fab-container')
else:
    print('NOT FOUND - checking...')
    # Find partial match
    wa = html.find('mobile-fab-whatsapp')
    da = html.find('mobile-fab-donate')
    print(f'WhatsApp FAB at index: {wa}, Donate FAB at index: {da}')

# Now update CSS - add fab-container, remove individual bottom from FABs
with open('assets/css/unio-template.webflow.c4cead615.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add fab-container CSS
new_css = '''
/* === FAB CONTAINER === */
.fab-container {
    position: fixed;
    right: 20px;
    bottom: 90px;
    z-index: 9999;
    display: none;
    flex-direction: column;
    align-items: center;
    gap: 12px;
}
@media screen and (max-width: 767px) {
    .fab-container {
        display: flex;
    }
}
@media screen and (max-width: 479px) {
    .fab-container {
        bottom: 80px;
    }
}
'''

# Insert fab-container before .mobile-fab-whatsapp
idx = css.find('.mobile-fab-whatsapp {')
if idx > 0:
    css = css[:idx] + new_css + '\n' + css[idx:]
    print('OK 1: Added fab-container CSS')
else:
    print('NOT FOUND: .mobile-fab-whatsapp in CSS')

# Remove bottom from .mobile-fab-whatsapp (it's now handled by container gap)
# The .mobile-fab-whatsapp should not have position:fixed anymore - it'll be inside the container
# Actually, the individual FABs inside the container should NOT be fixed
# Replace position:fixed + bottom + right in .mobile-fab-whatsapp
old_wa_css = '''.mobile-fab-whatsapp {
    position: fixed;
    right: 20px;
    bottom: 235px;
    z-index: 9999;'''

new_wa_css = '''.mobile-fab-whatsapp {
    position: relative;
    z-index: auto;'''

if old_wa_css in css:
    css = css.replace(old_wa_css, new_wa_css)
    print('OK 2: WhatsApp FAB now position:relative (inside container)')
else:
    print('NOT FOUND: WhatsApp FAB base CSS')

# Remove position:fixed from .mobile-fab-donate
old_don_css = '''.mobile-fab-donate {
    position: fixed;
    bottom: 90px;
    right: 20px;
    z-index: 1000;'''

new_don_css = '''.mobile-fab-donate {
    position: relative;
    z-index: auto;'''

if old_don_css in css:
    css = css.replace(old_don_css, new_don_css)
    print('OK 3: Donate FAB now position:relative (inside container)')
else:
    print('NOT FOUND: Donate FAB base CSS')

# Remove the 479px WhatsApp FAB bottom override since it no longer applies
old_479 = '''@media screen and (max-width: 479px) {
    .mobile-fab-whatsapp {
        bottom: 180px;
    }
}'''
# Check if this still exists
if old_479 in css:
    css = css.replace(old_479, '')
    print('OK 4: Removed old 479px WhatsApp FAB bottom override')

# Also remove the old 767px display rule since it's now on the container
old_display = '''@media screen and (max-width: 767px) {
    .mobile-fab-whatsapp {
        display: flex;
    }
}'''
new_display = '@media screen and (max-width: 767px) {\n    .fab-container {\n        display: flex;\n    }\n}'
if old_display in css:
    css = css.replace(old_display, '')
    print('OK 5: Removed old 767px WhatsApp display, now on container')

with open('assets/css/unio-template.webflow.c4cead615.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('\nDone!')
