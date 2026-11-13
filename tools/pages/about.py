"""About page. Section rhythm: hero (skyline photo / Shark Blue overlay), 01 mission (white),
02 ownership (Light Grey), 03 principles (Shark Blue photo band), 04 credentials (white),
05 Rocklane Group (Light Grey, shared COMMERCIAL_SPLIT), partners (white), final CTA.

Claims rules: "HAAG Certified Inspector" appears only beside Justin Reddick / Kevin Kortzendorf,
"IBHS FORTIFIED(TM) Roofing Contractor" only beside Greg Burkert / Michael Burkert. Versico appears
only inside COMMERCIAL_SPLIT, beside the Rocklane Commercial Contractors LLC credit.
"""
from site_common import *

PATH = "/about"
CURRENT = "/about"
TITLE = "About Rocklane Co. | Owner-Operated Since 1980"
DESC = ("Rocklane Company General Contractors LLC: owner-operated in central Indiana since 1980, "
        "a GAF Master Elite roofing contractor, part of the Rocklane Group.")
HEAD = ('\n  <link rel="preload" as="image" href="/images/photos/indianapolis-skyline-dusk-1200.jpg" '
        'imagesrcset="/images/photos/indianapolis-skyline-dusk-1200.jpg 1200w, /images/photos/indianapolis-skyline-dusk.jpg 2400w" '
        'imagesizes="100vw">')

CSS = """
/* about: hero */
.ab-hero { padding-bottom: clamp(110px, 12vw, 170px); }
.ab-hero h1 { max-width: 15ch; }
.ab-hero .ab-lede { font-size: clamp(1.1rem, 1.5vw, 1.3rem); max-width: 40rem; margin-top: .6rem; }
.ab-hero .hero-foot { list-style: none; padding-left: 0; margin-bottom: 0; }
.ab-hero .hero-foot li { display: inline-flex; gap: 8px; align-items: center; }
.ab-hero .hero-foot .i { font-size: 17px; color: var(--green); }

/* about: 01 mission */
.ab-mission { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: clamp(40px, 6vw, 104px); align-items: center; }
.ab-mission > * { min-width: 0; }
.ab-mission .ab-state { font-size: clamp(1.25rem, 2vw, 1.6rem); font-weight: 700; line-height: 1.35; color: var(--char); letter-spacing: -.01em; margin: 0 0 1.4rem; }
.ab-mission .ab-state em { font-style: normal; background: linear-gradient(transparent 62%, var(--green) 62%); }
.ab-owner-line { display: flex; gap: 16px; align-items: flex-start; margin-top: 2rem; padding-top: 1.6rem; border-top: 1px solid rgba(74,74,74,.2); }
.ab-owner-line p { margin: 0; }
.ab-mission .offset-media .om-big { aspect-ratio: 4 / 3; object-position: center 15%; }
.ab-mission .offset-media .om-sm { object-position: 45% center; }

/* about: 02 owners */
.ab-people { gap: clamp(14px, 1.6vw, 24px); }
.ab-people .person { display: flex; flex-direction: column; padding: clamp(26px, 2.4vw, 36px) clamp(22px, 2vw, 30px) clamp(26px, 2.4vw, 32px); min-height: 100%; }
.ab-people .person .mono { width: 76px; height: 76px; font-size: 24px; letter-spacing: .02em; margin-bottom: 26px; }
.ab-people .person h3 { font-size: clamp(1.2rem, 1.5vw, 1.4rem); margin: 0 0 .9rem; color: var(--blue); }
.ab-people .person .ab-role { display: block; font-size: .74rem; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: var(--blue); margin: 0 0 .7rem; line-height: 1.5; }
.ab-people .person .ab-cred { margin: auto 0 0; padding-top: 1rem; border-top: 1px solid var(--grey); font-size: .95rem; font-weight: 600; line-height: 1.5; color: var(--char); }
.ab-people .person.ab-next { border-top-color: var(--green); }
.ab-team { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: clamp(14px, 1.6vw, 24px); margin-top: clamp(14px, 1.6vw, 24px); }
.ab-team > div { display: grid; grid-template-columns: 56px 1fr; gap: 18px; align-items: start; background: var(--white); padding: clamp(24px, 2.4vw, 34px); }
.ab-team h3 { margin: 0 0 .35em; font-size: 1.15rem; }
.ab-team p { margin: 0; }
.ab-team .ico { width: 56px; height: 56px; }

/* about: 03 principles band */
.ab-band { position: relative; isolation: isolate; overflow: hidden; background: var(--blue-d); }
.ab-band-bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: -2; }
/* uniform >=88% Shark Blue: white text >=6.5:1 even over a white pixel */
.ab-band::before { content: ""; position: absolute; inset: 0; z-index: -1; background: linear-gradient(135deg, rgba(30,90,168,.9), rgba(23,72,138,.95)); }
.ab-band .values li { border-top-color: rgba(255,255,255,.35); }
.ab-band .values li::before { color: var(--white); }
.ab-band .values { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0 clamp(24px, 3vw, 48px); }
.ab-band .values h3 { font-size: clamp(1.15rem, 1.5vw, 1.35rem); }
.ab-band .values li:first-child { grid-column: 1 / -1; padding-bottom: 36px; }
.ab-band .values li:first-child h3 { font-size: clamp(1.4rem, 2.4vw, 2rem); }
.ab-band .values li:first-child p { font-size: clamp(1.1rem, 1.6vw, 1.35rem); font-weight: 600; max-width: 40rem; }
.ab-band .values li:first-child::before { font-size: 2.4rem; }

/* about: 04 credentials */
.ab-creds .card { min-height: 100%; }
.ab-creds .ab-k { display: block; font-size: .74rem; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: var(--char); margin-bottom: .7rem; }
.ab-creds .gaf-badge { margin-bottom: 22px; }
.ab-creds .ab-names { list-style: none; margin: auto 0 0; padding: 0; }
.ab-creds .ab-names li { display: flex; gap: 12px; align-items: center; padding: 12px 0; border-top: 1px solid var(--grey); font-weight: 700; color: var(--char); }
.ab-creds .ab-names .i { color: var(--blue); }
.ab-creds .ab-fine { font-size: .85rem; margin: auto 0 0; padding-top: 14px; border-top: 1px solid var(--grey); }

/* about: 05 group (shared commercial cards without the overlapping hero) */
.ab-group .com-cards { margin-top: 0; }

@media (max-width: 1100px) {
  .ab-people, .ab-band .values { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 900px) {
  .ab-mission, .ab-team { grid-template-columns: 1fr; }
  .ab-mission .offset-media { order: -1; margin-right: 6%; }
}
@media (max-width: 767px) {
  .ab-people { grid-template-columns: 1fr; }
  .ab-band .values { grid-template-columns: 1fr; }
  .ab-team > div { grid-template-columns: 1fr; }
}
@media print {
  .ab-band { background: var(--blue-d); }
  .person, .card { break-inside: avoid; }
}
"""


