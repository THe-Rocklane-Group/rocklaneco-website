"""Commercial page: two companies, one page, an unmistakable line between them.

Rhythm: hero (photo/blue) with two company jump cards, 01 who-does-what ledger (white),
02 Company 01 Rocklane Co. exteriors (Light Grey), 03 Company 02 Rocklane Commercial Contractors LLC
membrane roofing (blue photo band + white panel), 04 property-manager handoff (Light Grey),
05 portal process (blue), final CTA.

Rules: Rocklane Co. does NOT roof commercial buildings. Its commercial scope is gutters, siding and
metal wall panels. Low-slope membrane roofing (EPDM/TPO/PVC) belongs to Rocklane Commercial
Contractors LLC, "a GAF Certified Commercial Contractor and Versico Authorized". The Versico logo
appears only once, directly beside that credit, inside the Rocklane Commercial section.
"""
from site_common import *

PATH = "/commercial"
CURRENT = "/commercial"
TITLE = "Commercial & Warehouse Exteriors in Indianapolis | Rocklane Co."
DESC = ("Gutters, siding and metal wall panels for warehouses, apartment and condo buildings from Rocklane Co. "
        "Low-slope EPDM, TPO and PVC membrane roofing from Rocklane Commercial Contractors LLC. Central Indiana.")
HEAD = ('\n  <link rel="preload" as="image" href="/images/photos/commercial-corridor-aerial-1200.jpg" '
        'imagesrcset="/images/photos/commercial-corridor-aerial-1200.jpg 1200w, /images/photos/commercial-corridor-aerial.jpg 2400w" '
        'imagesizes="100vw">')

RC = "Rocklane Commercial Contractors LLC"

