"""HOA & property managers page.

Section rhythm: hero (photo/blue), credentials (white), 01 who we serve (Light Grey),
02 board-ready scope (white), 03 process (blue), 04 accountability (Light Grey),
05 warranty (white), partners (white strip), 06 service area (photo/blue), final CTA.

Rules: no HAAG / FORTIFIED wording (no named people here), "owner-led inspections" only.
Rocklane Co. scope on warehouses = gutters, siding, metal wall panels (never roofing).
Stock photos are never captioned as Rocklane projects.
"""
from site_common import *

PATH = "/property-managers"
CURRENT = "/property-managers"
TITLE = "HOA & Property Manager Roofing, Siding & Gutters in Indiana | Rocklane Co."
DESC = ("Roofing, siding and gutter projects for HOA boards and property managers, plus gutters, siding and "
        "metal wall panels on warehouses. 100+ completed communities and commercial properties across "
        "central Indiana. Owner-operated since 1980.")
HEAD = ('\n  <link rel="preload" as="image" href="/images/photos/condo-community-aerial-1200.jpg" '
        'imagesrcset="/images/photos/condo-community-aerial-1200.jpg 1200w, /images/photos/condo-community-aerial.jpg 2400w" '
        'imagesizes="100vw">')

CSS = """
.pm-hero{display:flex;align-items:flex-end;min-height:min(82vh,860px);min-height:min(82svh,860px);padding:clamp(96px,14vh,160px) 0 clamp(64px,9vh,104px)}
.pm-hero .wrap{width:100%}
.pm-hero h1{font-size:clamp(2.5rem,5.8vw,4.6rem);max-width:15ch;line-height:1.02;letter-spacing:-.03em}
.pm-hero p.pm-lede{max-width:38rem;font-size:clamp(1.05rem,1.4vw,1.2rem);line-height:1.6;margin:0 0 2rem}
.pm-hero .hero-foot{margin-top:clamp(32px,6vh,64px)}
.pm-aud{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(12px,1.5vw,20px)}
.pm-aud .photo-card{min-height:620px}
.pm-aud .photo-card:nth-child(2){margin-top:72px}
.pm-aud h3{font-size:clamp(1.4rem,2vw,1.85rem)}
.pm-scope{list-style:none;margin:0 0 1rem;padding:0;display:flex;flex-wrap:wrap;gap:6px 18px;font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase}
.pm-scope li{display:inline-flex;align-items:center;gap:8px}
.pm-scope li::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--green);flex:none}
.pm-aud a.pc-go{color:var(--white);text-decoration:none}
.pm-aud a.pc-go:hover .i{transform:translateX(4px)}
.pm-board .checks{margin-top:1.8rem}
.pm-board .checks strong{display:block}
@media (max-width:1100px){
  .pm-aud{grid-template-columns:1fr 1fr}
  .pm-aud .photo-card:nth-child(2){margin-top:48px}
  .pm-aud .photo-card:nth-child(3){grid-column:1/-1;min-height:480px}
}
@media (max-width:767px){
  .pm-hero{min-height:0;padding:72px 0 64px}
  .pm-aud{grid-template-columns:1fr}
  .pm-aud .photo-card,.pm-aud .photo-card:nth-child(3){min-height:440px;grid-column:auto}
  .pm-aud .photo-card:nth-child(2){margin-top:0}
  .pm-hero .hero-foot{flex-direction:column;gap:8px}
}
@media (max-width:420px){.pm-hero .btn{width:100%}}
@media print{.pm-hero{min-height:0;padding:48px 0}}
@media (max-height:820px) and (min-width:768px){.pm-hero{min-height:0;padding:56px 0 48px}.pm-hero h1{font-size:clamp(2.4rem,5vw,3.8rem)}.pm-hero .hero-foot{margin-top:28px}}
"""

CARD_SIZES = "(max-width:767px) 100vw, (max-width:1100px) 50vw, 33vw"

