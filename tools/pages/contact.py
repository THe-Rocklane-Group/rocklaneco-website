"""Contact page with the estimate form (js/estimate.js depends on its IDs: f-estimate, estimate-msg, estimate-fallback).

The <form id="f-estimate"> markup, field names/ids and #estimate-fallback are UNCHANGED; the page is
redesigned around them. Rhythm: page head (photo/blue), form + contact details (white),
01 who answers (Light Grey, media frame), 02 process (blue photo band), 03 visit the office (white, map),
04 service area (photo/blue).
"""
from site_common import *

PATH = "/contact"
CURRENT = '/contact'
TITLE = 'Contact Rocklane Co. | (317) 898-8696 | Indianapolis'
DESC = 'Call (317) 898-8696 or email rocklane@rocklaneco.com for a roofing, siding or gutter estimate. 1690 S. Franklin Rd., Indianapolis. Mon-Fri 9-4 ET.'
HEAD = ('\n  <link rel="preload" as="image" href="/images/photos/indy-brick-townhomes-1200.jpg" '
        'imagesrcset="/images/photos/indy-brick-townhomes-1200.jpg 1200w, /images/photos/indy-brick-townhomes.jpg 2400w" '
        'imagesizes="100vw">')
SCRIPTS = '\n  <script type="module" src="/js/estimate.js"></script>'

CSS = """
    .ct-head .page-head { padding-bottom: clamp(120px, 12vw, 176px); }
    .ct-head .page-head h1 { max-width: 14ch; }
    .ct-main { padding-top: 0; }
    .ct-main .contact-grid { gap: clamp(36px, 5vw, 80px); }
    .ct-main .form-card { margin-top: -112px; padding: clamp(26px, 3.4vw, 48px); }
    .ct-main .form-card > h2 { font-size: clamp(1.6rem, 2.6vw, 2.2rem); }
    .ct-main .form-card > .muted { margin-bottom: 1.6rem; }
    .ct-aside { padding-top: clamp(28px, 4vw, 56px); }
    .ct-aside h2 { font-size: clamp(1.6rem, 2.6vw, 2.2rem); }
    .ct-aside .info-list a { overflow-wrap: anywhere; }
    .ct-aside .info-list li { align-items: flex-start; }
    .ct-aside .info-list .ico { width: 44px; height: 44px; font-size: 20px; }
    .ct-aside h3 { display: flex; align-items: center; gap: 10px; font-size: 1.1rem; margin: 0 0 .4rem; }
    .ct-aside h3 .i { color: var(--blue); font-size: 20px; }
    .ct-aside .hours { margin-bottom: 1.4rem; }
    .ct-aside .hours td { font-size: .98rem; }
    .ct-aside .notice { margin: 1.4rem 0 0; }
    .ct-aside .notice a { white-space: nowrap; }
    .ct-who .split { align-items: center; }
    .ct-who .media-frame img { object-position: 78% center; }
    .ct-steps { list-style: none; margin: 1.6rem 0 2rem; padding: 0; counter-reset: s; display: grid; gap: 0; border-top: 1px solid rgba(74,74,74,.25); }
    .ct-steps li { counter-increment: s; display: grid; grid-template-columns: 56px minmax(0, 1fr); gap: 4px 16px; padding: 18px 0; border-bottom: 1px solid rgba(74,74,74,.25); }
    .ct-steps li::before { content: counter(s, decimal-leading-zero); grid-row: span 2; font-weight: 900; font-size: 1.9rem; line-height: 1; letter-spacing: -.04em; color: var(--blue); }
    .ct-steps strong { display: block; font-size: 1.02rem; }
    .ct-steps span { font-size: .96rem; line-height: 1.55; }
    .ct-visit { display: grid; grid-template-columns: minmax(0, 4fr) minmax(0, 8fr); gap: clamp(32px, 5vw, 72px); align-items: center; }
    .ct-visit address { font-style: normal; font-size: 1.15rem; font-weight: 700; color: var(--char); line-height: 1.5; margin-bottom: 1rem; }
    .ct-visit .map { height: clamp(320px, 38vw, 520px); background: var(--grey); }
    @media (max-width: 980px) {
      .ct-main .form-card { margin-top: -96px; }
      .ct-aside { padding-top: 0; }
      .ct-visit { grid-template-columns: 1fr; }
    }
    @media (max-width: 767px) {
      .ct-main .form-card { margin-top: -72px; }
    }
    @media print {
      .ct-main .form-card { margin-top: 0; box-shadow: none; }
      .ct-visit .map { display: none; }
    }
"""

