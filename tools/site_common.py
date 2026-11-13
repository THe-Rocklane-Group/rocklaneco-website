"""Shared constants, helpers, page chrome and section blocks for the Rocklane Co. site.

Page modules in tools/pages/ do `from site_common import *`.
Page agents never edit this file: describe a needed shared change in your report.
Copy, claims, colors and type follow The Rocklane Group Brand Foundation v2.
See tools/DESIGN.md for the component guide.
"""
import json
import re

# ---------------------------------------------------------------- constants
DOMAIN = "https://rocklaneco.com"
LEGAL = "Rocklane Company General Contractors LLC"
SHORT = "Rocklane Co."
TAGLINE = "Built to Outlast the Warranty."
PHONE = "(317) 898-8696"
TEL = "+13178988696"
EMAIL = "rocklane@rocklaneco.com"
ADDRESS = "1690 S. Franklin Rd.<br>Indianapolis, IN 46239"
HOURS = "Mon&ndash;Fri 9 AM&ndash;4 PM ET"
HOURS_SAT = "Saturday by appointment"
GBP = "https://www.google.com/maps?cid=1030444210742474565"
CITIES = ["Indianapolis", "Carmel", "Fishers", "Westfield", "Zionsville", "Greenwood",
          "Bloomington", "Avon", "Brownsburg", "Noblesville", "Pittsboro", "Greenfield",
          "Lawrence", "West Lafayette", "Danville"]

NAV = [("/roofing", "Roofing"), ("/siding", "Siding"), ("/gutters", "Gutters"),
       ("/commercial", "Commercial"),
       ("/property-managers", "HOA &amp; Property Managers"), ("/about", "About"),
       ("/contact", "Contact")]

# Claims (binding wording; use these constants, never retype them).
GAF_CLAIM = "Only 2% of roofers in North America are invited to become GAF Master Elite Contractors"
GAF_DISCLOSURE = ("Contractors enrolled in GAF certification programs are not employees or agents of GAF, "
                  "and GAF does not control or otherwise supervise these independent businesses. Contractors "
                  "may receive benefits, such as loyalty rewards points and discounts on marketing tools from "
                  "GAF for participating in the program and offering GAF enhanced warranties, which require "
                  "the use of a minimum amount of GAF products. Your dealings with a Contractor, and any "
                  "services they provide to you, are subject to the Contractor Terms of Use. Visit "
                  "gaf.com/gaf-contractor-terms-of-use for details.")
GAF_FOOTNOTE2 = ("See System Plus Limited Warranty, Silver Pledge&trade; Limited Warranty, and Golden "
                 "Pledge&reg; Limited Warranty for complete coverage and restrictions. Visit gaf.com/LRS "
                 "for qualifying products.")
GAF_TRADEMARK = ("GAF, Golden Pledge, Master Elite, Silver Pledge and System Plus are either registered "
                 "trademarks or trademarks of BMIC LLC in the United States and/or other countries.")
GAF_ID = "GAF Contractor ID 1003357 &middot; Independent Contractor"
# Required by Atlas wherever its logo is used (atlasroofing.com/marketing-resources, Partner Brand Style Guide 2025).
ATLAS_DISCLAIMER = "Rocklane Co. is an Independent Roofing Contractor, not an Employee or Agent of Atlas Roofing Corporation."
# VELUX dealer digital guidelines (pro.veluxusa.com/digital-guidelines).
VELUX_TRADEMARK = "VELUX and the VELUX logo are registered trademarks of VKR Holding A/S."
OTHER_TRADEMARKS = ("Atlas, James Hardie, Royal, Variform and Versico are trademarks of their respective owners, "
                    "shown to identify products we install.")
QUOTE = "Manufacturers cover materials. We cover the work. If we installed it, we own it."

