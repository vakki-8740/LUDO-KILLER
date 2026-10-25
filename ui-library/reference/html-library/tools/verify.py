#!/usr/bin/env python3
"""Full verification: HTML structure, ids, links, CSS vars/braces, JS syntax."""
import pathlib
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from urllib.parse import unquote

ROOT = pathlib.Path("/storage/emulated/0/OWN LABRARY")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


class Check(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.ids = []
        self.links = []
        self.scripts = []
        self.styles = []
        self.cur_script = None
        self.cur_style = None
        self.external = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a" and "href" in a:
            self.links.append(a["href"])
        if tag == "script" and "src" in a:
            self.external.append(a["src"])
        if tag == "link" and "href" in a:
            self.external.append(a["href"])
        if tag == "script":
            self.cur_script = []
        elif tag == "style":
            self.cur_style = []
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_startendtag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a" and "href" in a:
            self.links.append(a["href"])

    def handle_endtag(self, tag):
        if tag == "script" and self.cur_script is not None:
            self.scripts.append("".join(self.cur_script))
            self.cur_script = None
            if self.stack and self.stack[-1][0] == "script":
                self.stack.pop()
            return
        if tag == "style" and self.cur_style is not None:
            self.styles.append("".join(self.cur_style))
            self.cur_style = None
            if self.stack and self.stack[-1][0] == "style":
                self.stack.pop()
            return
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append("unexpected </%s> at %s" % (tag, self.getpos()))
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
            return
        self.errors.append("mismatched </%s> at %s, open: %s" % (
            tag, self.getpos(), self.stack[-3:]))
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.cur_script is not None:
            self.cur_script.append(data)
        if self.cur_style is not None:
            self.cur_style.append(data)


def css_vars():
    viewer = (ROOT / "lib" / "viewer.css").read_text(encoding="utf-8")
    return set(re.findall(r"(--[a-zA-Z0-9_-]+)\s*:", viewer))


def strip_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r'"(?:\\.|[^"\\])*"', '""', css)
    css = re.sub(r"'(?:\\.|[^'\\])*'", "''", css)
    return css


def main():
    base_vars = css_vars()
    problems = 0
    js_files = []
    for path in sorted(ROOT.rglob("*.html")):
        if "tools" in path.parts:
            continue
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        c = Check()
        c.feed(text)
        c.close()
        issues = []
        if c.stack:
            issues.append("unclosed tags: %s" % (c.stack,))
        issues.extend(c.errors)
        dups = sorted({x for x in c.ids if c.ids.count(x) > 1})
        if dups:
            issues.append("duplicate ids: %s" % dups)

        for i, style in enumerate(c.styles):
            body = strip_css(style)
            depth = 0
            bad = False
            for ch in body:
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth < 0:
                        bad = True
            if depth != 0 or bad:
                issues.append("CSS brace problem in style#%d" % i)
            defined = set(re.findall(r"(--[a-zA-Z0-9_-]+)\s*:", style))
            used = set(re.findall(r"var\(\s*(--[a-zA-Z0-9_-]+)", style))
            missing = sorted(used - defined - base_vars)
            if missing:
                issues.append("undefined CSS vars: %s" % missing)
        used_html = set(re.findall(r"var\(\s*(--[a-zA-Z0-9_-]+)", text))
        defined_all = base_vars | set(re.findall(r"(--[a-zA-Z0-9_-]+)\s*:", text))
        missing = sorted(used_html - defined_all)
        if missing:
            issues.append("undefined CSS vars in markup: %s" % missing)

        for href in c.links + c.external:
            if href.startswith(("#", "http://", "https://", "mailto:", "tel:", "javascript:")) or not href:
                continue
            target = unquote(href.split("#")[0].split("?")[0])
            if not target:
                continue
            tp = (path.parent / target).resolve()
            if not tp.exists():
                issues.append("broken reference: %s" % href)

        for i, script in enumerate(c.scripts):
            s = script.strip()
            if s:
                js_files.append((str(rel), i, s))

        if issues:
            problems += 1
            print("ISSUES: %s" % rel)
            for x in issues:
                print("   - %s" % x)

    for js_path in sorted(ROOT.rglob("*.js")):
        if "node_modules" in js_path.parts:
            continue
        js_files.append((str(js_path.relative_to(ROOT)), 0, js_path.read_text(encoding="utf-8")))

    tmp = tempfile.mkdtemp(prefix="ownlib_js_")
    js_bad = 0
    for rel, i, s in js_files:
        f = pathlib.Path(tmp) / ("%s_%d.js" % (re.sub(r"[^\w]", "_", rel), i))
        f.write_text(s, encoding="utf-8")
        r = subprocess.run(["node", "--check", str(f)], capture_output=True, text=True)
        if r.returncode != 0:
            js_bad += 1
            print("JS SYNTAX ERROR: %s (script #%d)" % (rel, i))
            print(r.stderr.strip()[:400])

    print("html files checked: %d" % len(list(ROOT.rglob('*.html'))))
    print("files with problems: %d" % problems)
    print("inline scripts checked: %d (failures %d)" % (len(js_files), js_bad))
    return 1 if (problems or js_bad) else 0


if __name__ == "__main__":
    sys.exit(main())
