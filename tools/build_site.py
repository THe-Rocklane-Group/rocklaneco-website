"""Builds the Rocklane Co. website (plain HTML) into ../site.

Run:  python3 tools/build_site.py
Copy, claims, colors and type follow The Rocklane Group Brand Foundation v2.
Edit the text below, re-run, then publish the site/ folder.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "site")

DOMAIN = "https://rocklaneco.com"
LEGAL = "Rocklane Company General Contractors LLC"
SHORT = "Rocklane Co."
TAGLINE = "Built to Outlast the Warranty."
PHONE = "(317) 898-8696"
TEL = "+13178988696"
EMAIL = "rocklane@rocklaneco.com"
ADDRESS = "1690 S. Franklin Rd.<br>Indianapolis, IN 46239"
GBP = "https://www.google.com/maps?cid=1030444210742474565"
CITIES = ["Indianapolis", "Carmel", "Fishers", "Westfield", "Zionsville", "Greenwood",
          "Bloomington", "Avon", "Brownsburg", "Noblesville", "Pittsboro", "Greenfield",
          "Lawrence", "West Lafayette", "Danville"]

NAV = [("/roofing", "Roofing"), ("/siding", "Siding"), ("/gutters", "Gutters"),
       ("/property-managers", "HOA &amp; Property Managers"), ("/about", "About"),
       ("/contact", "Contact")]

SCHEMA = {
    "@context": "https://schema.org",
    "@type": "RoofingContractor",
    "name": LEGAL,
    "alternateName": SHORT,
    "slogan": TAGLINE,
    "foundingDate": "1980",
    "url": DOMAIN + "/",
    "image": DOMAIN + "/images/home.jpg",
    "logo": DOMAIN + "/images/rocklane-co-logo.jpg",
    "telephone": "+1-317-898-8696",
    "email": EMAIL,
    "address": {"@type": "PostalAddress", "streetAddress": "1690 S. Franklin Rd.",
                "addressLocality": "Indianapolis", "addressRegion": "IN",
                "postalCode": "46239", "addressCountry": "US"},
    "geo": {"@type": "GeoCoordinates", "latitude": 39.7472691, "longitude": -86.0266018},
    "areaServed": [{"@type": "City", "name": c + ", IN"} for c in CITIES],
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "09:00", "closes": "16:00"}],
    "hasMap": GBP,
    "sameAs": [GBP],
}


def page(path, title, desc, body, current, head="", scripts="", index=True):
    cur = ' aria-current="page"'
    nav = "\n".join('        <a href="%s"%s>%s</a>' % (h, cur if h == current else "", t)
                    for h, t in NAV)
    canonical = DOMAIN + path
    schema = json.dumps(SCHEMA, indent=2)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">{'' if index else chr(10) + '  <meta name="robots" content="noindex, nofollow">'}{head}
  <meta name="theme-color" content="#1E5AA8">
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
  <link rel="apple-touch-icon" href="/images/icon-180.png">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SHORT}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{DOMAIN}/images/home.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;900&display=swap">
  <link rel="stylesheet" href="/css/style.css">
  <script type="application/ld+json">
{schema}
  </script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <div class="topbar">
    <div class="wrap">
      <span>Owner-Operated. Indiana-Proven.<span class="hide-sm"> &nbsp;&middot;&nbsp; Since 1980</span></span>
      <span><a href="tel:{TEL}">{PHONE}</a><span class="hide-sm"> &nbsp;|&nbsp; Mon&ndash;Fri 9 AM&ndash;4 PM ET</span> &nbsp;|&nbsp; <a href="/portal">Customer Login</a></span>
    </div>
  </div>
  <header class="site-header">
    <div class="wrap">
      <!-- Approved Rocklane Co. primary lockup (Nov 4, 2026 kit). Do not stretch, recolor or add effects. -->
      <a class="brand" href="/">
        <img src="/images/rocklane-co-logo.jpg" width="560" height="135" alt="Rocklane Co. General Contractors LLC">
      </a>
      <button class="menu-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
      <nav class="nav" id="nav" aria-label="Main">
{nav}
        <a class="btn" href="tel:{TEL}">Call {PHONE}</a>
      </nav>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer on-blue">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <p class="tagline">{TAGLINE}</p>
          <p>{LEGAL}<br>Roofing, siding and gutters for property managers, HOA boards and homeowners across central Indiana. Since 1980.</p>
        </div>
        <div>
          <h3>Contact</h3>
          <ul>
            <li><a href="tel:{TEL}">{PHONE}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>{ADDRESS}</li>
          </ul>
        </div>
        <div>
          <h3>Hours</h3>
          <ul>
            <li>Mon&ndash;Fri: 9 AM&ndash;4 PM ET</li>
            <li>Saturday: By appointment</li>
            <li>Sunday: Closed</li>
          </ul>
        </div>
      </div>
      <p class="legal">&copy; <span id="yr">2026</span> {LEGAL}, a Rocklane Group company. GAF, Master Elite and Golden Pledge are registered trademarks of GAF. &middot; <a href="/privacy-policy">Privacy</a> &middot; <a href="/portal-terms">Portal Terms</a> &middot; <a href="/portal">Customer Login</a></p>
    </div>
  </footer>

  <div class="call-bar">
    <a href="tel:{TEL}">Call Now</a>
    <a href="/contact">Request an Estimate</a>
  </div>

  <script src="/js/site.js" defer></script>{scripts}
</body>
</html>
"""


CTA = f"""    <section>
      <div class="wrap">
        <div class="callout on-blue">
          <div>
            <h2>Talk to an owner about your project.</h2>
            <p>Call the office and you&rsquo;ll reach the people who run the work &mdash; not a call center.</p>
          </div>
          <div class="btn-row">
            <a class="btn" href="tel:{TEL}">Call {PHONE}</a>
            <a class="btn btn-outline" href="/contact">Request an Estimate</a>
          </div>
        </div>
      </div>
    </section>"""