SCHEMA = {
    "@context": "https://schema.org",
    "@type": "RoofingContractor",
    "name": LEGAL,
    "alternateName": SHORT,
    "slogan": TAGLINE,
    "foundingDate": "1980",
    "url": DOMAIN + "/",
    "image": DOMAIN + "/images/photos/carmel-townhomes-aerial-1200.jpg",
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


# ---------------------------------------------------------------- icons
# Line icons (24px grid, stroke = currentColor). Decorative only: always aria-hidden.
ICONS = {
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "award": '<circle cx="12" cy="8" r="6.5"/><path d="M8.2 13.6 7 22l5-3 5 3-1.2-8.4"/>',
    "search": '<circle cx="11" cy="11" r="7.5"/><path d="m21 21-4.6-4.6"/>',
    "home": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9v12h14V9"/><path d="M10 21v-6h4v6"/>',
    "layers": '<path d="M12 2 2 7l10 5 10-5-10-5z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
    "droplet": '<path d="M12 2.7 17.7 8.4a8 8 0 1 1-11.3 0z"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "clipboard": '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/><path d="m9 14 2 2 4-4"/>',
    "tool": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9l-3.8 3.8z"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "check-circle": '<path d="M22 11.1V12a10 10 0 1 1-5.9-9.1"/><path d="M22 4 12 14l-3-3"/>',
    "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9"/><path d="M16 3.1a4 4 0 0 1 0 7.8"/>',
    "user": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "storm": '<path d="M19 16.9A5 5 0 0 0 18 7h-1.3A8 8 0 1 0 5.1 16"/><path d="m13 11-4 6h6l-4 6"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    "alert": '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    "monitor": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8"/><path d="M12 17v4"/>',
    "menu": '<path d="M3 6h18"/><path d="M3 12h18"/><path d="M3 18h18"/>',
    "close": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "building": '<rect x="4" y="2" width="16" height="20" rx="1"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
    "camera": '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
    "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "handshake": '<path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.9-3.9a2 2 0 0 0-2.8 0l-.9.9a1 1 0 1 1-3-3l2.8-2.8a5.8 5.8 0 0 1 7.1-.9l.5.3a2 2 0 0 0 1.4.2L21 4"/><path d="m21 3 1 11h-2"/><path d="M3 3 2 14l6.5 6.5a1 1 0 1 0 3-3"/><path d="M3 4h8"/>',
}


def ic(name, cls="i"):
    """Decorative inline SVG icon (aria-hidden)."""
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'


# ---------------------------------------------------------------- photos
# Licensed stock (see images/photos/CREDITS.md). Never caption as Rocklane projects.
PHOTOS = {
    "carmel-townhomes-aerial": (2400, 1800), "noblesville-neighborhood-aerial": (2400, 1800),
    "indy-apartments-courtyard": (2400, 1600), "indy-brick-townhomes": (2400, 1600),
    "indiana-farmhouse-fall": (2400, 1600), "tipton-roof-topdown": (2400, 1348),
    "indianapolis-skyline-dusk": (2400, 1349), "broad-ripple-brick-texture": (2400, 1600),
    "broad-ripple-siding-texture": (2400, 1600), "west-lafayette-apartments": (2316, 1350),
    "two-story-home-hero": (2400, 1854), "siding-rooflines": (2400, 1600),
    "commercial-corridor-aerial": (2400, 1800), "condo-community-aerial": (2400, 1800),
    "apartment-community-aerial": (2400, 1350), "farmhouse-new-roof": (1752, 1590),
    "k-style-gutters": (1600, 2413), "shingle-texture": (2400, 1600),
    "warehouse-dock-doors": (2400, 1600),
}


def picture(name, alt, sizes="100vw", w=None, h=None, cls="", eager=False, pos=None):
    """Responsive <img> for images/photos/<name>.jpg (+ <name>-1200.jpg).

    alt="" marks a decorative background. w/h default to the file's real size.
    eager=True for the above-the-fold image (fetchpriority=high); otherwise lazy.
    pos sets object-position, e.g. "center 20%".
    """
    dw, dh = PHOTOS[name]
    w, h = w or dw, h or dh
    base = f"/images/photos/{name}"
    attrs = [f'src="{base}-1200.jpg"',
             f'srcset="{base}-1200.jpg 1200w, {base}.jpg {dw}w"',
             f'sizes="{sizes}"', f'width="{w}"', f'height="{h}"', f'alt="{alt}"']
    if cls:
        attrs.insert(0, f'class="{cls}"')
    attrs.append('fetchpriority="high"' if eager else 'loading="lazy" decoding="async"')
    if pos:
        attrs.append(f'style="object-position:{pos}"')
    return "<img " + " ".join(attrs) + ">"


def fn(n):
    """Superscript footnote marker linking to the footer footnote (1 = GAF disclosure, 2 = warranty terms)."""
    return f'<sup class="fn-ref"><a href="#fn-{n}" aria-label="Footnote {n}">{n}</a></sup>'


def gaf_badge():
    """GAF's own Master Elite Residential Roofing Contractor badge (from gaf.com, Rocklane's directory listing).
    GAF rule: keep it smaller than the Rocklane logo (logo at least 2x the badge) and never alter it."""
    return ('<img class="gaf-badge" src="/images/brands/gaf-master-elite.png" width="400" height="400" '
            'alt="GAF Master Elite&reg; Residential Roofing Contractor" loading="lazy">')


def gaf_presidents_club():
    """GAF's President's Club award badge (from gaf.com, Rocklane's directory listing). No year is claimed:
    GAF's listing shows the award without one. Same size rule as the Master Elite badge."""
    return ('<img class="gaf-badge" src="/images/brands/gaf-presidents-club.png" width="400" height="400" '
            'alt="GAF President&rsquo;s Club Award" loading="lazy">')


def gaf_awards():
    """Master Elite badge and President's Club badge side by side."""
    return f'<div class="gaf-awards">{gaf_badge()}{gaf_presidents_club()}</div>'


GAF_CLAIM_HTML = GAF_CLAIM + fn(1)
# Paraphrases GAF's own description on Rocklane's gaf.com listing; GAF marks that description with the same
# independent-contractor footnote, so it carries footnote 1.
PRESIDENTS_CLUB_HTML = ("GAF President&rsquo;s Club Award: GAF gives President&rsquo;s Club status to a select few "
                        "Master Elite&reg; contractors for excellence in performance, reliability and service" + fn(1))


# ---------------------------------------------------------------- section helpers
def sec_hd(num, eyebrow, title, lead="", hid=None, center=False):
    """Numbered section header: big outlined number, eyebrow, H2 and optional lead."""
    n = f'<span class="sec-num" aria-hidden="true">{num}</span>' if num else ""
    hid_attr = f' id="{hid}"' if hid else ""
    lp = f"\n          <p>{lead}</p>" if lead else ""
    c = " center" if center else ""
    return f"""        <div class="sec-hd{c} reveal">
          <div>{n}<span class="eyebrow">{eyebrow}</span><h2{hid_attr}>{title}</h2></div>{lp}
        </div>"""


_CARD_IDS = {}


def _card_id(href, title):
    """Stable, unique id stem for a photo card heading (unique across the build)."""
    stem = "pc-" + (re.sub(r"[^a-z0-9]+", "-", (href + " " + re.sub(r"&\w+;", "", title)).lower()).strip("-") or "card")
    n = _CARD_IDS.get(stem, 0) + 1
    _CARD_IDS[stem] = n
    return stem if n == 1 else f"{stem}-{n}"


def photo_card(href, photo, alt, title, text, go, sizes, cls="", pos=None, kicker=None):
    """Full-bleed photo link card with a Shark Blue text panel (AA over any photo).

    The photo is decorative inside the link (alt=""; the `alt` argument is kept for call
    compatibility and ignored). The link is named by its <h3> and described by its text.
    """
    k = f'<span class="pc-k">{kicker}</span>' if kicker else ""
    c = f" {cls}" if cls else ""
    g = f'<span class="pc-go">{go} {ic("arrow")}</span>' if go else ""
    i = _card_id(href, title)
    return f"""<a class="photo-card{c} reveal" href="{href}" aria-labelledby="{i}" aria-describedby="{i}-d">
            {picture(photo, "", sizes, pos=pos)}
            <div class="pc-body">{k}<h3 id="{i}">{title}</h3><p id="{i}-d">{text}</p>{g}</div>
          </a>"""


def page_head(eyebrow, title, lead, crumb=None, photo=None, alt="", pos=None):
    """Interior page hero (the page's single <h1>). With photo=..., a photo sits under a Shark Blue overlay."""
    crumbs = (f'\n        <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>{crumb}</span></nav>'
              if crumb else "")
    eb = f'\n        <span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    lp = f"\n        <p>{lead}</p>" if lead else ""
    if photo:
        img = "\n      " + picture(photo, alt, "100vw", cls="ph-bg", eager=True, pos=pos)
        cls = "page-head on-blue has-photo"
    else:
        img, cls = "", "page-head on-blue"
    return f"""    <div class="{cls}">{img}
      <div class="wrap">{crumbs}{eb}
        <h1>{title}</h1>{lp}
      </div>
    </div>"""


# ---------------------------------------------------------------- shared blocks
CTA = f"""    <section class="final" aria-labelledby="cta-h">
      {picture("broad-ripple-brick-texture", "", "100vw", cls="final-bg")}
      <div class="wrap">
        <div class="final-card on-blue reveal">
          <div><span class="eyebrow">Free estimates</span><h2 id="cta-h">Talk to an owner about your project.</h2></div>
          <div>
            <p>Call the office and you&rsquo;ll reach the people who run the work. An estimate is the first status in your project.</p>
            <div class="btn-row">
              <a class="btn" href="/contact">Request an Estimate {ic("arrow")}</a>
              <a class="btn btn-outline" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
            </div>
          </div>
        </div>
      </div>
    </section>"""


def warranty_band(num="", photo="two-story-home-hero", alt="Two-story suburban home with charcoal architectural shingles, gray vinyl lap siding, stone base and white gutters in fall",
                  small="tipton-roof-topdown", small_alt="Top-down drone view of a ranch home showing each roof plane"):
    """Warranty split: offset photo pair + pull quote + 10/5-year figures."""
    return f"""    <section aria-labelledby="war-h">
      <div class="wrap warranty-split">
        <div class="offset-media reveal">
          {picture(photo, alt, "(max-width:900px) 100vw, 56vw", cls="om-big")}
          {picture(small, small_alt, "(max-width:900px) 46vw, 26vw", cls="om-sm")}
        </div>
        <div class="reveal">
          {f'<span class="sec-num" aria-hidden="true">{num}</span>' if num else ''}<span class="eyebrow">Workmanship warranty</span>
          <h2 id="war-h">Our name is on the work.</h2>
          <blockquote class="pullquote"><p>&ldquo;{QUOTE}&rdquo;</p></blockquote>
          <div class="yrs">
            <div><b>10<small>years</small></b><span>on roof replacements</span></div>
            <div><b>5<small>years</small></b><span>on repairs, gutters, chimneys and siding</span></div>
          </div>
          <a class="text-link" href="/about">How we stand behind it {ic("arrow")}</a>
        </div>
      </div>
    </section>"""


WARRANTY_BAND = warranty_band()

STATUSES = [("Estimate", "We inspect and put the scope in writing."),
            ("Approved", "You sign off on the scope and materials."),
            ("Scheduled", "Your install date is set in the portal."),
            ("In progress", "Rocklane crews on site, with updates and photos."),
            ("Final walkthrough", "We review the finished work together."),
            ("Complete", "Documents and warranty details stay in your portal.")]


def status_card(current=3):
    """Illustration of the customer-portal tracker (decorative; role=img)."""
    rows = []
    for i, (s, _) in enumerate(STATUSES):
        if i < current:
            rows.append(f'<li class="done"><span class="dot">{ic("check")}</span>{s}</li>')
        elif i == current:
            rows.append(f'<li class="now"><span class="dot"></span>{s}</li>')
        else:
            rows.append(f'<li><span class="dot"></span>{s}</li>')
    return f"""<div class="status-card" role="img" aria-label="Illustration of the customer portal: a project at the {STATUSES[current][0]} status">
            <div class="sc-top"><b>Your project</b><span class="pill">{STATUSES[current][0]}</span></div>
            <ul class="sc-track">{"".join(rows)}</ul>
            <div class="sc-feat"><span>{ic("clock")}Status</span><span>{ic("chat")}Updates</span><span>{ic("camera")}Photos</span><span>{ic("file")}Documents</span></div>
          </div>"""


def process(num=""):
    """Six portal statuses on a Shark Blue photo band, with the portal status card beside them."""
    steps = "".join(f'<li class="reveal"><h3>{s}</h3><p>{d}</p></li>' for s, d in STATUSES)
    return f"""    <section class="process on-blue" aria-labelledby="proc-h">
      {picture("shingle-texture", "", "100vw", cls="process-bg")}
      <div class="wrap">
{sec_hd(num, "How it works", "Six steps. Always visible.", "Every project moves through the same six statuses, and you can follow each one in the online customer portal.", "proc-h")}
        <div class="proc-grid">
          <ol class="process-steps">{steps}</ol>
          <div class="reveal">{status_card()}</div>
        </div>
        <div class="proc-ft reveal">
          <p>Status, updates, photos and documents, in one place, for every project.</p>
          <a class="btn btn-outline" href="/portal/">{ic("user")}Customer Login</a>
        </div>
      </div>
    </section>"""


PROCESS = process()

PARTNERS = f"""    <section class="partners" aria-labelledby="pt-h">
      <div class="wrap">
        <div><h2 id="pt-h" class="sr">Products we install</h2><p>We install Atlas&reg; shingles, VELUX&reg; skylights, James Hardie&reg; fiber cement siding, and Variform and Royal&reg; vinyl siding, and roof as a GAF Master Elite&reg; contractor.</p></div>
        <div class="logos">
          <div class="logo-box"><img src="/images/brands/atlas-logo.jpg" width="600" height="412" alt="Atlas Roofing" loading="lazy"></div>
          <div class="logo-box"><img src="/images/brands/velux-logo.svg" width="124" height="42" alt="VELUX" loading="lazy"></div>
          <div class="logo-box"><img src="/images/brands/james-hardie-logo.svg" width="193" height="40" alt="James Hardie" loading="lazy"></div>
          <div class="logo-box"><img src="/images/brands/variform-logo.svg" width="196" height="52" alt="Variform" loading="lazy"></div>
          <div class="logo-box"><img src="/images/brands/royal-siding-logo.svg" width="308" height="208" alt="Royal siding" loading="lazy"></div>
          <div class="logo-box"><img src="/images/brands/gaf-logo.svg" width="100" height="100" alt="GAF" loading="lazy"></div>
        </div>
      </div>
    </section>"""

COMMERCIAL_SPLIT = f"""        <div class="com-cards">
          <article class="com-card reveal">
            {picture("warehouse-dock-doors", "White tilt-up warehouse wall with loading dock doors", "(max-width:900px) 100vw, 50vw", pos="center 60%")}
            <div class="b">
              <span class="who">{SHORT}</span>
              <h3>Warehouse &amp; commercial exteriors</h3>
              <ul class="ticks">
                <li>{ic("check")}Commercial gutters and downspouts</li>
                <li>{ic("check")}Siding</li>
                <li>{ic("check")}Metal wall panels</li>
              </ul>
              <a class="text-link" href="/commercial">Commercial exteriors {ic("arrow")}</a>
            </div>
          </article>
          <article class="com-card reveal" style="--d:.08s">
            {picture("commercial-corridor-aerial", "Aerial view of flat-roof office buildings and a mid-rise condominium building", "(max-width:900px) 100vw, 50vw")}
            <div class="b">
              <span class="who">Rocklane Commercial Contractors LLC</span>
              <h3>Low-slope membrane roofing</h3>
              <ul class="ticks">
                <li>{ic("check")}EPDM, TPO and PVC membrane systems</li>
                <li>{ic("check")}A GAF Certified Commercial Contractor</li>
              </ul>
              <div class="versico">
                <img src="/images/brands/versico-logo.png" width="2382" height="1077" alt="Versico Roofing Systems" loading="lazy">
                <p>Rocklane Commercial Contractors LLC is a GAF Certified Commercial Contractor and Versico Authorized.</p>
              </div>
              <a class="text-link" href="/commercial#membrane">Commercial roofing {ic("arrow")}</a>
            </div>
          </article>
        </div>"""

CITY_ITEMS = "".join(f"<li>{c}</li>" for c in CITIES)


def service_area(num=""):
    return f"""    <section class="area on-blue" aria-labelledby="area-h">
      {picture("noblesville-neighborhood-aerial", "Sunset aerial view of a Noblesville, Indiana subdivision of two-story homes around a pond in fall color", "100vw", cls="area-bg", pos="center 20%")}
      <div class="wrap">
        <div class="area-in reveal">
          {f'<span class="sec-num" aria-hidden="true">{num}</span>' if num else ''}<span class="eyebrow">Service area</span>
          <h2 id="area-h">Rooted in central Indiana.</h2>
          <p>Based in Indianapolis and working across the region.</p>
          <ul class="cities">{CITY_ITEMS}</ul>
          <a class="btn" href="/contact">Contact our office {ic("arrow")}</a>
        </div>
      </div>
      <span class="photo-cap">{ic("pin")}Pictured: Noblesville, Indiana</span>
    </section>"""


SERVICE_AREA = service_area()


# ---------------------------------------------------------------- document chrome
def page(path, title, desc, body, current, head="", scripts="", index=True, css=""):
    cur = ' aria-current="page"'
    nav = "\n".join('          <li><a href="%s"%s>%s</a></li>' % (h, cur if h == current else "", t)
                    for h, t in NAV)
    canonical = DOMAIN + path
    # Indexable pages carry rel=canonical; noindex pages (portal, 404) carry robots noindex instead.
    meta_idx = (f'\n  <link rel="canonical" href="{canonical}">' if index
                else '\n  <meta name="robots" content="noindex, nofollow">')
    schema = json.dumps(SCHEMA, indent=2)
    style = f"\n  <style>\n{css.strip()}\n  </style>" if css.strip() else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">{meta_idx}{head}
  <meta name="theme-color" content="#1E5AA8">
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
  <link rel="apple-touch-icon" href="/images/icon-180.png">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SHORT}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{DOMAIN}/images/photos/carmel-townhomes-aerial-1200.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap">
  <link rel="stylesheet" href="/css/style.css">{style}
  <script type="application/ld+json">
{schema}
  </script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <div class="util on-blue">
    <div class="wrap">
      <div class="util-l">
        <a href="tel:{TEL}">{ic("phone")}{PHONE}</a>
        <span class="util-hrs">{ic("clock")}{HOURS} &middot; {HOURS_SAT}</span>
      </div>
      <div class="util-r">
        <span class="util-gaf">{ic("award")}GAF Master Elite&reg; roofing contractor</span>
        <a href="/portal/">{ic("user")}<span>Customer Login</span></a>
      </div>
    </div>
  </div>
  <header class="site-header">
    <div class="wrap">
      <!-- Approved Rocklane Co. primary lockup. Do not stretch, crop, recolor or add effects. -->
      <a class="brand" href="/"><img src="/images/rocklane-co-logo.jpg" width="560" height="135" alt="Rocklane Co. General Contractors LLC, home"></a>
      <nav class="nav" id="nav" aria-label="Main">
        <ul>
{nav}
        </ul>
      </nav>
      <div class="hdr-cta">
        <a class="hdr-ph" href="tel:{TEL}" aria-label="Call {PHONE}">{ic("phone")}<span>{PHONE}</span></a>
        <a class="btn btn-sm" href="/contact">Request an Estimate</a>
        <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav">{ic("menu")}<span>Menu</span></button>
      </div>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer on-blue">
    <div class="wrap ftr-g">
      <div>
        <a class="foot-logo" href="/"><img src="/images/rocklane-co-logo.jpg" width="560" height="135" alt="Rocklane Co. General Contractors LLC, home" loading="lazy"></a>
        <p class="tagline">{TAGLINE}</p>
        <p>{LEGAL}. Owner-operated in central Indiana since 1980. Part of the Rocklane Group.</p>
      </div>
      <nav aria-labelledby="ft-s"><h2 id="ft-s">Services</h2><ul>
        <li><a href="/roofing">Roofing</a></li><li><a href="/siding">Siding</a></li><li><a href="/gutters">Gutters</a></li><li><a href="/commercial">Commercial</a></li>
      </ul></nav>
      <nav aria-labelledby="ft-c"><h2 id="ft-c">Company</h2><ul>
        <li><a href="/property-managers">HOA &amp; Property Managers</a></li><li><a href="/about">About</a></li><li><a href="/contact">Contact</a></li><li><a href="/contact">Request an Estimate</a></li><li><a href="/portal/">Customer Login</a></li>
      </ul></nav>
      <div><h2>Visit or call</h2>
        <ul class="foot-contact">
          <li>{ic("phone")}<a href="tel:{TEL}">{PHONE}</a></li>
          <li>{ic("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{ic("pin")}<span>{ADDRESS}</span></li>
          <li>{ic("clock")}<span>{HOURS}<br>{HOURS_SAT}</span></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <div class="wrap">
        <div class="legal-row"><span>&copy; <span id="yr">2026</span> {LEGAL}, a Rocklane Group company</span><span>{GAF_ID}</span><nav aria-label="Legal"><a href="/privacy-policy">Privacy</a><a href="/portal-terms">Portal Terms</a><a href="/portal/">Customer Login</a></nav></div>
        <ol class="footnotes">
          <li id="fn-1">{GAF_DISCLOSURE}</li>
          <li id="fn-2">{GAF_FOOTNOTE2}</li>
        </ol>
        <p>{GAF_TRADEMARK} {VELUX_TRADEMARK} {OTHER_TRADEMARKS}</p>
        <p>{ATLAS_DISCLAIMER}</p>
      </div>
    </div>
  </footer>

  <nav class="call-bar" aria-label="Quick actions">
    <a href="tel:{TEL}">{ic("phone")}Call Now</a>
    <a href="/contact">Request an Estimate</a>
  </nav>

  <script src="/js/site.js" defer></script>{scripts}
</body>
</html>
"""


__all__ = [n for n in dir() if not n.startswith("_") and n not in ("json", "re")]
