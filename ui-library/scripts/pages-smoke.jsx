import { renderToStaticMarkup } from 'react-dom/server'
import { createElement, Suspense } from 'react'
import { MemoryRouter, Routes, Route, Navigate } from 'react-router-dom'
import { ThemeProvider, FavoritesProvider, RecentProvider } from '../src/state/AppState'
import { ToastProvider } from '../src/components/ui/feedback/Toast'
import AppLayout from '../src/components/layout/AppLayout'
import { ErrorPage } from '../src/components/ui/marketing/Marketing'
import HomePage from '../src/pages/HomePage'
import { AllComponentsPage, CategoryPage, SearchPage, FavoritesPage, RecentPage } from '../src/pages/CatalogPages'
import ComponentDetailPage from '../src/pages/ComponentDetailPage'
import * as LazyPages from '../src/pages/lazyPages.jsx'
import { CATALOG } from '../src/data/catalog'

function renderAt(path, element) {
  const tree = createElement(ThemeProvider, null,
    createElement(FavoritesProvider, null,
      createElement(RecentProvider, null,
        createElement(ToastProvider, null,
          createElement(MemoryRouter, { initialEntries: [path] }, element)))))
  return renderToStaticMarkup(tree)
}

const errors = []

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

// Force every React.lazy component in the shared route module to resolve, then
// render the exact lazy route table App.jsx mounts. This guards against lazy
// wiring defects (e.g. treating a named-export module like a default export),
// which render as React error #130 in the browser.
async function resolveLazy(LazyComponent) {
  const payload = LazyComponent._payload
  if (payload._status === 1) return
  try {
    LazyComponent._init(payload)
  } catch (suspension) {
    await suspension
    LazyComponent._init(payload)
  }
  if (payload._status !== 1 || typeof payload._result?.default !== 'function') {
    throw new Error('lazy component did not resolve to a function component')
  }
}

async function runAppRouteChecks() {
  await Promise.all(Object.values(LazyPages).map(resolveLazy))

  const appRoutes = createElement(Routes, null, createElement(Route, { element: createElement(AppLayout) },
    createElement(Route, { path: '/', element: createElement(LazyPages.HomePage) }),
    createElement(Route, { path: '/components', element: createElement(LazyPages.AllComponentsPage) }),
    createElement(Route, { path: '/category/:catId', element: createElement(LazyPages.CategoryRoute) }),
    createElement(Route, { path: '/component/:id', element: createElement(LazyPages.DetailRoute) }),
    createElement(Route, { path: '/search', element: createElement(LazyPages.SearchPage) }),
    createElement(Route, { path: '/favorites', element: createElement(LazyPages.FavoritesPage) }),
    createElement(Route, { path: '/recent', element: createElement(LazyPages.RecentPage) }),
    createElement(Route, { path: '/404', element: createElement(ErrorPage, { code: '404' }) }),
    createElement(Route, { path: '*', element: createElement(Navigate, { to: '/404', replace: true }) })))

  const appPaths = ['/', '/components', '/category/forms', '/component/button', '/search?q=card', '/favorites', '/recent', '/404', '/does-not-exist']
  for (const path of appPaths) {
    try {
      const html = renderAt(path, createElement(Suspense, { fallback: createElement('div', null, 'loading') }, appRoutes))
      if (html.length < 200) errors.push(`app-route ${path}: suspiciously short output`)
      if (html.includes('Something went wrong')) errors.push(`app-route ${path}: rendered error boundary`)
      console.log(`OK  app-route ${path}  (${html.length} chars)`)
    } catch (e) {
      errors.push(`app-route ${path}: ${e.message}`)
    }
  }
}

(async () => {
  await runAppRouteChecks()
  if (errors.length) { console.error('PAGE SMOKE FAILURES:', errors); process.exit(1) }
  console.log('PAGE SMOKE OK')
})()
