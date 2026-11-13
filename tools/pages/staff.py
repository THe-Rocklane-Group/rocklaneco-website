"""Staff portal shell. Body, IDs, classes, CSP head and script tag must stay UNCHANGED (portal/staff.js depends on them)."""
from site_common import *

PATH = "/portal/staff"
CURRENT = None
TITLE = 'Portal Admin | Rocklane Co.'
DESC = 'Rocklane Co. staff portal.'
CSS = ""
OUT = "portal/staff.html"
INDEX = False
SITEMAP = False
SCRIPTS = '\n  <script type="module" src="/portal/staff.js"></script>'


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
            <p class="fine">No portal account yet? <a href="/portal/">Create one in the customer portal</a> (choose <strong>Create account</strong>) with your @rocklaneco.com email, then confirm the verification email. Staff access also needs an owner to add your email to the staff list in the Firebase console.</p>
          </form>
        </div>
        <div class="view panel" id="v-denied" hidden>
          <h2>Staff access only</h2>
          <p>This account isn&rsquo;t on the staff list, or its email isn&rsquo;t verified yet. If you&rsquo;re Rocklane staff, confirm your email from the verification message, then ask an owner to add your email to the staff list in the Firebase console. Customers can use the <a href="/portal/">customer portal</a>.</p>
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
