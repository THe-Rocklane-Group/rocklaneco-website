"""Home page, ported from mockup A ("Editorial premium") with mockup B's stat band and
mockup C's portal status card grafted in. Section rhythm: hero (photo/blue), stats (white),
01 services (white), 02 audiences (Light Grey), 03 warranty (white), 04 GAF (Light Grey),
05 process (blue), 06 commercial (blue band + white cards), 07 HOA (Light Grey), partners (white),
08 service area (photo/blue), final CTA.
"""
from site_common import *

PATH = "/"
CURRENT = None
OUT = "index.html"
TITLE = "Rocklane Co. | Roofing, Siding & Gutters in Indianapolis Since 1980"
DESC = ("Owner-operated roofing, siding and gutter contractor serving central Indiana since 1980. "
        "A GAF Master Elite roofing contractor with a 10-year workmanship warranty on roof replacements.")
HEAD = ('\n  <link rel="preload" as="image" href="/images/photos/carmel-townhomes-aerial-1200.jpg" '
        'imagesrcset="/images/photos/carmel-townhomes-aerial-1200.jpg 1200w, /images/photos/carmel-townhomes-aerial.jpg 2400w" '
        'imagesizes="100vw">')
CSS = ""

AUD_SIZES = "(max-width:767px) 100vw, (max-width:1100px) 50vw, 25vw"

