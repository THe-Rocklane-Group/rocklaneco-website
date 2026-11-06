/**
 * Rocklane Co. — website + customer portal mail and file service.
 *
 * Runs free inside Rocklane's Google Workspace, deployed as a web app from the
 * rocklane@rocklaneco.com account ("Execute as: Me", "Who has access: Anyone").
 *
 *  - estimate : website estimate form → email to rocklane@, confirmation to the
 *               customer, row in the "Estimate requests" sheet.
 *  - signup   : new portal account → email to rocklane@, acknowledgement to the
 *               customer, row in the "Portal accounts" sheet.
 *  - upload   : customer/staff photo or document → saved in a private Drive
 *               folder for that job; office is emailed.
 *  - download : returns a file from the job's Drive folder to an authorized user.
 *  - notify   : staff only — emails the job's customers (new update, access ready,
 *               new video).
 *
 * Who-is-who is decided by Firebase, not by this script: every portal call
 * carries the user's Firebase ID token, and the script makes the Firestore REST
 * call *as that user*. Firestore validates the token and applies the same
 * security rules as the portal, so a request only succeeds for a real,
 * authorized user.
 *
 * Setup: see README.md → "Apps Script". Run setup() once, then Deploy.
 */

var NOTIFY_EMAIL = 'rocklane@rocklaneco.com';
var COMPANY = 'Rocklane Co.';
var LEGAL = 'Rocklane Company General Contractors LLC';
var PHONE = '(317) 898-8696';
var SITE = 'https://rocklaneco.com';
var MAX_BYTES = 25 * 1024 * 1024;
var ALLOWED_TYPES = /^(image\/(jpeg|png|gif|webp|heic|heif)|application\/pdf|application\/msword|application\/vnd\.openxmlformats-officedocument\.(wordprocessingml\.document|spreadsheetml\.sheet)|application\/vnd\.ms-excel|text\/plain)$/;
var STATUS_LABELS = {
  estimate: 'Estimate', approved: 'Approved', scheduled: 'Scheduled',
  in_progress: 'In progress', final_walkthrough: 'Final walkthrough',
  complete: 'Complete', on_hold: 'On hold'
};

function props_() { return PropertiesService.getScriptProperties(); }
function prop_(k) {
  var v = props_().getProperty(k);
  if (!v) throw new Error('Script property ' + k + ' is not set. Run setup().');
  return v;
}

/** Run once from the editor. Creates the Drive folder and the log sheet. */
function setup() {
  var p = props_();
  if (!p.getProperty('FIREBASE_PROJECT_ID')) {
    throw new Error('First add Script property FIREBASE_PROJECT_ID (Project Settings → Script properties).');
  }
  if (!p.getProperty('DRIVE_ROOT_FOLDER_ID')) {
    var f = DriveApp.createFolder('Rocklane Portal Files (private)');
    p.setProperty('DRIVE_ROOT_FOLDER_ID', f.getId());
  }
  if (!p.getProperty('SHEET_ID')) {
    var ss = SpreadsheetApp.create('Rocklane Website Requests');
    var est = ss.getSheets()[0].setName('Estimate requests');
    est.appendRow(['Received (ET)', 'Name', 'Email', 'Phone', 'Property address', 'Project', 'Details']);
    ss.insertSheet('Portal accounts').appendRow(['Created (ET)', 'Name', 'Email', 'Phone', 'Company', 'Property address']);
    ss.insertSheet('Uploads').appendRow(['Uploaded (ET)', 'Job ID', 'File', 'Size (KB)', 'By']);
    p.setProperty('SHEET_ID', ss.getId());
  }
  Logger.log('Drive folder: https://drive.google.com/drive/folders/' + p.getProperty('DRIVE_ROOT_FOLDER_ID'));
  Logger.log('Sheet: https://docs.google.com/spreadsheets/d/' + p.getProperty('SHEET_ID'));
}

function doGet() { return json_({ ok: true, service: 'rocklane-portal' }); }

function doPost(e) {
  try {
    var body = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    switch (body.action) {
      case 'estimate': return json_(estimate_(body));
      case 'signup':   return json_(signup_(body));
      case 'upload':   return json_(upload_(body));
      case 'download': return json_(download_(body));
      case 'notify':   return json_(notify_(body));
      default:         return json_({ ok: false, error: 'Unknown request.' });
    }
  } catch (err) {
    console.error(err && err.stack || err);
    return json_({ ok: false, error: (err && err.userMessage) || 'Something went wrong. Please call ' + PHONE + '.' });
  }
}

