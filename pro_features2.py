# Script to add Achievement Counters + Testimonials Carousel to index.html
changes = 0

# ====== 1. ACHIEVEMENT COUNTERS SECTION ======
# Insert after feature-section and before about-section
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

counters_html = '''<div class="counters-section">
        <div class="container w-container">
            <div class="counters-grid">
                <div class="counter-card">
                    <div class="counter-number" data-target="15000">0</div>
                    <div class="counter-suffix">+</div>
                    <div class="counter-label">Constituents Helped</div>
                    <div class="counter-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                    </div>
                </div>
                <div class="counter-card">
                    <div class="counter-number" data-target="50">0</div>
                    <div class="counter-suffix">+</div>
                    <div class="counter-label">Community Projects</div>
                    <div class="counter-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 22 8.5 22 15.5 12 22 2 15.5 2 8.5 12 2"/><line x1="12" y1="22" x2="12" y2="15.5"/><polyline points="22 8.5 12 15.5 2 8.5"/></svg>
                    </div>
                </div>
                <div class="counter-card">
                    <div class="counter-number" data-target="10">0</div>
                    <div class="counter-label">Schools Renovated</div>
                    <div class="counter-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1.1 2.7 2 6 2s6-.9 6-2v-5"/></svg>
                    </div>
                </div>
                <div class="counter-card">
                    <div class="counter-number" data-target="500">0</div>
                    <div class="counter-suffix">+</div>
                    <div class="counter-label">Bursaries Awarded</div>
                    <div class="counter-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>
                    </div>
                </div>
                <div class="counter-card">
                    <div class="counter-number" data-target="5">0</div>
                    <div class="counter-label">Health Centres Upgraded</div>
                    <div class="counter-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
                    </div>
                </div>
                <div class="counter-card">
                    <div class="counter-number" data-target="1000000">0</div>
                    <div class="counter-suffix">+</div>
                    <div class="counter-label">Trees Planted</div>
                    <div class="counter-icon">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z"/></svg>
                    </div>
                </div>
            </div>
        </div>
    </div>
    '''

# Insert after </div> of feature-section (the closing div after feature-right-block)
old_marker = '</div>\n        <div class="about-section">'
if old_marker in html:
    html = html.replace(old_marker, '</div>\n' + counters_html + '        <div class="about-section">')
    changes += 1
    print('OK: Achievement Counters section added')
else:
    print('NOT FOUND: about-section marker')

# ====== 2. TESTIMONIALS CAROUSEL SECTION ======
# Insert after our-abilities-section and before upcoming-campaign-section
testimonials_html = '''<div class="testimonials-section">
        <div class="container w-container">
            <div class="join-our-movement-title-block">
                <div class="section-title-block section-block-center">
                    <h2 class="section-title">What People Say</h2>
                    <p class="section-summary">Hear from community leaders, elders, and constituents about Hon. Joan Alobo's impact in Soroti City East.</p>
                </div>
            </div>
            <div class="testimonials-carousel" id="testimonialCarousel">
                <div class="testimonials-track" id="testimonialTrack">
                    <div class="testimonial-card">
                        <div class="testimonial-quote-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#16327a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"/><path d="M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2h.75c0 2.25.25 4-2.75 4v3c0 1 0 1 1 1z"/></svg>
                        </div>
                        <p class="testimonial-text">Hon. Joan Alobo has transformed our community. Since she took office, we have seen real improvements in our health centre and our children's school. She truly listens to the people.</p>
                        <div class="testimonial-author">
                            <div class="testimonial-avatar">MO</div>
                            <div class="testimonial-author-info">
                                <div class="testimonial-name">Margaret Amongin</div>
                                <div class="testimonial-role">Market Vendor Leader, Soroti Central Market</div>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-card">
                        <div class="testimonial-quote-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#16327a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"/><path d="M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2h.75c0 2.25.25 4-2.75 4v3c0 1 0 1 1 1z"/></svg>
                        </div>
                        <p class="testimonial-text">I have known Joan for over 15 years. Her integrity and dedication to the people of Teso is unmatched. She fights for the voiceless and delivers on her promises. Our constituency is lucky to have her.</p>
                        <div class="testimonial-author">
                            <div class="testimonial-avatar">PO</div>
                            <div class="testimonial-author-info">
                                <div class="testimonial-name">Paul Ocen</div>
                                <div class="testimonial-role">Community Elder, Pamba Ward</div>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-card">
                        <div class="testimonial-quote-icon">
                            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#16327a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"/><path d="M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2h.75c0 2.25.25 4-2.75 4v3c0 1 0 1 1 1z"/></svg>
                        </div>
                        <p class="testimonial-text">Thanks to Hon. Alobo's bursary programme, my daughter is now studying at university. Without her support, we couldn't have afforded the fees. She truly cares about the youth and their future.</p>
                        <div class="testimonial-author">
                            <div class="testimonial-avatar">SA</div>
                            <div class="testimonial-author-info">
                                <div class="testimonial-name">Sarah Akello</div>
                                <div class="testimonial-role">Parent & Small Business Owner, Gweri</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="testimonials-dots" id="testimonialDots">
                    <button class="testimonial-dot active" data-index="0" aria-label="Slide 1"></button>
                    <button class="testimonial-dot" data-index="1" aria-label="Slide 2"></button>
                    <button class="testimonial-dot" data-index="2" aria-label="Slide 3"></button>
                </div>
            </div>
        </div>
    </div>
    '''

