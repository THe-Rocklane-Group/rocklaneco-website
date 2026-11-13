"""Customer portal shell. Body, IDs, classes, CSP head and script tag must stay UNCHANGED (portal/portal.js depends on them)."""
from site_common import *

PATH = "/portal"
CURRENT = None
TITLE = 'Customer Portal | Rocklane Co.'
DESC = 'Sign in to check your Rocklane Co. project status, share photos and documents, and view project videos.'
CSS = ""
OUT = "portal/index.html"
INDEX = False
SITEMAP = False
SCRIPTS = '\n  <script type="module" src="/portal/portal.js"></script>'


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
HEAD = PORTAL_HEAD

BODY = f"""    <div class="page-head on-blue">
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
              <div class="field"><label for="su-pass">Password</label><input id="su-pass" name="password" type="password" autocomplete="new-password" required minlength="10"><small>At least 10 characters, with lowercase letters and numbers.</small></div>
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
