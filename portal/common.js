// Shared helpers for the Rocklane Co. customer portal and staff pages.
import { firebaseConfig, SCRIPT_URL } from "./config.js";
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import {
  getAuth, setPersistence, browserLocalPersistence, browserSessionPersistence,
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
import {
  getFirestore, collection, addDoc, serverTimestamp,
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

export const configured = !/REPLACE_/.test(firebaseConfig.apiKey + firebaseConfig.projectId);
export const scriptConfigured = /^https:\/\/script\.google\.com\/macros\/s\/[\w-]+\/exec$/.test(SCRIPT_URL);

export let auth = null, db = null;
if (configured) {
  const app = initializeApp(firebaseConfig);
  auth = getAuth(app);
  db = getFirestore(app);
}

export const PHONE = "(317) 898-8696";
export const MAX_UPLOAD = 25 * 1024 * 1024;

export const STATUSES = [
  ["estimate", "Estimate"],
  ["approved", "Approved"],
  ["scheduled", "Scheduled"],
  ["in_progress", "In progress"],
  ["final_walkthrough", "Final walkthrough"],
  ["complete", "Complete"],
];
export const STATUS_LABEL = Object.fromEntries([...STATUSES, ["on_hold", "On hold"]]);

export const $ = (sel, root = document) => root.querySelector(sel);
export const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

export function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

/** Shows exactly one `.view` inside root. */
export function showView(id, root = document) {
  $$(".view", root).forEach((v) => { v.hidden = v.id !== id; });
  const h = $("#" + id + " h1, #" + id + " h2", root);
  if (h) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: false }); }
}

/** Message box: kind = "ok" | "error" | "info". Empty msg hides it. */
export function say(el, msg, kind = "info") {
  if (!el) return;
  el.hidden = !msg;
  el.className = "notice notice-" + kind;
  el.textContent = msg || "";
}

/** Formats a Firestore Timestamp/Date in Eastern time. */
export function fmtDate(ts, withTime = true) {
  if (!ts) return "";
  const d = ts.toDate ? ts.toDate() : new Date(ts);
  const opts = { timeZone: "America/New_York", month: "short", day: "numeric", year: "numeric" };
  if (withTime) Object.assign(opts, { hour: "numeric", minute: "2-digit", timeZoneName: "short" });
  return d.toLocaleString("en-US", opts);
}

export function fmtSize(n) {
  if (n >= 1048576) return (n / 1048576).toFixed(1) + " MB";
  return Math.max(1, Math.round(n / 1024)) + " KB";
}

export function setRemember(remember) {
  return setPersistence(auth, remember ? browserLocalPersistence : browserSessionPersistence);
}

/** Calls the Apps Script web app. Sends text/plain so the browser skips a CORS preflight. */
export async function callScript(action, payload = {}, withToken = true) {
  if (!scriptConfigured) throw new Error("This feature is not set up yet. Please call " + PHONE + ".");
  const body = { action, ...payload };
  if (withToken) body.idToken = await auth.currentUser.getIdToken();
  const res = await fetch(SCRIPT_URL, {
    method: "POST",
    headers: { "Content-Type": "text/plain;charset=utf-8" },
    body: JSON.stringify(body),
    redirect: "follow",
  });
  let out;
  try { out = await res.json(); } catch { out = { ok: false }; }
  if (!out.ok) throw new Error(out.error || "Something went wrong. Please call " + PHONE + ".");
  return out;
}

const TYPE_BY_EXT = {
  jpg: "image/jpeg", jpeg: "image/jpeg", png: "image/png", gif: "image/gif", webp: "image/webp",
  heic: "image/heic", heif: "image/heif", pdf: "application/pdf", txt: "text/plain",
  doc: "application/msword",
  docx: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
  xls: "application/vnd.ms-excel",
  xlsx: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
};
export const ACCEPT = Object.keys(TYPE_BY_EXT).map((e) => "." + e).join(",");

export function fileType(file) {
  const ext = (file.name.split(".").pop() || "").toLowerCase();
  return TYPE_BY_EXT[ext] || "";
}

function toBase64(file) {
  return new Promise((resolve, reject) => {
    const r = new FileReader();
    r.onload = () => resolve(String(r.result).split(",")[1] || "");
    r.onerror = () => reject(new Error("Could not read " + file.name + "."));
    r.readAsDataURL(file);
  });
}

/** Uploads one file to the job's private Drive folder and records it in Firestore. */
export async function uploadFile(jobId, file, byStaff) {
  const mimeType = fileType(file);
  if (!mimeType) throw new Error(file.name + ": please upload photos, PDFs, Word or Excel files.");
  if (file.size > MAX_UPLOAD) throw new Error(file.name + " is larger than 25 MB.");
  const data = await toBase64(file);
  const out = await callScript("upload", { jobId, name: file.name, mimeType, data });
  await addDoc(collection(db, "jobs", jobId, "files"), {
    name: out.name, size: out.size, mimeType, driveFileId: out.driveFileId,
    uploadedBy: auth.currentUser.email.toLowerCase(), byStaff, createdAt: serverTimestamp(),
  });
  logActivity("upload", jobId);
}

/** Downloads a file through the Apps Script and saves it in the browser. */
export async function downloadFile(jobId, fileDocId) {
  const out = await callScript("download", { jobId, fileDocId });
  const bytes = Uint8Array.from(atob(out.data), (c) => c.charCodeAt(0));
  const url = URL.createObjectURL(new Blob([bytes], { type: out.mimeType }));
  const a = document.createElement("a");
  a.href = url; a.download = out.name; document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 30000);
  logActivity("download", jobId);
}

/** Append-only audit trail; failures never block the user. */
export function logActivity(type, jobId = "") {
  const u = auth && auth.currentUser;
  if (!u || !u.emailVerified) return;
  addDoc(collection(db, "activity"), {
    type, jobId, email: u.email.toLowerCase(), at: serverTimestamp(),
  }).catch(() => {});
}

/** Extracts an 11-character YouTube video ID from a link or a bare ID. */
export function youtubeId(input) {
  const s = String(input || "").trim();
  if (/^[A-Za-z0-9_-]{11}$/.test(s)) return s;
  try {
    const u = new URL(s);
    if (/(^|\.)youtu\.be$/.test(u.hostname)) return u.pathname.slice(1, 12);
    if (/(^|\.)youtube(-nocookie)?\.com$/.test(u.hostname)) {
      if (u.searchParams.get("v")) return u.searchParams.get("v").slice(0, 11);
      const m = u.pathname.match(/\/(embed|shorts|live)\/([A-Za-z0-9_-]{11})/);
      if (m) return m[2];
    }
  } catch { /* not a URL */ }
  return "";
}

/** Signs the user out after 60 minutes without activity (shared computers). */
export function idleSignOut(onSignOut, minutes = 60) {
  let t;
  const reset = () => { clearTimeout(t); t = setTimeout(onSignOut, minutes * 60000); };
  ["click", "keydown", "scroll", "touchstart"].forEach((e) =>
    addEventListener(e, reset, { passive: true }));
  reset();
}
