"""Privacy policy.

Long-form legal article: interior hero on a decorative texture, sticky "On this page" index,
numbered h2s, ~72ch measure. The legal text is verbatim; only the layout changed.
legal_article() and LEGAL_CSS are reused by pages/portal_terms.py.
"""
from site_common import *

PATH = "/privacy-policy"
CURRENT = None
TITLE = 'Privacy Policy | Rocklane Co.'
DESC = 'Privacy policy for the Rocklane Company General Contractors LLC website.'
UPDATED = "Updated November 6, 2026"

LEGAL_CSS = """
.legal-sec { padding: clamp(56px, 8vw, 112px) 0 clamp(72px, 9vw, 128px); }
.lg { display: grid; grid-template-columns: minmax(0, 1fr); gap: 40px; }
.toc { background: var(--grey); padding: 24px 24px 18px; border-top: 4px solid var(--blue); }
.toc-t, .lg-help-t { display: block; font-weight: 700; font-size: .78rem; letter-spacing: .2em; text-transform: uppercase; color: var(--blue); margin-bottom: 10px; }
.toc ol { list-style: none; margin: 0; padding: 0; }
.toc li + li { border-top: 1px solid rgba(30,90,168,.14); }
.toc a { display: flex; align-items: center; gap: 14px; min-height: 44px; padding: 6px 0; font-weight: 600; font-size: .95rem; line-height: 1.35; color: var(--char); text-decoration: none; }
.toc a b { font-weight: 800; font-size: .8rem; color: var(--blue); min-width: 1.6em; }
.toc a:hover { color: var(--blue); text-decoration: underline; text-decoration-color: var(--green); text-decoration-thickness: 2px; text-underline-offset: 4px; }
.lg-help { max-width: 72ch; border: 1px solid var(--grey); border-left: 4px solid var(--green); padding: 22px 24px; font-size: .95rem; line-height: 1.55; }
.lg-help p { margin: 0 0 12px; }
.lg-help ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 4px; }
.lg-help li a { display: inline-flex; align-items: center; gap: 10px; min-height: 40px; color: var(--blue); font-weight: 600; text-decoration: none; overflow-wrap: anywhere; }
.lg-help li a:hover { text-decoration: underline; text-decoration-color: var(--green); }
.lg-help .i { color: var(--blue); font-size: 18px; }
.doc { max-width: 72ch; min-width: 0; }
.doc > p.doc-intro { font-size: clamp(1.1rem, 1.6vw, 1.25rem); line-height: 1.65; color: var(--char); margin: 0 0 1.6em; }
.doc-s { padding: 1.6em 0 0; margin-top: 1.6em; border-top: 1px solid var(--grey); scroll-margin-top: 120px; }
.doc-s:first-of-type { margin-top: 0; padding-top: 0; border-top: 0; }
.doc h2 { font-size: clamp(1.45rem, 2.4vw, 2rem); line-height: 1.15; margin: 0 0 .7em; }
.doc h2 .n { display: flex; align-items: center; gap: 14px; font-size: .8rem; font-weight: 800; letter-spacing: .2em; margin-bottom: .9em; color: var(--blue); }
.doc h2 .n::before { content: ""; width: 40px; height: 2px; background: var(--green); flex: none; }
.doc p, .doc li { line-height: 1.75; }
.doc p { margin: 0 0 1em; }
.doc ul { padding-left: 1.2em; margin: 0 0 1em; }
.doc li { margin-bottom: .6em; padding-left: .2em; }
.doc li::marker { color: var(--blue); }
.doc strong { color: var(--char); }
.doc a { color: var(--blue); font-weight: 600; text-decoration: underline; text-decoration-color: var(--green); text-decoration-thickness: 2px; text-underline-offset: 3px; overflow-wrap: anywhere; }
.doc-ft { margin-top: 2.4em; padding-top: 1.4em; border-top: 1px solid var(--grey); display: flex; flex-wrap: wrap; gap: 12px 28px; align-items: center; justify-content: space-between; }
.doc-ft .fine { margin: 0; font-size: .9rem; }
@media (min-width: 1024px) {
  .lg { grid-template-columns: 290px minmax(0, 72ch); grid-template-areas: "toc doc" "toc help";
        column-gap: clamp(56px, 6vw, 112px); row-gap: 48px; justify-content: start; }
  .toc { grid-area: toc; align-self: start; position: sticky; top: 112px; }
  .doc { grid-area: doc; }
  .lg-help { grid-area: help; }
}
@media (min-width: 1600px) { .lg { grid-template-columns: 320px minmax(0, 72ch); } }
@media print {
  .lg { display: block; }
  .toc { position: static; margin-bottom: 24px; }
  .lg-help { margin-top: 24px; }
  .doc { max-width: none; }
}
"""
CSS = LEGAL_CSS


