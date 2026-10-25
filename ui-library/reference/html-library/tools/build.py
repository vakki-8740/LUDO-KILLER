#!/usr/bin/env python3
import html
import importlib.util
import json
import pathlib
import re
import sys

ROOT = pathlib.Path("/storage/emulated/0/OWN LABRARY")
TOOLS = ROOT / "tools"
SPECS = TOOLS / "specs"
TEMPLATE = (TOOLS / "template.html").read_text(encoding="utf-8")

FORBIDDEN_JS = ["document.write", "eval(", "new Function"]
SCOPED_OK = re.compile(r"(:root|@media|@keyframes|@supports|@font-face|@import|@container)")
BARE_SELECTOR = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9]*|#[a-zA-Z][\w-]*|\*)$")


def err(msg):
    raise SystemExit("BUILD ERROR: " + msg)


def clean_js(js):
    js = js.rstrip()
    if not js:
        return ""
    for bad in FORBIDDEN_JS:
        if bad in js:
            err("JS contains forbidden construct: %s" % bad)
    js = js.replace("</script", "<\\/script")
    if js.lstrip().startswith("(function"):
        return js
    indented = "\n".join(("  " + ln) if ln.strip() else ln for ln in js.split("\n"))
    return "(function () {\n\"use strict\";\n%s\n})();" % indented


def clean_css(css):
    css = css.rstrip()
    if "</style" in css:
        err("CSS must not contain '</style'")
    return css


def lint_css(css, where):
    body = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    for block in re.findall(r"@media[^{]*\{|@supports[^{]*\{|@container[^{]*\{", body):
        body = body.replace(block, "{", 1)
    depth = 0
    sel_buf = ""
    for ch in body:
        if ch == "{":
            if depth == 0:
                for sel in sel_buf.split(","):
                    sel = sel.strip()
                    if sel and not SCOPED_OK.search(sel) and BARE_SELECTOR.match(sel):
                        err("%s: unscoped selector %r (selectors must use a component class)" % (where, sel))
                    if sel.startswith("@"):
                        continue
            sel_buf = ""
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                err("%s: extra '}' in CSS" % where)
            sel_buf = ""
        elif depth == 0:
            sel_buf += ch
    if depth != 0:
        err("%s: unbalanced CSS braces" % where)


def load_specs():
    pages = []
    for path in sorted(SPECS.glob("*.py")):
        if path.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(path.stem, path)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception as e:
            err("%s failed to load: %s" % (path.name, e))
        cat = getattr(mod, "CAT", None)
        cat_id = getattr(mod, "CAT_ID", None)
        cat_desc = getattr(mod, "CAT_DESC", "")
        for page in getattr(mod, "PAGES", []):
            page["_cat"] = page.get("cat") or cat
            page["_cat_id"] = page.get("cat_id") or cat_id
            page["_cat_desc"] = page.get("cat_desc") or cat_desc
            page["_spec"] = path.name
            pages.append(page)
    return pages


def render_block(block, page):
    where = "%s/%s#%s" % (page["_spec"], page["slug"], block.get("id", "?"))
    for key in ("id", "title", "html", "css"):
        if key not in block:
            err("%s missing block key %r" % (where, key))
    css = clean_css(block["css"])
    lint_css(css, where)
    js = clean_js(block.get("js", "").strip())
    note = block.get("note", "")
    note_html = '<span class="vw-note">%s</span>' % html.escape(note) if note else ""
    bid = block["id"]
    return (
        '  <section class="vw-block" id="{bid}" aria-labelledby="{bid}-t">\n'
        '    <div class="vw-bhead">\n'
        '      <h2 class="vw-btitle" id="{bid}-t">{title}</h2>\n'
        '      {note}\n'
        '      <div class="vw-tools">\n'
        '        <div class="vw-seg" role="group" aria-label="Preview size">\n'
        '          <button type="button" data-size="desktop" aria-pressed="true">Desktop</button>\n'
        '          <button type="button" data-size="mobile" aria-pressed="false">Mobile</button>\n'
        '        </div>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="vw-stage">\n'
        '      <p class="vw-mobile-tag">Mobile preview · 375px</p>\n'
        '      <div class="vw-stage-inner">\n'
        '        <div class="vw-frame">\n'
        '{html}\n'
        '        </div>\n'
        '      </div>\n'
        '    </div>\n'
        '    <style data-block>{css}</style>\n'
        '    <script data-block>{js}</script>\n'
        '  </section>'
    ).format(bid=bid, title=html.escape(block["title"]), note=note_html,
             html=block["html"].rstrip(), css=css, js=js)


def render_page(page):
    for key in ("folder", "slug", "title", "desc", "blocks"):
        if key not in page:
            err("%s missing page key %r" % (page.get("_spec", "?"), key))
    ids = [b.get("id") for b in page["blocks"]]
    if len(ids) != len(set(ids)):
        err("%s/%s has duplicate block ids" % (page["_spec"], page["slug"]))
    if "/" in page["folder"] or page["folder"].startswith(".."):
        err("folder must be a single level: %r" % page["folder"])
    blocks = "\n\n".join(render_block(b, page) for b in page["blocks"])
    out = (TEMPLATE
           .replace("{{TITLE}}", html.escape(page["title"]))
           .replace("{{CAT}}", html.escape(page["_cat"] or ""))
           .replace("{{DESC}}", html.escape(page["desc"]))
           .replace("{{BLOCKS}}", blocks))
    folder = ROOT / page["folder"]
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / (page["slug"] + ".html")
    target.write_text(out, encoding="utf-8")
    return "%s/%s.html" % (page["folder"], page["slug"])


def build_index_cards(pages):
    cards = []
    sections = {}
    for page in pages:
        href = "%s/%s.html" % (page["folder"], page["slug"])
        mini = page.get("mini", "")
        if not mini:
            err("%s: missing mini" % page["slug"])
        desc = page.get("idx_desc") or page["desc"]
        if not page.get("_cat_id"):
            err("%s: spec missing CAT_ID" % page["slug"])
        if page.get("_cat_desc"):
            sections.setdefault(page["_cat_id"], {"label": page["_cat"], "desc": page["_cat_desc"]})
        cards.append({"cat": page["_cat_id"], "href": href, "title": page["title"],
                      "desc": desc, "mini": mini})
        for extra in page.get("more_cards", []):
            cards.append({"cat": page["_cat_id"],
                          "href": "%s/%s.html#%s" % (page["folder"], page["slug"], extra["id"]),
                          "title": extra["title"], "desc": extra["desc"],
                          "mini": extra.get("mini", "")})
    payload = {"cards": cards, "sections": sections}
    (TOOLS / "_cards.json").write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return cards, sections


def main():
    pages = load_specs()
    if not pages:
        err("no specs found in tools/specs/")
    made = []
    seen = {}
    for page in pages:
        key = "%s/%s.html" % (page["folder"], page["slug"])
        if key in seen:
            err("duplicate page target %s (%s and %s)" % (key, seen[key], page["_spec"]))
        seen[key] = page["_spec"]
        made.append(render_page(page))
    cards, sections = build_index_cards(pages)
    print("pages built: %d" % len(made))
    print("index cards: %d" % len(cards))
    cats = {}
    for c in cards:
        cats[c["cat"]] = cats.get(c["cat"], 0) + 1
    for k in sorted(cats):
        print("  %-14s %d" % (k, cats[k]))
    if sections:
        print("new sections: %s" % ", ".join(sorted(sections)))


if __name__ == "__main__":
    main()
