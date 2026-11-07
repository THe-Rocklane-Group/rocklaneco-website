"""404 page: a full-height Shark Blue block with the Rocklane lockup on a white card,
direct links to the main service pages and Contact, and the office phone. No search.
All links are root-absolute because GitHub Pages serves 404.html at any depth.
"""
from site_common import *

PATH = "/404"
CURRENT = None
TITLE = 'Page Not Found | Rocklane Co.'
DESC = 'This page has moved. Visit Rocklane Co. for roofing, siding and gutters in central Indiana.'
OUT = "404.html"
SITEMAP = False
INDEX = False

CSS = """
.nf4 { position: relative; isolation: isolate; overflow: hidden; display: grid; align-items: center;
  min-height: calc(100vh - 118px); min-height: calc(100svh - 118px); padding: clamp(56px, 8vw, 112px) 0; }
.nf4-code { position: absolute; z-index: -1; right: -.04em; bottom: -.18em; font-weight: 900; line-height: .8;
  font-size: clamp(11rem, 34vw, 30rem); letter-spacing: -.06em; color: transparent;
  -webkit-text-stroke: 2px rgba(255,255,255,.22); pointer-events: none; user-select: none; }
.nf4-in { display: grid; gap: clamp(40px, 6vw, 96px); align-items: center; }
.nf4-logo { display: block; width: fit-content; max-width: 100%; background: var(--white); padding: 22px 24px; margin-bottom: clamp(28px, 4vw, 44px); box-shadow: var(--shadow-lg); }
.nf4-logo img { display: block; width: 240px; max-width: 100%; height: auto; }
.nf4 h1 { font-size: clamp(2.4rem, 5.6vw, 4.4rem); max-width: 14ch; margin-bottom: .35em; }
.nf4-lede { font-size: clamp(1.05rem, 1.6vw, 1.25rem); max-width: 34rem; margin: 0 0 1.8em; }
.nf4-call { display: flex; flex-wrap: wrap; align-items: center; gap: 12px 22px; }
.nf4-call .fine { margin: 0; font-size: .9rem; }
.nf4-links { list-style: none; margin: 0; padding: 0; display: grid; gap: 12px; }
.nf4-links a { display: grid; grid-template-columns: 48px minmax(0, 1fr) auto; align-items: center; gap: 18px;
  min-height: 76px; padding: 14px 20px; border: 1px solid rgba(255,255,255,.55); text-decoration: none;
  transition: background-color .2s var(--ease), border-color .2s var(--ease); }
.nf4-links .ico { background: rgba(255,255,255,.12); color: var(--green); }
.nf4-links strong { display: block; font-size: 1.12rem; line-height: 1.2; }
.nf4-links small { display: block; font-size: .9rem; line-height: 1.45; margin-top: 3px; }
.nf4-links .go { font-size: 20px; transition: transform .2s var(--ease); }
.nf4-links a:hover { background-color: var(--white); border-color: var(--white); }
.nf4-links a:hover strong, .nf4-links a:hover small, .nf4-links a:hover .go { color: var(--blue); }
.nf4-links a:hover .ico { background: var(--blue); color: var(--white); }
.nf4-links a:hover .go { transform: translateX(4px); }
@media (min-width: 1024px) { .nf4-in { grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr); } }
@media (max-width: 479px) {
  .nf4-links a { grid-template-columns: 40px minmax(0, 1fr) auto; gap: 14px; padding: 12px 14px; }
  .nf4-links .ico { width: 40px; height: 40px; font-size: 19px; }
}
@media print { .nf4 { min-height: 0; } .nf4-code { display: none; } }
"""

LINKS = [
    ("/roofing", "home", "Roofing", "Asphalt shingle replacement, repair and storm-damage inspection"),
    ("/siding", "layers", "Siding", "James Hardie&reg; fiber cement and Variform vinyl siding"),
    ("/gutters", "droplet", "Gutters", "Seamless gutters cut on site, guards, repair and cleaning"),
    ("/commercial", "building", "Commercial", "Gutters, siding and metal wall panels for warehouses and commercial buildings"),
    ("/contact", "mail", "Contact", "Request an Estimate or send the office a note"),
]

ITEMS = "\n".join(f"""            <li><a href="{h}"><span class="ico">{ic(i)}</span><span><strong>{t}</strong><small>{d}</small></span>{ic("arrow", "i go")}</a></li>"""
                  for h, i, t, d in LINKS)

BODY = f"""    <section class="nf4 on-blue" aria-labelledby="nf-h">
      <span class="nf4-code" aria-hidden="true">404</span>
      <div class="wrap nf4-in">
        <div>
          <!-- Approved Rocklane Co. primary lockup on a white card. Do not stretch, crop, recolor or add effects. -->
          <div class="nf4-logo"><img src="/images/rocklane-co-logo.jpg" width="560" height="135" alt="Rocklane Co. General Contractors LLC"></div>
          <span class="eyebrow">Error 404</span>
          <h1 id="nf-h">This page has moved.</h1>
          <p class="nf4-lede">The address may be from our old website. Pick where you were headed, or call the office and we&rsquo;ll point you the right way.</p>
          <div class="nf4-call">
            <a class="btn" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
            <p class="fine">{HOURS} &middot; {HOURS_SAT}</p>
          </div>
        </div>
        <nav aria-label="Popular pages">
          <ul class="nf4-links">
{ITEMS}
          </ul>
          <p class="fine" style="margin:18px 0 0"><a href="/">Back to the {SHORT} home page</a></p>
        </nav>
      </div>
    </section>"""
