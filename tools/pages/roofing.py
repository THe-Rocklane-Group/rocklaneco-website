"""Roofing page. Section rhythm: hero (photo/blue), 01 owner-led inspections (white),
02 replacement vs repair (Light Grey), 03 storm damage & insurance (blue photo band),
04 GAF Master Elite (white), 05 GAF enhanced warranties (Light Grey), 06 workmanship warranty
(white), 07 warning signs (Light Grey), 08 process (blue), final CTA.
"""
from site_common import *

PATH = "/roofing"
CURRENT = "/roofing"
TITLE = "Roof Replacement & Repair in Indianapolis | Rocklane Co."
DESC = ("Asphalt shingle roof replacement, repair and storm-damage inspections from a GAF Master Elite "
        "roofing contractor, backed by a 10-year workmanship warranty. Call (317) 898-8696.")
HEAD = ('\n  <link rel="preload" as="image" href="/images/photos/farmhouse-new-roof-1200.jpg" '
        'imagesrcset="/images/photos/farmhouse-new-roof-1200.jpg 1200w, /images/photos/farmhouse-new-roof.jpg 1752w" '
        'imagesizes="100vw">')

# Page-only CSS. Overlay math (white text on Shark Blue over a worst-case white pixel):
# Shark Blue rgba(30,90,168,.9) -> gradient end #17488a at .86 -> rgb(56,98,154), contrast with white 6.1:1 (AA).
CSS = """
  .rf-hero { min-height: 82vh; min-height: 82svh; }
  .rf-hero .hero-bg { object-position: 62% 45%; }
  .rf-hero h1 { max-width: 15ch; font-size: clamp(2.4rem, 5.2vw, 4.4rem); }
  .rf-hero .crumbs { margin-bottom: 28px; }

  .rf-opts { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: clamp(16px, 2.4vw, 36px); }
  .rf-opt { display: flex; flex-direction: column; background: var(--white); border-top: 4px solid var(--blue); }
  .rf-opt > img { width: 100%; aspect-ratio: 16 / 10; object-fit: cover; }
  .rf-opt .b { flex: 1; display: flex; flex-direction: column; padding: clamp(26px, 3.2vw, 48px); }
  .rf-opt .k { font-size: .75rem; font-weight: 700; letter-spacing: .2em; text-transform: uppercase; color: var(--char); margin-bottom: .9rem; }
  .rf-opt h3 { font-size: clamp(1.5rem, 2.4vw, 2.1rem); }
  .rf-yr { display: flex; align-items: baseline; gap: 14px; padding: 18px 0; margin: 4px 0 22px; border-top: 1px solid var(--grey); border-bottom: 1px solid var(--grey); }
  .rf-yr b { font-size: clamp(2.6rem, 4.4vw, 3.6rem); font-weight: 900; color: var(--blue); line-height: 1; letter-spacing: -.04em; }
  .rf-yr span { font-size: .92rem; line-height: 1.4; font-weight: 600; color: var(--char); }
  .rf-opt .checks { margin-bottom: 0; }
  .rf-note { display: flex; flex-wrap: wrap; gap: 12px 40px; justify-content: space-between; align-items: center; margin-top: clamp(32px, 4vw, 52px); padding-top: 28px; border-top: 1px solid rgba(74,74,74,.25); }
  .rf-note p { margin: 0; max-width: 46rem; }

  .rf-storm { position: relative; isolation: isolate; overflow: hidden; background: var(--blue-d); }
  .rf-storm .rf-bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: -2; }
  .rf-storm::before { content: ""; position: absolute; inset: 0; z-index: -1; background: linear-gradient(160deg, rgba(30,90,168,.9) 0%, rgba(23,72,138,.86) 100%); }
  .rf-storm-g { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: clamp(36px, 6vw, 96px); align-items: start; }
  .rf-storm-g > * { min-width: 0; }
  .rf-storm h2 { max-width: 14ch; }
  .rf-storm .lead { max-width: 34rem; }
  .rf-handoff { display: inline-block; margin: .4rem 0 2rem; padding: 14px 20px; border-left: 4px solid var(--green); background: rgba(30,90,168,.6); font-weight: 800; font-size: 1.15rem; color: var(--white); }
  .rf-steps { list-style: none; margin: 0; padding: 0; counter-reset: s; border-top: 1px solid rgba(255,255,255,.35); }
  .rf-steps li { display: grid; grid-template-columns: 56px 1fr; gap: 4px 20px; padding: 26px 0; border-bottom: 1px solid rgba(255,255,255,.35); }
  .rf-steps li::before { counter-increment: s; content: counter(s, decimal-leading-zero); grid-row: span 2; width: 48px; height: 48px; border-radius: 50%; background: var(--green); color: var(--ink); display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: .95rem; }
  .rf-steps h3 { margin: 0; font-size: 1.2rem; }
  .rf-steps p { margin: 0; }

  .rf-pct { display: grid; grid-template-columns: auto 1fr; gap: 24px; align-items: center; margin: 2rem 0; padding: 24px 0; border-top: 1px solid var(--grey); border-bottom: 1px solid var(--grey); }
  .rf-pct b { font-size: clamp(3.4rem, 6vw, 5rem); font-weight: 900; color: var(--blue); line-height: 1; letter-spacing: -.05em; }
  .rf-pct p { margin: 0; font-weight: 700; color: var(--char); font-size: 1.05rem; line-height: 1.5; }
  .rf-gaf .media-frame img { aspect-ratio: 4 / 3.6; }

  .rf-tier-ft { display: grid; grid-template-columns: auto 1fr; gap: 28px; align-items: center; margin-top: clamp(40px, 5vw, 64px); padding-top: 32px; border-top: 1px solid rgba(74,74,74,.25); }
  .rf-tier-ft p { margin: 0; max-width: 46rem; }

  .rf-signs { display: grid; grid-template-columns: minmax(0, 7fr) minmax(0, 5fr); gap: clamp(36px, 6vw, 96px); align-items: center; }
  .rf-signs > * { min-width: 0; }
  .rf-signs .signs { grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); }
  .rf-signs-ph { margin: 0; }
  .rf-signs-ph img { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; box-shadow: var(--shadow-lg); }

  @media (max-width: 1100px) {
    .rf-storm-g, .rf-signs { grid-template-columns: 1fr; }
    .rf-signs-ph img { aspect-ratio: 16 / 10; }
  }
  @media (max-width: 900px) {
    .rf-opts { grid-template-columns: 1fr; }
  }
  @media (max-width: 767px) {
    .rf-hero { min-height: 0; }
    .rf-pct, .rf-tier-ft { grid-template-columns: 1fr; gap: 14px; }
    .rf-steps li { grid-template-columns: 48px 1fr; gap: 4px 16px; }
    .rf-signs-ph { order: -1; }
  }
  @media (max-width: 420px) {
    .rf-hero .btn, .rf-storm .btn { width: 100%; }
  }
  @media print {
    .rf-hero { min-height: 0; }
  }
"""