WARRANTY = """    <section class="grey">
      <div class="wrap">
        <div class="center"><span class="eyebrow">Workmanship is the warranty</span></div>
        <h2 class="center">Manufacturers cover materials. We cover the work.</h2>
        <p class="section-intro">If we installed it, we own it. Every Rocklane Co. project carries our own written workmanship warranty, on top of the manufacturer&rsquo;s coverage.</p>
        <div class="warranty">
          <div><b>10 years</b><strong>Roof replacements</strong><p>Workmanship coverage on every roof replacement we install.</p></div>
          <div><b>5 years</b><strong>Repairs, gutters, chimneys &amp; siding</strong><p>Workmanship coverage on repair work, gutter systems, chimneys and siding.</p></div>
        </div>
      </div>
    </section>"""

PILLARS = """    <section>
      <div class="wrap">
        <h2 class="center">Why property managers and homeowners call Rocklane Co.</h2>
        <p class="section-intro">Four commitments behind every project.</p>
        <div class="cards four">
          <div class="card"><h3>Owner-operated accountability</h3><p>Owners are active in daily management. If something goes wrong, you get an owner on the phone.</p></div>
          <div class="card"><h3>Certified craftsmanship</h3><p>GAF Master Elite&reg; (top 2% nationally), HAAG Certified Inspectors and IBHS FORTIFIED&trade; Roofing Contractors on the team.</p></div>
          <div class="card"><h3>The specialist network</h3><p>Storm damage inspectors, public adjusters, engineers and more, activated on demand. You never manage the handoff.</p></div>
          <div class="card"><h3>Central Indiana track record</h3><p>100+ completed communities and commercial properties across central Indiana. The same team, every time.</p></div>
        </div>
      </div>
    </section>"""


HOME = f"""    <section class="hero on-blue">
      <div class="wrap">
        <div>
          <p class="tag">Roofing. Siding. Gutters. Handled.</p>
          <h1>{TAGLINE}</h1>
          <p class="lead">{SHORT} protects homes, condominiums and townhome communities across central Indiana. Owner-operated since 1980, with a GAF Master Elite&reg; certification held by the top 2% of roofing contractors nationally.</p>
          <ul class="proof">
            <li>Since 1980</li>
            <li>GAF Master Elite&reg;</li>
            <li>10-year workmanship warranty</li>
          </ul>
          <div class="btn-row">
            <a class="btn" href="tel:{TEL}">Call {PHONE}</a>
            <a class="btn btn-outline" href="/contact">Request an Estimate</a>
          </div>
        </div>
        <img src="/images/home.jpg" width="370" height="300" alt="Two-story home with a dark shingle roof and vinyl siding">
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="center"><span class="eyebrow">What we install</span></div>
        <h2 class="center">The whole exterior, one accountable contractor.</h2>
        <p class="section-intro">Roofs, siding and gutters work as one system to protect a building. We install and maintain all three, so nothing falls between trades.</p>
        <div class="cards">
          <div class="card">
            <h3>Roofing</h3>
            <p>Replacements, repairs and inspections, installed as complete GAF roofing systems by a Master Elite&reg; contractor.</p>
            <a class="more" href="/roofing">Roofing</a>
          </div>
          <div class="card">
            <h3>Siding</h3>
            <p>James Hardie&reg; fiber cement and Variform vinyl siding, installed and repaired by our own crews.</p>
            <a class="more" href="/siding">Siding</a>
          </div>
          <div class="card">
            <h3>Gutters</h3>
            <p>Seamless gutters, gutter guards, repairs and cleaning that move water away from the building.</p>
            <a class="more" href="/gutters">Gutters</a>
          </div>
        </div>
      </div>
    </section>

{WARRANTY}

{PILLARS}

    <section class="on-blue">
      <div class="wrap">
        <div class="stat-row">
          <div class="stat"><b>1980</b><span>Serving Indiana since</span></div>
          <div class="stat"><b>Top 2%</b><span>GAF Master Elite&reg; nationally</span></div>
          <div class="stat"><b>100+</b><span>Communities &amp; properties completed</span></div>
          <div class="stat"><b>10 yr</b><span>Workmanship warranty on roof replacements</span></div>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap split">
        <div>
          <span class="eyebrow">For HOA boards &amp; property managers</span>
          <h2>Capital exterior projects without the risk.</h2>
          <p>A board answers to owners who fear special assessments. We help you plan the investment, document the condition of every building, and deliver the project on the scope we bid.</p>
          <a class="btn btn-outline" href="/property-managers">How we work with communities</a>
        </div>
        <img src="/images/roofing.jpg" width="370" height="300" loading="lazy" alt="Roofer hand-nailing asphalt shingles">
      </div>
    </section>

{CTA}"""


