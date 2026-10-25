# Component spec format — OWN UI Design Library

You write ONE Python file: `tools/specs/<your-file>.py`. Nothing else.
The build script (`tools/build.py`) turns specs into real standalone pages.

## File anatomy

```python
CAT = "Forms & Inputs"          # topbar badge text on generated pages
CAT_ID = "forms"                # index section the cards go into (see mapping below)
CAT_DESC = ""                   # ONLY for NEW sections (see mapping); else omit

PAGES = [
    {
        "folder": "forms",      # folder inside the library (single level, no slashes)
        "slug": "search-bar",   # page file: forms/search-bar.html
        "title": "Search Bar",
        "desc": "One-line description shown under the page heading.",
        "idx_desc": "Short card text for the library index.",
        "mini": '<div class="p-row" style="gap: 6px;"><div class="p-search"><i></i><span></span></div></div>',
        "blocks": [
            {
                "id": "search-bar",       # unique anchor id in this page
                "title": "Search bar",
                "note": "optional small note shown next to the title",
                "html": "...component markup only...",
                "css": "...component css...",
                "js": "...component js (optional)...",
            },
        ],
        "more_cards": [          # optional: extra index cards linking to blocks of this page
            {"id": "other-block", "title": "Other Thing", "desc": "…", "mini": "…"},
        ],
    },
]
```

Per-page override keys (rarely needed): `"cat"`, `"cat_id"`, `"cat_desc"`.

## Index section mapping (`CAT_ID`)

| CAT_ID    | status         | when to use |
|-----------|----------------|-------------|
| navigation | existing      | nav components (CAT_DESC omit) |
| layout     | existing      | layout components (omit) |
| interactive| existing      | buttons / actions (omit) |
| forms      | existing      | form components (omit) |
| feedback   | existing      | feedback components (omit) |
| data       | NEW section   | data display — set CAT_DESC |
| overlays   | NEW section   | overlays — set CAT_DESC |
| auth       | NEW section   | auth UI — set CAT_DESC |
| dashboard  | NEW section   | dashboard/app UI — set CAT_DESC |
| ecommerce  | NEW section   | e-commerce — set CAT_DESC |
| system     | NEW section   | design system — set CAT_DESC |

Folders used by convention: `navigation`, `layout`, `buttons`, `forms`, `feedback`,
`data`, `overlays`, `auth`, `dashboard`, `ecommerce`, `system`.

## Design tokens (the ONLY shared CSS variables)

```
--bg, --card, --text, --muted, --border, --shadow, --accent, --accent-soft,
--yes, --no, --warn, --track-off, --radius
```
Light values: `#f4f5f7 #ffffff #1f2430 #6b7280 #e5e7eb 0 8px 30px rgba(0,0,0,.08) #4f6bed rgba(79,107,237,.10) #22a06b #e5484d #c2740a #d8dce3 6px`
Dark values are provided automatically by the library theme.
Never hardcode page background/text colors — always use tokens so dark mode works.
Component-specific vars (e.g. `--sb-w`) are allowed but define them on a component class, not `:root`.

## CSS rules (build lints these)

1. **No code comments.**
2. **Every selector must contain a class** — no bare `body`, `html`, `*`, `button`, `input` etc.
3. **Prefix every class** with your component prefix (e.g. `sb-` for search bar, `mm-` mega menu).
   Never use the `vw-` prefix — reserved for the viewer.
4. Looks good standalone inside a padded stage: give panels `background: var(--card); border: 1px solid var(--border); border-radius: 6px`.
5. Must not overflow at **360px** width; add scoped `@media (max-width: 640px)` rules when needed.
6. Visible `:focus-visible` styles on every interactive element.
7. No external resources: no `@import`, no remote `url()`, no web fonts.

## HTML rules

