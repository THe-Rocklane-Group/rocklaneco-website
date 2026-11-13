# Rocklane Co. site: component guide for page authors

Build: `cd D:/Code/Rocklane/rocklaneco-website && python tools/build_site.py`, then `python tools/check_site.py`.
Reference design: home page (`tools/pages/home.py`), ported from mockup A "Editorial premium".

## Page-module contract

One file per page in `tools/pages/<slug>.py`, starting with `from site_common import *`. Define:

| Name | Meaning |
|---|---|
| `PATH` | URL path, e.g. `"/roofing"` (output file is `<path>.html`, `/` → `index.html`) |
| `CURRENT` | nav href to mark `aria-current`, or `None` |
| `TITLE`, `DESC` | `<title>` and meta description (plain text, no banned words) |
| `CSS` | page-only CSS string (inlined in `<head>`), may be `""` |
| `BODY` | HTML for `<main>`; must contain exactly one `<h1>` (usually via `page_head`) |
| optional `HEAD`, `SCRIPTS`, `INDEX` (False → noindex), `OUT` (file name), `SITEMAP` (False → leave out of sitemap) |

Never edit `css/style.css` or `tools/site_common.py`; describe needed shared changes in your report. Never change the bodies, IDs, classes, CSP or scripts of `pages/portal.py`, `pages/staff.py` or the estimate form in `pages/contact.py`.

## Helpers and shared blocks (site_common)