CSS = """
/* hero: shorter than home, text kept in the >=83% overlay zone on desktop */
.cm-hero { min-height: 84vh; min-height: 84svh; }
.cm-hero .hero-bg { object-position: center 45%; }
.cm-hero h1 { max-width: 13ch; font-size: clamp(2.5rem, 5.4vw, 4.4rem); }
.cm-hero .hero-lede { max-width: 34rem; }
.cm-jump { list-style: none; margin: clamp(36px, 6vh, 64px) 0 0; padding: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; max-width: 44rem; }
.cm-jump a { display: flex; flex-direction: column; gap: 4px; height: 100%; padding: 18px 20px 16px; background: rgba(30,90,168,.94); border-top: 4px solid var(--green); text-decoration: none; transition: box-shadow .2s var(--ease); }
.cm-jump a:hover { box-shadow: inset 0 0 0 2px var(--white); }
.cm-jump .k { font-size: .72rem; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; }
.cm-jump strong { font-size: 1.02rem; line-height: 1.3; }
.cm-jump span.d { display: inline-flex; align-items: center; gap: 8px; font-size: .9rem; font-weight: 500; }
.cm-jump .i { color: var(--green); }

/* company tag: ink on Lizard Green fill (7.4:1) */
.co-tag { display: block; width: fit-content; align-self: flex-start; padding: 6px 12px; background: var(--green); color: var(--ink); font-size: .72rem; font-weight: 800; letter-spacing: .18em; text-transform: uppercase; line-height: 1.3; margin-bottom: 1.1rem; }

/* 01 ledger: Rocklane Co. (white card) | Rocklane Commercial (Shark Blue card) */
.ledger { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 0; box-shadow: var(--shadow-lg); }
.ledger > article { padding: clamp(28px, 4vw, 60px); display: flex; flex-direction: column; }
.ledger .lg-co { background: var(--white); border-top: 6px solid var(--blue); border-left: 1px solid var(--grey); }
.ledger .lg-rc { border-top: 6px solid var(--green); }
.ledger h3 { font-size: clamp(1.5rem, 2.4vw, 2.1rem); margin-bottom: .35em; }
.ledger .lg-sub { font-weight: 600; margin-bottom: 1.6rem; }
.ledger dl { margin: 0 0 1.8rem; }
.ledger dt { font-size: .74rem; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; margin: 0 0 .5rem; }
.ledger dd { margin: 0 0 1.3rem; }
.ledger .ticks { margin-bottom: 0; }
.lg-rc .ticks li { color: var(--white); border-bottom-color: rgba(255,255,255,.28); }
.lg-rc .ticks .i { color: var(--green); }
.ledger .text-link { margin-top: auto; align-self: flex-start; }
.lg-rc .text-link { border-bottom-color: var(--green); }
.lg-note { display: flex; gap: 14px; align-items: flex-start; margin: clamp(28px, 4vw, 44px) 0 0; padding: 20px 24px; background: var(--grey); border-left: 6px solid var(--blue); font-weight: 600; color: var(--char); max-width: 60rem; }
.lg-note .i { color: var(--blue); font-size: 22px; margin-top: 2px; }

/* 02 Rocklane Co.: photos left, scope right */
.co-split { display: grid; grid-template-columns: minmax(0, 7fr) minmax(0, 5fr); gap: clamp(40px, 6vw, 96px); align-items: center; }
.co-split > * { min-width: 0; }
.scope { list-style: none; margin: 0 0 2rem; padding: 0; counter-reset: sc; }
.scope li { display: grid; grid-template-columns: 64px minmax(0, 1fr); gap: 18px; padding: 22px 0; border-top: 1px solid rgba(74,74,74,.22); }
.scope li:last-child { border-bottom: 1px solid rgba(74,74,74,.22); }
.scope li::before { counter-increment: sc; content: "0" counter(sc); font-size: 2.6rem; font-weight: 900; line-height: .9; letter-spacing: -.04em; color: transparent; -webkit-text-stroke: 1.3px var(--blue); }
.scope h3 { margin-bottom: .25em; }
.scope p { margin: 0; }
.btypes { list-style: none; margin: clamp(48px, 6vw, 80px) 0 0; padding: 0; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: clamp(12px, 1.6vw, 20px); }
.btypes li { display: flex; gap: 14px; align-items: center; background: var(--white); padding: 18px 20px; border-top: 4px solid var(--blue); font-weight: 700; color: var(--char); line-height: 1.35; }
.btypes .ico { width: 44px; height: 44px; font-size: 20px; }
.co-war { display: flex; gap: 16px; align-items: center; margin: 0 0 1.8rem; }
.co-war b { font-size: 3.2rem; font-weight: 900; line-height: .9; letter-spacing: -.05em; color: var(--blue); }
.co-war b small { font-size: .38em; letter-spacing: 0; margin-left: 4px; }
.co-war span { font-weight: 600; max-width: 22ch; line-height: 1.45; }

/* 03 Rocklane Commercial: blue photo band + overlapping white panel */
.cm-band .com-hero h2 { max-width: 18ch; }
.cm-band .com-hero p { max-width: 42rem; }
.cm-band .photo-cap { top: 0; bottom: auto; }
/* let the skyline show on the right; text column (<=58%) stays on >=88% Shark Blue */
.cm-band .com-hero::before { background: linear-gradient(90deg, rgba(30,90,168,.92) 0%, rgba(30,90,168,.88) 58%, rgba(30,90,168,.5) 80%, rgba(30,90,168,.2) 100%); }
@media (max-width: 1100px) { .cm-band .com-hero::before { background: var(--ov-v); } }
.mem-panel { position: relative; background: var(--white); box-shadow: var(--shadow-lg); margin-top: calc(-1 * clamp(100px, 11vw, 150px)); padding: clamp(28px, 4vw, 60px); border-top: 6px solid var(--green); }
.mem-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0; margin-bottom: clamp(28px, 4vw, 48px); }
.mem-grid article { padding: 0 clamp(18px, 2.4vw, 36px); border-left: 1px solid var(--grey); }
.mem-grid article:first-child { padding-left: 0; border-left: 0; }
.mem-grid .mk { display: block; font-size: clamp(3rem, 5.6vw, 5.2rem); font-weight: 900; line-height: .9; letter-spacing: -.05em; color: var(--blue); margin-bottom: 14px; }
.mem-grid .bar { display: block; width: 56px; height: 6px; background: var(--green); margin-bottom: 16px; }
.mem-grid h3 { font-size: 1.05rem; margin-bottom: .4em; }
.mem-grid p { margin: 0; font-size: .97rem; }
.mem-foot { display: grid; grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); gap: clamp(20px, 3vw, 40px); align-items: center; padding-top: clamp(24px, 3vw, 36px); border-top: 1px solid var(--grey); }
.mem-foot .versico { margin: 0; }
.mem-foot .versico p { font-size: 1rem; font-weight: 600; color: var(--char); }
.mem-foot .mf-r p { margin: 0 0 1rem; }

/* 04 handoff */
.handoff { list-style: none; margin: 2rem 0 2.4rem; padding: 0; counter-reset: ho; }
.handoff li { position: relative; display: grid; grid-template-columns: 48px minmax(0, 1fr); gap: 18px; padding: 0 0 26px; }
.handoff li::before { counter-increment: ho; content: counter(ho); display: grid; place-items: center; width: 48px; height: 48px; border-radius: 50%; background: var(--blue); color: var(--white); font-weight: 800; font-size: 1.05rem; }
.handoff li:not(:last-child)::after { content: ""; position: absolute; left: 23px; top: 52px; bottom: 4px; width: 2px; background: var(--green); }
.handoff strong { display: block; font-size: 1.05rem; margin: 10px 0 4px; }
.handoff span { display: block; font-size: .97rem; line-height: 1.6; }
.ho-stat { display: flex; gap: 18px; align-items: center; padding: 20px 0 0; border-top: 4px solid var(--blue); margin-bottom: 2rem; }
.ho-stat b { font-size: clamp(2.8rem, 5vw, 4rem); font-weight: 900; line-height: .9; letter-spacing: -.05em; color: var(--blue); }
.ho-stat span { font-weight: 600; max-width: 30ch; line-height: 1.45; }

@media (max-width: 1100px) {
  .btypes { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 900px) {
  .ledger, .co-split, .mem-foot { grid-template-columns: 1fr; }
  .ledger .lg-co { border-left: 0; }
  .mem-panel { margin-top: -80px; }
  .mem-grid { grid-template-columns: 1fr; }
  .mem-grid article { padding: 22px 0; border-left: 0; border-top: 1px solid var(--grey); }
  .mem-grid article:first-child { padding-top: 0; border-top: 0; }
}
@media (max-width: 767px) {
  .cm-jump { grid-template-columns: 1fr; }
  .btypes { grid-template-columns: 1fr; }
  .scope li { grid-template-columns: 48px minmax(0, 1fr); gap: 14px; }
  .scope li::before { font-size: 2rem; }
}
@media print {
  .cm-hero { min-height: 0; }
  .mem-panel { margin-top: 0; box-shadow: none; }
  .ledger { box-shadow: none; }
}
"""