def legal_article(intro, sections, label, path):
    """sections: list of (id, title, html). Returns the white article band with numbered h2s."""
    toc = "\n".join(f'              <li><a href="#{sid}"><b aria-hidden="true">{i:02d}</b>{t}</a></li>'
                    for i, (sid, t, _) in enumerate(sections, 1))
    body = "\n".join(f"""          <section class="doc-s" id="{sid}" aria-labelledby="{sid}-h">
            <h2 id="{sid}-h"><span class="n" aria-hidden="true">{i:02d}</span>{t}</h2>
{html}
          </section>""" for i, (sid, t, html) in enumerate(sections, 1))
    cur = ' aria-current="page"'
    links = "\n".join(f'            <li><a href="{h}"{cur if h == path else ""}>{ic("file")}{t}</a></li>'
                      for h, t in (("/privacy-policy", "Privacy Policy"), ("/portal-terms", "Customer Portal Terms of Use"),
                                   ("/portal/", "Customer Login")))
    intro_html = f'\n          <p class="doc-intro">{intro}</p>' if intro else ""
    return f"""    <div class="legal-sec">
      <div class="wrap lg">
        <nav class="toc" aria-label="On this page">
          <span class="toc-t">On this page</span>
          <ol>
{toc}
          </ol>
        </nav>
        <article class="doc" aria-label="{label}">{intro_html}
{body}
          <div class="doc-ft">
            <p class="fine">{LEGAL} &middot; {UPDATED}</p>
            <a class="text-link" href="#main">Back to top {ic("arrow")}</a>
          </div>
        </article>
        <aside class="lg-help" aria-label="Questions about this page">
          <span class="lg-help-t">Questions?</span>
          <p>Reach the {SHORT} office, {HOURS}.</p>
          <ul>
            <li><a href="mailto:{EMAIL}">{ic("mail")}{EMAIL}</a></li>
            <li><a href="tel:{TEL}">{ic("phone")}{PHONE}</a></li>
{links}
          </ul>
        </aside>
      </div>
    </div>"""


SECTIONS = [
    ("collect", "What we collect", """            <ul>
              <li><strong>Estimate requests.</strong> Your name, email, phone number, property address and the project details you send through our contact form, by phone or by email.</li>
              <li><strong>Customer portal accounts.</strong> Your name, email, phone number, company or HOA name and property address, plus a password that is stored only in encrypted form by Google Firebase. We never see your password.</li>
              <li><strong>Project files.</strong> Photos and documents you or our team upload to your project.</li>
              <li><strong>Portal activity.</strong> A record of sign-ins, uploads and downloads, kept for security and to support you.</li>
            </ul>"""),
    ("use", "How we use it", """            <p>We use your information only to respond to you, prepare estimates, carry out and document your project, give you access to the customer portal, and keep the portal secure. We do not sell or rent your personal information, and we do not use advertising trackers.</p>"""),
    ("storage", "Who stores it", """            <p>Portal accounts and project records are stored with Google Firebase. Estimate requests, emails and project files are stored in our Google Workspace account. Project videos are hosted on YouTube as unlisted videos, shown in the portal only to the customers on that project. Our pages load the Montserrat typeface from Google Fonts, and the map on our contact page is provided by Google. Google may collect technical information under its own privacy policy.</p>"""),
    ("cookies", "Cookies and storage", """            <p>The public website sets no cookies of its own. When you sign in to the customer portal, your browser stores a sign-in token so you stay signed in. Uncheck &ldquo;Keep me signed in&rdquo; on shared computers. The portal signs you out after 60 minutes without activity.</p>"""),
    ("retention", "How long we keep it", """            <p>We keep project records and files for as long as needed for your project, its warranty period and our legal and tax obligations. You may ask us to close your portal account at any time.</p>"""),
    ("choices", "Your choices", f"""            <p>To see, correct or delete your information, or to close your portal account, contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{TEL}">{PHONE}</a>.</p>"""),
]

PRIVACY_HEAD = page_head("Legal", "Privacy Policy", f"{LEGAL} &middot; {UPDATED}",
                         crumb="Privacy Policy", photo="broad-ripple-siding-texture", alt="")

BODY = f"""{PRIVACY_HEAD}
{legal_article("", SECTIONS, "Privacy Policy", PATH)}"""
