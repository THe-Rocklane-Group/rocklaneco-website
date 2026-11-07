// Header shrink, menu toggle, footer year and scroll reveal.
// Menu: opening moves focus to the first link; Escape closes and returns focus to the toggle;
// focus leaving the menu (and its toggle) closes it, so tab order never runs on behind it.
// Kept out of the HTML so pages work with a strict CSP. Content is visible without JS.
(function () {
  var doc = document.documentElement, hdr = document.querySelector('.site-header');
  var t = document.querySelector('.menu-toggle'), n = document.getElementById('nav');

  function isOpen() { return !!(n && n.classList.contains('open')); }
  function setMenu(open, focusBack) {
    if (!t || !n) return;
    n.classList.toggle('open', open);
    t.setAttribute('aria-expanded', String(open));
    if (hdr) hdr.classList.toggle('menu-open', open);
    if (open) {
      var first = n.querySelector('a');
      if (first) first.focus();
    } else if (focusBack) {
      t.focus();
    }
  }
  if (t && n) {
    t.addEventListener('click', function () { setMenu(!isOpen()); });
    document.addEventListener('keydown', function (e) {
      if ((e.key === 'Escape' || e.key === 'Esc') && isOpen()) setMenu(false, true);
    });
    n.addEventListener('click', function (e) { if (e.target.closest && e.target.closest('a')) setMenu(false); });
    function leaving(e) {
      var to = e.relatedTarget;
      if (isOpen() && to && !n.contains(to) && to !== t && !t.contains(to)) setMenu(false);
    }
    n.addEventListener('focusout', leaving);
    t.addEventListener('focusout', leaving);
    window.addEventListener('resize', function () { if (window.innerWidth >= 1100 && isOpen()) setMenu(false); });
  }

  var y = document.getElementById('yr');
  if (y) y.textContent = new Date().getFullYear();

  function onScroll() {
    var s = window.scrollY > 40;
    if (hdr) hdr.classList.toggle('scrolled', s);
    document.body.classList.toggle('scrolled', s);
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Reveal on scroll: only when motion is allowed and IntersectionObserver exists.
  // Anything already on screen is shown at once; CSS hides .reveal only under .js-reveal.
  var items = [].slice.call(document.querySelectorAll('.reveal'));
  var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!items.length || calm || !('IntersectionObserver' in window)) return;
  var h = window.innerHeight;
  items.forEach(function (el) { if (el.getBoundingClientRect().top < h * 0.92) el.classList.add('in'); });
  doc.classList.add('js-reveal');
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -8% 0px' });
  items.forEach(function (el) { if (!el.classList.contains('in')) io.observe(el); });
  window.addEventListener('beforeprint', function () { items.forEach(function (el) { el.classList.add('in'); }); });
})();
