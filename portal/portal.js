// Rocklane Co. customer portal (customer side).
import {
  auth, db, configured, $, $$, esc, say, showView, fmtDate, fmtSize, callScript, setRemember,
  uploadFile, downloadFile, logActivity, idleSignOut, STATUSES, STATUS_LABEL, PHONE, ACCEPT,
} from "./common.js";
import {
  onAuthStateChanged, signInWithEmailAndPassword, createUserWithEmailAndPassword,
  sendEmailVerification, sendPasswordResetEmail, signOut, reload,
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
import {
  collection, doc, getDoc, getDocs, query, where, orderBy, setDoc, serverTimestamp,
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

const RETURN_URL = location.origin + "/portal";
let jobs = [];

function friendlyAuthError(e) {
  const c = (e && e.code) || "";
  if (/invalid-credential|wrong-password|user-not-found|invalid-email/.test(c))
    return "That email and password don't match our records.";
  if (/email-already-in-use/.test(c))
    return "An account already exists for that email. Sign in, or reset your password.";
  if (/weak-password|password-does-not-meet/.test(c))
    return "Please choose a stronger password: at least 10 characters with a mix of letters and numbers.";
  if (/too-many-requests/.test(c))
    return "Too many attempts. Please wait a few minutes and try again.";
  if (/network/.test(c)) return "We couldn't reach the server. Check your connection and try again.";
  return (e && e.message && !/Firebase/.test(e.message)) ? e.message
    : "Something went wrong. Please try again or call " + PHONE + ".";
}

function busy(form, on) {
  $$("button, input, select, textarea", form).forEach((el) => { el.disabled = on; });
}

// ------------------------------------------------------------ auth screens

function initAuthForms() {
  $$("[data-tab]").forEach((b) => b.addEventListener("click", () => {
    $$("[data-tab]").forEach((x) => x.setAttribute("aria-selected", String(x === b)));
    $$(".auth-form").forEach((f) => { f.hidden = f.id !== "f-" + b.dataset.tab; });
    say($("#auth-msg"), "");
  }));

  $("#f-signin").addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const f = ev.target;
    busy(f, true); say($("#auth-msg"), "");
    try {
      await setRemember(f.remember.checked);
      await signInWithEmailAndPassword(auth, f.email.value.trim(), f.password.value);
      logActivity("sign_in");
    } catch (e) { say($("#auth-msg"), friendlyAuthError(e), "error"); }
    busy(f, false);
  });

  $("#f-signup").addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const f = ev.target;
    say($("#auth-msg"), "");
    if (f.password.value.length < 10 || !/[a-z]/.test(f.password.value) || !/\d/.test(f.password.value))
      return say($("#auth-msg"), "Please use at least 10 characters, including lowercase letters and numbers.", "error");
    if (f.password.value !== f.password2.value)
      return say($("#auth-msg"), "The two passwords don't match.", "error");
    if (!f.terms.checked)
      return say($("#auth-msg"), "Please agree to the portal terms and privacy policy.", "error");
    busy(f, true);
    try {
      const cred = await createUserWithEmailAndPassword(auth, f.email.value.trim(), f.password.value);
      await setDoc(doc(db, "users", cred.user.uid), {
        name: f.name.value.trim().slice(0, 100),
        email: cred.user.email.toLowerCase(),
        phone: f.phone.value.trim().slice(0, 40),
        company: f.company.value.trim().slice(0, 120),
        propertyAddress: f.address.value.trim().slice(0, 200),
        createdAt: serverTimestamp(),
        termsAcceptedAt: serverTimestamp(),
      });
      await sendEmailVerification(cred.user, { url: RETURN_URL });
      callScript("signup").catch((e) => console.warn("Office notice failed:", e));
      f.reset();
      render(cred.user);
    } catch (e) { say($("#auth-msg"), friendlyAuthError(e), "error"); }
    busy(f, false);
  });

  $("#f-reset").addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const f = ev.target;
    busy(f, true);
    try { await sendPasswordResetEmail(auth, f.email.value.trim(), { url: RETURN_URL }); }
    catch (e) { if (!/user-not-found|invalid-email/.test(e.code || "")) console.warn(e); }
    // Same message either way, so the form can't be used to discover accounts.
    say($("#auth-msg"), "If an account exists for that email, a reset link is on its way. Check your inbox and spam folder.", "ok");
    busy(f, false);
  });

  $("#btn-resend").addEventListener("click", async () => {
    try {
      await sendEmailVerification(auth.currentUser, { url: RETURN_URL });
      say($("#verify-msg"), "We sent a new verification email.", "ok");
    } catch (e) { say($("#verify-msg"), friendlyAuthError(e), "error"); }
  });
  $("#btn-verified").addEventListener("click", async () => {
    await reload(auth.currentUser);
    if (!auth.currentUser.emailVerified)
      return say($("#verify-msg"), "We haven't seen the confirmation yet. Open the link in the email, then try again.", "error");
    render(auth.currentUser);
  });
  $$(".btn-signout").forEach((b) => b.addEventListener("click", () => signOut(auth)));
}

