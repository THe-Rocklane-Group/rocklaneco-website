# rocklaneco.com

The Rocklane Co. website and customer portal. Hosted free on GitHub Pages from this
repository (branch `main`, root folder). Custom domain: rocklaneco.com.

| Folder / file | What it is | Published on the site? |
|---|---|---|
| `*.html`, `css/`, `images/`, `js/` | The website | Yes |
| `portal/` | Customer portal (`/portal`) and staff admin (`/portal/staff`) | Yes (not indexed by search engines) |
| `tools/build_site.py` | Generates the HTML pages | No |
| `firebase/` | Firestore security rules for the portal | No |
| `apps-script/` | Google Apps Script: email + file service | No |

## Editing the website

1. Edit the copy in `tools/build_site.py` (follow the Rocklane Brand Foundation v2).
2. Run `python3 tools/build_site.py` from the project folder.
3. Upload the changed files to this repository. GitHub Pages republishes in about a minute.

The portal's code lives in `portal/*.js` and `css/style.css` and is edited directly.

## How the customer portal works

- **Accounts:** customers create an account at rocklaneco.com/portal with their email and a password,
  then confirm their email address. Firebase Authentication stores the password; Rocklane never sees it.
- **Automatic approval:** a customer sees a project only when their verified email is listed in
  that job's *Customer emails*. When someone signs up, rocklane@rocklaneco.com is emailed. If the
  email is already on a job, they're in as soon as they confirm their email. If not, staff pick the job on
  the *Customer accounts* tab and the customer is emailed that access is ready.
- **Status:** staff set the status (Estimate → Approved → Scheduled → In progress → Final walkthrough →
  Complete, or On hold), a short status note, and post dated updates. Customers can be emailed on each change.
- **Photos & documents:** customers and staff upload files (photos, PDF, Word, Excel; 25 MB each).
  Files are stored in a private Google Drive folder, *Rocklane Portal Files (private)*, with one subfolder
  per job. They're never public. Downloads go through the Apps Script, which checks access first.
- **Videos:** upload to YouTube as **Unlisted**, then paste the link on the job. Customers see videos only
  after the job is marked **Paid in full**.
- **Audit trail:** sign-ins, project views, uploads and downloads are logged on the *Activity log* tab.

Cost: $0. This uses Firebase's free Spark plan (Authentication + Firestore), Google Workspace (Apps Script,
Drive, Gmail, Sheets) and YouTube.

## One-time setup

### 1. Firebase project

> **Done Nov 6, 2026.** Project `rocklane-portal` (free Spark plan, under the rocklaneco.com organization), owned by
> justin.reddick@rocklaneco.com. Staff: justin.reddick@rocklaneco.com. The steps below are kept for reference.

1. Go to https://console.firebase.google.com while signed in as rocklane@rocklaneco.com. Create a project
   named `rocklane-portal`. Turn Google Analytics off. Stay on the free Spark plan.
2. **Build → Authentication → Get started → Email/Password → Enable** (leave passwordless off).
   - *Settings → Password policy:* require at least 10 characters, with lowercase letters and numbers (enforced).
   - *Settings → User actions:* keep **Email enumeration protection** on.
   - *Settings → Authorized domains:* add `rocklaneco.com` and `www.rocklaneco.com`.
   - *Templates:* set the sender name to `Rocklane Co.` and the reply-to address to rocklane@rocklaneco.com.
3. **Build → Firestore Database → Create database.** Choose location `nam5 (United States)`, start in
   **production mode**.
4. **Firestore → Rules:** replace everything with the contents of `firebase/firestore.rules`, then click **Publish**.
5. **Project settings → General → Your apps → Web (</>)**: register the app as `rocklaneco.com`. Do *not*
   set up Firebase Hosting. Copy `apiKey`, `authDomain`, `projectId` and `appId` into `portal/config.js`.
6. **Staff list:** in Firestore → Data, start a collection named `staff`. Add one document per staff member.
   The *Document ID* is their email in lowercase (e.g. `justin.reddick@rocklaneco.com`), with a field
   `name` (string). Each staff member then creates a portal account at /portal and confirms their email.
   After that, /portal/staff works for them. Remove the document to remove staff access.
7. **API key restriction (recommended):** Google Cloud console → APIs & Services → Credentials → the
   "Browser key (auto created by Firebase)" → *Website restrictions*: add `https://rocklaneco.com/*` and
   `https://www.rocklaneco.com/*`.

### 2. Apps Script (email + files)

> **Done Nov 6, 2026.** Project *Rocklane Portal Service* in justin.reddick@rocklaneco.com's Drive. It runs as Justin, so
> emails are sent from justin.reddick@rocklaneco.com as "Rocklane Co.", with replies going to rocklane@rocklaneco.com.
> The private Drive folder is *Rocklane Portal Files (private)*, and the log is the *Rocklane Website Requests* sheet.

1. Go to https://script.google.com and click **New project**. Name it `Rocklane Portal Service`.
2. Paste `apps-script/Code.gs` into `Code.gs`. Under *Project Settings*, check **Show "appsscript.json"**,
   then paste `apps-script/appsscript.json` into it.
3. **Project Settings → Script properties:** add `FIREBASE_PROJECT_ID` = your Firebase project ID.
4. Select the `setup` function and click **Run**. Approve the permissions. This creates the private Drive
   folder and the *Rocklane Website Requests* sheet (links appear in the log).
5. **Deploy → New deployment → Web app.** Execute as **Me**, Who has access **Anyone**. Copy the URL
   ending in `/exec` into `SCRIPT_URL` in `portal/config.js`.
6. Upload the updated `portal/config.js` to this repository. The portal and the contact-page estimate form
   go live a minute later.

When you change `Code.gs` later: **Deploy → Manage deployments → Edit → Version: New version → Deploy**.
That keeps the same URL.

## Security and business practices built in

- Access is enforced by Firestore security rules on Google's servers, not by the web page. Customers can
  read only jobs that list their verified email. Staff are listed only in the console.
- Email verification is required before any project data is shown. Password resets and sign-in errors
  don't reveal whether an account exists.
- Staff sessions end when the browser closes or after 30 minutes idle. Customer sessions end after 60
  minutes idle, and customers can choose not to stay signed in.
- Files are private in Rocklane's Google Drive. Only the uploader, staff and the job's customers can download
  them, and file types and sizes are limited.
- The portal pages use a strict Content-Security-Policy and are hidden from search engines.
- Job records can't be deleted from the portal (mark them Complete instead). That keeps records for the
  warranty period. Updates and activity are timestamped by the server in Eastern time.
- The estimate form has spam protection (hidden field, timing check, rate limits). Requests are logged
  to a Google Sheet as well as emailed.
- The privacy policy and portal terms on the site describe all of this. Have them reviewed by counsel
  before launch.

### Recommended next steps

- Turn on 2-Step Verification for every Rocklane Google Workspace account. That protects Firebase, Apps
  Script and Drive.
- Add a DMARC record for rocklaneco.com (email deliverability and anti-spoofing).
- Back up monthly: File → Download the *Rocklane Website Requests* sheet. Drive keeps the files.