old_marker2 = '<div class="upcoming-campaign-section">'
if old_marker2 in html:
    html = html.replace(old_marker2, testimonials_html + '\n        ' + old_marker2)
    changes += 1
    print('OK: Testimonials Carousel section added')
else:
    print('NOT FOUND: upcoming-campaign-section marker')

# Also add JS for both features before closing </body>
counters_js = '''
    <!-- Achievement Counters Animation -->
    <script>
        (function() {
            var counters = document.querySelectorAll('.counter-number');
            var animated = false;

            function animateCounter(el) {
                var target = parseInt(el.getAttribute('data-target'));
                var duration = 2000;
                var step = target / (duration / 16);
                var current = 0;
                var suffix = el.parentElement.querySelector('.counter-suffix');

                function update() {
                    current += step;
                    if (current < target) {
                        el.textContent = Math.floor(current).toLocaleString();
                        requestAnimationFrame(update);
                    } else {
                        el.textContent = target.toLocaleString();
                    }
                }
                update();
            }

            function checkCounters() {
                if (animated) return;
                var firstCounter = counters[0];
                if (!firstCounter) return;
                var rect = firstCounter.getBoundingClientRect();
                if (rect.top < window.innerHeight - 100) {
                    animated = true;
                    counters.forEach(function(c) { animateCounter(c); });
                }
            }

            window.addEventListener('scroll', checkCounters);
            window.addEventListener('load', checkCounters);
            checkCounters();
        })();
    </script>'''

carousel_js = '''
    <!-- Testimonials Carousel -->
    <script>
        (function() {
            var track = document.getElementById('testimonialTrack');
            var dots = document.querySelectorAll('#testimonialDots .testimonial-dot');
            var currentIndex = 0;
            var totalSlides = dots.length;
            var autoplayInterval;

            function goToSlide(index) {
                currentIndex = index;
                track.style.transform = 'translateX(-' + (index * 100) + '%)';
                dots.forEach(function(d, i) {
                    d.classList.toggle('active', i === index);
                });
            }

            dots.forEach(function(dot) {
                dot.addEventListener('click', function() {
                    var idx = parseInt(this.getAttribute('data-index'));
                    goToSlide(idx);
                    resetAutoplay();
                });
            });

            // Touch swipe support
            var startX = 0;
            track.addEventListener('touchstart', function(e) {
                startX = e.touches[0].clientX;
            }, {passive: true});

            track.addEventListener('touchend', function(e) {
                var diff = startX - e.changedTouches[0].clientX;
                if (Math.abs(diff) > 50) {
                    if (diff > 0 && currentIndex < totalSlides - 1) {
                        goToSlide(currentIndex + 1);
                    } else if (diff < 0 && currentIndex > 0) {
                        goToSlide(currentIndex - 1);
                    }
                    resetAutoplay();
                }
            });

            function startAutoplay() {
                autoplayInterval = setInterval(function() {
                    var next = (currentIndex + 1) % totalSlides;
                    goToSlide(next);
                }, 5000);
            }

            function resetAutoplay() {
                clearInterval(autoplayInterval);
                startAutoplay();
            }

            startAutoplay();
        })();
    </script>'''