ROOFING = f"""    <div class="page-head on-blue">
      <div class="wrap">
        <span class="eyebrow">GAF Master Elite&reg; Roofing Contractor</span>
        <h1>Roofing</h1>
        <p>Roof replacements, repairs and inspections for homes, condominiums and townhome communities across central Indiana.</p>
      </div>
    </div>

    <section>
      <div class="wrap split">
        <div>
          <h2>A roof installed to outlast its warranty.</h2>
          <p>We build to last past the warranty, not to the warranty. Every roof is installed to a standard that makes the callback unnecessary.</p>
          <ul class="checks">
            <li><strong>Roof replacement:</strong> complete GAF roofing systems, hand-nailed by our crews and backed by our 10-year workmanship warranty.</li>
            <li><strong>Roof repair:</strong> we find the cause of the leak or damage, not just the symptom, and back the repair for 5 years.</li>
            <li><strong>Inspections:</strong> HAAG Certified Inspectors document the condition of your roof so you can plan the investment.</li>
            <li><strong>Storm damage:</strong> we coordinate inspectors, adjusters and engineers from our specialist network, so you never manage the handoff.</li>
          </ul>
          <div class="btn-row"><a class="btn" href="tel:{TEL}">Call {PHONE}</a></div>
        </div>
        <img src="/images/roofing.jpg" width="370" height="300" alt="Roofer hand-nailing asphalt shingles">
      </div>
    </section>

    <section class="grey">
      <div class="wrap">
        <div class="center"><span class="eyebrow">Top 2% nationally</span></div>
        <h2 class="center">What GAF Master Elite&reg; means for your building.</h2>
        <p class="section-intro">Only about 2% of roofing contractors earn GAF Master Elite&reg; certification. It gives you access to GAF&rsquo;s extended warranty programs, which most regional contractors cannot offer.</p>
        <div class="cards">
          <div class="card"><h3>System Plus Limited Warranty</h3><p>GAF shingles plus three qualifying GAF accessory products.</p></div>
          <div class="card"><h3>Silver Pledge&reg; Limited Warranty</h3><p>GAF shingles plus four qualifying accessories, with added coverage.</p></div>
          <div class="card"><h3>Golden Pledge&reg; Limited Warranty</h3><p>GAF&rsquo;s strongest coverage, available only through Master Elite&reg; contractors.</p></div>
        </div>
        <p class="center" style="margin-top:20px">GAF sets warranty terms and eligibility. We&rsquo;ll walk you through the options for your building.</p>
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2>Signs a roof needs attention</h2>
        <ul class="checks">
          <li>Curling, cracked or missing shingles</li>
          <li>Shingle granules collecting in the gutters</li>
          <li>Water stains on ceilings or in the attic</li>
          <li>Sagging areas or daylight through the roof deck</li>
          <li>Hail or wind damage after a storm</li>
        </ul>
        <p>If a repair will outperform a replacement, we&rsquo;ll tell you. Straight answers, every time.</p>
      </div>
    </section>

{CTA}"""


SIDING = f"""    <div class="page-head on-blue">
      <div class="wrap">
        <span class="eyebrow">Fiber cement &amp; vinyl</span>
        <h1>Siding</h1>
        <p>James Hardie&reg; and Variform siding, installed and repaired by our own crews.</p>
      </div>
    </div>

    <section>
      <div class="wrap split">
        <div>
          <h2>Siding that protects the building envelope.</h2>
          <p>Siding is the first layer of protection for every wall. We install it to keep water out for decades and back our siding work with a 5-year workmanship warranty.</p>
          <ul class="checks">
            <li><strong>Siding replacement:</strong> fiber cement, vinyl or wood siding, installed with precise flashing and trim details.</li>
            <li><strong>Siding repair:</strong> storm, impact and moisture damage repaired and matched to the existing exterior.</li>
            <li><strong>Inspections:</strong> we identify problem areas before they turn into rot, mold or interior damage.</li>
          </ul>
          <div class="btn-row"><a class="btn" href="tel:{TEL}">Call {PHONE}</a></div>
        </div>
        <img src="/images/siding.jpg" width="370" height="300" alt="Installer fitting a panel of vinyl siding">
      </div>
    </section>

    <section class="grey">
      <div class="wrap">
        <h2 class="center">The siding we install</h2>
        <div class="cards two">
          <div class="card"><h3>James Hardie&reg; fiber cement</h3><p>Durable, weather-resistant fiber cement siding in a wide range of profiles and colors.</p></div>
          <div class="card"><h3>Variform vinyl siding</h3><p>High-performance vinyl siding that stands up to Indiana weather with very little upkeep.</p></div>
        </div>
      </div>
    </section>

{WARRANTY}

{CTA}"""


GUTTERS = f"""    <div class="page-head on-blue">
      <div class="wrap">
        <span class="eyebrow">Seamless gutters &amp; guards</span>
        <h1>Gutters</h1>
        <p>Installation, gutter protection, repair and cleaning for homes and communities.</p>
      </div>
    </div>

    <section>
      <div class="wrap">
        <h2>Move water away from the building.</h2>
        <p>Working gutters protect the roof, siding, foundation and landscaping from water damage. We custom-cut seamless gutters on site to fit each roofline, and back gutter work with our 5-year workmanship warranty.</p>
        <div class="cards">
          <div class="card"><h3>Installation &amp; repair</h3><p>New seamless gutter systems, replacement of worn-out runs, or repair of a damaged system.</p></div>
          <div class="card"><h3>Gutter protection</h3><p>Gutter guards from leading manufacturers to prevent clogs, overflow and ice buildup.</p></div>
          <div class="card"><h3>Cleaning</h3><p>Seasonal cleaning so gutters and downspouts are clear before the next storm.</p></div>
        </div>
      </div>
    </section>

    <section class="grey">
      <div class="wrap">
        <h2>Colors to match the exterior</h2>
        <p>Choose from dozens of gutter colors, including white, almond, bronze, black, clay, musket brown, forest green and copper. We&rsquo;ll help you match the trim and roof.</p>
      </div>
    </section>

{CTA}"""