BODY = f"""    <section class="hero on-blue rf-hero" aria-labelledby="h1">
      {picture("farmhouse-new-roof", "Gray farmhouse with a new gray architectural-shingle hip roof, a covered front porch and white gutters on a green lawn", "100vw", cls="hero-bg", eager=True)}
      <div class="wrap hero-in">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>Roofing</span></nav>
        <span class="eyebrow">Roofing &middot; GAF Master Elite&reg; roofing contractor</span>
        <h1 id="h1">Roof replacement &amp; repair, <span class="u">owner-inspected.</span></h1>
        <p class="hero-lede">Asphalt shingle roof replacement, repair and storm-damage inspection for homes, condominium and townhome communities across central Indiana. Installed by Rocklane crews and backed by our own workmanship warranty.</p>
        <div class="btn-row">
          <a class="btn" href="/contact">Request an Estimate {ic("arrow")}</a>
          <a class="btn btn-outline" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
        </div>
        <div class="hero-foot">
          <span>{ic("search")}Owner-led inspections</span>
          <span>{ic("clipboard")}10-year workmanship warranty on roof replacements</span>
        </div>
      </div>
    </section>

    <section aria-labelledby="insp-h">
      <div class="wrap split">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">01</span>
          <span class="eyebrow">Owner-led inspections</span>
          <h2 id="insp-h">An owner walks your roof first.</h2>
          <p class="lead">Every roofing project starts with an inspection, and at {SHORT} inspections are led by owners Justin Reddick and Kevin Kortzendorf, HAAG Certified Inspectors (Residential Roofs).</p>
          <p>You hear what we find from the people who run the company, so you can plan the investment with straight answers.</p>
          <ul class="checks">
            <li><strong>The condition, documented.</strong> We inspect and put the scope in writing before anything is approved.</li>
            <li><strong>Repair or replace, honestly.</strong> If a repair will outperform a replacement, we&rsquo;ll tell you.</li>
            <li><strong>Everything in one place.</strong> Status, updates, photos and documents in your customer portal.</li>
            <li><strong>An owner on the phone.</strong> Owners stay active in daily management. If something goes wrong, you get an owner on the phone.</li>
          </ul>
          <div class="btn-row"><a class="btn" href="/contact">Request an Estimate {ic("arrow")}</a><a class="text-link" href="tel:{TEL}">{ic("phone")}Call {PHONE}</a></div>
        </div>
        <figure class="media-frame reveal" style="--d:.1s">
          {picture("tipton-roof-topdown", "Top-down drone view of a ranch home in Tipton, Indiana, showing each gray asphalt-shingle roof plane beside a green lawn and fall trees", "(max-width:980px) 100vw, 50vw")}
          <div class="tag"><span class="ico ico-blue">{ic("search")}</span><div><strong>Owner-led inspections</strong><span>Every roof plane, before any scope is written</span></div></div>
        </figure>
      </div>
    </section>

    <section class="grey" aria-labelledby="rr-h">
      <div class="wrap">
{sec_hd("02", "Replacement vs. repair", "The right fix, not the biggest one.", "Some roofs need a full replacement. Many need a well-made repair. We recommend the one that will last, and we back either with our own workmanship warranty.", "rr-h")}
        <div class="rf-opts">
          <article class="rf-opt reveal">
            {picture("two-story-home-hero", "Two-story suburban home with charcoal architectural shingles, gray lap siding and white K-style gutters", "(max-width:900px) 100vw, 50vw", pos="80% 40%")}
            <div class="b">
              <span class="k">Roof replacement</span>
              <h3>A complete GAF roofing system.</h3>
              <div class="rf-yr"><b>10</b><span>Year workmanship warranty on roof replacements</span></div>
              <ul class="checks">
                <li>Asphalt shingle roof replacement for homes, condominium and townhome communities.</li>
                <li>Complete GAF roofing systems, installed by Rocklane crews.</li>
                <li>GAF enhanced warranty options on qualifying roofing systems, up to the Golden Pledge&reg;.</li>
              </ul>
            </div>
          </article>
          <article class="rf-opt reveal" style="--d:.08s">
            {picture("indiana-farmhouse-fall", "White two-story Indiana farmhouse with a shingle roof framed by orange and gold fall maples", "(max-width:900px) 100vw, 50vw", pos="45% center")}
            <div class="b">
              <span class="k">Roof repair</span>
              <h3>Find the cause, not just the symptom.</h3>
              <div class="rf-yr"><b>5</b><span>Year workmanship warranty on repairs</span></div>
              <ul class="checks">
                <li>We trace the leak or damage to its source before we fix it.</li>
                <li>Storm, wind and hail damage repaired after an owner-led inspection.</li>
                <li>If a repair will outperform a replacement, we&rsquo;ll tell you. Straight answers, every time.</li>
              </ul>
            </div>
          </article>
        </div>
        <div class="rf-note reveal">
          <p class="fine">{SHORT} installs steep-slope roofing. Low-slope membrane roofs on commercial buildings are handled by our sister company, Rocklane Commercial Contractors LLC.</p>
          <a class="text-link" href="/commercial">Commercial roofing {ic("arrow")}</a>
        </div>
      </div>
    </section>

    <section class="rf-storm on-blue" aria-labelledby="storm-h">
      {picture("condo-community-aerial", "", "100vw", cls="rf-bg")}
      <div class="wrap rf-storm-g">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">03</span>
          <span class="eyebrow">Storm damage &amp; insurance</span>
          <h2 id="storm-h">After the storm, one call.</h2>
          <p class="lead">Hail and wind damage is rarely just a roofing job. We bring in storm-damage inspectors, public adjusters and engineers from our specialist network when your claim needs them, and we coordinate the work from inspection to final walkthrough.</p>
          <p class="rf-handoff">You never manage the handoff.</p>
          <div class="btn-row">
            <a class="btn" href="/contact">Request an Estimate {ic("arrow")}</a>
            <a class="btn btn-outline" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
          </div>
        </div>
        <ol class="rf-steps reveal" style="--d:.08s">
          <li><h3>Owner-led inspection</h3><p>An owner documents the damage, and the photos and written scope go to your customer portal.</p></li>
          <li><h3>Specialists on demand</h3><p>Storm-damage inspectors, public adjusters and engineers from our network, activated only when your claim calls for them.</p></li>
          <li><h3>One point of contact</h3><p>We coordinate the specialists working your claim, so you are not passing paperwork between companies.</p></li>
          <li><h3>Repair or replacement</h3><p>Rocklane crews do the work, backed by our workmanship warranty.</p></li>
        </ol>
      </div>
    </section>

    <section class="rf-gaf" aria-labelledby="gaf-h">
      <div class="wrap split">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">04</span>
          <span class="eyebrow">GAF Master Elite&reg;</span>
          <h2 id="gaf-h">A GAF Master Elite&reg; roofing contractor.</h2>
          <p class="lead">{SHORT} is a GAF Master Elite&reg; roofing contractor. That status lets us offer GAF enhanced warranties on qualifying roofing systems, including the Golden Pledge&reg;, which is available only through Master Elite&reg; contractors.</p>
          <div class="rf-pct"><b>2%</b><p>{GAF_CLAIM_HTML}</p></div>
          <p>Our Director of Training &amp; Quality Control is on staff, setting the standard our crews install to on every roof.</p>
          <a class="text-link" href="/about">About {SHORT} {ic("arrow")}</a>
        </div>
        <figure class="media-frame reveal" style="--d:.1s">
          {picture("indy-brick-townhomes", "Two-story brick townhome buildings with shingle roofs under large shade trees in Indianapolis at golden hour", "(max-width:980px) 100vw, 50vw", pos="center 15%")}
          <div class="tag"><span class="ico ico-blue">{ic("home")}</span><div><strong>Steep-slope roofing</strong><span>Homes, condominium and townhome communities</span></div></div>
        </figure>
      </div>
    </section>

    <section class="grey" aria-labelledby="tiers-h">
      <div class="wrap">
{sec_hd("05", "GAF enhanced warranties", "Three ways to extend your coverage.", "GAF sets the terms and eligibility for each enhanced warranty. We walk you through the options for your roof before you choose.", "tiers-h")}
        <div class="tiers">
          <article class="tier reveal"><span class="lvl">Tier 01</span><h3>System Plus</h3><p>Enhanced GAF coverage on a qualifying GAF roofing system.</p></article>
          <article class="tier reveal" style="--d:.08s"><span class="lvl">Tier 02</span><h3>Silver Pledge&trade;</h3><p>A step up in enhanced GAF coverage on a qualifying roofing system.</p></article>
          <article class="tier featured reveal" style="--d:.16s"><span class="ribbon">Master Elite&reg; only</span><span class="lvl">Tier 03 &middot; Strongest</span><h3>Golden Pledge&reg;</h3><p>GAF&rsquo;s strongest warranty, available only through Master Elite&reg; contractors, with up to 25&ndash;30 years of workmanship coverage on qualifying roofing systems.{fn(2)}</p></article>
        </div>
        <div class="rf-tier-ft reveal">
          {gaf_awards()}
          <p class="fine">Enhanced warranties require a qualifying GAF roofing system. Complete coverage and restrictions are in the footnotes at the bottom of this page.</p>
        </div>
      </div>
    </section>

{warranty_band("06", photo="west-lafayette-apartments", alt="Three-story garden-style apartment building with a charcoal shingle hip roof in West Lafayette, Indiana", small="k-style-gutters", small_alt="White K-style seamless gutter and downspout on a tan vinyl-sided home")}

    <section class="grey" aria-labelledby="signs-h">
      <div class="wrap rf-signs">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">07</span>
          <span class="eyebrow">Know the warning signs</span>
          <h2 id="signs-h">Signs a roof needs attention.</h2>
          <p class="lead">Spot any of these? Ask for an owner-led inspection. If a repair will outperform a replacement, we&rsquo;ll tell you.</p>
          <ul class="signs">
            <li>{ic("alert")}Curling, cracked or missing shingles</li>
            <li>{ic("alert")}Shingle granules collecting in the gutters</li>
            <li>{ic("droplet")}Water stains on ceilings or in the attic</li>
            <li>{ic("home")}Sagging areas or daylight through the roof deck</li>
            <li>{ic("storm")}Hail or wind damage after a storm</li>
          </ul>
          <a class="btn btn-blue" href="/contact">Request an Estimate {ic("arrow")}</a>
        </div>
        <figure class="rf-signs-ph reveal" style="--d:.1s">
          {picture("noblesville-neighborhood-aerial", "Sunset aerial view of two-story homes with shingle roofs in a Noblesville, Indiana subdivision in fall color", "(max-width:1100px) 100vw, 40vw", pos="center 20%")}
        </figure>
      </div>
    </section>

{process("08")}

{CTA}"""