# Add JS before closing </body>
old_body = '</body>'
if old_body in html:
    html = html.replace(old_body, counters_js + '\n' + carousel_js + '\n' + old_body)
    changes += 1
    print('OK: JS scripts added')
else:
    print('NOT FOUND: closing body tag')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ====== 3. CSS STYLES ======
with open('assets/css/unio-template.webflow.c4cead615.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* === ACHIEVEMENT COUNTERS === */
.counters-section {
    padding: 60px 0;
    background: linear-gradient(135deg, #16327a, #1a3d8f);
}
.counters-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 20px;
}
.counter-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    padding: 20px 10px;
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.08);
    transition: transform 0.3s ease, background 0.3s ease;
}
.counter-card:hover {
    transform: translateY(-4px);
    background: rgba(255, 255, 255, 0.14);
}
.counter-number {
    font-family: Urbanist, sans-serif;
    font-size: 38px;
    font-weight: 800;
    color: #fff;
    line-height: 1;
}
.counter-suffix {
    display: none;
    font-family: Urbanist, sans-serif;
    font-size: 38px;
    font-weight: 800;
    color: #99ccff;
    line-height: 1;
}
.counter-card:has(.counter-suffix) .counter-number {
    display: inline;
}
.counter-label {
    font-size: 13px;
    color: rgba(255, 255, 255, 0.85);
    text-align: center;
    line-height: 1.3;
    font-weight: 500;
}
.counter-icon {
    color: rgba(255, 255, 255, 0.5);
    margin-top: 4px;
}
/* === TESTIMONIALS CAROUSEL === */
.testimonials-section {
    padding-top: 40px;
    padding-bottom: 80px;
    background: transparent;
}
.testimonials-carousel {
    max-width: 700px;
    margin: 40px auto 0;
    overflow: hidden;
    position: relative;
}
.testimonials-track {
    display: flex;
    transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
.testimonial-card {
    min-width: 100%;
    padding: 40px 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 20px;
}
.testimonial-quote-icon {
    opacity: 0.6;
}
.testimonial-text {
    font-size: 18px;
    line-height: 1.7;
    color: #444;
    font-style: italic;
    max-width: 580px;
}
.testimonial-author {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 8px;
}
.testimonial-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: linear-gradient(135deg, #16327a, #1a5cb0);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 16px;
    flex-shrink: 0;
}
.testimonial-author-info {
    text-align: left;
}
.testimonial-name {
    font-weight: 700;
    color: #333;
    font-size: 15px;
}
.testimonial-role {
    font-size: 13px;
    color: #888;
    line-height: 1.3;
}
.testimonials-dots {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-top: 24px;
}
.testimonial-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    border: none;
    background: #d0d0d0;
    cursor: pointer;
    padding: 0;
    transition: background 0.3s ease, transform 0.3s ease;
}
.testimonial-dot.active {
    background: #16327a;
    transform: scale(1.3);
}
.testimonial-dot:hover {
    background: #99ccff;
}
/* Responsive counters */
@media screen and (max-width: 991px) {
    .counters-grid {
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
    }
    .counter-number {
        font-size: 32px;
    }
    .testimonial-card {
        padding: 30px 30px;
    }
    .testimonial-text {
        font-size: 16px;
    }
}
@media screen and (max-width: 767px) {
    .counters-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
    }
    .counter-card {
        padding: 16px 8px;
        gap: 4px;
    }
    .counter-number {
        font-size: 28px;
    }
    .counter-label {
        font-size: 11px;
    }
    .testimonial-card {
        padding: 24px 20px;
    }
    .testimonial-text {
        font-size: 15px;
    }
}
@media screen and (max-width: 479px) {
    .counters-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
    }
    .counter-number {
        font-size: 26px;
    }
    .counter-label {
        font-size: 10px;
    }
}
'''

# Insert before the donatePulse keyframes
insert_marker = '@keyframes donatePulse'
if insert_marker in css:
    css = css.replace(insert_marker, new_css + '\n' + insert_marker)
    changes += 1
    print('OK: CSS styles added for counters and carousel')
else:
    print('NOT FOUND: donatePulse keyframes in CSS')

with open('assets/css/unio-template.webflow.c4cead615.css', 'w', encoding='utf-8') as f:
    f.write(css)

print(f'\n=== Total changes: {changes} ===')