1. `html` = **only component markup** (no `<html>`, `<head>`, `<body>`, `<style>`, `<script>`, no `<img>`).
2. Icons = inline SVG (`stroke="currentColor"`, 1.5–2 width), `aria-hidden="true"` when decorative.
   Icon-only buttons need `aria-label`.
3. Copy language: **English**, realistic (names like Aman Kumar, prices like ₹1,240 / $49).
4. Semantic markup + ARIA: `role="tablist"` for tabs, `aria-expanded` for menus, `aria-live="polite"` for toasts, labels tied to inputs (`<label for>`).
5. Prefer **static markup** that JS only enhances. If JS builds markup, the container starts empty and JS must be idempotent (`el.innerHTML = …` on every run) — the viewer snapshots HTML at load.

## JS rules

1. **No comments**, plain modern JS, no libraries/frameworks/CDN.
2. No `document.write`, `eval`, `new Function`.
3. Anything user-typed → render with `textContent`, never `innerHTML`.
4. Keyboard: Enter/Space activate buttons/toggles, Escape closes menus/sheets/dialogs, Arrow keys move within tabs/lists where natural. Keep `aria-*` in sync.
5. Scope queries with your prefixed ids/classes; multiple components share a page.
6. Do NOT write theme/dark-mode code — the library handles it.
7. Build wraps your JS in an IIFE automatically — write top-level code as-is.

## Thumbnail (`mini`) for the library index

Raw inner HTML placed inside `<div class="thumb">` (about 160×96 box).
No text except where noted, no links, no scripts, no images.

Available classes in `index.html`:

- boxes/lines: `p-row` (flex wrapper, use inline `style="gap: Npx"`), `p-row-tight`, `p-line` (inline width via `style="width:40px"`), `p-pill`, `p-box`, `p-tile`, `p-tiles` (3-up grid), `p-logo`, `p-label`, `p-field`, `p-input`
- nav: `p-nav`, `p-sidebar`, `p-frame` (sidebar+content), `p-footer`, `p-burger` (+`accent`, `x`), `p-crumb`, `p-slash`, `p-page` (+`arrow`, `active`), `p-drop`
- controls: `p-btn` (+`accent`, `ghost`), `p-iconbtn` (+`filled`, `soft`) with `p-glyph`, `p-check` (+`on`), `p-radio` (+`on`), `p-toggle` (+`on` with `p-knob`), `p-fab`, `p-slider`? (no — use `p-line`), `p-field`+`p-input`+`p-label` for forms
- feedback: `p-alert` (+`p-adot` inside), `p-badge` (+`p-bdot` inside), `p-tooltip`/`p-tipbtn`/`p-tipstage`, `p-spinner`, `p-dots` (3 spans), `p-modal-stage`>`p-modal-card`
- data: `p-avatar`, `p-avgroup` (4 `<i>`), `p-mini-card`, `p-mini-img`, `p-listrow`, `p-table` (3 `<span>`), `p-bars` (4 `<span>`), `p-bubble` (3 `<span>`), `p-steps` (`<i>`+`<b>` alternating, `done` class), `p-tl` (3 `<span>`), `p-gal` (4 `<span>`), `p-cal` (with inner `<span>`), `p-money` (2 `<span>` + `<strong>`)
- misc: `p-upload` (with inner `<span>`), `p-search` (`<i></i><span></span>`), `p-avatar`

Composition example:

```python
"mini": '<div class="p-row" style="gap: 7px;"><span class="p-avatar"></span><span class="p-avatar"></span><span class="p-avatar"></span></div>'
```

## Multi-block pages

Put several related components on one page (each block = own preview + code + copy).
Give each a unique `id`. Extra index cards via `more_cards`.

## Self-check (run this; it writes nothing)

```bash
cd /storage/emulated/0/OWN\ LABRARY && python3 tools/lint_spec.py tools/specs/<your-file>.py
```

Must print `LINT OK`. Do NOT run `tools/build.py` (the orchestrator builds after collecting all specs).
