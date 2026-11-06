// Rocklane Co. customer portal — staff page.
// Access is enforced by the Firestore rules: only verified emails listed in /staff can read or write here.
import {
  auth, db, configured, $, $$, esc, say, showView, fmtDate, fmtSize, callScript, setRemember,
  uploadFile, downloadFile, logActivity, idleSignOut, youtubeId, STATUSES, STATUS_LABEL, ACCEPT,
} from "./common.js";
import {
  onAuthStateChanged, signInWithEmailAndPassword, signOut, reload,
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
import {
  collection, doc, getDoc, getDocs, addDoc, setDoc, deleteDoc, query, orderBy, limit,
  serverTimestamp,
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

let jobs = [], users = [], current = null;

const me = () => auth.currentUser.email.toLowerCase();
const busy = (form, on) => $$("button, input, select, textarea", form).forEach((el) => { el.disabled = on; });

function parseEmails(text) {
  return [...new Set(String(text).toLowerCase().split(/[\s,;]+/)
    .map((s) => s.trim()).filter((s) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s)))].slice(0, 20);
}

// ------------------------------------------------------------------ boot

async function render(user) {
  $("#acct").hidden = !user;
  $(".staff-tabs").hidden = true;
  if (!user) return showView("v-signin");
  $("#acct-email").textContent = user.email;
  if (!user.emailVerified) await reload(user).catch(() => {});
  if (!user.emailVerified) return showView("v-denied");
  await user.getIdToken(true);
  const staff = await getDoc(doc(db, "staff", me())).catch(() => null);
  if (!staff || !staff.exists()) return showView("v-denied");
  logActivity("staff_sign_in");
  $(".staff-tabs").hidden = false;
  await loadAll();
  route();
}

async function loadAll() {
  const [j, u] = await Promise.all([
    getDocs(query(collection(db, "jobs"), orderBy("updatedAt", "desc"))),
    getDocs(query(collection(db, "users"), orderBy("createdAt", "desc"))),
  ]);
  jobs = j.docs.map((d) => ({ id: d.id, ...d.data() }));
  users = u.docs.map((d) => ({ id: d.id, ...d.data() }));
}

function route() {
  const h = decodeURIComponent(location.hash.slice(1));
  $$(".staff-tabs a").forEach((a) => a.setAttribute("aria-current",
    String(a.getAttribute("href") === "#" + (h === "accounts" || h === "activity" ? h : ""))));
  if (h === "accounts") return renderAccounts();
  if (h === "activity") return renderActivity();
  if (h === "new") return renderJob(null);
  const job = jobs.find((j) => j.id === h);
  if (job) return renderJob(job);
  renderJobs();
}

// --------------------------------------------------------------- job list

function renderJobs() {
  const q = $("#job-search").value.trim().toLowerCase();
  const st = $("#job-filter").value;
  const rows = jobs.filter((j) =>
    (!st || j.status === st) &&
    (!q || [j.title, j.address, ...(j.customerEmails || [])].join(" ").toLowerCase().includes(q)));
  $("#jobs-body").innerHTML = rows.length ? rows.map((j) => `
    <tr>
      <td><a href="#${esc(j.id)}">${esc(j.title)}</a><br><small>${esc(j.address)}</small></td>
      <td><span class="job-status status-${esc(j.status)}">${esc(STATUS_LABEL[j.status])}</span></td>
      <td>${j.paid ? "Paid" : "—"}</td>
      <td><small>${(j.customerEmails || []).map(esc).join("<br>") || "—"}</small></td>
      <td><small>${esc(fmtDate(j.updatedAt, false))}</small></td>
    </tr>`).join("") : `<tr><td colspan="5" class="muted">No jobs match.</td></tr>`;
  const pending = users.filter((u) => !jobs.some((j) => (j.customerEmails || []).includes(u.email))).length;
  $("#pending-count").textContent = pending ? ` (${pending} waiting)` : "";
  showView("v-jobs");
}

// --------------------------------------------------------------- job edit

async function renderJob(job) {
  current = job;
  const f = $("#f-job");
  f.reset();
  say($("#job-msg"), "");
  $("#job-heading").textContent = job ? job.title : "New job";
  f.title.value = job?.title || "";
  f.address.value = job?.address || "";
  f.status.value = job?.status || "estimate";
  f.statusNote.value = job?.statusNote || "";
  f.paid.checked = !!job?.paid;
  f.emails.value = (job?.customerEmails || []).join("\n");
  $$(".job-only").forEach((el) => { el.hidden = !job; });
  showView("v-job");
  if (!job) return;

  const base = ["jobs", job.id];
  const [ups, files, media] = await Promise.all([
    getDocs(query(collection(db, ...base, "updates"), orderBy("createdAt", "desc"))),
    getDocs(query(collection(db, ...base, "files"), orderBy("createdAt", "desc"))),
    getDocs(query(collection(db, ...base, "media"), orderBy("createdAt", "desc"))),
  ]);
  $("#s-updates").innerHTML = ups.size ? ups.docs.map((d) => { const u = d.data(); return `
    <li><time>${esc(fmtDate(u.createdAt))} · ${esc(u.author)}</time><p>${esc(u.text).replace(/\n/g, "<br>")}</p>
      <button type="button" class="link danger" data-del="updates/${esc(d.id)}">Delete</button></li>`; }).join("")
    : `<li class="muted">No updates yet.</li>`;
  $("#s-files").innerHTML = files.size ? files.docs.map((d) => { const x = d.data(); return `
    <li><button type="button" class="link" data-file="${esc(d.id)}">${esc(x.name)}</button>
      <small>${esc(fmtSize(x.size))} · ${x.byStaff ? "Staff" : "Customer"}: ${esc(x.uploadedBy)} · ${esc(fmtDate(x.createdAt, false))}</small>
      <button type="button" class="link danger" data-del="files/${esc(d.id)}">Remove from portal</button></li>`; }).join("")
    : `<li class="muted">No files yet.</li>`;
  $("#s-media").innerHTML = media.size ? media.docs.map((d) => { const m = d.data(); return `
    <li><a href="https://youtu.be/${esc(m.youtubeId)}" target="_blank" rel="noopener">${esc(m.title)}</a>
      <button type="button" class="link danger" data-del="media/${esc(d.id)}">Delete</button></li>`; }).join("")
    : `<li class="muted">No videos yet.${job.paid ? "" : " Customers see videos once the job is marked paid."}</li>`;

  $$("#v-job [data-file]").forEach((b) => b.addEventListener("click", () =>
    downloadFile(job.id, b.dataset.file).catch((e) => say($("#job-msg"), e.message, "error"))));
  $$("#v-job [data-del]").forEach((b) => b.addEventListener("click", async () => {
    if (!confirm("Delete this item from the portal? (Files stay in the Drive folder.)")) return;
    await deleteDoc(doc(db, ...base, ...b.dataset.del.split("/")));
    renderJob(job);
  }));
}

async function notify(jobId, kind) {
  try {
    const out = await callScript("notify", { jobId, kind });
    return out.sent ? ` Emailed ${out.sent} customer${out.sent === 1 ? "" : "s"}.` : "";
  } catch (e) { return " (Email not sent: " + e.message + ")"; }
}

function initJobForms() {
  $("#f-job").addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const f = ev.target;
    const data = {
      title: f.title.value.trim().slice(0, 140),
      address: f.address.value.trim().slice(0, 200),
      status: f.status.value,
      statusNote: f.statusNote.value.trim().slice(0, 500),
      paid: f.paid.checked,
      customerEmails: parseEmails(f.emails.value),
      updatedAt: serverTimestamp(),
      updatedBy: me(),
    };
    if (!data.title) return say($("#job-msg"), "Give the job a name.", "error");
    busy(f, true);
    try {
      let id = current?.id, added = data.customerEmails;
      if (current) {
        added = data.customerEmails.filter((e) => !(current.customerEmails || []).includes(e));
        await setDoc(doc(db, "jobs", id), { ...data, createdAt: current.createdAt });
      } else {
        id = (await addDoc(collection(db, "jobs"), { ...data, createdAt: serverTimestamp() })).id;
      }
      let extra = "";
      if (added.length && f.notifyLinked.checked) extra = await notify(id, "linked");
      else if (current && current.status !== data.status && f.notifyLinked.checked) extra = await notify(id, "update");
      await loadAll();
      location.hash = id;
      route();
      say($("#job-msg"), "Saved." + extra, "ok");
    } catch (e) { console.error(e); say($("#job-msg"), "Couldn't save: " + e.message, "error"); }
    busy(f, false);
  });

  $("#f-update").addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const f = ev.target, text = f.text.value.trim().slice(0, 4000);
    if (!text) return;
    busy(f, true);
    try {
      await addDoc(collection(db, "jobs", current.id, "updates"), { text, createdAt: serverTimestamp(), author: me() });
      const extra = f.notify.checked ? await notify(current.id, "update") : "";
      f.reset();
      await renderJob(current);
      say($("#job-msg"), "Update posted." + extra, "ok");
    } catch (e) { say($("#job-msg"), "Couldn't post: " + e.message, "error"); }
    busy(f, false);
  });

  $("#f-media").addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const f = ev.target, id = youtubeId(f.url.value);
    if (!id) return say($("#job-msg"), "That doesn't look like a YouTube link.", "error");
    busy(f, true);
    try {
      await addDoc(collection(db, "jobs", current.id, "media"), {
        title: f.title.value.trim().slice(0, 140) || "Project video", youtubeId: id, createdAt: serverTimestamp(),
      });
      const extra = f.notify.checked && current.paid ? await notify(current.id, "media") : "";
      f.reset();
      await renderJob(current);
      say($("#job-msg"), "Video added." + extra, "ok");
    } catch (e) { say($("#job-msg"), "Couldn't add video: " + e.message, "error"); }
    busy(f, false);
  });

  $("#s-up-files").setAttribute("accept", ACCEPT);
  $("#f-s-upload").addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const f = ev.target, list = [...$("#s-up-files").files];
    if (!list.length) return;
    busy(f, true);
    try {
      for (const file of list) {
        say($("#job-msg"), "Uploading " + file.name + "…", "info");
        await uploadFile(current.id, file, true);
      }
      f.reset();
      await renderJob(current);
      say($("#job-msg"), "Uploaded. The customer can download it from the portal.", "ok");
    } catch (e) { say($("#job-msg"), e.message, "error"); }
    busy(f, false);
  });
}