CITY_LIST = "".join(f"<li>{c}</li>" for c in CITIES)
PM = f"""    <div class="page-head on-blue">
      <div class="wrap">
        <span class="eyebrow">Communities &amp; multi-family</span>
        <h1>HOA &amp; Property Managers</h1>
        <p>Roofing, siding and gutter projects for condominium and townhome communities across central Indiana.</p>
      </div>
    </div>

    <section>
      <div class="wrap split">
        <div>
          <h2>We remove the risk from capital exterior projects.</h2>
          <p>Your board answers to owners who don&rsquo;t want a special assessment. You need a contractor whose scope holds, whose crews show up, and whose owners answer the phone. Our name is on the building, the paperwork, and the phone when you call.</p>
          <ul class="checks">
            <li><strong>Reserve planning support:</strong> documented condition reports from HAAG Certified Inspectors, so the board can plan the investment.</li>
            <li><strong>One point of contact:</strong> a Rocklane project manager from first walk-through to final inspection.</li>
            <li><strong>Storm response:</strong> we activate inspectors, public adjusters and engineers from our network, with no retainers passed to the community.</li>
            <li><strong>Warranty you can file:</strong> GAF extended warranties plus our 10-year workmanship warranty on roof replacements.</li>
          </ul>
        </div>
        <img src="/images/home.jpg" width="370" height="300" loading="lazy" alt="Two-story home with a dark shingle roof and vinyl siding">
      </div>
    </section>

    <section class="on-blue">
      <div class="wrap">
        <div class="stat-row">
          <div class="stat"><b>100+</b><span>Communities &amp; properties completed</span></div>
          <div class="stat"><b>Since 1980</b><span>Owner-operated</span></div>
          <div class="stat"><b>Top 2%</b><span>GAF Master Elite&reg;</span></div>
          <div class="stat"><b>15</b><span>Central Indiana cities served</span></div>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2>Where we work</h2>
        <p>Recurring clients include communities managed by major central Indiana property management firms. A documented list of completed projects is available to any board or manager on request.</p>
        <ul class="cities">{CITY_LIST}</ul>
      </div>
    </section>

{CTA}"""


ABOUT = f"""    <div class="page-head on-blue">
      <div class="wrap">
        <span class="eyebrow">Since 1980</span>
        <h1>About {SHORT}</h1>
        <p>Owner-operated. Indiana-proven.</p>
      </div>
    </div>

    <section>
      <div class="wrap">
        <h2>Our mission</h2>
        <p class="lead">We protect the buildings that shelter Indiana &mdash; with the craftsmanship of owners, the knowledge of specialists, and the accountability of a team that signs its name to every project.</p>
        <p>{LEGAL} is owned and operated by Justin Reddick, Kevin Kortzendorf and Greg Burkert, owners with decades of hands-on experience. Michael Burkert joins as an owner on January 1, 2027. Owners are active in daily management, and you can reach them directly through the office at <a href="tel:{TEL}">{PHONE}</a>.</p>
      </div>
    </section>

    <section class="grey">
      <div class="wrap">
        <h2 class="center">Credentials</h2>
        <div class="cards">
          <div class="card"><h3>GAF Master Elite&reg; Roofing Contractor</h3><p>Held by the top 2% of roofing contractors nationally.</p></div>
          <div class="card"><h3>HAAG Certified Inspector &mdash; Residential Roofs</h3><p>Justin Reddick and Kevin Kortzendorf.</p></div>
          <div class="card"><h3>IBHS FORTIFIED&trade; Roofing Contractor</h3><p>Greg Burkert and Michael Burkert.</p></div>
        </div>
        <p class="center" style="margin-top:20px">A Director of Training &amp; Quality Control is on staff &mdash; not an outsourced function.</p>
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2>What we stand for</h2>
        <div class="cards">
          <div class="card"><h3>Workmanship is the warranty.</h3><p>Manufacturer warranties cover materials. We cover the work. If we installed it, we own it.</p></div>
          <div class="card"><h3>One contractor, accountable.</h3><p>We coordinate the specialists, adjusters, engineers and suppliers. You never get handed off.</p></div>
          <div class="card"><h3>Straight answers, every time.</h3><p>If a repair will outperform a replacement, we say so &mdash; even when it means a smaller job.</p></div>
          <div class="card"><h3>Permanent results.</h3><p>We build to last past the warranty, not to the warranty.</p></div>
          <div class="card"><h3>Owners on every job.</h3><p>If something goes wrong, you get an owner on the phone &mdash; not a message system.</p></div>
        </div>
      </div>
    </section>

    <section class="grey">
      <div class="wrap">
        <h2>Part of the Rocklane Group</h2>
        <p>{SHORT} is one of the operating companies of the Rocklane Group, which shares one quality standard, one team and one equipment base. Commercial low-slope roofing (EPDM, TPO and PVC) is handled by Rocklane Commercial Contractors LLC, a GAF Certified Commercial Contractor and Versico Authorized Contractor.</p>
      </div>
    </section>

{CTA}"""


CONTACT = f"""    <div class="page-head on-blue">
      <div class="wrap">
        <span class="eyebrow">Free estimates</span>
        <h1>Contact</h1>
        <p>Call the office or send the form below to request an estimate or an inspection.</p>
      </div>
    </div>

    <section>
      <div class="wrap contact-grid">
        <div>
          <h2>Request an estimate</h2>
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
        <div>
          <h2>Talk to our team</h2>
          <p>The fastest way to reach us is by phone.</p>
          <ul class="info-list">
            <li><small>Office</small><a href="tel:{TEL}">{PHONE}</a></li>
            <li><small>Email</small><a href="mailto:{EMAIL}?subject=Estimate%20request">{EMAIL}</a></li>
            <li><small>Address</small>{ADDRESS.replace('<br>', ', ')}</li>
          </ul>
          <h3 style="margin-top:28px">Hours</h3>
          <table class="hours">
            <tr><td>Monday &ndash; Friday</td><td>9 AM &ndash; 4 PM ET</td></tr>
            <tr><td>Saturday</td><td>By appointment</td></tr>
            <tr><td>Sunday</td><td>Closed</td></tr>
          </table>
          <p style="margin-top:20px"><a href="{GBP}" rel="noopener">Directions on Google Maps</a></p>
          <p>Current customers: <a href="/portal">sign in to the customer portal</a> to check your project.</p>
        </div>
      </div>
    </section>

    <section style="padding-top:0">
      <div class="wrap">
        <iframe class="map" title="Map to {SHORT}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          src="https://www.google.com/maps?q=Rocklane+Co.+General+Contractors,+1690+S+Franklin+Rd,+Indianapolis,+IN+46239&amp;output=embed"></iframe>
      </div>
    </section>"""