| Signature | Returns |
|---|---|
| `ic(name, cls="i")` | decorative SVG icon. Names: shield award search home layers droplet phone clipboard tool check check-circle users user pin clock mail arrow storm file alert monitor menu close building camera chat handshake |
| `picture(name, alt, sizes="100vw", w=None, h=None, cls="", eager=False, pos=None)` | responsive `<img>` for `images/photos/<name>.jpg` with the `-1200.jpg` variant in `srcset`; real width/height filled in from `PHOTOS`; lazy unless `eager=True` (use eager only for the page's first, above-the-fold image); `alt=""` for decorative backgrounds; `pos` sets `object-position` |
| `fn(n)` | superscript footnote marker linking to the footer (1 = GAF disclosure, 2 = GAF warranty terms) |
| `gaf_badge()` | GAF's own Master Elite® Residential Roofing Contractor badge (`/images/brands/gaf-master-elite.png`), 104px wide, unaltered |
| `GAF_CLAIM_HTML` | `GAF_CLAIM` + `fn(1)`; the only approved 2% wording |
| `sec_hd(num, eyebrow, title, lead="", hid=None, center=False)` | numbered section header (outlined number, eyebrow, `<h2 id=hid>`, lead) |
| `photo_card(href, photo, alt, title, text, go, sizes, cls="", pos=None, kicker=None)` | full-bleed photo link card; the photo renders with `alt=""` (decorative inside the link, `alt` is ignored) and the link is named by its `<h3>` (`aria-labelledby`) and described by its text |
| `page_head(eyebrow, title, lead, crumb=None, photo=None, alt="", pos=None)` | interior hero with the page `<h1>`; with `photo=`, the photo sits under a Shark Blue overlay (pass `alt=""`, it is decorative) |
| `warranty_band(num="", photo=..., alt=..., small=..., small_alt=...)` / `WARRANTY_BAND` | warranty split: offset photo pair, pull quote, 10/5-year figures |
| `process(num="")` / `PROCESS` | six portal statuses on a Shark Blue photo band + portal status card + Customer Login |
| `status_card(current=3)` | the "Your project — In progress" portal illustration on its own |
| `PARTNERS` | Products strip: Atlas, VELUX, James Hardie, Variform, Royal siding and GAF logos in equal tiles |
| `COMMERCIAL_SPLIT` | two `.com-card`s: Rocklane Co. exteriors / Rocklane Commercial membrane + Versico (place inside a `.wrap`; on home it follows a `.com-hero`) |
| `service_area(num="")` / `SERVICE_AREA` | Noblesville photo band with the 15 cities and a solid caption bar |
| `CTA` | final call-to-action (brick texture + Shark Blue card, Request an Estimate → /contact + phone) |
| Constants | `LEGAL SHORT TAGLINE PHONE TEL EMAIL ADDRESS HOURS HOURS_SAT CITIES NAV DOMAIN QUOTE STATUSES PHOTOS GAF_CLAIM GAF_DISCLOSURE GAF_FOOTNOTE2 GAF_TRADEMARK GAF_ID` |

The footer (every page) renders the GAF disclosure as footnote 1, `GAF_FOOTNOTE2` as footnote 2, `GAF_TRADEMARK` and "GAF Contractor ID 1003357 · Independent Contractor". Page bodies only add the markers.

## Section rhythm

- Alternate bands: white (`<section>`), Light Grey (`<section class="grey">`), Shark Blue (`.on-blue`, usually a photo band). Never two Light Grey bands in a row; a blue photo band every two or three sections.
- Each major section opens with `sec_hd()` (or `.sec-num` + `.eyebrow` + `h2` inline) numbered 01, 02, 03… in page order. One `<h1>` per page, `<h2>` per section, `<h3>` inside.
- One big photo per section (a photo band, an offset pair, or a card mosaic). Never upscale; use `sizes` that match the layout.
- Add `class="reveal"` (and optional `style="--d:.08s"` stagger) to blocks that should fade in. Content is visible without JS and in print.

## Components (css/style.css)

Base and type
- `.wrap` — centered container (max 1320px, 1480px at ≥1600px, fluid gutter). `<div class="wrap">…</div>`
- `.eyebrow` — uppercase label with a Lizard Green rule. `<span class="eyebrow">Service area</span>`
- `.sec-num` — big outlined section number (aria-hidden). `<span class="sec-num" aria-hidden="true">03</span>`
- `.sec-hd` (alias `.sec-head`), `.sec-hd.center` — 7/5 header grid. Use `sec_hd()`.
- `.lead`, `.muted`, `.fine`, `.center`, `.section-intro`, `.hl` (green underline highlight), `.sr` (visually hidden), `.rule` (1px divider)
- `.grey`, `.on-blue`, `.dark`, `.tight` — band backgrounds / compact padding. `<section class="grey">`

Buttons and links
- `.btn` — Lizard Green, dark text; hover adds an ink ring (never a lighter green). `<a class="btn" href="/contact">Request an Estimate</a>`
- `.btn-outline` — Shark Blue outline (white outline on `.on-blue`). `<a class="btn btn-outline" href="tel:…">…</a>`
- `.btn-blue` — solid Shark Blue. `.btn-sm` — compact. `.btn-row` — wrapping button group.
- `.text-link` (alias `.lnk`) — bold link with green underline and arrow. `<a class="text-link" href="/about">How we stand behind it {ic("arrow")}</a>`
- `.ico`, `.ico-blue`, `.ico-green` — round icon chips. `<span class="ico ico-blue">{ic("tool")}</span>`

Header, hero, footer (chrome; rendered by `page()`)
- `.util` utility bar, `.site-header` (gets `.scrolled` on scroll → shrinks), `.brand`, `.nav` (`#nav`, collapses to `.menu-toggle` below 1100px; opening focuses the first link, Escape closes and returns focus to the toggle, tabbing out closes it); compact header (no phone number text, 220px lockup) up to 1599px, `.hdr-cta`, `.hdr-ph`
- `.hero` home hero: `<section class="hero on-blue">{picture(..., cls="hero-bg", eager=True)}<div class="wrap hero-in">…<h1>…</h1><p class="hero-lede">…</p>…<div class="hero-foot">…</div></div><span class="photo-cap">{ic("pin")}Pictured: Carmel, Indiana</span></section>`
- `.page-head`, `.page-head.has-photo`, `.ph-bg`, `.crumbs` — interior hero. Use `page_head()`.
- `.photo-cap` — location caption on a solid Shark Blue (`--blue`) bar (the only allowed way to caption a photo band).
- `.site-footer`, `.ftr-g`, `.foot-logo` (lockup on white card), `.legal`, `.legal-row`, `.footnotes`; `.call-bar` (mobile call / estimate bar).

Content blocks
- `.stats-band` + `.sb-head`, `.sb-aside`, `.sb-grid`, `.sb-num`, `.sb-bar` — bold four-figure credentials band.
  `<ul class="sb-grid"><li><span class="sb-num">10<small>YR</small></span><span class="sb-bar"></span><p>Workmanship warranty on roof replacements</p></li>…</ul>`
- `.photo-card` + `.pc-body`, `.pc-k`, `.pc-go` — photo link card; text sits on its own ≥88% Shark Blue panel (deepening to `#17488a` only at the bottom). Focus ring is Shark Blue outside the card. Use `photo_card()`.
- `.svc-grid` with `.c1 .c2 .c3 .c4` — asymmetric 12-column mosaic of four photo cards.
- `.aud-grid` — four staggered tall photo cards.
- `.offset-media` (`.om-big`, `.om-sm`), `.offset-media.left` — big photo with an inset second photo.
  `<div class="offset-media">{picture(a, alt, sizes, cls="om-big")}{picture(b, alt, sizes, cls="om-sm")}</div>`
- `.media-frame` + `.tag` — single photo with offset green block and floating tag (interior pages).
- `.warranty-split`, `.pullquote`, `.yrs` — warranty layout. Use `warranty_band()`.
- `.tiers`, `.tier`, `.tier .lvl`, `.tier.featured` (alias `.tier.top`), `.ribbon` — GAF warranty tiers; only Golden Pledge® is `.featured` with ribbon "Master Elite® only".
- `.claim` — `gaf_badge()` beside `GAF_CLAIM_HTML`. `.gaf-badge` — the Master Elite badge (keep it smaller than the Rocklane logo; GAF requires the company logo to be at least 2x the badge).
- `.process`, `.process-bg`, `.proc-grid`, `.process-steps`, `.proc-ft` — status timeline band. Use `process()`.
- `.status-card`, `.sc-top`, `.pill`, `.sc-track` (`li.done`, `li.now`), `.sc-feat` — portal illustration. Use `status_card()`.
- `.com-band`, `.com-hero`, `.com-bg`, `.com-cards`, `.com-card` (`.b`, `.who`), `.ticks`, `.versico` — commercial band.
- `.hoa-split`, `.pts`, `.pt-ic` — split with icon points. `<ul class="pts"><li><span class="pt-ic">{ic("phone")}</span><div><strong>…</strong><span>…</span></div></li></ul>`
- `.partners`, `.logos`, `.logo-box` — partner marks on white. Use `PARTNERS`.
- `.area`, `.area-bg`, `.area-in`, `.area .cities` — service-area band. Use `service_area()`. `.cities` alone = pill list on light backgrounds.
- `.final`, `.final-bg`, `.final-card` — CTA. Use `CTA`.
- `.split` (`.flip`), `.checks`, `.cards` (`.two`, `.four`), `.card`, `.signs`, `.swatches`, `.people`, `.person` (`.mono`), `.values`, `.stats`/`.stat-row`/`.stat` — interior-page building blocks.
  `<div class="cards"><div class="card reveal"><span class="ico ico-blue">{ic("tool")}</span><h3>…</h3><p>…</p></div></div>`
- Contact and legal: `.contact-grid`, `.form-card`, `.info-list`, `.hours`, `.map`, `.prose`, `.nf` (404).
- Forms and portal (do not rename): `.form .field .field-row .check .hp .notice .notice-ok .notice-error .notice-info .link .back .portal .panel .view .acct .tabs .job-list .job-card .job-status .status-* .tracker .status-note .portal-grid .timeline .files .upload .videos .video .video-frame .staff-tabs .toolbar .table-wrap .data`.

## Brand, accessibility and motion rules

- Colors: Shark Blue `#1E5AA8` leads; `#17488a` only for gradient ends/hover; Lizard Green `#A8CF3E` only for fills, rules, icons and green buttons with `#26303D` text — never small text on white, never any text on Shark Blue, no translucent green halos (rings are solid: `0 0 0 3px white, 0 0 0 5px green`); `--ink` `#26303D` is text on Lizard Green only (`.btn`, `.ico-green`, `.ribbon`, `.status-complete`, `.tracker li.current`, call bar, `::selection`) — all other strong/label/list text is Charcoal (`--char`) or Shark Blue; Charcoal `#4A4A4A` body; Light Grey `#E8EAED`; white. No other hues, no navy fills, no lightened/darkened greens. Montserrat only.
- White text on a photo needs ≥84% Shark Blue `#1E5AA8` under it (≥4.5:1 over a white pixel; use the built-in overlays: `.hero`, `.page-head.has-photo`, `.area`, `.com-hero`, `.process`, `.pc-body`, built on `--ov-h` / `--ov-v`). `--ov-h` holds ≥84% out to 72% of the width, so keep hero copy left; between 1100 and 1279px `.page-head p`, `.hero-foot`, `.ab-lede` and `.sd-hero-facts` are capped at 36rem. Captions go in `.photo-cap`.
- Form fields: 1.5px `#767c86` border (≥3:1 on white), Charcoal text; focus = Shark Blue ring with a transparent outline (shows as `CanvasText` in forced-colors mode).
- Focus rings are automatic (Shark Blue on light, Lizard Green only on blue/dark bands). Don't remove outlines.
- Customer portal links go to `/portal/` (trailing slash, no redirect). Noindex pages (`INDEX = False`) get robots noindex and no rel=canonical.
- Logos: Rocklane lockup `/images/rocklane-co-logo.jpg` unmodified on white/Light Grey, ≥200px wide. Variform/James Hardie marks ≥140px, unmodified, on white. Versico mark only inside commercial content, directly beside the Rocklane Commercial Contractors LLC "Versico Authorized" credit. GAF artwork only via `gaf_badge()` and the `PARTNERS` strip (sources in `images/brands/SOURCES.md`); never the retired Weather Stopper badge, never the GAF tagline. No HAAG or IBHS artwork.

## Claims and wording (binding)

- GAF: say "GAF Master Elite® roofing contractor" for Rocklane Co. The only 2% claim is `GAF_CLAIM_HTML`. Never "top 2% of roofing contractors", never "GAF certified" for Rocklane Co., never the GAF tagline. Silver Pledge™ (™, never ®). Golden Pledge® is the strongest and Master Elite only; it may be described as "up to 25–30 years of workmanship coverage on qualifying roofing systems" + `fn(2)`. System Plus and Silver Pledge™ are not Master Elite exclusives.
- HAAG Certified Inspector: only beside Justin Reddick or Kevin Kortzendorf by name (Residential Roofs). Elsewhere say "owner-led inspections". IBHS FORTIFIED™ Roofing Contractor: only beside Greg Burkert or Michael Burkert by name. Michael Burkert "joins as an owner on January 1, 2027".
- Scope: Rocklane Co. = steep-slope roofing (asphalt shingle replacement, repair, storm-damage inspection), siding (James Hardie® fiber cement — "we install James Hardie® siding", no program/preferred claims — and Variform vinyl, own crews), seamless gutters (custom-cut on site, guards, repair, cleaning), and on warehouses/commercial buildings: gutters, siding, metal wall panels. Low-slope membrane (EPDM/TPO/PVC) = Rocklane Commercial Contractors LLC, "a GAF Certified Commercial Contractor and Versico Authorized". Never imply Rocklane Co. roofs commercial buildings.
- Usable facts: owner-operated since 1980; owners active in daily management ("if something goes wrong, you get an owner on the phone"); Director of Training & Quality Control on staff; 100+ completed communities and commercial properties across central Indiana; specialist network ("you never manage the handoff"); workmanship warranty 10 years on roof replacements, 5 years on repairs, gutters, chimneys and siding; `QUOTE`; the six portal statuses; the 15 cities; contact details; tagline; part of the Rocklane Group.
- Invent nothing: no testimonials, reviews, ratings, prices, crew sizes, response times, years of experience, or new numbers. Banned words: cheap, discount, deal, unbeatable, best-in-class, family-owned (the GAF disclosure's "discounts" is required verbatim and is the only exception).
- Stock photos (see `images/photos/CREDITS.md`) are never captioned as Rocklane projects or "our work". "Pictured: <place>" only in `.photo-cap`, with the place as the source states it.
- Every estimate CTA says "Request an Estimate" and links to `/contact` (no `/request-estimate` page).
