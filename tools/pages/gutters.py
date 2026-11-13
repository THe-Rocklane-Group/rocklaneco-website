"""Gutters page. Section rhythm: split hero (blue + tall K-style photo), 01 services (white),
02 communities & warehouses (Light Grey), 03 process (blue photo band), 04 colors (white),
05 warning signs (Light Grey), 06 warranty (white), 07 service area (photo/blue), final CTA.
"""
from site_common import *

PATH = "/gutters"
CURRENT = "/gutters"
TITLE = "Seamless Gutters & Gutter Guards in Indianapolis | Rocklane Co."
DESC = ("Seamless gutters custom-cut on site, gutter guards, repair and cleaning in central Indiana, "
        "with a 5-year workmanship warranty. Call (317) 898-8696.")

HERO_SIZES = "(max-width:900px) 100vw, 44vw"
HEAD = ('\n  <link rel="preload" as="image" href="/images/photos/k-style-gutters-1200.jpg" '
        'imagesrcset="/images/photos/k-style-gutters-1200.jpg 1200w, /images/photos/k-style-gutters.jpg 1600w" '
        f'imagesizes="{HERO_SIZES}">')

CSS = """
/* gutters: split hero (text on solid Shark Blue gradient; photo beside, never under, the text) */
.g-hero { position: relative; padding: clamp(48px, 6vw, 96px) 0 0; overflow: hidden; isolation: isolate; }
.g-hero-g { display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr); gap: clamp(32px, 5vw, 96px); align-items: end; }
.g-hero-tx { align-self: center; padding-bottom: clamp(56px, 7vw, 112px); }
.g-hero h1 { color: var(--white); font-size: clamp(2.6rem, 6vw, 5rem); line-height: .98; letter-spacing: -.035em; max-width: 11ch; margin-bottom: .4em; }
.g-hero h1 .u { box-shadow: inset 0 -.12em 0 var(--green); }
.g-hero-lede { font-size: clamp(1.05rem, 1.4vw, 1.22rem); line-height: 1.6; max-width: 36rem; margin-bottom: 2rem; }
.g-hero .hero-foot { margin-top: clamp(36px, 6vh, 72px); }
.g-hero-fig { position: relative; margin: 0; }
.g-hero-fig::before { content: ""; position: absolute; left: -22px; bottom: 0; width: 62%; height: 58%; background: var(--green); }
.g-hero-fig img { position: relative; width: 100%; height: clamp(540px, 76vh, 860px); object-fit: cover; object-position: center 74%; box-shadow: var(--shadow-lg); }

/* 01 services: numbered editorial list */
.g-svc { list-style: none; margin: 0 0 2rem; padding: 0; }
.g-svc li { display: grid; grid-template-columns: 64px minmax(0, 1fr); gap: 20px; padding: 24px 0; border-top: 1px solid var(--grey); }
.g-svc li:last-child { border-bottom: 1px solid var(--grey); }
.g-svc .n { align-self: start; padding-top: 10px; border-top: 3px solid var(--green); font-weight: 800; font-size: .82rem; letter-spacing: .16em; color: var(--blue); }
.g-svc h3 { margin-bottom: .3em; }
.g-svc p { margin: 0; }
.g-svc-split { align-items: start; }
.g-svc-split .media-frame { position: sticky; top: 120px; }
.g-svc-split .media-frame img { aspect-ratio: 4 / 4.4; }

/* 02 communities & warehouses */
.g-aud { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: clamp(16px, 2vw, 28px); }
.g-aud .photo-card { min-height: clamp(460px, 46vw, 660px); }
.g-aud .photo-card:nth-child(2) { margin-top: 72px; }
.g-note { display: flex; gap: 14px; align-items: flex-start; max-width: 54rem; margin: 40px 0 0; font-size: .98rem; }
.g-note .i { flex: none; margin-top: .3em; color: var(--blue); font-size: 20px; }

/* 04 colors */
.g-colors .swatches { grid-template-columns: repeat(auto-fill, minmax(112px, 1fr)); }
.g-colors .media-frame img { aspect-ratio: 4 / 4.6; }

/* 05 signs */
.g-signs-ft { display: flex; flex-wrap: wrap; gap: 14px 28px; align-items: center; }

@media (max-width: 980px) {
  .g-svc-split .media-frame { position: relative; top: 0; }
  .g-svc-split .media-frame img, .g-colors .media-frame img { aspect-ratio: 4 / 3; }
}
@media (max-width: 900px) {
  .g-hero-g { grid-template-columns: 1fr; gap: 0; }
  .g-hero-tx { padding-bottom: 48px; }
  .g-hero-fig::before { left: auto; right: calc(-1 * var(--gut)); width: 70%; height: 50%; }
  .g-hero-fig img { height: auto; aspect-ratio: 4 / 3.2; object-position: center 72%; }
}
@media (max-width: 767px) {
  .g-aud { grid-template-columns: 1fr; }
  .g-aud .photo-card:nth-child(2) { margin-top: 0; }
  .g-svc li { grid-template-columns: 1fr; gap: 10px; }
  .g-svc .n { width: 48px; }
}
@media (max-width: 420px) {
  .g-hero .btn { width: 100%; }
}
@media print {
  .g-hero-fig img { height: auto; aspect-ratio: 4 / 3; }
  .g-svc-split .media-frame { position: relative; top: 0; }
  .g-aud .photo-card { break-inside: avoid; }
}
"""