BODY = f"""    <section class="hero on-blue" aria-labelledby="h1">
      {picture("carmel-townhomes-aerial", "Golden-hour aerial view of brick townhomes and condominiums with architectural shingle roofs around a reflecting pool in Carmel, Indiana", "100vw", cls="hero-bg", eager=True)}
      <div class="wrap hero-in">
        <span class="eyebrow">Central Indiana &middot; Owner-operated since 1980</span>
        <h1 id="h1">Built to Outlast the <span class="u">Warranty.</span></h1>
        <p class="hero-lede">Roofing, siding and seamless gutters for Indiana homes, condominium and townhome communities and apartment communities, plus gutters, siding and metal wall panels on warehouses and commercial buildings. Installed by Rocklane crews and backed by our own workmanship warranty.</p>
        <div class="btn-row">
          <a class="btn" href="/contact">Request an Estimate {ic("arrow")}</a>
          <a class="btn btn-outline" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
        </div>
        <div class="hero-foot">
          <span>{ic("shield")}GAF Master Elite&reg; roofing contractor</span>
          <span>{ic("clipboard")}10-year workmanship warranty on roof replacements</span>
        </div>
      </div>
      <span class="photo-cap">{ic("pin")}Pictured: Carmel, Indiana</span>
    </section>

    <section class="stats-band" aria-labelledby="stats-h">
      <div class="wrap">
        <div class="sb-head reveal">
          <div><span class="eyebrow">Why {SHORT}</span><h2 id="stats-h">Credentials that hold up on the roof.</h2></div>
          <div class="sb-aside"><p>An owner-run contractor with a Director of Training &amp; Quality Control on staff, a written workmanship warranty and the GAF status behind GAF&rsquo;s strongest roof warranty, plus GAF&rsquo;s President&rsquo;s Club Award.</p>{gaf_awards()}</div>
        </div>
        <ul class="sb-grid reveal">
          <li><span class="sb-num">2%</span><span class="sb-bar"></span><p>{GAF_CLAIM_HTML}</p></li>
          <li><span class="sb-num">10<small>YR</small></span><span class="sb-bar"></span><p>Workmanship warranty on roof replacements</p></li>
          <li><span class="sb-num">1980</span><span class="sb-bar"></span><p>Owner-operated in central Indiana since 1980</p></li>
          <li><span class="sb-num">100+</span><span class="sb-bar"></span><p>Completed communities and commercial properties across central Indiana</p></li>
        </ul>
      </div>
    </section>

    <section aria-labelledby="svc-h">
      <div class="wrap">
{sec_hd("01", "What we install", "The whole exterior, one accountable crew.", "Steep-slope roofing, James Hardie&reg; and Variform siding, and seamless gutters cut on site, plus gutters, siding and metal wall panels for warehouses and commercial buildings.", "svc-h")}
        <div class="svc-grid">
          {photo_card("/roofing", "farmhouse-new-roof", "Farmhouse with a new gray architectural-shingle hip roof, front porch and white gutters under a blue sky", "Roofing", "Asphalt shingle roof replacement, repair and storm-damage inspection, from a GAF Master Elite&reg; roofing contractor.", "Explore roofing", "(max-width:900px) 100vw, 58vw", cls="c1")}
          {photo_card("/gutters", "k-style-gutters", "White K-style seamless gutter and downspout on a tan vinyl-sided home against a deep blue sky", "Gutters", "Seamless gutters custom-cut on site, gutter guards, repair and cleaning.", "Explore gutters", "(max-width:900px) 100vw, 40vw", cls="c2", pos="center 30%")}
          {photo_card("/siding", "siding-rooflines", "Close-set homes with vinyl lap siding, shake gables and architectural shingle roofs", "Siding", "James Hardie&reg; fiber cement and Variform vinyl, installed by Rocklane crews.", "Explore siding", "(max-width:900px) 100vw, 40vw", cls="c3")}
          {photo_card("/commercial", "warehouse-dock-doors", "White tilt-up warehouse wall with loading dock doors and yellow bollards", "Commercial &amp; Warehouse", "Gutters, siding and metal wall panels on warehouses and commercial buildings.", "Explore commercial", "(max-width:900px) 100vw, 58vw", cls="c4")}
        </div>
      </div>
    </section>

    <section class="grey" aria-labelledby="aud-h">
      <div class="wrap">
{sec_hd("02", "Who we serve", "From a single home to an entire community.", "Homeowners, HOA boards, property managers and building owners across central Indiana work with the same owners, crews and standards.", "aud-h")}
        <div class="aud-grid">
          {photo_card("/roofing", "indiana-farmhouse-fall", "White two-story Indiana farmhouse with a shingle roof among bright fall maples", "Single-family homes", "Roof, siding and gutter work for the house you live in.", "", AUD_SIZES, pos="58% 58%", kicker="01")}
          {photo_card("/property-managers", "indy-brick-townhomes", "Two-story brick townhome buildings under large shade trees in Indianapolis at golden hour", "Condos &amp; townhomes", "Planned, phased exterior work for HOA boards.", "", AUD_SIZES, pos="center 15%", kicker="02")}
          {photo_card("/property-managers", "indy-apartments-courtyard", "Courtyard lawn and mature tree at a garden-style Indianapolis apartment complex with brick and vinyl siding", "Apartment communities", "One accountable partner for property managers.", "", AUD_SIZES, kicker="03")}
          {photo_card("/commercial", "commercial-corridor-aerial", "Aerial view of a suburban business corridor with flat-roof office buildings and parking", "Warehouses &amp; commercial", "Gutters, siding and metal wall panels for buildings that work hard.", "", AUD_SIZES, kicker="04")}
        </div>
      </div>
    </section>

{warranty_band("03")}

    <section class="grey" aria-labelledby="gaf-h">
      <div class="wrap">
{sec_hd("04", "GAF enhanced warranties", "GAF warranty options, up to the Golden Pledge&reg;.", f"As a GAF Master Elite&reg; roofing contractor, {SHORT} can offer GAF enhanced warranties on qualifying roofing systems. The strongest, Golden Pledge&reg;, is available only through Master Elite&reg; contractors.", "gaf-h")}
        <div class="tiers">
          <article class="tier reveal"><span class="lvl">Tier 01</span><h3>System Plus</h3><p>Enhanced GAF coverage on a qualifying GAF roofing system.</p></article>
          <article class="tier reveal" style="--d:.08s"><span class="lvl">Tier 02</span><h3>Silver Pledge&trade;</h3><p>A step up in enhanced GAF coverage on a qualifying roofing system.</p></article>
          <article class="tier featured reveal" style="--d:.16s"><span class="ribbon">Master Elite&reg; only</span><span class="lvl">Tier 03 &middot; Strongest</span><h3>Golden Pledge&reg;</h3><p>GAF&rsquo;s strongest warranty, available only through Master Elite&reg; contractors, with up to 25&ndash;30 years of workmanship coverage on qualifying roofing systems.{fn(2)}</p></article>
        </div>
        <div class="claim reveal">
          {gaf_badge()}
          <p>{GAF_CLAIM_HTML}<small>Footnotes appear at the bottom of this page.</small></p>
        </div>
      </div>
    </section>

{process("05")}

    <section class="com-band" aria-labelledby="com-h">
      <div class="com-hero on-blue">
        {picture("indianapolis-skyline-dusk", "Downtown Indianapolis skyline at dusk", "100vw", cls="com-bg", pos="center 60%")}
        <div class="wrap reveal">
          <span class="sec-num" aria-hidden="true">06</span>
          <span class="eyebrow">Commercial</span>
          <h2 id="com-h">Two companies. One standard, top to bottom.</h2>
          <p>{SHORT} handles the walls and water management on warehouses and commercial buildings. Low-slope membrane roofs go to our sister company, Rocklane Commercial Contractors LLC.</p>
        </div>
      </div>
      <div class="wrap">
{COMMERCIAL_SPLIT}
      </div>
    </section>

    <section class="grey" aria-labelledby="hoa-h">
      <div class="wrap hoa-split">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">07</span>
          <span class="eyebrow">HOA boards &amp; property managers</span>
          <h2 id="hoa-h">You never manage the handoff.</h2>
          <p>More than 100 completed communities and commercial properties across central Indiana. Here is what stays the same on every one.</p>
          <ul class="pts">
            <li><span class="pt-ic">{ic("phone")}</span><div><strong>Owners in daily management</strong><span>If something goes wrong, you get an owner on the phone.</span></div></li>
            <li><span class="pt-ic">{ic("shield")}</span><div><strong>Director of Training &amp; Quality Control</strong><span>On staff, setting the standard our crews install to.</span></div></li>
            <li><span class="pt-ic">{ic("users")}</span><div><strong>Specialist network on demand</strong><span>Storm-damage inspectors, public adjusters and engineers, activated when needed.</span></div></li>
            <li><span class="pt-ic">{ic("file")}</span><div><strong>Board-ready records</strong><span>Status, photos and documents for every building in the customer portal.</span></div></li>
          </ul>
          <a class="btn btn-blue" href="/property-managers">For HOA boards &amp; managers {ic("arrow")}</a>
        </div>
        <div class="offset-media left reveal">
          {picture("condo-community-aerial", "Aerial view of a townhome and condominium community with shingle roofs on tree-lined cul-de-sacs", "(max-width:900px) 100vw, 56vw", cls="om-big")}
          {picture("west-lafayette-apartments", "Three-story garden-style apartment building with a charcoal shingle hip roof in West Lafayette, Indiana", "(max-width:900px) 44vw, 25vw", cls="om-sm")}
        </div>
      </div>
    </section>

{PARTNERS}

{service_area("08")}

{CTA}"""
