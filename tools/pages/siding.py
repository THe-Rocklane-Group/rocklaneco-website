"""Siding page. Section rhythm: photo hero (blue), 01 services split (white),
02 fiber cement vs vinyl comparison (Light Grey), 03 installation details on the
siding-texture band (blue), 04 warranty (white), 05 warehouse & commercial siding (Light Grey),
06 process (blue), partners (white), final CTA.
"""
from site_common import *

PATH = "/siding"
CURRENT = "/siding"
TITLE = "Siding Installation & Repair in Indianapolis | Rocklane Co."
DESC = ("James Hardie fiber cement and Variform vinyl siding installation and repair across central Indiana, "
        "installed by Rocklane crews and backed by a 5-year workmanship warranty.")
HEAD = ('\n  <link rel="preload" as="image" href="/images/photos/siding-rooflines-1200.jpg" '
        'imagesrcset="/images/photos/siding-rooflines-1200.jpg 1200w, /images/photos/siding-rooflines.jpg 2400w" '
        'imagesizes="100vw">')

CSS = """
    .sd-hero-facts { display: flex; flex-wrap: wrap; gap: 10px 28px; max-width: 40rem; margin: 2rem 0 0; padding: 0; list-style: none; font-weight: 600; font-size: .95rem; }
    .sd-hero-facts li { display: inline-flex; align-items: center; gap: 10px; }
    .sd-hero-facts .i { font-size: 18px; color: var(--green); }
    .page-head .btn-row { margin-top: 2rem; }

    .sd-intro h2 { max-width: 15ch; }
    .sd-intro .checks { margin-top: 1.8rem; }

    /* 02 comparison */
    .sd-mats { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: clamp(16px, 2vw, 28px); margin-bottom: clamp(28px, 4vw, 48px); }
    .sd-mat { background: var(--white); padding: clamp(28px, 3.4vw, 48px); border-top: 4px solid var(--blue); box-shadow: var(--shadow-sm); }
    .sd-mat .lvl { display: block; font-size: .75rem; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: var(--char); margin-bottom: .9rem; }
    .sd-mat h3 { font-size: clamp(1.5rem, 2.4vw, 2rem); }
    .sd-mat p { margin: 0; }
    .sd-table { width: 100%; border-collapse: collapse; background: var(--white); box-shadow: var(--shadow-sm); font-size: 1rem; }
    .sd-table caption { text-align: left; font-weight: 700; color: var(--char); padding: 0 0 14px; }
    .sd-table th, .sd-table td { padding: 18px clamp(16px, 2vw, 28px); text-align: left; vertical-align: top; border-bottom: 1px solid var(--grey); line-height: 1.55; }
    .sd-table thead th { background: var(--blue); color: var(--white); font-size: .8rem; letter-spacing: .14em; text-transform: uppercase; border-bottom: 4px solid var(--green); }
    .sd-table tbody th { width: 22%; color: var(--blue); font-weight: 700; }
    .sd-table tbody tr:last-child > * { border-bottom: 0; }
    .sd-note { margin: 22px 0 0; }

    /* 03 details band on the siding texture */
    .sd-band { position: relative; isolation: isolate; overflow: hidden; background: var(--blue-d); }
    .sd-band-bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: -2; }
    .sd-band::before { content: ""; position: absolute; inset: 0; z-index: -1; background: linear-gradient(160deg, rgba(30,90,168,.9), rgba(23,72,138,.93)); }
    .sd-details { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); border-top: 1px solid rgba(255,255,255,.35); }
    .sd-details li { padding: 32px clamp(18px, 2vw, 32px) 8px 0; }
    .sd-details li + li { padding-left: clamp(18px, 2vw, 32px); border-left: 1px solid rgba(255,255,255,.35); }
    .sd-details .i { display: block; font-size: 30px; color: var(--green); margin-bottom: 18px; }
    .sd-details h3 { font-size: 1.2rem; margin-bottom: .5em; }
    .sd-details p { margin: 0; font-size: .98rem; line-height: 1.6; }

    /* 05 warehouse & commercial */
    .sd-com .media-frame img { aspect-ratio: 16 / 11; }
    .sd-com .checks { margin-top: 1.6rem; }

    @media (max-width: 1100px) {
      .sd-details { grid-template-columns: 1fr 1fr; }
      .sd-details li:nth-child(3) { padding-left: 0; border-left: 0; }
      .sd-details li:nth-child(n+3) { border-top: 1px solid rgba(255,255,255,.35); margin-top: 24px; }
    }
    @media (max-width: 767px) {
      .sd-mats { grid-template-columns: 1fr; }
      .sd-details { grid-template-columns: 1fr; }
      .sd-details li, .sd-details li + li { padding: 26px 0 0; border-left: 0; }
      .sd-details li + li { border-top: 1px solid rgba(255,255,255,.35); margin-top: 26px; }
    }
    /* Comparison table stacks below 700px: one block per row, the row label as its heading,
       each cell labelled from data-label. The caption is made a plain block so it is not
       shrink-wrapped to min-content inside an anonymous table box (one word per line). */
    @media (max-width: 700px) {
      .sd-table { display: block; width: 100%; background: transparent; box-shadow: none; }
      .sd-table caption { display: block; width: 100%; padding: 0 0 14px; font-size: 1.05rem; line-height: 1.4; }
      .sd-table thead { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
      .sd-table tbody, .sd-table tr, .sd-table th, .sd-table td { display: block; width: 100%; min-width: 0; }
      .sd-table tbody { display: grid; gap: 12px; }
      .sd-table tr { background: var(--white); box-shadow: var(--shadow-sm); border-top: 4px solid var(--blue); padding: 18px 20px 12px; }
      .sd-table tbody th { width: auto; padding: 0 0 10px; margin-bottom: 4px; border: 0; border-bottom: 1px solid var(--grey); font-size: 1.1rem; line-height: 1.3; }
      .sd-table td { padding: 10px 0; border: 0; overflow-wrap: anywhere; }
      .sd-table td + td { border-top: 1px solid var(--grey); }
      .sd-table tbody tr:last-child > * { border-bottom: 0; }
      .sd-table tbody tr:last-child th { border-bottom: 1px solid var(--grey); }
      .sd-table td::before { content: attr(data-label); display: block; font-size: .72rem; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--blue); margin-bottom: 4px; }
    }
    @media print {
      .sd-band { background: var(--blue-d); }
    }
"""