BODY = f"""    <section class="hero cm-hero on-blue" aria-labelledby="h1">
      {picture("commercial-corridor-aerial", "", "100vw", cls="hero-bg", eager=True)}
      <div class="wrap hero-in">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>Commercial</span></nav>
        <span class="eyebrow">Commercial &middot; Part of the Rocklane Group</span>
        <h1 id="h1">The walls, the gutters, the roof. <span class="u">Two companies.</span></h1>
        <p class="hero-lede">{SHORT} installs gutters, siding and metal wall panels on warehouses, apartment and condo buildings and commercial exteriors. Low-slope membrane roofs are the work of a separate company: {RC}.</p>
        <div class="btn-row">
          <a class="btn" href="/contact">Request an Estimate {ic("arrow")}</a>
          <a class="btn btn-outline" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
        </div>
        <ul class="cm-jump" aria-label="The two companies on this page">
          <li><a href="#co"><span class="k">Company 01</span><strong>{SHORT}</strong><span class="d">Gutters, siding, metal wall panels {ic("arrow")}</span></a></li>
          <li><a href="#membrane"><span class="k">Company 02</span><strong>{RC}</strong><span class="d">EPDM, TPO and PVC membrane roofs {ic("arrow")}</span></a></li>
        </ul>
      </div>
    </section>

    <section aria-labelledby="who-h">
      <div class="wrap">
{sec_hd("01", "Who does what", "Know which company is on your building.", f"Both companies belong to the Rocklane Group and share the same owner-operated standard. The scope is split cleanly: {SHORT} takes the walls and the water management, {RC} takes the low-slope roof.", "who-h")}
        <div class="ledger reveal">
          <article class="lg-co" aria-labelledby="lg-co-h">
            <span class="co-tag">Company 01</span>
            <h3 id="lg-co-h">{SHORT}</h3>
            <p class="lg-sub">Commercial exteriors: walls and water management.</p>
            <dl>
              <dt>Installs</dt>
              <dd><ul class="ticks">
                <li>{ic("check")}Commercial gutters and downspouts</li>
                <li>{ic("check")}Siding: James Hardie&reg; fiber cement and Variform vinyl</li>
                <li>{ic("check")}Metal wall panels</li>
              </ul></dd>
              <dt>On</dt>
              <dd>Warehouses, apartment and condo buildings, and commercial exteriors.</dd>
            </dl>
            <a class="text-link" href="#co">{SHORT} commercial exteriors {ic("arrow")}</a>
          </article>
          <article class="lg-rc on-blue" aria-labelledby="lg-rc-h">
            <span class="co-tag">Company 02</span>
            <h3 id="lg-rc-h">{RC}</h3>
            <p class="lg-sub">Commercial low-slope membrane roofing.</p>
            <dl>
              <dt>Installs</dt>
              <dd><ul class="ticks">
                <li>{ic("check")}EPDM membrane roofing</li>
                <li>{ic("check")}TPO membrane roofing</li>
                <li>{ic("check")}PVC membrane roofing</li>
              </ul></dd>
              <dt>Credentials</dt>
              <dd>A GAF Certified Commercial Contractor and Versico Authorized.</dd>
            </dl>
            <a class="text-link" href="#membrane">Membrane roofing {ic("arrow")}</a>
          </article>
        </div>
        <p class="lg-note reveal">{ic("alert")}<span>{SHORT} does not install commercial roofs. Every low-slope membrane roof is {RC} work.</span></p>
      </div>
    </section>

    <section class="grey" id="co" aria-labelledby="co-h">
      <div class="wrap">
{sec_hd("02", f"Company 01 &middot; {SHORT}", "Gutters, siding and metal wall panels on buildings that work hard.", "On warehouses, apartment and condo buildings and commercial exteriors, we install and repair the exterior envelope, with the same owners, crews and standards as our residential work.", "co-h")}
        <div class="co-split">
          <div class="offset-media reveal">
            {picture("warehouse-dock-doors", "White tilt-up warehouse wall with loading dock doors and yellow bollards in sunlight", "(max-width:900px) 100vw, 56vw", cls="om-big", pos="center 60%")}
            {picture("indy-apartments-courtyard", "Courtyard lawn and mature tree at a garden-style Indianapolis apartment complex with brick and vinyl siding", "(max-width:900px) 46vw, 26vw", cls="om-sm")}
          </div>
          <div class="reveal" style="--d:.08s">
            <span class="co-tag">Company 01</span>
            <ol class="scope">
              <li><div><h3>Commercial gutters &amp; downspouts</h3><p>Seamless gutters custom-cut on site, plus guards, repair and cleaning, sized to move water away from the building.</p></div></li>
              <li><div><h3>Siding</h3><p>James Hardie&reg; fiber cement and Variform vinyl siding, installed and repaired by our own crews.</p></div></li>
              <li><div><h3>Metal wall panels</h3><p>Metal wall panel installation and repair on warehouse and commercial walls.</p></div></li>
            </ol>
            <div class="co-war"><b>5<small>yr</small></b><span>Workmanship warranty on gutters and siding</span></div>
            <div class="btn-row"><a class="btn btn-blue" href="/contact">Request an Estimate {ic("arrow")}</a><a class="text-link" href="/gutters">Seamless gutters {ic("arrow")}</a></div>
          </div>
        </div>
        <ul class="btypes reveal" aria-label="Building types">
          <li><span class="ico ico-blue">{ic("building")}</span>Warehouses</li>
          <li><span class="ico ico-blue">{ic("home")}</span>Apartment buildings</li>
          <li><span class="ico ico-blue">{ic("users")}</span>Condo buildings</li>
          <li><span class="ico ico-blue">{ic("layers")}</span>Commercial exteriors</li>
        </ul>
      </div>
    </section>

    <section class="com-band cm-band" id="membrane" aria-labelledby="mem-h">
      <div class="com-hero on-blue">
        {picture("indianapolis-skyline-dusk", "", "100vw", cls="com-bg", pos="center 60%")}
        <div class="wrap reveal">
          <span class="sec-num" aria-hidden="true">03</span>
          <span class="co-tag">Company 02</span>
          <span class="eyebrow">{RC}</span>
          <h2 id="mem-h">Low-slope membrane roofs, from a separate Rocklane company.</h2>
          <p>Commercial low-slope roofing is handled by {RC}, part of the Rocklane Group. {SHORT} does not install commercial roofs.</p>
        </div>
        <span class="photo-cap">{ic("pin")}Pictured: Indianapolis, Indiana</span>
      </div>
      <div class="wrap">
        <div class="mem-panel reveal">
          <div class="mem-grid">
            <article><span class="mk" aria-hidden="true">EPDM</span><span class="bar"></span><h3>EPDM membrane roofing</h3><p>Ethylene propylene diene monomer: a synthetic rubber roofing membrane for low-slope roofs.</p></article>
            <article><span class="mk" aria-hidden="true">TPO</span><span class="bar"></span><h3>TPO membrane roofing</h3><p>Thermoplastic polyolefin: a single-ply membrane with heat-welded seams.</p></article>
            <article><span class="mk" aria-hidden="true">PVC</span><span class="bar"></span><h3>PVC membrane roofing</h3><p>Polyvinyl chloride: a single-ply membrane with heat-welded seams.</p></article>
          </div>
          <div class="mem-foot">
            <div class="versico">
              <img src="/images/brands/versico-logo.png" width="2382" height="1077" alt="Versico Roofing Systems" loading="lazy">
              <p>{RC} is a GAF Certified Commercial Contractor and Versico Authorized.</p>
            </div>
            <div class="mf-r">
              <p>Call the Rocklane office to talk through a membrane roof.</p>
              <a class="btn btn-blue" href="tel:{TEL}">{ic("phone")}Call {PHONE}</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="grey" aria-labelledby="ho-h">
      <div class="wrap hoa-split">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">04</span>
          <span class="eyebrow">Property managers &amp; building owners</span>
          <h2 id="ho-h">One call for the whole building.</h2>
          <p>You manage buildings, not contractor org charts. Here is how a commercial or multifamily exterior project moves.</p>
          <ol class="handoff">
            <li><div><strong>You call the office</strong><span>Owners are active in daily management. If something goes wrong, you get an owner on the phone.</span></div></li>
            <li><div><strong>The scope is split by company</strong><span>Gutters, siding and metal wall panels go to {SHORT}. A low-slope membrane roof goes to {RC}. Both are part of the Rocklane Group.</span></div></li>
            <li><div><strong>Specialists when the building needs them</strong><span>Storm-damage inspectors, public adjusters and engineers from our specialist network. You never manage the handoff.</span></div></li>
            <li><div><strong>One record of the work</strong><span>Status, updates, photos and documents for {SHORT} projects in the customer portal.</span></div></li>
          </ol>
          <div class="ho-stat"><b>100+</b><span>Completed communities and commercial properties across central Indiana</span></div>
          <div class="btn-row"><a class="btn btn-blue" href="/property-managers">For HOA boards &amp; managers {ic("arrow")}</a></div>
        </div>
        <div class="offset-media left reveal">
          {picture("apartment-community-aerial", "Aerial view of a suburban garden-style apartment community among trees", "(max-width:900px) 100vw, 56vw", cls="om-big")}
          {picture("indy-brick-townhomes", "Two-story brick townhome buildings under large shade trees in Indianapolis at golden hour", "(max-width:900px) 44vw, 25vw", cls="om-sm", pos="center top")}
        </div>
      </div>
    </section>

{process("05")}

{CTA}"""