PRIVACY = f"""    <div class="page-head on-blue">
      <div class="wrap">
        <h1>Privacy Policy</h1>
        <p>{LEGAL} &middot; Updated November 6, 2026</p>
      </div>
    </div>
    <section>
      <div class="wrap prose">
        <h2>What we collect</h2>
        <ul>
          <li><strong>Estimate requests.</strong> Your name, email, phone number, property address and the project details you send through our contact form, by phone or by email.</li>
          <li><strong>Customer portal accounts.</strong> Your name, email, phone number, company or HOA name and property address, plus a password that is stored only in encrypted form by Google Firebase. We never see your password.</li>
          <li><strong>Project files.</strong> Photos and documents you or our team upload to your project.</li>
          <li><strong>Portal activity.</strong> A record of sign-ins, uploads and downloads, kept for security and to support you.</li>
        </ul>
        <h2>How we use it</h2>
        <p>We use your information only to respond to you, prepare estimates, carry out and document your project, give you access to the customer portal, and keep the portal secure. We do not sell or rent your personal information, and we do not use advertising trackers.</p>
        <h2>Who stores it</h2>
        <p>Portal accounts and project records are stored with Google Firebase. Estimate requests, emails and project files are stored in our Google Workspace account. Project videos are hosted on YouTube as unlisted videos, shown in the portal only to the customers on that project. Our pages load the Montserrat typeface from Google Fonts, and the map on our contact page is provided by Google. Google may collect technical information under its own privacy policy.</p>
        <h2>Cookies and storage</h2>
        <p>The public website sets no cookies of its own. When you sign in to the customer portal, your browser stores a sign-in token so you stay signed in. Uncheck &ldquo;Keep me signed in&rdquo; on shared computers. The portal signs you out after 60 minutes without activity.</p>
        <h2>How long we keep it</h2>
        <p>We keep project records and files for as long as needed for your project, its warranty period and our legal and tax obligations. You may ask us to close your portal account at any time.</p>
        <h2>Your choices</h2>
        <p>To see, correct or delete your information, or to close your portal account, contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{TEL}">{PHONE}</a>.</p>
      </div>
    </section>"""


TERMS = f"""    <div class="page-head on-blue">
      <div class="wrap">
        <h1>Customer Portal Terms of Use</h1>
        <p>{LEGAL} &middot; Updated November 6, 2026</p>
      </div>
    </div>
    <section>
      <div class="wrap prose">
        <p>The {SHORT} customer portal lets our customers follow their projects, share photos and documents with our team, and view project videos. By creating an account you agree to these terms.</p>
        <h2>Your account</h2>
        <ul>
          <li>Accounts are for {SHORT} customers, property managers and board members with a project we are performing or have performed.</li>
          <li>Keep your password private and don&rsquo;t share your account. Tell us right away at {PHONE} if you think someone else has used it.</li>
          <li>We give access to a project only to the email addresses connected to it. We may change or remove access when a project&rsquo;s contacts change.</li>
        </ul>
        <h2>Files you upload</h2>
        <ul>
          <li>Upload only photos and documents related to your project that you have the right to share.</li>
          <li>Files are visible to our team and to the other contacts on the same project.</li>
          <li>Don&rsquo;t upload payment card numbers, Social Security numbers or other sensitive personal information.</li>
        </ul>
        <h2>Project information and videos</h2>
        <p>Project status, updates and videos are provided for your convenience. Your signed contract, estimate and warranty documents govern your project. Project videos are for your use in connection with your property and may not be republished without our permission.</p>
        <h2>Availability</h2>
        <p>We work to keep the portal available but cannot guarantee it will always be. If you can&rsquo;t reach it, call the office at <a href="tel:{TEL}">{PHONE}</a>.</p>
        <h2>Privacy</h2>
        <p>Our <a href="/privacy-policy">privacy policy</a> explains what we collect and how we use it.</p>
      </div>
    </section>"""


NOTFOUND = """    <section>
      <div class="wrap center">
        <h1>Page not found</h1>
        <p class="section-intro">That page has moved. Try one of these:</p>
        <div class="btn-row" style="justify-content:center">
          <a class="btn" href="/">Home</a>
          <a class="btn btn-outline" href="/roofing">Roofing</a>
          <a class="btn btn-outline" href="/contact">Contact</a>
        </div>
      </div>
    </section>"""


# ---------------------------------------------------------------- customer portal
# The portal's logic lives in hand-written files in site/portal/ (config.js, common.js,
# portal.js, staff.js). This script only writes the HTML around them.

CSP = ("default-src 'self'; script-src 'self' https://www.gstatic.com; "
       "connect-src 'self' https://*.googleapis.com https://script.google.com https://script.googleusercontent.com; "
       "frame-src https://www.youtube-nocookie.com https://*.firebaseapp.com; "
       "img-src 'self' data: blob:; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
       "font-src https://fonts.gstatic.com; object-src 'none'; base-uri 'self'; form-action 'self'")
PORTAL_HEAD = f'\n  <meta http-equiv="Content-Security-Policy" content="{CSP}">\n  <meta name="referrer" content="strict-origin-when-cross-origin">'

SETUP_VIEW = """        <div class="view" id="v-setup" hidden>
          <h2>Coming soon</h2>
          <p>Our customer portal is being set up. In the meantime, call the office at <a href="tel:{TEL}">{PHONE}</a> for an update on your project.</p>
        </div>""".format(TEL=TEL, PHONE=PHONE)

ACCOUNT_BAR = """      <div class="acct" id="acct" hidden>
        <span>Signed in as <strong id="acct-email"></strong></span>
        <button type="button" class="link btn-signout">Sign out</button>
      </div>"""

