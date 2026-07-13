# Script to add Live Donation Tracker + Enhanced Newsletter Signup
changes = 0

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ====== 1. LIVE DONATION TRACKER ======
# Add progress bar inside the donation section, above the quick-select pills
tracker_html = '''<div class="donation-tracker" data-goal="50000000" data-raised="12750000">
                            <div class="donation-tracker-header">
                                <div class="donation-tracker-info">
                                    <span class="donation-tracker-label">Campaign Fundraising Goal</span>
                                    <span class="donation-tracker-goal">UGX 50,000,000</span>
                                </div>
                                <div class="donation-tracker-percent" id="donationPercent">25%</div>
                            </div>
                            <div class="donation-tracker-bar">
                                <div class="donation-tracker-fill" id="donationFill"></div>
                                <div class="donation-tracker-glow"></div>
                            </div>
                            <div class="donation-tracker-stats">
                                <div class="donation-tracker-stat">
                                    <span class="donation-stat-amount" id="donationRaised">UGX 12,750,000</span>
                                    <span class="donation-stat-label">Raised so far</span>
                                </div>
                                <div class="donation-tracker-stat">
                                    <span class="donation-stat-amount">1,247</span>
                                    <span class="donation-stat-label">Donors</span>
                                </div>
                                <div class="donation-tracker-stat">
                                    <span class="donation-stat-amount">46</span>
                                    <span class="donation-stat-label">Days remaining</span>
                                </div>
                            </div>
                        </div>
                        '''

old_donation = '<div class="donation-quick-select"'
if old_donation in html:
    html = html.replace(old_donation, tracker_html + '\n                        ' + old_donation)
    changes += 1
    print('OK 1: Donation tracker added')
else:
    print('NOT FOUND: donation-quick-select')

# ====== 2. NEWSLETTER CTA SECTION ======
# Add an enhanced newsletter section before the footer
newsletter_html = '''<div class="newsletter-cta-section">
        <div class="container w-container">
            <div class="newsletter-cta-wrapper">
                <div class="newsletter-cta-content">
                    <div class="newsletter-cta-icon">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                    </div>
                    <h2 class="newsletter-cta-title">Stay Informed, Stay Connected</h2>
                    <p class="newsletter-cta-text">Get weekly updates on constituency projects, parliamentary work, and upcoming events delivered straight to your inbox. Join 5,000+ subscribers across Soroti City East.</p>
                </div>
                <div class="newsletter-cta-form-block w-form">
                    <form id="newsletter-form" name="newsletter-form" data-name="Newsletter Form" method="post" class="newsletter-cta-form" action="https://formspree.io/f/PLACEHOLDER_FORM_ID">
                        <div class="newsletter-input-group">
                            <input class="newsletter-input w-input" maxlength="256" name="name" data-name="Name" placeholder="Your name" type="text" id="news-name" />
                            <input class="newsletter-input w-input" maxlength="256" name="email" data-name="Email" placeholder="your@email.com" type="email" id="news-email" required="" />
                            <input type="submit" data-wait="Subscribing..." class="newsletter-submit w-button" value="Subscribe Now" />
                        </div>
                        <div class="newsletter-disclaimer">No spam, ever. Unsubscribe anytime. We respect your privacy.</div>
                    </form>
                    <div class="w-form-done">
                        <div class="newsletter-success">Thank you! Please check your inbox to confirm your subscription.</div>
                    </div>
                    <div class="w-form-fail">
                        <div>Oops! Something went wrong. Please try again.</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    '''

old_footer = '<footer class="footer">'
if old_footer in html:
    html = html.replace(old_footer, newsletter_html + '\n    ' + old_footer)
    changes += 1
    print('OK 2: Newsletter CTA section added')
else:
    print('NOT FOUND: footer')

# ====== 3. DONATION TRACKER JS ======
tracker_js = '''
    <!-- Donation Tracker Animation -->
    <script>
        (function() {
            var tracker = document.querySelector('.donation-tracker');
            if (!tracker) return;
            
            var goal = parseInt(tracker.getAttribute('data-goal'));
            var raised = parseInt(tracker.getAttribute('data-raised'));
            var percent = Math.min(Math.round((raised / goal) * 100), 100);
            var fill = document.getElementById('donationFill');
            var percentEl = document.getElementById('donationPercent');
            var animated = false;

            function formatUGX(amount) {
                return 'UGX ' + amount.toLocaleString();
            }

            function animateTracker() {
                if (animated) return;
                var rect = tracker.getBoundingClientRect();
                if (rect.top < window.innerHeight) {
                    animated = true;
                    var currentWidth = 0;
                    var duration = 1500;
                    var startTime = null;

                    function step(timestamp) {
                        if (!startTime) startTime = timestamp;
                        var elapsed = timestamp - startTime;
                        var progress = Math.min(elapsed / duration, 1);
                        // Ease out cubic
                        var eased = 1 - Math.pow(1 - progress, 3);
                        var currentPercent = Math.round(eased * percent);
                        
                        fill.style.width = currentPercent + '%';
                        percentEl.textContent = currentPercent + '%';
                        
                        if (progress < 1) {
                            requestAnimationFrame(step);
                        } else {
                            fill.style.width = percent + '%';
                            percentEl.textContent = percent + '%';
                        }
                    }
                    requestAnimationFrame(step);
                }
            }

            // Set initial state
            fill.style.width = '0%';
            percentEl.textContent = '0%';
            document.getElementById('donationRaised').textContent = formatUGX(raised);

            window.addEventListener('scroll', animateTracker);
            window.addEventListener('load', animateTracker);
            setTimeout(animateTracker, 500);
        })();
    </script>'''