// --------------------------------------------------------------- accounts

function renderAccounts() {
  $("#accounts-body").innerHTML = users.length ? users.map((u) => {
    const linked = jobs.filter((j) => (j.customerEmails || []).includes(u.email));
    return `<tr${linked.length ? "" : ' class="pending"'}>
      <td><strong>${esc(u.name)}</strong><br><small>${esc(u.company || "")}</small></td>
      <td><a href="mailto:${esc(u.email)}">${esc(u.email)}</a><br><small>${esc(u.phone)}</small></td>
      <td><small>${esc(u.propertyAddress)}</small></td>
      <td><small>${esc(fmtDate(u.createdAt, false))}</small></td>
      <td>${linked.length ? linked.map((j) => `<a href="#${esc(j.id)}">${esc(j.title)}</a>`).join("<br>")
        : `<select data-link="${esc(u.email)}" aria-label="Link ${esc(u.email)} to a job">
             <option value="">Link to job…</option>
             ${jobs.map((j) => `<option value="${esc(j.id)}">${esc(j.title)}</option>`).join("")}
           </select>`}</td>
    </tr>`; }).join("") : `<tr><td colspan="5" class="muted">No customer accounts yet.</td></tr>`;
  $$("[data-link]").forEach((s) => s.addEventListener("change", async () => {
    const job = jobs.find((j) => j.id === s.value);
    if (!job || !confirm(`Give ${s.dataset.link} access to "${job.title}" and email them?`)) { s.value = ""; return; }
    const emails = [...new Set([...(job.customerEmails || []), s.dataset.link])].slice(0, 20);
    const { id, ...rest } = job;
    await setDoc(doc(db, "jobs", id), { ...rest, customerEmails: emails, updatedAt: serverTimestamp(), updatedBy: me() });
    const extra = await notify(id, "linked");
    await loadAll();
    renderAccounts();
    say($("#accounts-msg"), "Linked." + extra, "ok");
  }));
  showView("v-accounts");
}