PORTAL = f"""    <div class="page-head on-blue">
      <div class="wrap">
        <span class="eyebrow">Customer portal</span>
        <h1>Your Project</h1>
        <p>Check your project&rsquo;s status, share photos and documents with our team, and watch your project videos.</p>
      </div>
    </div>
    <section class="portal">
      <div class="wrap">
{ACCOUNT_BAR}
        <p id="portal-msg" class="notice" role="alert" hidden></p>
{SETUP_VIEW}

        <div class="view panel" id="v-auth" hidden>
          <div class="tabs" role="tablist">
            <button type="button" role="tab" data-tab="signin" aria-selected="true">Sign in</button>
            <button type="button" role="tab" data-tab="signup" aria-selected="false">Create account</button>
            <button type="button" role="tab" data-tab="reset" aria-selected="false">Forgot password</button>
          </div>
          <p id="auth-msg" class="notice" role="alert" hidden></p>

          <form id="f-signin" class="form auth-form">
            <h2>Sign in</h2>
            <div class="field"><label for="si-email">Email</label><input id="si-email" name="email" type="email" autocomplete="username" required></div>
            <div class="field"><label for="si-pass">Password</label><input id="si-pass" name="password" type="password" autocomplete="current-password" required></div>
            <label class="check"><input type="checkbox" name="remember" checked> Keep me signed in on this device</label>
            <button class="btn" type="submit">Sign In</button>
          </form>

          <form id="f-signup" class="form auth-form" hidden>
            <h2>Create your account</h2>
            <p class="fine">Use the email address you gave our office. Your project appears automatically once your email is verified and linked to your project.</p>
            <div class="field"><label for="su-name">Full name</label><input id="su-name" name="name" autocomplete="name" required maxlength="100"></div>
            <div class="field"><label for="su-company">Company, HOA or property name <span class="muted">(optional)</span></label><input id="su-company" name="company" autocomplete="organization" maxlength="120"></div>
            <div class="field-row">
              <div class="field"><label for="su-email">Email</label><input id="su-email" name="email" type="email" autocomplete="email" required maxlength="200"></div>
              <div class="field"><label for="su-phone">Phone</label><input id="su-phone" name="phone" type="tel" autocomplete="tel" required maxlength="40"></div>
            </div>
            <div class="field"><label for="su-address">Project property address</label><input id="su-address" name="address" autocomplete="street-address" required maxlength="200"></div>
            <div class="field-row">
              <div class="field"><label for="su-pass">Password</label><input id="su-pass" name="password" type="password" autocomplete="new-password" required minlength="10"><small>At least 10 characters, with letters and numbers.</small></div>
              <div class="field"><label for="su-pass2">Confirm password</label><input id="su-pass2" name="password2" type="password" autocomplete="new-password" required minlength="10"></div>
            </div>
            <label class="check"><input type="checkbox" name="terms" required> I agree to the <a href="/portal-terms" target="_blank">portal terms</a> and <a href="/privacy-policy" target="_blank">privacy policy</a>.</label>
            <button class="btn" type="submit">Create Account</button>
          </form>

          <form id="f-reset" class="form auth-form" hidden>
            <h2>Reset your password</h2>
            <div class="field"><label for="rs-email">Email</label><input id="rs-email" name="email" type="email" autocomplete="email" required></div>
            <button class="btn" type="submit">Send Reset Link</button>
          </form>
        </div>

        <div class="view panel" id="v-verify" hidden>
          <h2>Confirm your email</h2>
          <p>We sent a verification link to <strong id="verify-email"></strong>. Open it to finish setting up your account, then come back here. Check your spam folder if you don&rsquo;t see it.</p>
          <p id="verify-msg" class="notice" role="status" hidden></p>
          <div class="btn-row">
            <button type="button" class="btn" id="btn-verified">I&rsquo;ve Confirmed My Email</button>
            <button type="button" class="btn btn-outline" id="btn-resend">Send the Link Again</button>
          </div>
        </div>

        <div class="view panel" id="v-pending" hidden>
          <h2>We&rsquo;re connecting your project</h2>
          <p>Your account is ready, but no project is linked to <strong id="pending-email"></strong> yet. Our office has been notified and will link your project within one business day. We&rsquo;ll email you when it&rsquo;s ready.</p>
          <p>Need it sooner? Call <a href="tel:{TEL}">{PHONE}</a>, Monday&ndash;Friday 9 AM&ndash;4 PM ET.</p>
        </div>

        <div class="view" id="v-jobs" hidden>
          <h2>Your projects</h2>
          <div class="job-list" id="jobs-list"></div>
        </div>

        <div class="view" id="v-job" hidden>
          <a href="#" id="job-back" class="back">All projects</a>
          <h2 id="job-title"></h2>
          <p class="muted" id="job-address"></p>
          <div id="job-tracker"></div>
          <p class="status-note" id="job-note" hidden></p>
          <p class="fine" id="job-updated"></p>

          <div class="portal-grid">
            <div class="panel">
              <h3>Project updates</h3>
              <ul class="timeline" id="job-updates"></ul>
            </div>
            <div class="panel">
              <h3>Photos &amp; documents</h3>
              <ul class="files" id="job-files"></ul>
              <form id="f-upload" class="form upload">
                <label for="up-files">Add photos or documents</label>
                <input id="up-files" type="file" multiple>
                <small>Photos, PDF, Word or Excel &middot; up to 25 MB each</small>
                <button class="btn" type="submit">Upload</button>
                <p id="up-msg" class="notice" role="status" hidden></p>
              </form>
            </div>
          </div>

          <div class="panel">
            <h3>Project videos</h3>
            <div class="videos" id="job-videos"></div>
          </div>
        </div>
      </div>
    </section>"""