BODY = f"""    <div class="page-head on-blue has-photo pm-hero">
      {picture("condo-community-aerial", "", "100vw", cls="ph-bg", eager=True, pos="center 40%")}
      <div class="wrap">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>HOA &amp; Property Managers</span></nav>
        <span class="eyebrow">HOA boards &amp; property managers</span>
        <h1>Exterior projects your board can sign off on.</h1>
        <p class="pm-lede">Roofing, siding and seamless gutters for condominium, townhome and apartment communities across central Indiana, plus gutters, siding and metal wall panels on warehouses. Owner-led inspections, and owners active in daily management.</p>
        <div class="btn-row">
          <a class="btn" href="/contact">Request an Estimate {ic("arrow")}</a>
          <a class="btn btn-outline" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
        </div>
        <div class="hero-foot">
          <span>{ic("building")}100+ communities &amp; commercial properties</span>
          <span>{ic("users")}Owner-operated since 1980</span>
        </div>
      </div>
    </div>

    <section class="stats-band" aria-labelledby="stats-h">
      <div class="wrap">
        <div class="sb-head reveal">
          <div><span class="eyebrow">Why boards choose {SHORT}</span><h2 id="stats-h">Credentials a board can check.</h2></div>
          <div class="sb-aside"><p>An owner-run contractor with a Director of Training &amp; Quality Control on staff, a written workmanship warranty, and the GAF status behind GAF&rsquo;s strongest roof warranty.</p>{gaf_badge()}</div>
        </div>
        <ul class="sb-grid reveal">
          <li><span class="sb-num">100+</span><span class="sb-bar"></span><p>Completed communities and commercial properties across central Indiana</p></li>
          <li><span class="sb-num">1980</span><span class="sb-bar"></span><p>Owner-operated in central Indiana since 1980</p></li>
          <li><span class="sb-num">10<small>YR</small></span><span class="sb-bar"></span><p>Workmanship warranty on roof replacements</p></li>
          <li><span class="sb-num">2%</span><span class="sb-bar"></span><p>{GAF_CLAIM_HTML}</p></li>
        </ul>
      </div>
    </section>

    <section class="grey" aria-labelledby="aud-h">
      <div class="wrap">
{sec_hd("01", "Who we serve", "Communities, apartments and the buildings behind them.", "HOA boards, property managers and building owners work with the same owners, crews and standards, whether the job is one building or every building on the property.", "aud-h")}
        <div class="pm-aud">
          <article class="photo-card reveal">
            {picture("indy-brick-townhomes", "Two-story brick townhome buildings under large shade trees in Indianapolis at golden hour", CARD_SIZES, pos="center 15%")}
            <div class="pc-body">
              <span class="pc-k">01</span>
              <h3>Condos &amp; townhomes</h3>
              <ul class="pm-scope"><li>Roofing</li><li>Siding</li><li>Gutters</li></ul>
              <p>Planned, phased exterior work for HOA boards, with the condition of every building documented before the board votes.</p>
              <a class="pc-go" href="/roofing">Roofing {ic("arrow")}</a>
            </div>
          </article>
          <article class="photo-card reveal" style="--d:.08s">
            {picture("west-lafayette-apartments", "Three-story garden-style apartment building with a charcoal shingle hip roof in West Lafayette, Indiana", CARD_SIZES, pos="center 35%")}
            <div class="pc-body">
              <span class="pc-k">02</span>
              <h3>Apartment communities</h3>
              <ul class="pm-scope"><li>Roofing</li><li>Siding</li><li>Gutters</li></ul>
              <p>One accountable partner for property managers, with status, photos and documents for each building in the customer portal.</p>
              <a class="pc-go" href="/siding">Siding {ic("arrow")}</a>
            </div>
          </article>
          <article class="photo-card reveal" style="--d:.16s">
            {picture("warehouse-dock-doors", "White tilt-up warehouse wall with loading dock doors and yellow bollards", CARD_SIZES, pos="center 60%")}
            <div class="pc-body">
              <span class="pc-k">03</span>
              <h3>Warehouses &amp; commercial</h3>
              <ul class="pm-scope"><li>Gutters</li><li>Siding</li><li>Metal wall panels</li></ul>
              <p>The walls and water management on warehouses and commercial buildings. Low-slope membrane roofs go to our sister company, Rocklane Commercial Contractors LLC.</p>
              <a class="pc-go" href="/commercial">Commercial exteriors {ic("arrow")}</a>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="pm-board" aria-labelledby="board-h">
      <div class="wrap split">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">02</span>
          <span class="eyebrow">Board-ready scope</span>
          <h2 id="board-h">We remove the risk from capital exterior projects.</h2>
          <p class="lead">Your board answers to owners who don&rsquo;t want a special assessment. You need a contractor whose scope holds, whose crews show up, and whose owners answer the phone. Our name is on the building, the paperwork, and the phone when you call.</p>
          <ul class="checks">
            <li><strong>Reserve planning support</strong>Owner-led inspections document the condition of every building, so the board can plan the investment.</li>
            <li><strong>A written scope before anything is approved</strong>The estimate puts the scope and materials in writing; the board signs off before work is scheduled.</li>
            <li><strong>Planned, phased work</strong>Buildings scheduled in the portal, so residents and managers know what is next.</li>
            <li><strong>Warranty you can file</strong>GAF enhanced warranties on qualifying roofing systems, plus our 10-year workmanship warranty on roof replacements.</li>
          </ul>
        </div>
        <figure class="media-frame reveal" style="--d:.1s">
          {picture("tipton-roof-topdown", "Top-down drone view of a shingle roof showing each roof plane", "(max-width:980px) 100vw, 50vw")}
          <div class="tag"><span class="ico ico-blue">{ic("clipboard")}</span><div><strong>Documented condition</strong><span>Reports your board can plan around</span></div></div>
        </figure>
      </div>
    </section>

{process("03")}

    <section class="grey" aria-labelledby="acct-h">
      <div class="wrap hoa-split">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">04</span>
          <span class="eyebrow">Accountability</span>
          <h2 id="acct-h">More than 100 communities and commercial properties. One standard on every one.</h2>
          <p>More than 100 completed communities and commercial properties across central Indiana. Here is what stays the same on every one.</p>
          <ul class="pts">
            <li><span class="pt-ic">{ic("phone")}</span><div><strong>An owner on the phone</strong><span>Owners are active in daily management. If something goes wrong, you get an owner on the phone.</span></div></li>
            <li><span class="pt-ic">{ic("shield")}</span><div><strong>Director of Training &amp; Quality Control</strong><span>On staff, setting the standard our crews install to.</span></div></li>
            <li><span class="pt-ic">{ic("users")}</span><div><strong>Specialist network on demand</strong><span>After a storm we activate storm-damage inspectors, public adjusters and engineers. You never manage the handoff.</span></div></li>
            <li><span class="pt-ic">{ic("file")}</span><div><strong>Records in the portal</strong><span>Status, updates, photos and documents for every building, ready for the next board meeting.</span></div></li>
          </ul>
          <div class="btn-row">
            <a class="btn btn-blue" href="/contact">Request an Estimate {ic("arrow")}</a>
            <a class="text-link" href="/portal/">Customer Login {ic("arrow")}</a>
          </div>
        </div>
        <div class="offset-media left reveal">
          {picture("carmel-townhomes-aerial", "Golden-hour aerial view of brick townhomes and condominiums with architectural shingle roofs in Carmel, Indiana", "(max-width:900px) 100vw, 56vw", cls="om-big")}
          {picture("indy-apartments-courtyard", "Courtyard lawn and mature tree at a garden-style Indianapolis apartment complex with brick and vinyl siding", "(max-width:900px) 44vw, 25vw", cls="om-sm")}
        </div>
      </div>
    </section>

{warranty_band("05", photo="apartment-community-aerial", alt="Garden-style apartment community with shingle roofs at dusk", small="k-style-gutters", small_alt="White K-style seamless gutter and downspout against a deep blue sky")}

{PARTNERS}

{service_area("06")}

{CTA}"""
