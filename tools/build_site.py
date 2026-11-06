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


def page(path, title, desc, body, current):
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
  <link rel="canonical" href="{canonical}">
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
      <span><a href="tel:{TEL}">{PHONE}</a><span class="hide-sm"> &nbsp;|&nbsp; Mon&ndash;Fri 9 AM&ndash;4 PM ET</span></span>
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
      <p class="legal">&copy; <span id="yr">2026</span> {LEGAL}, a Rocklane Group company. GAF, Master Elite and Golden Pledge are registered trademarks of GAF. &middot; <a href="/privacy-policy">Privacy</a></p>
    </div>
  </footer>

  <div class="call-bar">
    <a href="tel:{TEL}">Call Now</a>
    <a href="/contact">Request an Estimate</a>
  </div>

  <script>
    var t = document.querySelector('.menu-toggle'), n = document.getElementById('nav');
    t.addEventListener('click', function () {{
      var o = n.classList.toggle('open'); t.setAttribute('aria-expanded', o);
    }});
    document.getElementById('yr').textContent = new Date().getFullYear();
  </script>
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
        <p>Call the office or email us to request an estimate or an inspection.</p>
      </div>
    </div>

    <section>
      <div class="wrap contact-grid">
        <div>
          <h2>Talk to our team</h2>
          <p>The fastest way to reach us is by phone. You can also email your name, the property address and a short description of the project, and we&rsquo;ll get back to you.</p>
          <ul class="info-list">
            <li><small>Office</small><a href="tel:{TEL}">{PHONE}</a></li>
            <li><small>Email</small><a href="mailto:{EMAIL}?subject=Estimate%20request">{EMAIL}</a></li>
            <li><small>Address</small>{ADDRESS.replace('<br>', ', ')}</li>
          </ul>
          <div class="btn-row" style="margin-top:22px">
            <a class="btn" href="tel:{TEL}">Call Now</a>
            <a class="btn btn-outline" href="mailto:{EMAIL}?subject=Estimate%20request&amp;body=Name%3A%0AProperty%20address%3A%0APhone%3A%0AProject%20(roof%2C%20siding%2C%20gutters%2C%20other)%3A%0ADetails%3A">Email an Estimate Request</a>
          </div>
        </div>
        <div>
          <h2>Hours</h2>
          <table class="hours">
            <tr><td>Monday &ndash; Friday</td><td>9 AM &ndash; 4 PM ET</td></tr>
            <tr><td>Saturday</td><td>By appointment</td></tr>
            <tr><td>Sunday</td><td>Closed</td></tr>
          </table>
          <p style="margin-top:20px"><a href="{GBP}" rel="noopener">Directions on Google Maps</a></p>
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
        <p>{LEGAL}</p>
      </div>
    </div>
    <section>
      <div class="wrap" style="max-width:820px">
        <p>This website has no forms, accounts, advertising trackers or cookies of its own. When you call or email us, we use your information only to respond to you and to provide the estimates and services you request. We do not sell your personal information.</p>
        <p>Our pages load the Montserrat typeface from Google Fonts, and the map on our contact page is provided by Google. Google may collect technical information under its own privacy policy.</p>
        <p>Questions? Contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{TEL}">{PHONE}</a>.</p>
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
     "Call (317) 898-8696 or email rocklane@rocklaneco.com for a roofing, siding or gutter estimate. 1690 S. Franklin Rd., Indianapolis. Mon-Fri 9-4 ET.", CONTACT, "/contact"),
    ("privacy-policy.html", "/privacy-policy", "Privacy Policy | Rocklane Co.",
     "Privacy policy for the Rocklane Company General Contractors LLC website.", PRIVACY, None),
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

for fn, path, title, desc, body, cur in PAGES:
    with open(os.path.join(OUT, fn), "w") as f:
        f.write(page(path, title, desc, body, cur))

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
    urls = "".join(f"  <url><loc>{DOMAIN}{p}</loc></url>\n" for _, p, *_ in PAGES if p != "/404")
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")

with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

with open(os.path.join(OUT, "CNAME"), "w") as f:
    f.write("rocklaneco.com\n")

print("built", len(PAGES), "pages and", len(REDIRECTS), "redirects into", os.path.normpath(OUT))