// ----------------------------------------------------------------- render

async function render(user) {
  const acct = $("#acct");
  if (!user) {
    acct.hidden = true;
    jobs = [];
    return showView("v-auth");
  }
  acct.hidden = false;
  $("#acct-email").textContent = user.email;

  if (!user.emailVerified) await reload(user).catch(() => {});
  if (!user.emailVerified) {
    $("#verify-email").textContent = user.email;
    return showView("v-verify");
  }
  await user.getIdToken(true); // pick up the email_verified claim for the security rules

  try {
    const snap = await getDocs(query(collection(db, "jobs"),
      where("customerEmails", "array-contains", user.email.toLowerCase())));
    jobs = snap.docs.map((d) => ({ id: d.id, ...d.data() }))
      .sort((a, b) => (b.updatedAt?.seconds || 0) - (a.updatedAt?.seconds || 0));
  } catch (e) {
    console.error(e);
    say($("#portal-msg"), "We couldn't load your projects. Please refresh, or call " + PHONE + ".", "error");
    jobs = [];
  }
  if (!jobs.length) {
    $("#pending-email").textContent = user.email;
    return showView("v-pending");
  }
  route();
}

function route() {
  if (!auth.currentUser || !auth.currentUser.emailVerified || !jobs.length) return;
  const id = decodeURIComponent(location.hash.slice(1));
  const job = jobs.find((j) => j.id === id);
  if (job) return renderJob(job);
  if (jobs.length === 1 && !id) return renderJob(jobs[0], true);
  renderList();
}

function renderList() {
  $("#jobs-list").innerHTML = jobs.map((j) => `
    <a class="job-card" href="#${esc(j.id)}">
      <span class="job-status status-${esc(j.status)}">${esc(STATUS_LABEL[j.status] || "")}</span>
      <strong>${esc(j.title)}</strong>
      <span>${esc(j.address)}</span>
      <small>Updated ${esc(fmtDate(j.updatedAt, false))}</small>
    </a>`).join("");
  showView("v-jobs");
}

function tracker(status) {
  const idx = STATUSES.findIndex(([k]) => k === status);
  return `<ol class="tracker" aria-label="Project progress">` + STATUSES.map(([k, label], i) => {
    const state = i < idx ? "done" : i === idx ? "current" : "todo";
    return `<li class="${state}"${i === idx ? ' aria-current="step"' : ""}><span>${esc(label)}</span></li>`;
  }).join("") + `</ol>`;
}