HERO = page_head(
    "James Hardie&reg; fiber cement &middot; Variform vinyl",
    "Siding, installed by our own crews.",
    "We install James Hardie&reg; fiber cement and Variform vinyl siding on homes, condominium and townhome "
    "communities, apartment buildings and commercial buildings across central Indiana.",
    "Siding", photo="siding-rooflines", alt="", pos="center 35%")

# Add the hero call to action and fact row inside the page_head wrap (after the lead).
HERO = HERO.replace("</p>\n      </div>\n    </div>", f"""</p>
        <div class="btn-row">
          <a class="btn" href="/contact">Request an Estimate {ic("arrow")}</a>
          <a class="btn btn-outline" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
        </div>
        <ul class="sd-hero-facts">
          <li>{ic("users")}Installed by Rocklane crews</li>
          <li>{ic("shield")}5-year workmanship warranty on siding</li>
          <li>{ic("clock")}Owner-operated since 1980</li>
        </ul>
      </div>
    </div>""", 1)

ROWS = [
    ("Material", "Fiber cement boards made from cement, sand and cellulose fibers",
     "Vinyl siding panels"),
    ("Look", "Crisp, deep lines with a painted finish",
     "Lap and shake profiles in a wide range of colors"),
    ("Upkeep", "Low; the painted finish may need refreshing over the long term",
     "Very little; no painting, an occasional wash"),
    ("Installation", "Heavier boards cut and fastened with fiber-cement tooling",
     "Lighter panels hung to allow for seasonal expansion and contraction"),
    ("Often chosen for", "Homes where a rigid, painted-wood look matters most",
     "Homes and multi-building communities that want low upkeep"),
    ("Workmanship warranty", "5 years from Rocklane Co.", "5 years from Rocklane Co."),
]
ROW_HTML = "\n".join(
    f'            <tr><th scope="row">{r}</th><td data-label="James Hardie&reg; fiber cement">{a}</td>'
    f'<td data-label="Variform vinyl">{b}</td></tr>' for r, a, b in ROWS)

