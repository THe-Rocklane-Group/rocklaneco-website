"""Quick checks for the generated site. Run after build:  python tools/check_site.py

1. Every class used by portal/*.html, js/*.js and portal/*.js is defined in css/style.css
   (or in a page's inline <style>).
2. Every class used in any generated page is defined (warns only; utility hooks are allowed).
3. Each page has exactly one <h1>; no banned words; every /images /css /js reference resolves.
"""
import glob, os, re, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
os.chdir(ROOT)

css = open("css/style.css", encoding="utf-8").read()
css_nocomment = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
defined = set(re.findall(r"\.(-?[_a-zA-Z][\w-]*)", re.sub(r"url\([^)]*\)", "", css_nocomment)))

# Classes JS adds or that only matter as JS hooks / state (no style needed).
HOOKS = {"open", "in", "js-reveal", "scrolled", "menu-open", "reveal", "auth-form", "btn-signout",
         "job-only", "view", "i", "u", "b", "who", "c1", "c2", "c3", "c4"}


def classes_in_html(text):
    out = set()
    for m in re.finditer(r'class="([^"]*)"', text):
        val = re.sub(r"\$\{[^}]*\}", " ", m.group(1))
        out.update(c for c in val.split() if re.match(r"^[_a-zA-Z][\w-]*$", c))
    return out


def classes_in_js(text):
    out = classes_in_html(text)
    for m in re.finditer(r'class(?:Name)?\s*=\s*["\']([^"\']+)["\']', text):
        out.update(m.group(1).split())
    out = {c for c in out if re.match(r"^[_a-zA-Z][\w-]*\w$", c)}
    for m in re.finditer(r"classList\.(?:add|remove|toggle|contains)\(\s*['\"]([\w-]+)", text):
        out.add(m.group(1))
    for m in re.finditer(r"querySelector(?:All)?\(\s*['\"]([^'\"]+)", text):
        out.update(re.findall(r"\.([_a-zA-Z][\w-]*)", m.group(1)))
    for m in re.finditer(r'\$\$?\(\s*["\']([^"\']+)', text):
        out.update(re.findall(r"\.([_a-zA-Z][\w-]*)", m.group(1)))
    for m in re.finditer(r'"notice notice-" \+ kind', text):
        out.update({"notice"})
    if "status-${" in text:
        out.update({"status-complete", "status-in_progress", "status-scheduled", "status-on_hold"})
    for m in re.finditer(r'notice-(ok|error|info)', text):
        out.add("notice-" + m.group(1))
    return out


fail = []
critical = set()
for f in glob.glob("portal/*.html"):
    critical |= classes_in_html(open(f, encoding="utf-8").read())
for f in glob.glob("js/*.js") + glob.glob("portal/*.js"):
    critical |= classes_in_js(open(f, encoding="utf-8").read())
missing = sorted(c for c in critical - defined - HOOKS)
if missing:
    fail.append("classes used by portal/estimate/site scripts but not in style.css: " + ", ".join(missing))

pages = [f for f in glob.glob("*.html") + glob.glob("portal/*.html")
         if 'http-equiv="refresh"' not in open(f, encoding="utf-8").read()]
warn = set()
BANNED = re.compile(r"\b(cheap|discount|deal|unbeatable|best-in-class|family-owned)\b", re.I)
for f in pages:
    t = open(f, encoding="utf-8").read()
    page_css = " ".join(re.findall(r"<style>(.*?)</style>", t, re.S))
    page_defined = defined | set(re.findall(r"\.(-?[_a-zA-Z][\w-]*)", page_css))
    for c in classes_in_html(t) - page_defined - HOOKS:
        warn.add(f"{f}: .{c}")
    h1 = len(re.findall(r"<h1[\s>]", t))
    if h1 != 1:
        fail.append(f"{f}: {h1} <h1> elements")
    visible = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
    visible = re.sub(r"<[^>]+>", " ", visible)
    # GAF's own disclosure text contains "discounts"; it is required verbatim.
    visible = visible.replace("discounts on marketing tools from GAF", "")
    for m in BANNED.finditer(visible):
        fail.append(f"{f}: banned word '{m.group(0)}'")
    for ref in re.findall(r'(?:src|href|srcset|imagesrcset)="([^"]+)"', t):
        for part in ref.split(","):
            u = part.strip().split(" ")[0]
            if re.match(r"^/(images|css|js|portal)/", u):
                if not os.path.exists(u.lstrip("/").split("#")[0].split("?")[0]):
                    fail.append(f"{f}: missing file {u}")
    if "fn-ref" in t and 'id="fn-1"' not in t:
        fail.append(f"{f}: footnote marker without footnote")

for w in sorted(warn):
    print("warn  undefined class", w)
for x in fail:
    print("FAIL ", x)
print("checked", len(pages), "pages;", len(critical), "script/portal classes;", "OK" if not fail else f"{len(fail)} failures")
sys.exit(1 if fail else 0)