old_body2 = '</body>'
if old_body2 in html:
    html = html.replace(old_body2, tracker_js + '\n' + old_body2)
    changes += 1
    print('OK 3: Tracker JS added')
else:
    print('NOT FOUND: closing body')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ====== 4. CSS STYLES ======
with open('assets/css/unio-template.webflow.c4cead615.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* === DONATION TRACKER === */
.donation-tracker {
    margin-bottom: 18px;
    padding: 16px 20px;
    background: rgba(255, 255, 255, 0.12);
    border-radius: 14px;
    border: 1px solid rgba(255, 255, 255, 0.15);
}
.donation-tracker-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-bottom: 10px;
}
.donation-tracker-info {
    display: flex;
    flex-direction: column;
    gap: 2px;
}
.donation-tracker-label {
    font-size: 12px;
    color: rgba(255, 255, 255, 0.7);
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 600;
}
.donation-tracker-goal {
    font-family: Urbanist, sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #fff;
    line-height: 1;
}
.donation-tracker-percent {
    font-family: Urbanist, sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: #99ccff;
    line-height: 1;
}
.donation-tracker-bar {
    position: relative;
    height: 10px;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 14px;
}
.donation-tracker-fill {
    height: 100%;
    background: linear-gradient(90deg, #99ccff, #66b3ff);
    border-radius: 10px;
    width: 0%;
    transition: width 0.1s linear;
    position: relative;
}
.donation-tracker-glow {
    position: absolute;
    top: 0;
    right: 0;
    width: 40px;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(153, 204, 255, 0.4));
    border-radius: 0 10px 10px 0;
}
.donation-tracker-stats {
    display: flex;
    justify-content: space-between;
}
.donation-tracker-stat {
    display: flex;
    flex-direction: column;
    gap: 1px;
}
.donation-stat-amount {
    font-family: Urbanist, sans-serif;
    font-size: 15px;
    font-weight: 700;
    color: #fff;
    line-height: 1;
}
.donation-stat-label {
    font-size: 10px;
    color: rgba(255, 255, 255, 0.6);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* === NEWSLETTER CTA === */
.newsletter-cta-section {
    padding: 80px 0;
    background: linear-gradient(135deg, #0f2354, #16327a);
}
.newsletter-cta-wrapper {
    display: flex;
    align-items: center;
    gap: 50px;
}
.newsletter-cta-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.newsletter-cta-icon {
    color: #99ccff;
}
.newsletter-cta-title {
    font-family: Urbanist, sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: #fff;
    line-height: 1.2;
}
.newsletter-cta-text {
    font-size: 16px;
    color: rgba(255, 255, 255, 0.8);
    line-height: 1.6;
    max-width: 500px;
}
.newsletter-cta-form-block {
    flex: 1;
    max-width: 420px;
}
.newsletter-cta-form {
    display: flex;
    flex-direction: column;
    gap: 12px;
}
.newsletter-input-group {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.newsletter-input {
    height: 50px;
    padding: 0 18px;
    border: 2px solid rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.1);
    color: #fff;
    font-size: 15px;
    transition: border-color 0.3s ease, background 0.3s ease;
}
.newsletter-input:focus {
    border-color: #99ccff;
    background: rgba(255, 255, 255, 0.15);
    outline: none;
}
.newsletter-input::placeholder {
    color: rgba(255, 255, 255, 0.5);
}
.newsletter-submit {
    height: 50px;
    padding: 0 30px;
    border: none;
    border-radius: 10px;
    background: linear-gradient(135deg, #99ccff, #66b3ff);
    color: #16327a;
    font-family: Urbanist, sans-serif;
    font-size: 16px;
    font-weight: 700;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.newsletter-submit:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(153, 204, 255, 0.3);
}
.newsletter-disclaimer {
    font-size: 11px;
    color: rgba(255, 255, 255, 0.5);
    text-align: center;
}
.newsletter-success {
    padding: 16px;
    background: rgba(37, 211, 102, 0.15);
    border: 1px solid rgba(37, 211, 102, 0.3);
    border-radius: 10px;
    color: #4ade80;
    font-size: 14px;
    text-align: center;
}

/* Responsive */
@media screen and (max-width: 767px) {
    .donation-tracker {
        padding: 14px 16px;
    }
    .donation-tracker-percent {
        font-size: 24px;
    }
    .donation-stat-amount {
        font-size: 13px;
    }
    .newsletter-cta-wrapper {
        flex-direction: column;
        gap: 30px;
        text-align: center;
    }
    .newsletter-cta-text {
        max-width: 100%;
    }
    .newsletter-cta-title {
        font-size: 26px;
    }
    .newsletter-cta-form-block {
        max-width: 100%;
        width: 100%;
    }
}
'''

insert_marker = '@keyframes donatePulse'
if insert_marker in css:
    css = css.replace(insert_marker, new_css + '\n' + insert_marker)
    changes += 1
    print('OK 4: CSS styles added')
else:
    print('NOT FOUND: donatePulse')

with open('assets/css/unio-template.webflow.c4cead615.css', 'w', encoding='utf-8') as f:
    f.write(css)

print(f'\n=== Total changes: {changes} ===')
