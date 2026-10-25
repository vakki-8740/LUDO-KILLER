# Phase 1 — Audit of the original OWN LABRARY (HTML version)

Source preserved at `reference/html-library/` (the original 143-file project, untouched).

## What existed before

| Area | Finding |
|---|---|
| Pages | 111 HTML pages — 87 generated from Python specs (`tools/specs/`), 23 legacy hand-written standalone pages + 1 old hand-written `index.html` |
| Components | 97 component blocks across 10 categories; 67 with JS, 30 static |
| Pipeline | `build.py` renders Python specs into `template.html`; `lint_spec.py` + `verify.py` + jsdom `dom_test.js` validate |
| Theming | Light + dark only, via CSS variables in `lib/viewer.css` |
| Viewer features | Desktop/mobile preview toggle, HTML/CSS/JS + Tokens code tabs, copy button, theme toggle |
| Verified state | All original checks pass: lint OK, build OK, verify 0 problems, DOM test 87 pages / 97 blocks / 0 failures; shipped HTML byte-identical to fresh build |

## Issues found in the original

1. `index.html` was stale — it still showed only 23 legacy components while `_cards.json` already described 87.
2. Hardcoded Termux path (`/storage/emulated/0/OWN LABRARY`) in all three tool scripts.
3. Hinglish copy in ~15 notes despite the "English copy" spec rule.
4. Search-bar spec injected user input via `innerHTML` (XSS-prone pattern).
5. No multi-theme system, no search/favorites/recent browsing, no tablet preview.
6. jsdom DOM test pinned to an old jsdom API (`ResourceLoader` removed in jsdom v26).

## Upgrade scope decisions

- Build a new React + Vite app **alongside** the original (`ui-library/`), preserving the original project in `reference/` — nothing removed or redesigned.
- Keep the exact design identity: same light/dark token values, 6px radius, system font stack, checkerboard preview stage.
- Every React component consumes only CSS variables, so the expanded 12-theme system propagates everywhere.
- Code-copy shows the **real source files** via Vite `?raw` imports — snippets can never drift from the shipped code.

## Coverage after upgrade

70 catalog entries / 88 live variants across 12 categories (see `README.md` for the full list).
All requested feature groups (A–J from the brief) are represented with working, interactive components.

## Remaining backlog (not yet ported — tracked honestly)

These existed in the HTML library or were requested but are not React components yet; the architecture
(`src/categories/*.jsx` + co-located component folders) makes each one a drop-in addition:

- Navigation: mega menu, hamburger drawer page, standalone sidebar component
- Layout: masonry, infinite-scroll feed, fullscreen modal layout
- Forms: date/time/color pickers, multi-select chips, autocomplete, email/phone combo
- Overlays: bottom sheet, context menu, fullscreen modal, image zoom, video player
- Auth: email verify, reset-password screen, profile settings, change-password screens
- Dashboard: admin panel, settings panel, file manager, full chat page (shell pieces exist)
- E-commerce: invoice, order tracker, product details page, review cards, product filters
- Data: comparison table, lightbox gallery (gallery exists), nested tabs
- Design-system showcase page: gradient/shadow/border/spacing token gallery