# Gutter colors (kept from the previous page; on-screen colors are approximate).
SWATCHES = [("White", "#F6F6F2"), ("Almond", "#E8DBC3"), ("Clay", "#B9A98C"), ("Bronze", "#5B4633"),
            ("Musket brown", "#5E4D3C"), ("Forest green", "#2F4A36"), ("Black", "#1F1F1F"), ("Copper", "#B4693B")]
SWATCH_LIST = "".join(f'<li><i style="background:{c}" aria-hidden="true"></i>{n}</li>' for n, c in SWATCHES)

SERVICES = [
    ("Seamless installation",
     "We custom-cut seamless gutters on site to fit each roofline, so every run is one continuous length "
     "with no seams along it to loosen or leak. New systems, or replacement of worn-out runs."),
    ("Gutter guards",
     "Gutter guards from leading manufacturers to help prevent clogs, overflow and ice buildup."),
    ("Repair",
     "Repair of a damaged system: sagging runs, separated joints and corners, and loose or leaking downspouts, "
     "fixed at the cause and backed by our 5-year workmanship warranty."),
    ("Cleaning",
     "Seasonal cleaning so gutters and downspouts are clear before the next storm."),
]
SVC_LIST = "".join(f'<li><span class="n" aria-hidden="true">{i:02d}</span><div><h3>{t}</h3><p>{d}</p></div></li>'
                   for i, (t, d) in enumerate(SERVICES, 1))

SIGNS = [("droplet", "Water spilling over the gutter edge in heavy rain"),
         ("alert", "Gutters sagging or pulling away from the fascia"),
         ("tool", "Leaking or separated joints, corners and end caps"),
         ("home", "Water stains or peeling paint on fascia and siding"),
         ("droplet", "Water pooling or soil washing out near the foundation"),
         ("storm", "Downspouts backing up with leaves and debris")]
SIGN_LIST = "".join(f'<li class="reveal" style="--d:{i * .05:.2f}s">{ic(icon)}{t}</li>'
                    for i, (icon, t) in enumerate(SIGNS))

