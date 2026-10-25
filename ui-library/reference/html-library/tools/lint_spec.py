#!/usr/bin/env python3
"""Lint a single spec file without writing any pages.

Usage: python3 tools/lint_spec.py tools/specs/<file>.py
"""
import importlib.util
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build as B


def lint_mini(mini, where):
    if not isinstance(mini, str) or not mini.strip():
        B.err("%s: mini must be a non-empty string" % where)
    low = mini.lower()
    for bad in ("<script", "<style", "<html", "http://", "https://", "src="):
        if bad in low:
            B.err("%s: mini must not contain %r" % (where, bad))
    if "<a " in low or "href=" in low:
        B.err("%s: mini must not contain links" % where)


def lint_page(page, spec_name):
    where = "%s/%s" % (spec_name, page.get("slug", "?"))
    for key in ("folder", "slug", "title", "desc", "mini", "blocks"):
        if key not in page:
            B.err("%s: missing page key %r" % (where, key))
    if not re.fullmatch(r"[a-z0-9-]+", page["slug"]):
        B.err("%s: slug must be lowercase-dash" % where)
    if not re.fullmatch(r"[a-z0-9-]+", page["folder"]):
        B.err("%s: folder must be lowercase-dash" % where)
    lint_mini(page["mini"], where)
    if not page.get("idx_desc") and not page.get("desc"):
        B.err("%s: needs idx_desc or desc" % where)
    ids = []
    for block in page["blocks"]:
        bwhere = "%s#%s" % (where, block.get("id", "?"))
        for key in ("id", "title", "html", "css"):
            if key not in block:
                B.err("%s: missing block key %r" % (bwhere, key))
        ids.append(block["id"])
        if not block["html"].strip():
            B.err("%s: html is empty" % bwhere)
        if "<html" in block["html"].lower() or "<body" in block["html"].lower():
            B.err("%s: html must be component markup only" % bwhere)
        if "<style" in block["html"].lower() or re.search(r"<script", block["html"], re.I):
            B.err("%s: html must not include style/script tags" % bwhere)
        if re.search(r"<img\b", block["html"], re.I):
            B.err("%s: no <img> — use inline SVG or CSS" % bwhere)
        if re.search(r"url\(\s*['\"]?https?:", block["css"], re.I):
            B.err("%s: css must not load remote urls" % bwhere)
        if "@import" in block["css"] or "@font-face" in block["css"]:
            B.err("%s: no @import/@font-face" % bwhere)
        css = B.clean_css(block["css"])
        B.lint_css(css, bwhere)
        js = block.get("js", "")
        if js:
            B.clean_js(js)
    if len(ids) != len(set(ids)):
        B.err("%s: duplicate block ids" % where)
    for card in page.get("more_cards", []):
        for key in ("id", "title", "desc", "mini"):
            if key not in card:
                B.err("%s: more_cards missing %r" % (where, key))
        lint_mini(card["mini"], where + "/more_cards")
        if card["id"] not in ids:
            B.err("%s: more_cards id %r not a block id" % (where, card["id"]))


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        raise SystemExit(2)
    path = pathlib.Path(sys.argv[1]).resolve()
    if not path.exists():
        B.err("no such file: %s" % path)
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    pages = getattr(mod, "PAGES", None)
    if not isinstance(pages, list) or not pages:
        B.err("%s: PAGES must be a non-empty list" % path.name)
    cat_id = getattr(mod, "CAT_ID", None)
    for page in pages:
        if not page.get("cat_id") and not cat_id:
            B.err("%s: page %r has no cat_id (set CAT_ID or page['cat_id'])" % (
                path.name, page.get("slug")))
        lint_page(page, path.name)
    total = sum(len(p["blocks"]) for p in pages)
    print("LINT OK · %s · %d pages · %d blocks" % (path.name, len(pages), total))


if __name__ == "__main__":
    main()