def person(initials, name, role, cred, cls=""):
    c = f" {cls}" if cls else ""
    return f"""<article class="person{c} reveal">
            <span class="mono" aria-hidden="true">{initials}</span>
            <h3>{name}</h3>
            <span class="ab-role">{role}</span>
            <p class="ab-cred">{cred}</p>
          </article>"""


HAAG = "HAAG Certified Inspector, Residential Roofs"
FORT = "IBHS FORTIFIED&trade; Roofing Contractor"

BODY = f"""    <div class="page-head on-blue has-photo ab-hero">
      {picture("indianapolis-skyline-dusk", "", "100vw", cls="ph-bg", eager=True, pos="center 60%")}
      <div class="wrap">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>About</span></nav>
        <span class="eyebrow">Owner-operated since 1980</span>
        <h1>The owners still answer the phone.</h1>
        <p class="ab-lede">{LEGAL} has been owner-operated in central Indiana since 1980. The people who own the company run the work, and if something goes wrong, you get an owner on the phone.</p>
        <ul class="hero-foot">
          <li>{ic("users")}Owners in daily management</li>
          <li>{ic("shield")}GAF Master Elite&reg; roofing contractor</li>
          <li>{ic("building")}Part of the Rocklane Group</li>
        </ul>
      </div>
      <span class="photo-cap">{ic("pin")}Pictured: Indianapolis, Indiana</span>
    </div>

    <section aria-labelledby="mis-h">
      <div class="wrap ab-mission">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">01</span>
          <span class="eyebrow">Our mission</span>
          <h2 id="mis-h">We protect the buildings that shelter Indiana.</h2>
          <p class="ab-state">With the craftsmanship of owners, the knowledge of specialists, and the accountability of a team that <em>signs its name to every project.</em></p>
          <p>Homes, condominium and townhome communities, apartment communities, and the walls and gutters of warehouses and commercial buildings across central Indiana, with more than 100 completed communities and commercial properties behind us. Roofing, siding and seamless gutters, installed by Rocklane crews and backed by our own workmanship warranty.</p>
          <div class="ab-owner-line">
            <span class="ico ico-blue">{ic("phone")}</span>
            <p>Owners are active in daily management. Reach them directly through the office at <a href="tel:{TEL}">{PHONE}</a>, {HOURS}.</p>
          </div>
        </div>
        <div class="offset-media reveal" style="--d:.1s">
          {picture("indy-brick-townhomes", "Two-story brick townhome buildings under large shade trees in Indianapolis at golden hour", "(max-width:900px) 94vw, 56vw", cls="om-big")}
          {picture("indiana-farmhouse-fall", "White two-story Indiana farmhouse with a shingle roof among bright fall maples", "(max-width:900px) 44vw, 26vw", cls="om-sm")}
        </div>
      </div>
    </section>

    <section class="grey" aria-labelledby="own-h">
      <div class="wrap">
{sec_hd("02", "Ownership", "The people who sign their name to the work.", f"{SHORT} is owned and operated by Justin Reddick, Kevin Kortzendorf and Greg Burkert. Michael Burkert joins as an owner on January 1, 2027.", "own-h")}
        <div class="people ab-people">
          {person("JR", "Justin Reddick", "Owner", HAAG)}
          {person("KK", "Kevin Kortzendorf", "Owner", HAAG)}
          {person("GB", "Greg Burkert", "Owner", FORT)}
          {person("MB", "Michael Burkert", "Joins as an owner on January 1, 2027", FORT, cls="ab-next")}
        </div>
        <div class="ab-team">
          <div class="reveal"><span class="ico ico-blue">{ic("clipboard")}</span><div><h3>Director of Training &amp; Quality Control</h3><p>On staff, not an outsourced function, setting the standard our crews install to.</p></div></div>
          <div class="reveal" style="--d:.08s"><span class="ico ico-blue">{ic("handshake")}</span><div><h3>Specialists on demand</h3><p>Storm-damage inspectors, public adjusters and engineers, brought in when a project needs them. You never manage the handoff.</p></div></div>
        </div>
      </div>
    </section>

    <section class="ab-band on-blue" aria-labelledby="val-h">
      {picture("tipton-roof-topdown", "", "100vw", cls="ab-band-bg")}
      <div class="wrap">
{sec_hd("03", "What we stand for", "Five principles, on every project.", "The standard we hold our crews, our specialists and ourselves to.", "val-h")}
        <ol class="values reveal">
          <li><h3>Workmanship is the warranty.</h3><p>&ldquo;{QUOTE}&rdquo;</p></li>
          <li><h3>One contractor, accountable.</h3><p>We coordinate the specialists, adjusters, engineers and suppliers. You never manage the handoff.</p></li>
          <li><h3>Straight answers, every time.</h3><p>If a repair will outperform a replacement, we say so &mdash; even when it means a smaller job.</p></li>
          <li><h3>Permanent results.</h3><p>We build to last past the warranty, not to the warranty.</p></li>
          <li><h3>Owners on every job.</h3><p>If something goes wrong, you get an owner on the phone &mdash; not a message system.</p></li>
        </ol>
      </div>
    </section>

    <section aria-labelledby="cred-h">
      <div class="wrap">
{sec_hd("04", "Credentials", "Certified where it counts.", "The company credential is GAF Master Elite&reg;. Individual inspection and resilience credentials belong to the owners who earned them.", "cred-h")}
        <div class="cards ab-creds">
          <article class="card reveal">
            {gaf_badge()}
            <span class="ab-k">{SHORT}</span>
            <h3>GAF Master Elite&reg; roofing contractor</h3>
            <p>{GAF_CLAIM_HTML}.</p>
            <p class="ab-fine">Master Elite&reg; status is what lets us offer GAF&rsquo;s Golden Pledge&reg; warranty on qualifying roofing systems. <a href="/roofing">GAF warranty options</a></p>
          </article>
          <article class="card reveal" style="--d:.08s">
            <span class="ico ico-blue">{ic("search")}</span>
            <span class="ab-k">Residential Roofs</span>
            <h3>Justin Reddick &amp; Kevin Kortzendorf</h3>
            <p>Owners, each a {HAAG}. Inspections at {SHORT} are owner-led.</p>
            <ul class="ab-names">
              <li>{ic("user")}Justin Reddick</li>
              <li>{ic("user")}Kevin Kortzendorf</li>
            </ul>
          </article>
          <article class="card reveal" style="--d:.16s">
            <span class="ico ico-blue">{ic("shield")}</span>
            <span class="ab-k">Resilient roofing</span>
            <h3>Greg Burkert &amp; Michael Burkert</h3>
            <p>Greg Burkert, owner, and Michael Burkert, who joins as an owner on January 1, 2027: each an {FORT}.</p>
            <ul class="ab-names">
              <li>{ic("user")}Greg Burkert</li>
              <li>{ic("user")}Michael Burkert</li>
            </ul>
          </article>
        </div>
      </div>
    </section>

    <section class="grey ab-group" aria-labelledby="grp-h">
      <div class="wrap">
{sec_hd("05", "The Rocklane Group", "Part of the Rocklane Group.", f"{SHORT} handles roofing, siding and gutters on homes and communities, plus gutters, siding and metal wall panels on warehouses and commercial buildings. Commercial low-slope membrane roofing is handled by our sister company, Rocklane Commercial Contractors LLC.", "grp-h")}
{COMMERCIAL_SPLIT}
      </div>
    </section>

{PARTNERS}

{CTA}"""
