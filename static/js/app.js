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
        // Open modal on product card click
        document.addEventListener('click', function (e) {
            var card = e.target.closest('.product-card[data-slug]');
            if (!card) return;
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

        function openProductModal(slug) {
            var box = modal.querySelector('.modal-body');
            box.innerHTML = '<div class="modal-loading">Cargando...</div>';
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';

            fetch('/api/producto/' + slug)
                .then(function (r) { return r.json(); })
                .then(function (p) {
                    var imgHtml = p.image
                        ? '<img src="' + p.image + '" alt="' + p.name + '">'
                        : '<span class="modal-placeholder">' + p.name.charAt(0) + '</span>';

                    var detailsHtml = '';
                    if (p.origin) {
                        detailsHtml += '<div class="modal-detail-row"><strong>Origen</strong><span>' + p.origin + '</span></div>';
                    }
                    if (p.presentation) {
                        detailsHtml += '<div class="modal-detail-row"><strong>Presentación</strong><span>' + p.presentation + '</span></div>';
                    }
                    if (p.category_name) {
                        detailsHtml += '<div class="modal-detail-row"><strong>Categoría</strong><span>' + p.category_name + '</span></div>';
                    }

                    var descHtml = '';
                    if (p.description) {
                        descHtml = '<div class="modal-desc"><h3>Descripción</h3><p>' + p.description + '</p></div>';
                    }

                    // Build WhatsApp link with dynamic number
                    var waDigits = document.querySelector('.wa-float') ? document.querySelector('.wa-float').href.replace('https://wa.me/', '') : '';
                    var waLink = 'https://wa.me/' + waDigits + '?text=' + encodeURIComponent('Hola, me interesa el producto: ' + p.name);

                    box.innerHTML =
                        '<div class="modal-img">' + imgHtml + '</div>' +
                        '<div class="modal-info">' +
                            (p.category_name ? '<span class="modal-cat">' + p.category_name + '</span>' : '') +
                            '<h2 class="modal-title">' + p.name + '</h2>' +
                            (detailsHtml ? '<div class="modal-details">' + detailsHtml + '</div>' : '') +
                            descHtml +
                            '<a href="' + waLink + '" target="_blank" class="btn btn-primary modal-wa-btn">' +
                                'Consultar por WhatsApp ' +
                                '<svg viewBox="0 0 32 32" width="18" height="18" fill="currentColor"><path d="M16.004 0C7.166 0 .002 7.16.002 15.995c0 2.818.737 5.574 2.14 7.998L0 32l8.245-2.102a16.02 16.02 0 007.755 1.978h.004C24.838 31.876 32 24.716 32 15.995 32 7.16 24.838 0 16.004 0zm7.34 19.293c-.402-.202-2.38-1.174-2.75-1.31-.37-.132-.64-.2-.91.202-.27.4-1.045 1.31-1.282 1.58-.236.27-.473.304-.876.1-.402-.2-1.698-.626-3.234-1.995-1.195-1.066-2.002-2.383-2.237-2.785-.236-.402-.025-.62.177-.82.182-.18.402-.47.604-.706.2-.236.268-.404.402-.674.134-.27.067-.506-.033-.708-.1-.2-.91-2.192-1.247-3.002-.328-.788-.662-.682-.91-.694l-.774-.014c-.268 0-.706.1-1.076.506-.37.404-1.414 1.38-1.414 3.37 0 1.988 1.448 3.908 1.65 4.178.2.27 2.85 4.348 6.904 6.098.964.416 1.717.664 2.304.85.968.308 1.85.264 2.547.16.777-.116 2.38-.974 2.716-1.914.336-.94.336-1.746.236-1.914-.1-.168-.37-.268-.776-.47z"/></svg>' +
                            '</a>' +
                        '</div>';
                })
                .catch(function () {
                    box.innerHTML = '<div class="modal-loading">Error al cargar el producto.</div>';
                });
        }
    }

});
