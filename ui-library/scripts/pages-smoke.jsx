import { renderToStaticMarkup } from 'react-dom/server'
import { createElement } from 'react'
import { MemoryRouter, Routes, Route } from 'react-router-dom'
import { ThemeProvider, FavoritesProvider, RecentProvider } from '../src/state/AppState'
import { ToastProvider } from '../src/components/ui/feedback/Toast'
import AppLayout from '../src/components/layout/AppLayout'
import HomePage from '../src/pages/HomePage'
import { AllComponentsPage, CategoryPage, SearchPage, FavoritesPage, RecentPage } from '../src/pages/CatalogPages'
import ComponentDetailPage from '../src/pages/ComponentDetailPage'
import { CATALOG } from '../src/data/catalog'

function renderAt(path, element) {
  const tree = createElement(ThemeProvider, null,
    createElement(FavoritesProvider, null,
      createElement(RecentProvider, null,
        createElement(ToastProvider, null,
          createElement(MemoryRouter, { initialEntries: [path] }, element)))))
  return renderToStaticMarkup(tree)
}

const checks = [
  ['/', createElement(Routes, null, createElement(Route, { element: createElement(AppLayout) },
    createElement(Route, { path: '/', element: createElement(HomePage) })))],
  ['/components', createElement(Routes, null, createElement(Route, { element: createElement(AppLayout) },
    createElement(Route, { path: '/components', element: createElement(AllComponentsPage) })))],
  ['/category/forms', createElement(Routes, null, createElement(Route, { element: createElement(AppLayout) },
    createElement(Route, { path: '/category/:catId', element: createElement(CategoryPage, { catId: 'forms' }) })))],
  ['/component/button', createElement(Routes, null, createElement(Route, { element: createElement(AppLayout) },
    createElement(Route, { path: '/component/:id', element: createElement(ComponentDetailPage, { id: 'button' }) })))],
  ['/search?q=card', createElement(Routes, null, createElement(Route, { element: createElement(AppLayout) },
    createElement(Route, { path: '/search', element: createElement(SearchPage) })))],
  ['/favorites', createElement(Routes, null, createElement(Route, { element: createElement(AppLayout) },
    createElement(Route, { path: '/favorites', element: createElement(FavoritesPage) })))],
  ['/recent', createElement(Routes, null, createElement(Route, { element: createElement(AppLayout) },
    createElement(Route, { path: '/recent', element: createElement(RecentPage) })))],
]

const errors = []
for (const [path, tree] of checks) {
  try {
    const html = renderAt(path, tree)
    if (html.length < 200) errors.push(`${path}: suspiciously short output`)
    console.log(`OK  ${path}  (${html.length} chars)`)
  } catch (e) {
    errors.push(`${path}: ${e.message}`)
  }
}

// every catalog id must resolve through the detail page
const sample = CATALOG.slice(0, 6)
for (const c of sample) {
  try {
    renderAt(`/component/${c.id}`, createElement(Routes, null, createElement(Route, { element: createElement(AppLayout) },
      createElement(Route, { path: '/component/:id', element: createElement(ComponentDetailPage, { id: c.id }) }))))
  } catch (e) {
    errors.push(`detail ${c.id}: ${e.message}`)
  }
}

if (errors.length) { console.error('PAGE SMOKE FAILURES:', errors); process.exit(1) }
console.log('PAGE SMOKE OK')