BODY = f"""    <div class="ct-head">
{page_head("Free estimates", "Request an Estimate", "Call the office or send the form below. Owners are active in daily management, so the people you reach are the people who run the work.", "Contact", photo="indy-brick-townhomes", alt="", pos="center 15%")}
    </div>

    <section class="ct-main" aria-label="Estimate request and contact details">
      <div class="wrap contact-grid">
        <div class="form-card">
          <h2>Request an estimate</h2>
          <p class="muted">Tell us about the property and the work, and our office will get back to you.</p>
          <form id="f-estimate" class="form" hidden novalidate>
            <div class="field"><label for="e-name">Name</label><input id="e-name" name="name" autocomplete="name" required maxlength="100"></div>
            <div class="field-row">
              <div class="field"><label for="e-email">Email</label><input id="e-email" name="email" type="email" autocomplete="email" required maxlength="200"></div>
              <div class="field"><label for="e-phone">Phone</label><input id="e-phone" name="phone" type="tel" autocomplete="tel" required maxlength="40"></div>
            </div>
            <div class="field"><label for="e-address">Property address</label><input id="e-address" name="address" autocomplete="street-address" required maxlength="200"></div>
            <div class="field"><label for="e-project">Project</label>
              <select id="e-project" name="project">
                <option>Roof replacement</option><option>Roof repair</option><option>Roof inspection</option>
                <option>Storm damage</option><option>Siding</option><option>Gutters</option>
                <option>HOA or multi-building property</option><option>Other</option>
              </select></div>
            <div class="field"><label for="e-details">Details <span class="muted">(optional)</span></label><textarea id="e-details" name="details" rows="4" maxlength="3000"></textarea></div>
            <div class="hp" aria-hidden="true"><label for="e-website">Leave this field empty</label><input id="e-website" name="website" tabindex="-1" autocomplete="off"></div>
            <p class="fine">We use your information only to respond to this request. See our <a href="/privacy-policy">privacy policy</a>.</p>
            <button class="btn" type="submit">Send Request</button>
            <p id="estimate-msg" class="notice" role="status" hidden></p>
          </form>
          <div id="estimate-fallback">
            <p>Email your name, the property address and a short description of the project, and we&rsquo;ll get back to you.</p>
            <a class="btn btn-outline" href="mailto:{EMAIL}?subject=Estimate%20request&amp;body=Name%3A%0AProperty%20address%3A%0APhone%3A%0AProject%20(roof%2C%20siding%2C%20gutters%2C%20other)%3A%0ADetails%3A">Email an Estimate Request</a>
          </div>
        </div>
        <div class="ct-aside">
          <span class="eyebrow">Talk to our team</span>
          <h2>Prefer to talk it through?</h2>
          <p>The fastest way to reach us is by phone. If something goes wrong, you get an owner on the phone.</p>
          <ul class="info-list">
            <li><span class="ico ico-blue">{ic("phone")}</span><div><small>Office</small><a href="tel:{TEL}">{PHONE}</a></div></li>
            <li><span class="ico ico-blue">{ic("mail")}</span><div><small>Email</small><a href="mailto:{EMAIL}?subject=Estimate%20request">{EMAIL}</a></div></li>
            <li><span class="ico ico-blue">{ic("pin")}</span><div><small>Office address</small><address>{ADDRESS.replace('<br>', ', ')}</address></div></li>
          </ul>
          <h3>{ic("clock")}Office hours</h3>
          <table class="hours">
            <caption class="sr">Office hours, Eastern Time</caption>
            <tr><td>Monday &ndash; Friday</td><td>9 AM &ndash; 4 PM ET</td></tr>
            <tr><td>Saturday</td><td>By appointment</td></tr>
            <tr><td>Sunday</td><td>Closed</td></tr>
          </table>
          <a class="text-link" href="{GBP}" rel="noopener">Directions on Google Maps {ic("arrow")}</a>
          <p class="notice">Current customers: <a href="/portal/">sign in to the customer portal</a> to check your project.</p>
        </div>
      </div>
    </section>

    <section class="grey ct-who" aria-labelledby="who-h">
      <div class="wrap split">
        <figure class="media-frame reveal">
          {picture("two-story-home-hero", "Two-story suburban home with charcoal architectural shingles, gray vinyl lap siding, stone base and white K-style gutters", "(max-width:980px) 100vw, 50vw")}
          <div class="tag"><span class="ico ico-blue">{ic("shield")}</span><div><strong>10-year workmanship warranty</strong><span>on roof replacements</span></div></div>
        </figure>
        <div class="reveal" style="--d:.08s">
          <span class="sec-num" aria-hidden="true">01</span>
          <span class="eyebrow">After you reach out</span>
          <h2 id="who-h">One office, from the first call to the final walkthrough.</h2>
          <p class="lead">Roofing, siding and seamless gutters for Indiana homes and communities, owner-operated since 1980.</p>
          <ol class="ct-steps">
            <li><strong>Owner-led inspections</strong><span>We look at the roof, siding or gutters in person and put the scope in writing.</span></li>
            <li><strong>Specialists when you need them</strong><span>Storm-damage inspectors, public adjusters and engineers, activated on demand. You never manage the handoff.</span></li>
            <li><strong>Our name on the work</strong><span>10 years on roof replacements, 5 years on repairs, gutters, chimneys and siding.</span></li>
          </ol>
          <a class="text-link" href="/about">Meet the owners {ic("arrow")}</a>
        </div>
      </div>
    </section>

{process("02")}

    <section aria-labelledby="visit-h">
      <div class="wrap ct-visit">
        <div class="reveal">
          <span class="sec-num" aria-hidden="true">03</span>
          <span class="eyebrow">Visit the office</span>
          <h2 id="visit-h">Stop by the Indianapolis office.</h2>
          <address>{LEGAL}<br>{ADDRESS}</address>
          <p>{HOURS}<br>{HOURS_SAT}</p>
          <div class="btn-row">
            <a class="btn btn-blue" href="{GBP}" rel="noopener">{ic("pin")}Open in Google Maps</a>
            <a class="btn btn-outline" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
          </div>
        </div>
        <iframe class="map reveal" title="Map to {SHORT}, 1690 S. Franklin Rd., Indianapolis" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          src="https://www.google.com/maps?q=Rocklane+Co.+General+Contractors,+1690+S+Franklin+Rd,+Indianapolis,+IN+46239&amp;output=embed"></iframe>
      </div>
    </section>

{service_area("04")}"""