function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
function userError_(msg) { var e = new Error(msg); e.userMessage = msg; return e; }

function clean_(v, max) {
  return String(v == null ? '' : v).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, '').trim().slice(0, max || 500);
}
function validEmail_(s) { return /^[^\s@<>"]+@[^\s@<>"]+\.[^\s@<>"]+$/.test(s); }
function nowET_() { return Utilities.formatDate(new Date(), 'America/New_York', 'yyyy-MM-dd h:mm a z'); }
function sheet_(name) { return SpreadsheetApp.openById(prop_('SHEET_ID')).getSheetByName(name); }
// Stop formulas being injected into the log sheet.
function cell_(s) { return /^[=+\-@]/.test(s) ? "'" + s : s; }

/** Allow `limit` calls per `key` per hour. */
function rateLimit_(key, limit) {
  var cache = CacheService.getScriptCache();
  var k = 'rl:' + Utilities.base64EncodeWebSafe(key).slice(0, 200);
  var n = Number(cache.get(k) || 0);
  if (n >= limit) throw userError_('Too many requests. Please try again later or call ' + PHONE + '.');
  cache.put(k, String(n + 1), 3600);
}

function footer_() {
  return '\n\n' + COMPANY + ' | ' + PHONE + '\n1690 S. Franklin Rd., Indianapolis, IN 46239\n' +
    'Mon–Fri 9 AM–4 PM ET\n' + SITE;
}
function send_(to, subject, text, replyTo) {
  var opts = { name: COMPANY };
  if (replyTo) opts.replyTo = replyTo;
  MailApp.sendEmail(to, subject, text, opts);
}

// ---------------------------------------------------------------- estimate

function estimate_(b) {
  // Spam checks: hidden field must be empty; a person takes >3 s to fill the form.
  if (clean_(b.website)) return { ok: true };
  if (Number(b.elapsedMs) < 3000) return { ok: true };

  var r = {
    name: clean_(b.name, 100), email: clean_(b.email, 200).toLowerCase(),
    phone: clean_(b.phone, 40), address: clean_(b.address, 200),
    project: clean_(b.project, 60), details: clean_(b.details, 3000)
  };
  if (!r.name || !validEmail_(r.email) || !r.phone || !r.address) {
    throw userError_('Please fill in your name, email, phone and property address.');
  }
  rateLimit_('est:' + r.email, 3);
  rateLimit_('est:all', 60);

  sheet_('Estimate requests').appendRow([nowET_(), cell_(r.name), cell_(r.email), cell_(r.phone),
    cell_(r.address), cell_(r.project), cell_(r.details)]);

  send_(NOTIFY_EMAIL, 'Estimate request: ' + r.name + ' — ' + r.project,
    'New estimate request from rocklaneco.com\n\n' +
    'Name: ' + r.name + '\nEmail: ' + r.email + '\nPhone: ' + r.phone +
    '\nProperty: ' + r.address + '\nProject: ' + r.project + '\n\n' + r.details +
    '\n\nReceived ' + nowET_() + '. Reply to this email to answer the customer.', r.email);

  send_(r.email, 'We received your estimate request — ' + COMPANY,
    'Hi ' + r.name + ',\n\nThank you for contacting ' + COMPANY + '. We received your request for ' +
    (r.project || 'an estimate').toLowerCase() + ' at ' + r.address + '. A member of our team will ' +
    'contact you within one business day to schedule a time to look at the property.\n\n' +
    'Need us sooner? Call the office at ' + PHONE + '.' + footer_());
  return { ok: true };
}

// ------------------------------------------------------- Firebase (as user)

function decodeToken_(idToken) {
  var parts = String(idToken || '').split('.');
  if (parts.length !== 3) throw userError_('Please sign in again.');
  var payload = JSON.parse(Utilities.newBlob(Utilities.base64DecodeWebSafe(parts[1])).getDataAsString());
  var pid = prop_('FIREBASE_PROJECT_ID');
  if (payload.aud !== pid || payload.iss !== 'https://securetoken.google.com/' + pid ||
      !(payload.exp * 1000 > Date.now())) {
    throw userError_('Your session has expired. Please sign in again.');
  }
  return { uid: payload.user_id || payload.sub, email: String(payload.email || '').toLowerCase(),
           verified: payload.email_verified === true, token: idToken };
}

/** GET a Firestore document as the signed-in user. Null when denied or missing. */
function fsGet_(user, path) {
  var url = 'https://firestore.googleapis.com/v1/projects/' + prop_('FIREBASE_PROJECT_ID') +
    '/databases/(default)/documents/' + path;
  var res = UrlFetchApp.fetch(url, {
    headers: { Authorization: 'Bearer ' + user.token }, muteHttpExceptions: true
  });
  var code = res.getResponseCode();
  if (code === 401) throw userError_('Your session has expired. Please sign in again.');
  if (code !== 200) return null;
  return JSON.parse(res.getContentText()).fields || {};
}
function fsStr_(f, k) { return f && f[k] && f[k].stringValue || ''; }
function fsList_(f, k) {
  var v = f && f[k] && f[k].arrayValue && f[k].arrayValue.values || [];
  return v.map(function (x) { return x.stringValue; }).filter(Boolean);
}

function isStaff_(user) {
  return user.verified && /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+$/.test(user.email) &&
    fsGet_(user, 'staff/' + encodeURIComponent(user.email)) !== null;
}

/** Throws unless the user may see this job. Returns the job's fields. */
function requireJob_(user, jobId) {
  if (!/^[A-Za-z0-9_-]{1,60}$/.test(jobId || '')) throw userError_('Unknown project.');
  if (!user.verified) throw userError_('Please verify your email address first.');
  var job = fsGet_(user, 'jobs/' + jobId);
  if (!job) throw userError_('You do not have access to this project.');
  return job;
}

// ------------------------------------------------------------------ signup

function signup_(b) {
  var user = decodeToken_(b.idToken);
  // Proves the token is genuine: Firestore only returns the profile to its owner.
  var profile = fsGet_(user, 'users/' + user.uid);
  if (!profile) throw userError_('We could not find your new account. Please try again.');
  rateLimit_('signup:' + user.uid, 2);

  var p = { name: fsStr_(profile, 'name'), phone: fsStr_(profile, 'phone'),
            company: fsStr_(profile, 'company'), address: fsStr_(profile, 'propertyAddress') };
  sheet_('Portal accounts').appendRow([nowET_(), cell_(p.name), cell_(user.email), cell_(p.phone),
    cell_(p.company), cell_(p.address)]);

  send_(NOTIFY_EMAIL, 'Portal account request: ' + p.name,
    'A customer created a portal account on rocklaneco.com.\n\n' +
    'Name: ' + p.name + '\nEmail: ' + user.email + '\nPhone: ' + p.phone +
    '\nCompany/HOA: ' + (p.company || '—') + '\nProperty: ' + p.address + '\n\n' +
    'Approval is automatic: if this email is already listed on their job, they can see it as soon as ' +
    'they verify their email. If not, open the staff page and add ' + user.email + ' to their job:\n' +
    SITE + '/portal/staff', user.email);

  send_(user.email, 'Your ' + COMPANY + ' customer portal account',
    'Hi ' + p.name + ',\n\nThank you for creating a ' + COMPANY + ' customer portal account. ' +
    'Please confirm your email address using the separate verification email we sent.\n\n' +
    'Once your email is confirmed and your project is linked to your account, you will be able to ' +
    'check its status, share photos and documents with our team, and view your project videos at ' +
    SITE + '/portal\n\nIf your project is not showing yet, our office has been notified and will ' +
    'link it within one business day.' + footer_());
  return { ok: true };
}

// ---------------------------------------------------------- upload/download

function jobFolder_(jobId) {
  var root = DriveApp.getFolderById(prop_('DRIVE_ROOT_FOLDER_ID'));
  var it = root.getFoldersByName(jobId);
  return it.hasNext() ? it.next() : root.createFolder(jobId);
}

function upload_(b) {
  var user = decodeToken_(b.idToken);
  var job = requireJob_(user, b.jobId);
  rateLimit_('up:' + user.uid, 40);

  var name = clean_(b.name, 180).replace(/[\\/:*?"<>|]/g, '_') || 'upload';
  var type = clean_(b.mimeType, 120);
  if (!ALLOWED_TYPES.test(type)) throw userError_('That file type is not supported. Please upload photos, PDFs, Word or Excel files.');
  var bytes = Utilities.base64Decode(String(b.data || ''));
  if (!bytes.length) throw userError_('The file is empty.');
  if (bytes.length > MAX_BYTES) throw userError_('Files must be 25 MB or smaller.');

  var staff = isStaff_(user);
  var file = jobFolder_(b.jobId).createFile(Utilities.newBlob(bytes, type, name));
  file.setDescription('Uploaded by ' + user.email + ' via the customer portal, ' + nowET_());

  sheet_('Uploads').appendRow([nowET_(), b.jobId, cell_(name), Math.round(bytes.length / 1024), user.email]);
  if (!staff) {
    send_(NOTIFY_EMAIL, 'New customer upload: ' + fsStr_(job, 'title'),
      user.email + ' uploaded "' + name + '" (' + Math.round(bytes.length / 1024) + ' KB) to ' +
      fsStr_(job, 'title') + ' (' + fsStr_(job, 'address') + ').\n\n' +
      'Open the job: ' + SITE + '/portal/staff#' + b.jobId + '\nDrive: ' + file.getUrl());
  }
  return { ok: true, driveFileId: file.getId(), size: bytes.length, name: name, byStaff: staff };
}

function download_(b) {
  var user = decodeToken_(b.idToken);
  requireJob_(user, b.jobId);
  if (!/^[A-Za-z0-9_-]{1,100}$/.test(b.fileDocId || '')) throw userError_('Unknown file.');
  var rec = fsGet_(user, 'jobs/' + b.jobId + '/files/' + b.fileDocId);
  if (!rec) throw userError_('You do not have access to this file.');

  var file = DriveApp.getFileById(fsStr_(rec, 'driveFileId'));
  // Only serve files that live in this job's own folder.
  var parents = file.getParents(), ok = false;
  var rootId = prop_('DRIVE_ROOT_FOLDER_ID');
  while (parents.hasNext()) {
    var p = parents.next();
    if (p.getName() === b.jobId) {
      var gp = p.getParents();
      while (gp.hasNext()) if (gp.next().getId() === rootId) ok = true;
    }
  }
  if (!ok || file.isTrashed()) throw userError_('That file is no longer available.');
  var blob = file.getBlob();
  if (blob.getBytes().length > MAX_BYTES) throw userError_('That file is too large to download here. Please call the office.');
  return { ok: true, name: file.getName(), mimeType: blob.getContentType(),
           data: Utilities.base64Encode(blob.getBytes()) };
}

// ------------------------------------------------------------------ notify

function notify_(b) {
  var user = decodeToken_(b.idToken);
  if (!isStaff_(user)) throw userError_('Staff only.');
  var job = requireJob_(user, b.jobId);
  var to = fsList_(job, 'customerEmails').filter(validEmail_);
  if (!to.length) return { ok: true, sent: 0 };
  rateLimit_('notify:' + b.jobId, 20);

  var title = fsStr_(job, 'title');
  var status = STATUS_LABELS[fsStr_(job, 'status')] || '';
  var link = SITE + '/portal#' + b.jobId;
  var subject, text;
  if (b.kind === 'linked') {
    subject = 'Your project is ready to view — ' + COMPANY;
    text = 'Hello,\n\nYour ' + COMPANY + ' customer portal access is ready. Sign in to see the status of ' +
      title + ', share photos and documents with our team, and view project updates:\n' + link +
      '\n\nUse this email address to sign in. If you have not created an account yet, choose ' +
      '"Create account" on that page.';
  } else if (b.kind === 'media') {
    subject = 'New project video: ' + title;
    text = 'Hello,\n\nA new video of your project, ' + title + ', is ready in your customer portal:\n' + link;
  } else {
    subject = 'Project update: ' + title + (status ? ' — ' + status : '');
    text = 'Hello,\n\nThere is a new update on your project, ' + title + '.' +
      (status ? ' Current status: ' + status + '.' : '') + '\n\nSign in to read it:\n' + link;
  }
  text += '\n\nQuestions? Reply to this email or call ' + PHONE + '.' + footer_();
  to.forEach(function (addr) { send_(addr, subject, text, NOTIFY_EMAIL); });
  return { ok: true, sent: to.length };
}