BODY = f"""    <section class="g-hero on-blue" aria-labelledby="h1">
      <div class="wrap g-hero-g">
        <div class="g-hero-tx">
          <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>Gutters</span></nav>
          <span class="eyebrow">Seamless gutters &amp; guards</span>
          <h1 id="h1">Gutters cut to fit, <span class="u">on site.</span></h1>
          <p class="g-hero-lede">Seamless gutter installation, gutter guards, repair and cleaning for homes, condominium and townhome communities, apartment communities and warehouses across central Indiana. Installed by Rocklane crews and backed by our own workmanship warranty.</p>
          <div class="btn-row">
            <a class="btn" href="/contact">Request an Estimate {ic("arrow")}</a>
            <a class="btn btn-outline" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
          </div>
          <div class="hero-foot">
            <span>{ic("clipboard")}5-year workmanship warranty on gutters</span>
            <span>{ic("users")}Owner-operated since 1980</span>
          </div>
        </div>
        <figure class="g-hero-fig">
          {picture("k-style-gutters", "White K-style seamless gutter and downspout along the eave of a two-story home with tan vinyl lap siding under a deep blue sky", HERO_SIZES, eager=True)}
        </figure>
      </div>
    </section>

    <section aria-labelledby="svc-h">
      <div class="wrap">
{sec_hd("01", "What we do", "Move water away from the building.", "Working gutters protect the roof, siding, foundation and landscaping from water damage. Four services, one crew that answers for the result.", "svc-h")}
        <div class="split g-svc-split">
          <div class="reveal">
            <ol class="g-svc">{SVC_LIST}</ol>
            <div class="btn-row"><a class="btn" href="/contact">Request an Estimate {ic("arrow")}</a><a class="text-link" href="tel:{TEL}">{ic("phone")}Call {PHONE}</a></div>
          </div>
          <figure class="media-frame reveal" style="--d:.1s">
            {picture("two-story-home-hero", "New two-story home with charcoal architectural shingles, gray lap siding and white K-style gutters and downspouts", "(max-width:980px) 100vw, 46vw", pos="right center")}
            <div class="tag"><span class="ico ico-blue">{ic("shield")}</span><div><strong>5-year warranty</strong><span>Workmanship on gutter installation and repair</span></div></div>
          </figure>
        </div>
      </div>
    </section>

    <section class="grey" aria-labelledby="aud-h">
      <div class="wrap">
{sec_hd("02", "Homes, communities &amp; warehouses", "From one roofline to a whole property.", f"{SHORT} installs and repairs gutters on single-family homes, across condominium, townhome and apartment communities, and on warehouses and commercial buildings.", "aud-h")}
        <div class="g-aud">
          {photo_card("/property-managers", "condo-community-aerial", "Aerial view of a townhome and condominium community with shingle roofs on tree-lined cul-de-sacs", "Condo, townhome &amp; apartment communities", "Planned, phased gutter work across every building, with status, photos and documents in the customer portal.", "For HOA &amp; property managers", "(max-width:767px) 100vw, 50vw", kicker="Communities")}
          {photo_card("/commercial", "warehouse-dock-doors", "White tilt-up warehouse wall with loading dock doors and yellow bollards", "Warehouses &amp; commercial buildings", f"Commercial gutters and downspouts from {SHORT}, alongside siding and metal wall panels.", "Commercial exteriors", "(max-width:767px) 100vw, 50vw", pos="center 60%", kicker="Commercial")}
        </div>
        <p class="g-note reveal">{ic("building")}<span>Low-slope membrane roofs on commercial buildings are handled by our sister company, Rocklane Commercial Contractors LLC. {SHORT} handles the gutters, siding and metal wall panels.</span></p>
      </div>
    </section>

{process("03")}

    <section aria-labelledby="col-h">
      <div class="wrap split flip g-colors">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">04</span><span class="eyebrow">Finish</span>
          <h2 id="col-h">Colors to match the exterior.</h2>
          <p>Choose from dozens of gutter colors. We&rsquo;ll help you match the trim and roof.</p>
          <ul class="swatches" aria-label="Popular gutter colors">{SWATCH_LIST}</ul>
          <p class="fine muted">A few popular choices. Colors on screen are approximate.</p>
        </div>
        <figure class="media-frame reveal" style="--d:.1s">
          {picture("siding-rooflines", "Close-set homes with vinyl lap siding, shake gables, architectural shingle roofs and brown gutters", "(max-width:980px) 100vw, 46vw", pos="center 40%")}
          <div class="tag"><span class="ico ico-green">{ic("droplet")}</span><div><strong>Matched to the trim</strong><span>Gutter color chosen with your roof and siding</span></div></div>
        </figure>
      </div>
    </section>

    <section class="grey" aria-labelledby="sig-h">
      <div class="wrap">
{sec_hd("05", "Know the warning signs", "Signs your gutters need attention.", "If a repair will do the job, we&rsquo;ll tell you. If the system has reached the end of its life, we&rsquo;ll show you why.", "sig-h")}
        <ul class="signs">{SIGN_LIST}</ul>
        <div class="g-signs-ft reveal"><a class="btn" href="/contact">Request an Estimate {ic("arrow")}</a><a class="text-link" href="tel:{TEL}">{ic("phone")}Call {PHONE}</a></div>
      </div>
    </section>

{warranty_band("06", photo="indiana-farmhouse-fall", alt="White two-story Indiana farmhouse with a shingle roof among bright orange and gold fall maples")}

{service_area("07")}

{CTA}"""
