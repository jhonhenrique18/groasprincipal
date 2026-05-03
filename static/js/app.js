/* ═══ META PIXEL HELPERS (shared) ═══ */
function epMetaEventId() {
    if (window.crypto && typeof crypto.randomUUID === 'function') return crypto.randomUUID();
    return 'ep-' + Date.now() + '-' + Math.random().toString(36).slice(2, 10);
}

function epMetaTrack(eventName, customData, opts) {
    customData = customData || {};
    opts = opts || {};
    var eventId = opts.eventId || epMetaEventId();
    if (typeof fbq === 'function') {
        try { fbq('track', eventName, customData, { eventID: eventId }); } catch (_) {}
    }
    if (opts.capi !== false) {
        try {
            var body = JSON.stringify({
                event_name: eventName,
                event_id: eventId,
                event_source_url: window.location.href,
                custom_data: customData
            });
            if (navigator.sendBeacon) {
                var blob = new Blob([body], { type: 'application/json' });
                navigator.sendBeacon('/api/meta-capi-event', blob);
            } else {
                fetch('/api/meta-capi-event', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: body,
                    keepalive: true
                }).catch(function () {});
            }
        } catch (_) {}
    }
    return eventId;
}

document.addEventListener('DOMContentLoaded', function () {

    /* ═══ NAVBAR SCROLL ═══ */
    var navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            navbar.classList.toggle('scrolled', window.scrollY > 20);
        }, { passive: true });
    }

    /* ═══ MOBILE NAV TOGGLE ═══ */
    var toggle = document.getElementById('navToggle');
    var links = document.getElementById('navLinks');
    if (toggle && links) {
        toggle.addEventListener('click', function () {
            toggle.classList.toggle('active');
            links.classList.toggle('open');
        });
        links.querySelectorAll('a').forEach(function (a) {
            a.addEventListener('click', function () {
                toggle.classList.remove('active');
                links.classList.remove('open');
            });
        });
    }

    /* ═══ SCROLL REVEAL ═══ */
    var reveals = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window && reveals.length) {
        var obs = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) {
                if (e.isIntersecting) {
                    e.target.classList.add('visible');
                    obs.unobserve(e.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -30px 0px' });
        reveals.forEach(function (el, i) {
            el.style.transitionDelay = (i % 4) * 80 + 'ms';
            obs.observe(el);
        });
    } else {
        reveals.forEach(function (el) { el.classList.add('visible'); });
    }

    /* ═══ COUNTER ANIMATION ═══ */
    var counters = document.querySelectorAll('.stat-num[data-target]');
    if (counters.length && 'IntersectionObserver' in window) {
        var counted = false;
        var counterObs = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) {
                if (e.isIntersecting && !counted) {
                    counted = true;
                    counters.forEach(function (el) {
                        var target = parseInt(el.getAttribute('data-target'));
                        var duration = 2000;
                        var start = 0;
                        var startTime = null;
                        function step(ts) {
                            if (!startTime) startTime = ts;
                            var progress = Math.min((ts - startTime) / duration, 1);
                            var eased = 1 - Math.pow(1 - progress, 3);
                            el.textContent = Math.floor(eased * target).toLocaleString('es');
                            if (progress < 1) requestAnimationFrame(step);
                        }
                        requestAnimationFrame(step);
                    });
                }
            });
        }, { threshold: 0.3 });
        counterObs.observe(counters[0].closest('.stats'));
    }

    /* ═══ PAUSE CAROUSELS ON HOVER ═══ */
    document.querySelectorAll('.clients-track').forEach(function (t) {
        t.addEventListener('mouseenter', function () { this.style.animationPlayState = 'paused'; });
        t.addEventListener('mouseleave', function () { this.style.animationPlayState = 'running'; });
    });

    /* ═══ PRODUCT MODAL ═══ */
    var modal = document.getElementById('productModal');
    var modalClose = document.getElementById('modalClose');
    if (modal) {
        // Open modal on product card click — but explicitly LET THROUGH any
        // click that lands on an element marked with data-go-to-page (the
        // "Ver producto" button), so users have a deliberate path to the
        // full product page when they want it.
        document.addEventListener('click', function (e) {
            var card = e.target.closest('.product-card[data-slug]');
            if (!card) return;
            // Click landed on the explicit "go to page" button → let the
            // browser follow the <a href> normally.
            if (e.target.closest('[data-go-to-page]')) return;
            e.preventDefault();
            var slug = card.getAttribute('data-slug');
            openProductModal(slug);
        });

        // Close modal
        modalClose.addEventListener('click', closeModal);
        modal.addEventListener('click', function (e) {
            if (e.target === modal) closeModal();
        });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && modal.classList.contains('active')) closeModal();
        });

        function closeModal() {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }

        function isSafeImageUrl(url) {
            // Accept only relative paths (/static/... or /uploads/...) or explicit https URLs.
            if (typeof url !== 'string' || !url) return false;
            return url.charAt(0) === '/' || /^https:\/\//i.test(url);
        }

        function setLoading(box, text) {
            var div = document.createElement('div');
            div.className = 'modal-loading';
            div.textContent = text;
            box.replaceChildren(div);
        }

        function buildDetailRow(label, value) {
            var row = document.createElement('div');
            row.className = 'modal-detail-row';
            var s = document.createElement('strong');
            s.textContent = label;
            var span = document.createElement('span');
            span.textContent = value;
            row.appendChild(s);
            row.appendChild(span);
            return row;
        }

        function openProductModal(slug) {
            var box = modal.querySelector('.modal-body');
            setLoading(box, 'Cargando...');
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';

            fetch('/api/producto/' + encodeURIComponent(slug))
                .then(function (r) { return r.json(); })
                .then(function (p) {
                    // All user-provided fields below are inserted via textContent or
                    // attribute setters that are XSS-safe. Do NOT switch back to innerHTML.
                    var imgWrap = document.createElement('div');
                    imgWrap.className = 'modal-img';
                    if (p.image && isSafeImageUrl(p.image)) {
                        var img = document.createElement('img');
                        img.src = p.image;
                        img.alt = p.name || '';
                        imgWrap.appendChild(img);
                    } else {
                        var ph = document.createElement('span');
                        ph.className = 'modal-placeholder';
                        ph.textContent = (p.name || '?').charAt(0);
                        imgWrap.appendChild(ph);
                    }

                    var info = document.createElement('div');
                    info.className = 'modal-info';

                    if (p.category_name) {
                        var catSpan = document.createElement('span');
                        catSpan.className = 'modal-cat';
                        catSpan.textContent = p.category_name;
                        info.appendChild(catSpan);
                    }

                    var h2 = document.createElement('h2');
                    h2.className = 'modal-title';
                    h2.textContent = p.name || '';
                    info.appendChild(h2);

                    var rows = [];
                    if (p.origin) rows.push(buildDetailRow('Origen', p.origin));
                    if (p.presentation) rows.push(buildDetailRow('Presentación', p.presentation));
                    if (p.category_name) rows.push(buildDetailRow('Categoría', p.category_name));
                    if (rows.length) {
                        var details = document.createElement('div');
                        details.className = 'modal-details';
                        rows.forEach(function (r) { details.appendChild(r); });
                        info.appendChild(details);
                    }

                    if (p.description) {
                        var desc = document.createElement('div');
                        desc.className = 'modal-desc';
                        var h3 = document.createElement('h3');
                        h3.textContent = 'Descripción';
                        var pEl = document.createElement('p');
                        pEl.textContent = p.description;
                        desc.appendChild(h3);
                        desc.appendChild(pEl);
                        info.appendChild(desc);
                    }

                    var waFloat = document.querySelector('.wa-float');
                    var waDigits = waFloat ? waFloat.href.replace('https://wa.me/', '') : '';
                    var waLink = document.createElement('a');
                    waLink.href = 'https://wa.me/' + encodeURIComponent(waDigits) + '?text=' + encodeURIComponent('Hola, me interesa el producto: ' + (p.name || ''));
                    waLink.target = '_blank';
                    waLink.rel = 'noopener noreferrer';
                    waLink.className = 'btn btn-primary modal-wa-btn';
                    waLink.appendChild(document.createTextNode('Consultar por WhatsApp '));
                    // Static SVG icon — safe to use innerHTML on a fresh span containing
                    // only trusted markup (no user data concatenated into it).
                    var icon = document.createElement('span');
                    icon.setAttribute('aria-hidden', 'true');
                    icon.innerHTML = '<svg viewBox="0 0 32 32" width="18" height="18" fill="currentColor"><path d="M16.004 0C7.166 0 .002 7.16.002 15.995c0 2.818.737 5.574 2.14 7.998L0 32l8.245-2.102a16.02 16.02 0 007.755 1.978h.004C24.838 31.876 32 24.716 32 15.995 32 7.16 24.838 0 16.004 0zm7.34 19.293c-.402-.202-2.38-1.174-2.75-1.31-.37-.132-.64-.2-.91.202-.27.4-1.045 1.31-1.282 1.58-.236.27-.473.304-.876.1-.402-.2-1.698-.626-3.234-1.995-1.195-1.066-2.002-2.383-2.237-2.785-.236-.402-.025-.62.177-.82.182-.18.402-.47.604-.706.2-.236.268-.404.402-.674.134-.27.067-.506-.033-.708-.1-.2-.91-2.192-1.247-3.002-.328-.788-.662-.682-.91-.694l-.774-.014c-.268 0-.706.1-1.076.506-.37.404-1.414 1.38-1.414 3.37 0 1.988 1.448 3.908 1.65 4.178.2.27 2.85 4.348 6.904 6.098.964.416 1.717.664 2.304.85.968.308 1.85.264 2.547.16.777-.116 2.38-.974 2.716-1.914.336-.94.336-1.746.236-1.914-.1-.168-.37-.268-.776-.47z"/></svg>';
                    waLink.appendChild(icon);
                    info.appendChild(waLink);

                    box.replaceChildren(imgWrap, info);
                })
                .catch(function () {
                    setLoading(box, 'Error al cargar el producto.');
                });
        }
    }

    /* ═══ TRACK WHATSAPP CLICKS (GA4 + Meta hybrid) ═══ */
    document.addEventListener('click', function (e) {
        var link = e.target.closest('a[href*="wa.me"], .wa-float');
        if (!link) return;
        if (typeof gtag === 'function') {
            gtag('event', 'whatsapp_click', {
                event_category: 'lead',
                event_label: window.location.pathname
            });
        }
        epMetaTrack('Contact', {
            content_name: 'whatsapp_click',
            content_category: window.location.pathname
        });
    }, true);

    /* ═══ TRACK CONTACT FORM SUBMIT (GA4 + Meta hybrid) ═══ */
    var contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function () {
            if (typeof gtag === 'function') {
                gtag('event', 'form_submit', {
                    event_category: 'lead',
                    event_label: 'contacto'
                });
            }
            var eventId = epMetaEventId();
            var hidden = contactForm.querySelector('input[name="meta_event_id"]');
            if (hidden) hidden.value = eventId;
            // Pixel fires client-side; server reads the hidden input and fires CAPI with the same event_id for dedup
            epMetaTrack('Lead', {
                content_name: 'contact_form',
                content_category: 'lead'
            }, { eventId: eventId, capi: false });
        });
    }

    /* ═══ TRACK PRODUCT MODAL OPEN (Meta ViewContent, pixel-only) ═══ */
    document.addEventListener('click', function (e) {
        var card = e.target.closest('.product-card[data-slug]');
        if (!card) return;
        epMetaTrack('ViewContent', {
            content_type: 'product',
            content_ids: [card.getAttribute('data-slug')],
            content_name: card.getAttribute('data-name') || ''
        }, { capi: false });
    });

});
