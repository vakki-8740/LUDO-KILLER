# OWN Library — Personal UI Design Library (React + Vite)

A complete, themeable, reusable component library with a built-in browsing application.
Every component is a real, interactive React component with co-located CSS — copy the JSX and CSS
straight into another project. No UI framework, no icon font, no remote assets.

The original HTML/Python version is preserved untouched under `reference/html-library/`.

## Quick start

```bash
npm install
npm run dev        # http://localhost:5173
npm run build      # production build in dist/
npm run smoke      # SSR render tests for every component + every route
```

## What is included

- **70 components, 88 live variants, 12 categories** — see `src/data/catalog.js`
- **12 themes** (Dark is permanent): Light, Dark, Blue, Sky Blue, Green, Purple, Pink,
  Orange, Red, Teal, Black, White — switcher in the top bar, persisted to `localStorage`
- **Library app**: global search (`/` shortcut), category filter, sorting, favorites,
  recently viewed, mobile/tablet/desktop preview switcher, JSX/CSS/Tokens code copy,
  props tables, keyboard navigation, Suspense loading state and an error boundary
- **Design tokens**: colors, typography, spacing, radius, shadows, z-index, motion —
  centralized in `src/styles/tokens.css`

## Architecture

```
src/
├── components/
│   ├── ui/            # the reusable components, one folder each (jsx + co-located css)
│   │   ├── button/ input/ feedback/ navigation/ layout/ data/
│   │   ├── overlays/ auth/ dashboard/ ecommerce/ social/ marketing/ icons/
│   ├── viewer/        # ComponentStage (preview + sizes) and CodePanel (copy source)
│   └── layout/        # app chrome: AppLayout, sidebar, topbar, theme switcher, cards
├── categories/        # catalog registries per category (metadata, variants, props, ?raw sources)
├── data/              # catalog.js (selectors/search/sort) and categories.js
├── pages/             # Home, All components, Category, Search, Favorites, Recent, Detail
├── state/             # Theme / Favorites / Recent React contexts (localStorage-backed)
├── themes/themes.js   # theme registry for the switcher
├── styles/            # tokens.css (all 12 themes) + global.css
├── hooks/ utils/      # useDebouncedValue, clipboard helper
└── scripts/           # SSR smoke tests (run via npm run smoke:*)
```

### Data flow

`src/categories/*.jsx` registers each component once: title, description, keywords,
rendered variant nodes, props documentation, and the component's real source imported
with Vite's `?raw` suffix. `src/data/catalog.js` merges the registries and powers search,
sorting, routing and the home page. Add a component = add one folder under `components/ui`
and one entry in the matching category file.

## Theme system

All component colors reference CSS variables (`--accent`, `--card`, `--border`, …).
A theme is one `[data-theme='id'] { … }` block in `tokens.css` plus one row in
`themes/themes.js`. Components never hardcode hex colors, so a new theme reaches every
component automatically. Contrast is tuned per theme (e.g. `--on-accent` flips for the
monochrome Black theme).

## Adding a component

1. Create `src/components/ui/<group>/<Name>/` with `Name.jsx` and `Name.css`
   (use only `var(--…)` tokens, inline SVG icons from `icons/Icons.jsx`).
2. Register it in the matching `src/categories/<group>.jsx` with variants, props and
   `?raw` source imports — the detail page, search, favorites and copy-code work automatically.
3. Run `npm run smoke` to verify every variant renders.

## Testing

- `npm run build` — Vite production build (fails on any import/transform error)
- `npm run smoke:catalog` — server-renders all 88 variants inside all providers,
  validates unique ids, known categories and non-empty JSX/CSS sources
- `npm run smoke:pages` — server-renders every route (home, catalog, category, detail,
  search, favorites, recent) and resolves the real lazy route table mounted by `App.jsx`

## Deployment (Vercel)

- The app is a static SPA built with `vite build` (output `dist/`). `vercel.json` adds a
  catch-all rewrite to `index.html` so deep links such as `/component/button` work.
- Vercel project: **vakeem-library**, framework Vite, root directory `ui-library`,
  Node engine pinned to `24.x` in `package.json`.
- Live URL: <https://vakeem-library.vercel.app>
- Lazy pages live in `src/pages/lazyPages.jsx`: `React.lazy` needs a default export, so
  named exports from `CatalogPages.jsx` are wrapped via `loader().then(m => ({ default: m[name] }))`.