async function renderJob(job, only = false) {
  $("#job-back").hidden = only;
  $("#job-title").textContent = job.title;
  $("#job-address").textContent = job.address || "";
  $("#job-tracker").innerHTML = job.status === "on_hold"
    ? `<p class="notice notice-info">This project is on hold. Our office will contact you with next steps.</p>`
    : tracker(job.status);
  $("#job-note").textContent = job.statusNote || "";
  $("#job-note").hidden = !job.statusNote;
  $("#job-updated").textContent = "Last updated " + fmtDate(job.updatedAt);
  $("#job-updates").innerHTML = `<p class="muted">Loading…</p>`;
  $("#job-files").innerHTML = `<p class="muted">Loading…</p>`;
  $("#job-videos").innerHTML = "";
  say($("#up-msg"), "");
  showView("v-job");
  $("#f-upload").dataset.job = job.id;
  logActivity("view_job", job.id);

  const base = ["jobs", job.id];
  const [ups, files] = await Promise.all([
    getDocs(query(collection(db, ...base, "updates"), orderBy("createdAt", "desc"))).catch(() => null),
    getDocs(query(collection(db, ...base, "files"), orderBy("createdAt", "desc"))).catch(() => null),
  ]);

  $("#job-updates").innerHTML = ups && ups.size
    ? ups.docs.map((d) => { const u = d.data(); return `
        <li><time>${esc(fmtDate(u.createdAt))}</time><p>${esc(u.text).replace(/\n/g, "<br>")}</p></li>`; }).join("")
    : `<li class="muted">No updates yet. We'll post progress here as your project moves forward.</li>`;

  renderFiles(job.id, files);

  if (job.paid) {
    const media = await getDocs(query(collection(db, ...base, "media"), orderBy("createdAt", "desc"))).catch(() => null);
    $("#job-videos").innerHTML = media && media.size
      ? media.docs.map((d) => { const m = d.data(); return `
          <figure class="video">
            <div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/${esc(m.youtubeId)}?rel=0"
              title="${esc(m.title)}" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe></div>
            <figcaption>${esc(m.title)}</figcaption>
          </figure>`; }).join("")
      : `<p class="muted">Your project videos will appear here once they're ready.</p>`;
  } else {
    $("#job-videos").innerHTML = `<p class="muted">Project videos become available here once your project is paid in full.</p>`;
  }
}

function renderFiles(jobId, files) {
  const rows = files && files.size ? files.docs.map((d) => { const f = d.data(); return `
      <li><button type="button" class="link" data-file="${esc(d.id)}">${esc(f.name)}</button>
        <small>${esc(fmtSize(f.size))} · ${f.byStaff ? "From Rocklane Co." : "Uploaded by " + esc(f.uploadedBy)} · ${esc(fmtDate(f.createdAt, false))}</small></li>`; }).join("")
    : `<li class="muted">No files yet.</li>`;
  $("#job-files").innerHTML = rows;
  $$("#job-files [data-file]").forEach((b) => b.addEventListener("click", async () => {
    b.disabled = true;
    try { await downloadFile(jobId, b.dataset.file); }
    catch (e) { say($("#up-msg"), e.message, "error"); }
    b.disabled = false;
  }));
}

function initUpload() {
  $("#up-files").setAttribute("accept", ACCEPT);
  $("#f-upload").addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const f = ev.target, jobId = f.dataset.job, list = [...$("#up-files").files];
    if (!list.length) return say($("#up-msg"), "Choose one or more files first.", "error");
    busy(f, true);
    let done = 0;
    try {
      for (const file of list) {
        say($("#up-msg"), `Uploading ${file.name} (${done + 1} of ${list.length})…`, "info");
        await uploadFile(jobId, file, false);
        done++;
      }
      say($("#up-msg"), `Uploaded ${done} file${done === 1 ? "" : "s"}. Our office has been notified.`, "ok");
      f.reset();
      const files = await getDocs(query(collection(db, "jobs", jobId, "files"), orderBy("createdAt", "desc")));
      renderFiles(jobId, files);
    } catch (e) { say($("#up-msg"), e.message, "error"); }
    busy(f, false);
  });
}

// ------------------------------------------------------------------- boot

if (!configured) {
  showView("v-setup");
} else {
  initAuthForms();
  initUpload();
  addEventListener("hashchange", route);
  onAuthStateChanged(auth, (u) => render(u));
  idleSignOut(() => auth.currentUser && signOut(auth));
}