STAFF = f"""    <div class="page-head on-blue">
      <div class="wrap">
        <span class="eyebrow">Staff only</span>
        <h1>Portal Admin</h1>
      </div>
    </div>
    <section class="portal">
      <div class="wrap">
{ACCOUNT_BAR}
{SETUP_VIEW}
        <div class="view panel" id="v-signin" hidden>
          <form id="f-signin" class="form">
            <h2>Staff sign in</h2>
            <p class="fine">Use your @rocklaneco.com portal account. Staff sessions end after 30 minutes without activity or when the browser closes.</p>
            <div class="field"><label for="st-email">Email</label><input id="st-email" name="email" type="email" autocomplete="username" required></div>
            <div class="field"><label for="st-pass">Password</label><input id="st-pass" name="password" type="password" autocomplete="current-password" required></div>
            <button class="btn" type="submit">Sign In</button>
            <p id="signin-msg" class="notice" role="alert" hidden></p>
          </form>
        </div>
        <div class="view panel" id="v-denied" hidden>
          <h2>Staff access only</h2>
          <p>This account isn&rsquo;t on the staff list, or its email isn&rsquo;t verified yet. Customers can use the <a href="/portal">customer portal</a>.</p>
        </div>

        <nav class="staff-tabs" aria-label="Admin sections" hidden>
          <a href="#">Jobs</a><a href="#accounts">Customer accounts<span id="pending-count"></span></a><a href="#activity">Activity log</a><a href="#new">+ New job</a>
        </nav>

        <div class="view" id="v-jobs" hidden>
          <div class="toolbar">
            <input id="job-search" type="search" placeholder="Search jobs, addresses, emails" aria-label="Search jobs">
            <select id="job-filter" aria-label="Filter by status"></select>
          </div>
          <div class="table-wrap"><table class="data">
            <thead><tr><th>Job</th><th>Status</th><th>Paid</th><th>Customer emails</th><th>Updated</th></tr></thead>
            <tbody id="jobs-body"></tbody>
          </table></div>
        </div>

        <div class="view" id="v-job" hidden>
          <a href="#" class="back">All jobs</a>
          <h2 id="job-heading"></h2>
          <p id="job-msg" class="notice" role="status" hidden></p>
          <div class="portal-grid">
            <form id="f-job" class="form panel">
              <h3>Job details</h3>
              <div class="field"><label for="j-title">Job name</label><input id="j-title" name="title" required maxlength="140" placeholder="e.g. Smith roof replacement"></div>
              <div class="field"><label for="j-address">Property address</label><input id="j-address" name="address" maxlength="200"></div>
              <div class="field"><label for="j-status">Status</label><select id="j-status" name="status"></select></div>
              <div class="field"><label for="j-note">Status note for the customer <span class="muted">(optional)</span></label><textarea id="j-note" name="statusNote" rows="2" maxlength="500"></textarea></div>
              <div class="field"><label for="j-emails">Customer emails <span class="muted">(one per line; these people get access)</span></label><textarea id="j-emails" name="emails" rows="3"></textarea></div>
              <label class="check"><input type="checkbox" name="paid"> Paid in full (shows project videos to the customer)</label>
              <label class="check"><input type="checkbox" name="notifyLinked" checked> Email customers about new access or a status change</label>
              <button class="btn" type="submit">Save Job</button>
            </form>
            <div class="job-only">
              <form id="f-update" class="form panel">
                <h3>Post an update</h3>
                <div class="field"><label for="u-text">Update for the customer</label><textarea id="u-text" name="text" rows="3" maxlength="4000" required></textarea></div>
                <label class="check"><input type="checkbox" name="notify" checked> Email the customer</label>
                <button class="btn" type="submit">Post Update</button>
              </form>
              <div class="panel"><h3>Updates</h3><ul class="timeline" id="s-updates"></ul></div>
            </div>
          </div>
          <div class="portal-grid job-only">
            <div class="panel">
              <h3>Photos &amp; documents</h3>
              <ul class="files" id="s-files"></ul>
              <form id="f-s-upload" class="form upload">
                <label for="s-up-files">Upload for the customer</label>
                <input id="s-up-files" type="file" multiple>
                <button class="btn" type="submit">Upload</button>
              </form>
            </div>
            <div class="panel">
              <h3>Project videos</h3>
              <p class="fine">Upload to YouTube as <strong>Unlisted</strong>, then paste the link. Customers see videos only after the job is marked paid.</p>
              <ul class="files" id="s-media"></ul>
              <form id="f-media" class="form">
                <div class="field"><label for="m-title">Title</label><input id="m-title" name="title" maxlength="140" placeholder="e.g. Final roof walkthrough"></div>
                <div class="field"><label for="m-url">YouTube link</label><input id="m-url" name="url" required></div>
                <label class="check"><input type="checkbox" name="notify" checked> Email the customer (if paid)</label>
                <button class="btn" type="submit">Add Video</button>
              </form>
            </div>
          </div>
        </div>

        <div class="view" id="v-accounts" hidden>
          <h2>Customer accounts</h2>
          <p class="fine">Highlighted accounts aren&rsquo;t linked to a job yet. Choose their job to approve them; they&rsquo;re emailed automatically.</p>
          <p id="accounts-msg" class="notice" role="status" hidden></p>
          <div class="table-wrap"><table class="data">
            <thead><tr><th>Name</th><th>Contact</th><th>Property</th><th>Created</th><th>Job access</th></tr></thead>
            <tbody id="accounts-body"></tbody>
          </table></div>
        </div>

        <div class="view" id="v-activity" hidden>
          <h2>Activity log</h2>
          <p class="fine">Most recent 200 events. Times are Eastern.</p>
          <div class="table-wrap"><table class="data">
            <thead><tr><th>When</th><th>Who</th><th>What</th><th>Job</th></tr></thead>
            <tbody id="activity-body"></tbody>
          </table></div>
        </div>
      </div>
    </section>"""


