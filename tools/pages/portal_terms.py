"""Customer portal terms of use.

Same long-form legal article as the privacy policy (legal_article / LEGAL_CSS from pages.privacy).
The legal text is verbatim; only the layout changed.
"""
from site_common import *
from pages.privacy import legal_article, LEGAL_CSS, UPDATED

PATH = "/portal-terms"
CURRENT = None
TITLE = 'Customer Portal Terms of Use | Rocklane Co.'
DESC = 'Terms of use for the Rocklane Co. customer portal.'
CSS = LEGAL_CSS

INTRO = (f"The {SHORT} customer portal lets our customers follow their projects, share photos and documents "
         "with our team, and view project videos. By creating an account you agree to these terms.")

SECTIONS = [
    ("account", "Your account", f"""            <ul>
              <li>Accounts are for {SHORT} customers, property managers and board members with a project we are performing or have performed.</li>
              <li>Keep your password private and don&rsquo;t share your account. Tell us right away at {PHONE} if you think someone else has used it.</li>
              <li>We give access to a project only to the email addresses connected to it. We may change or remove access when a project&rsquo;s contacts change.</li>
            </ul>"""),
    ("uploads", "Files you upload", """            <ul>
              <li>Upload only photos and documents related to your project that you have the right to share.</li>
              <li>Files are visible to our team and to the other contacts on the same project.</li>
              <li>Don&rsquo;t upload payment card numbers, Social Security numbers or other sensitive personal information.</li>
            </ul>"""),
    ("videos", "Project information and videos", """            <p>Project status, updates and videos are provided for your convenience. Your signed contract, estimate and warranty documents govern your project. Project videos are for your use in connection with your property and may not be republished without our permission.</p>"""),
    ("availability", "Availability", f"""            <p>We work to keep the portal available but cannot guarantee it will always be. If you can&rsquo;t reach it, call the office at <a href="tel:{TEL}">{PHONE}</a>.</p>"""),
    ("privacy", "Privacy", """            <p>Our <a href="/privacy-policy">privacy policy</a> explains what we collect and how we use it.</p>"""),
]

TERMS_HEAD = page_head("Legal", "Customer Portal Terms of Use", f"{LEGAL} &middot; {UPDATED}",
                       crumb="Portal Terms", photo="shingle-texture", alt="")

BODY = f"""{TERMS_HEAD}
{legal_article(INTRO, SECTIONS, "Customer Portal Terms of Use", PATH)}"""
