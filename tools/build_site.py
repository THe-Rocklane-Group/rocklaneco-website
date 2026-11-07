"""Builds the Rocklane Co. website (plain HTML) into the repository root.

Run:  cd <repo> && python tools/build_site.py
Copy, claims, colors and type follow The Rocklane Group Brand Foundation v2.

Layout:
  tools/site_common.py   constants, claims, icons, picture(), page() chrome, shared blocks
  tools/pages/<slug>.py  one module per page: PATH, CURRENT, TITLE, DESC, CSS, BODY
                         (+ optional HEAD, SCRIPTS, INDEX, OUT, SITEMAP)
  tools/DESIGN.md        component guide for page authors
Edit a page module, re-run, then commit and push.
"""
import importlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from site_common import DOMAIN, page  # noqa: E402

# Order = sitemap order.
PAGE_MODULES = ["home", "roofing", "siding", "gutters", "commercial", "property_managers", "about",
                "contact", "privacy", "portal_terms", "portal", "staff", "notfound"]

PAGES = []
for name in PAGE_MODULES:
    m = importlib.import_module("pages." + name)
    out = getattr(m, "OUT", None) or (m.PATH.strip("/") or "index") + ".html"
    PAGES.append(dict(
        name=name, out=out, path=m.PATH, sitemap=getattr(m, "SITEMAP", True),
        html=page(m.PATH, m.TITLE, m.DESC, m.BODY, m.CURRENT,
                  head=getattr(m, "HEAD", ""), scripts=getattr(m, "SCRIPTS", ""),
                  index=getattr(m, "INDEX", True), css=getattr(m, "CSS", ""))))

# Old Contractor Web Zone addresses -> new pages (GitHub Pages serves /x as /x.html).
# Note: file names that differ only by case collide on macOS, so none may match a page above.
REDIRECTS = {
    "about-us": "/about", "roofing-overview": "/roofing", "siding-overview": "/siding",
    "gutters-2": "/gutters", "gutter-install4": "/gutters", "gutter-protection4": "/gutters",
    "gutter-cleaning4": "/gutters", "Variform-Siding": "/siding", "Contact-Us": "/contact",
    "request-estimate": "/contact", "instant-roofing-estimate": "/contact", "Reviews": "/",
    "Other-Services": "/", "Privacy": "/privacy-policy", "roofs-for-troops-me": "/roofing",
    "gaf-me23-overview": "/roofing", "gaf-roof-system23": "/roofing", "gaf-me-attic-ventilation": "/roofing",
    "gaf-warranty23": "/roofing", "tline-hdz23": "/roofing", "visualizer23": "/roofing",
    "gaf-danger-signs23": "/roofing",
}

# Destination names for the redirect stubs' <title> and link text.
REDIRECT_TITLES = {"/": "Home", "/about": "About", "/roofing": "Roofing", "/siding": "Siding",
                   "/gutters": "Gutters", "/contact": "Contact", "/privacy-policy": "Privacy Policy"}


def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


names = {p["out"].lower() for p in PAGES}
assert len(names) == len(PAGES), "two page modules write the same file"
for old in REDIRECTS:
    assert old.lower() + ".html" not in names, "redirect collides with page: " + old

for p in PAGES:
    write(p["out"], p["html"])

for old, new in REDIRECTS.items():
    dest = REDIRECT_TITLES.get(new, new)
    write(old + ".html", f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Moved to {dest} | Rocklane Co.</title>
<link rel="canonical" href="{DOMAIN}{new}">
<meta http-equiv="refresh" content="0; url={new}">
</head><body><p>This page has moved to <a href="{new}">{dest}</a> ({DOMAIN}{new}).</p></body></html>
""")

urls = "".join(f"  <url><loc>{DOMAIN}{p['path']}</loc></url>\n" for p in PAGES if p["sitemap"])
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")

write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /portal/\n\nSitemap: {DOMAIN}/sitemap.xml\n")

write("CNAME", "rocklaneco.com")  # no trailing newline, matching the file GitHub Pages wrote

write(os.path.join("js", "site.js"), """// Header shrink, menu toggle, footer year and scroll reveal.
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
""")

write(os.path.join("js", "estimate.js"), """// Contact-page estimate form. Sends to the Rocklane Apps Script, which emails the office.
import { SCRIPT_URL } from "/portal/config.js";

const form = document.getElementById("f-estimate");
const msg = document.getElementById("estimate-msg");
const started = Date.now();

if (/^https:\\/\\/script\\.google\\.com\\/macros\\/s\\/[\\w-]+\\/exec$/.test(SCRIPT_URL)) {
  form.hidden = false;
  document.getElementById("estimate-fallback").hidden = true;
}

function show(text, kind) { msg.hidden = false; msg.className = "notice notice-" + kind; msg.textContent = text; }

form.addEventListener("submit", async (ev) => {
  ev.preventDefault();
  if (!form.reportValidity()) return;
  const data = Object.fromEntries(new FormData(form));
  data.action = "estimate";
  data.elapsedMs = Date.now() - started;
  const btn = form.querySelector("button");
  btn.disabled = true;
  try {
    const res = await fetch(SCRIPT_URL, { method: "POST", headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify(data), redirect: "follow" });
    const out = await res.json();
    if (!out.ok) throw new Error(out.error);
    form.reset();
    show("Thank you. We received your request and emailed you a confirmation. Our team will contact you within one business day.", "ok");
  } catch (e) {
    show((e && e.message) || "We couldn't send your request. Please call (317) 898-8696.", "error");
  }
  btn.disabled = false;
});
""")

write("_config.yml", "# GitHub Pages: publish only the website, not the tooling kept in this repository.\n"
      "exclude: [tools, firebase, apps-script, README.md]\n")

print("built", len(PAGES), "pages and", len(REDIRECTS), "redirects into", os.path.normpath(OUT))
