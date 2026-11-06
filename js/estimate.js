// Contact-page estimate form. Sends to the Rocklane Apps Script, which emails the office.
import { SCRIPT_URL } from "/portal/config.js";

const form = document.getElementById("f-estimate");
const msg = document.getElementById("estimate-msg");
const started = Date.now();

if (/^https:\/\/script\.google\.com\/macros\/s\/[\w-]+\/exec$/.test(SCRIPT_URL)) {
  form.hidden = false;
  document.getElementById("estimate-fallback").hidden = true;
}

function show(text, kind) { msg.hidden = false; msg.className = "notice notice-" + kind; msg.textContent = text; }

form.addEventListener("submit", async (ev) => {
  ev.preventDefault();
  if (!form.reportValidity()) return;
  const data = Object.fromEntries(new FormData(form));
  data.action = "estimate";
  data.elapsedMs = Date.now() - started;
  const btn = form.querySelector("button");
  btn.disabled = true;
  try {
    const res = await fetch(SCRIPT_URL, { method: "POST", headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify(data), redirect: "follow" });
    const out = await res.json();
    if (!out.ok) throw new Error(out.error);
    form.reset();
    show("Thank you. We received your request and emailed you a confirmation. Our team will contact you within one business day.", "ok");
  } catch (e) {
    show((e && e.message) || "We couldn't send your request. Please call (317) 898-8696.", "error");
  }
  btn.disabled = false;
});