// --------------------------------------------------------------- activity

async function renderActivity() {
  showView("v-activity");
  const snap = await getDocs(query(collection(db, "activity"), orderBy("at", "desc"), limit(200)));
  const title = (id) => jobs.find((j) => j.id === id)?.title || id;
  $("#activity-body").innerHTML = snap.size ? snap.docs.map((d) => { const a = d.data(); return `
    <tr><td><small>${esc(fmtDate(a.at))}</small></td><td>${esc(a.email)}</td>
      <td>${esc(a.type.replace(/_/g, " "))}</td><td>${a.jobId ? esc(title(a.jobId)) : ""}</td></tr>`; }).join("")
    : `<tr><td colspan="4" class="muted">No activity yet.</td></tr>`;
}

// ------------------------------------------------------------------- init

if (!configured) {
  showView("v-setup");
} else {
  $("#job-filter").innerHTML = `<option value="">All statuses</option>` +
    [...STATUSES, ["on_hold", "On hold"]].map(([k, l]) => `<option value="${k}">${l}</option>`).join("");
  $("#f-job").status.innerHTML = [...STATUSES, ["on_hold", "On hold"]]
    .map(([k, l]) => `<option value="${k}">${l}</option>`).join("");
  $("#job-search").addEventListener("input", renderJobs);
  $("#job-filter").addEventListener("change", renderJobs);
  $("#f-signin").addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const f = ev.target;
    busy(f, true); say($("#signin-msg"), "");
    try {
      await setRemember(false);
      await signInWithEmailAndPassword(auth, f.email.value.trim(), f.password.value);
    } catch { say($("#signin-msg"), "That email and password don't match our records.", "error"); }
    busy(f, false);
  });
  $$(".btn-signout").forEach((b) => b.addEventListener("click", () => signOut(auth)));
  initJobForms();
  addEventListener("hashchange", () => auth.currentUser && jobs && route());
  onAuthStateChanged(auth, render);
  idleSignOut(() => auth.currentUser && signOut(auth), 30);
}