PAGES = [
    ("index.html", "/", f"Rocklane Co. | Roofing, Siding & Gutters in Indianapolis Since 1980",
     "Owner-operated GAF Master Elite roofing contractor serving central Indiana since 1980. Roofing, siding and gutters with a 10-year workmanship warranty.", HOME, None),
    ("roofing.html", "/roofing", "Roof Replacement & Repair in Indianapolis | Rocklane Co.",
     "Roof replacement, repair and inspections from a GAF Master Elite contractor, backed by a 10-year workmanship warranty. Call (317) 898-8696.", ROOFING, "/roofing"),
    ("siding.html", "/siding", "Siding Installation & Repair in Indianapolis | Rocklane Co.",
     "James Hardie fiber cement and Variform vinyl siding installation and repair across central Indiana, with a 5-year workmanship warranty.", SIDING, "/siding"),
    ("gutters.html", "/gutters", "Seamless Gutters & Gutter Guards in Indianapolis | Rocklane Co.",
     "Seamless gutter installation, gutter protection, repair and cleaning in central Indiana, with a 5-year workmanship warranty. Call (317) 898-8696.", GUTTERS, "/gutters"),
    ("property-managers.html", "/property-managers", "HOA & Property Manager Roofing Contractor in Indiana | Rocklane Co.",
     "Roofing, siding and gutter projects for HOA boards and property managers. 100+ communities completed across central Indiana. Owner-operated since 1980.", PM, "/property-managers"),
    ("about.html", "/about", "About Rocklane Co. | Owner-Operated Since 1980",
     "Rocklane Company General Contractors LLC: owner-operated since 1980, GAF Master Elite, HAAG Certified Inspectors and IBHS FORTIFIED Roofing Contractors.", ABOUT, "/about"),
    ("contact.html", "/contact", "Contact Rocklane Co. | (317) 898-8696 | Indianapolis",
     "Call (317) 898-8696 or email rocklane@rocklaneco.com for a roofing, siding or gutter estimate. 1690 S. Franklin Rd., Indianapolis. Mon-Fri 9-4 ET.", CONTACT, "/contact",
     dict(scripts='\n  <script type="module" src="/js/estimate.js"></script>')),
    ("privacy-policy.html", "/privacy-policy", "Privacy Policy | Rocklane Co.",
     "Privacy policy for the Rocklane Company General Contractors LLC website.", PRIVACY, None),
    ("portal-terms.html", "/portal-terms", "Customer Portal Terms of Use | Rocklane Co.",
     "Terms of use for the Rocklane Co. customer portal.", TERMS, None),
    ("portal/index.html", "/portal", "Customer Portal | Rocklane Co.",
     "Sign in to check your Rocklane Co. project status, share photos and documents, and view project videos.", PORTAL, None,
     dict(head=PORTAL_HEAD, scripts='\n  <script type="module" src="/portal/portal.js"></script>', index=False)),
    ("portal/staff.html", "/portal/staff", "Portal Admin | Rocklane Co.",
     "Rocklane Co. staff portal.", STAFF, None,
     dict(head=PORTAL_HEAD, scripts='\n  <script type="module" src="/portal/staff.js"></script>', index=False)),
    ("404.html", "/404", "Page Not Found | Rocklane Co.",
     "This page has moved. Visit Rocklane Co. for roofing, siding and gutters in central Indiana.", NOTFOUND, None),
]

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

os.makedirs(OUT, exist_ok=True)
names = {p[0].lower() for p in PAGES}
for old in REDIRECTS:
    assert old.lower() + ".html" not in names, "redirect collides with page: " + old

for fn, path, title, desc, body, cur, *opts in PAGES:
    os.makedirs(os.path.dirname(os.path.join(OUT, fn)), exist_ok=True)
    with open(os.path.join(OUT, fn), "w") as f:
        f.write(page(path, title, desc, body, cur, **(opts[0] if opts else {})))

for old, new in REDIRECTS.items():
    with open(os.path.join(OUT, old + ".html"), "w") as f:
        f.write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Moved</title>
<link rel="canonical" href="{DOMAIN}{new}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={new}">
</head><body><p>This page has moved to <a href="{new}">{DOMAIN}{new}</a>.</p></body></html>
""")

with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    urls = "".join(f"  <url><loc>{DOMAIN}{p}</loc></url>\n" for _, p, *_ in PAGES if p not in ("/404", "/portal", "/portal/staff"))
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")

with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nDisallow: /portal/\n\nSitemap: {DOMAIN}/sitemap.xml\n")

with open(os.path.join(OUT, "CNAME"), "w") as f:
    f.write("rocklaneco.com\n")

os.makedirs(os.path.join(OUT, "js"), exist_ok=True)
with open(os.path.join(OUT, "js", "site.js"), "w") as f:
    f.write("""// Menu toggle and footer year (kept out of the HTML so pages work with a strict CSP).
(function () {
  var t = document.querySelector('.menu-toggle'), n = document.getElementById('nav');
  if (t && n) t.addEventListener('click', function () {
    var o = n.classList.toggle('open'); t.setAttribute('aria-expanded', o);
  });
  var y = document.getElementById('yr');
  if (y) y.textContent = new Date().getFullYear();
})();
""")

with open(os.path.join(OUT, "js", "estimate.js"), "w") as f:
    f.write("""// Contact-page estimate form. Sends to the Rocklane Apps Script, which emails the office.
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

with open(os.path.join(OUT, "_config.yml"), "w") as f:
    f.write("# GitHub Pages: publish only the website, not the tooling kept in this repository.\n"
            "exclude: [tools, firebase, apps-script, README.md]\n")

print("built", len(PAGES), "pages and", len(REDIRECTS), "redirects into", os.path.normpath(OUT))