BODY = f"""{HERO}

    <section aria-labelledby="svc-h">
      <div class="wrap split sd-intro">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">01</span>
          <span class="eyebrow">Replacement &middot; Repair &middot; Inspection</span>
          <h2 id="svc-h">Siding that protects the building envelope.</h2>
          <p class="lead">Siding is the first layer of protection for every wall. We install it to keep water out for decades, and we back our siding work with a 5-year workmanship warranty.</p>
          <ul class="checks">
            <li><strong>Siding replacement:</strong> James Hardie&reg; fiber cement or Variform vinyl siding, installed with precise flashing and trim details.</li>
            <li><strong>Siding repair:</strong> storm, impact and moisture damage repaired and matched to the existing exterior.</li>
            <li><strong>Inspections:</strong> we identify problem areas before they turn into rot, mold or interior damage.</li>
          </ul>
          <a class="text-link" href="#compare-h">Compare fiber cement and vinyl {ic("arrow")}</a>
        </div>
        <div class="offset-media reveal" style="--d:.1s">
          {picture("two-story-home-hero", "Two-story suburban home with gray vinyl lap siding, a stone base, charcoal shingles and white gutters", "(max-width:980px) 100vw, 50vw", cls="om-big", pos="70% center")}
          {picture("indy-apartments-courtyard", "Garden-style apartment buildings in Indianapolis with brick lower floors and vinyl siding above", "(max-width:980px) 46vw, 23vw", cls="om-sm")}
        </div>
      </div>
    </section>

    <section class="grey" aria-labelledby="compare-h">
      <div class="wrap">
{sec_hd("02", "Fiber cement vs. vinyl", "Two materials. One crew standard.", "We install both, with the same Rocklane crews and the same workmanship warranty. Here is how they compare, so you can choose the right siding for your building.", "compare-h")}
        <div class="sd-mats">
          <article class="sd-mat reveal">
            <span class="lvl">Fiber cement</span>
            <h3>James Hardie&reg; siding</h3>
            <p>We install James Hardie&reg; siding: rigid fiber cement boards with crisp lines and a painted finish, a strong choice when you want the look of painted wood with very little movement.</p>
          </article>
          <article class="sd-mat reveal" style="--d:.08s">
            <span class="lvl">Vinyl</span>
            <h3>Variform vinyl siding</h3>
            <p>Vinyl siding that stands up to Indiana weather with very little upkeep, in lap and shake profiles, a practical choice for single homes and whole communities.</p>
          </article>
        </div>
        <div class="reveal">
          <table class="sd-table">
            <caption>Fiber cement and vinyl siding at a glance</caption>
            <thead><tr><th scope="col"><span class="sr">Feature</span></th><th scope="col">James Hardie&reg; fiber cement</th><th scope="col">Variform vinyl</th></tr></thead>
            <tbody>
{ROW_HTML}
            </tbody>
          </table>
          <p class="sd-note fine">Manufacturers set their own product warranties. Our workmanship warranty covers the installation.</p>
        </div>
      </div>
    </section>

    <section class="sd-band on-blue" aria-labelledby="det-h">
      {picture("broad-ripple-siding-texture", "", "100vw", cls="sd-band-bg")}
      <div class="wrap">
{sec_hd("03", "How we install", "The details decide how long siding lasts.", "Water gets behind siding at its edges and openings. That is where our crews take the most care.", "det-h")}
        <ul class="sd-details">
          <li class="reveal">{ic("droplet")}<h3>Flashing</h3><p>Precise flashing at windows, doors and rooflines, so water is turned away from the wall.</p></li>
          <li class="reveal" style="--d:.06s">{ic("layers")}<h3>Trim details</h3><p>Trim fitted cleanly around corners and openings, finishing the wall and closing the gaps.</p></li>
          <li class="reveal" style="--d:.12s">{ic("tool")}<h3>Matched repairs</h3><p>Storm, impact and moisture damage repaired and matched to the existing exterior.</p></li>
          <li class="reveal" style="--d:.18s">{ic("search")}<h3>Problem areas found early</h3><p>We look for trouble spots before they turn into rot, mold or interior damage.</p></li>
        </ul>
      </div>
    </section>

{warranty_band("04", photo="indiana-farmhouse-fall", alt="White two-story Indiana farmhouse with a shingle roof among bright fall maples", small="k-style-gutters", small_alt="Tan vinyl lap siding with a white seamless gutter and downspout against a blue sky")}

    <section class="grey sd-com" aria-labelledby="whs-h">
      <div class="wrap split flip">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">05</span>
          <span class="eyebrow">Warehouses &amp; commercial buildings</span>
          <h2 id="whs-h">Siding and metal wall panels for buildings that work hard.</h2>
          <p>{SHORT} also installs siding, metal wall panels and gutters on warehouses and commercial buildings, with the same crews and the same owners in daily management. If something goes wrong, you get an owner on the phone.</p>
          <ul class="checks">
            <li>Siding on commercial buildings</li>
            <li>Metal wall panels</li>
            <li>Commercial gutters and downspouts</li>
          </ul>
          <a class="text-link" href="/commercial">Commercial exteriors {ic("arrow")}</a>
        </div>
        <figure class="media-frame reveal" style="--d:.1s">
          {picture("warehouse-dock-doors", "White tilt-up warehouse wall with loading dock doors and yellow bollards", "(max-width:980px) 100vw, 50vw", pos="center 60%")}
          <div class="tag"><span class="ico ico-blue">{ic("building")}</span><div><strong>Exterior walls &amp; water</strong><span>Siding, metal wall panels and gutters</span></div></div>
        </figure>
      </div>
    </section>

{process("06")}

{PARTNERS}

{CTA}"""
