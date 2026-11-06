// Menu toggle and footer year (kept out of the HTML so pages work with a strict CSP).
(function () {
  var t = document.querySelector('.menu-toggle'), n = document.getElementById('nav');
  if (t && n) t.addEventListener('click', function () {
    var o = n.classList.toggle('open'); t.setAttribute('aria-expanded', o);
  });
  var y = document.getElementById('yr');
  if (y) y.textContent = new Date().getFullYear();
})();
