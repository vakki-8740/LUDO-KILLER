import { renderToStaticMarkup } from 'react-dom/server'
import { createElement } from 'react'
import { CATALOG } from '../src/data/catalog'
import { CATEGORIES } from '../src/data/categories'
import { ThemeProvider, FavoritesProvider, RecentProvider } from '../src/state/AppState'
import { ToastProvider } from '../src/components/ui/feedback/Toast'

function wrap(node) {
  return createElement(ThemeProvider, null,
    createElement(FavoritesProvider, null,
      createElement(RecentProvider, null,
        createElement(ToastProvider, null, node))))
}

const errors = []
const ids = new Set()
let renderedVariants = 0

for (const entry of CATALOG) {
  if (ids.has(entry.id)) errors.push(`duplicate catalog id: ${entry.id}`)
  ids.add(entry.id)
  if (!CATEGORIES.some((c) => c.id === entry.category)) errors.push(`${entry.id}: unknown category ${entry.category}`)
  if (!entry.source?.jsx || entry.source.jsx.length < 40) errors.push(`${entry.id}: JSX source missing/too short`)
  if (!entry.source?.css || entry.source.css.length < 40) errors.push(`${entry.id}: CSS source missing/too short`)
  if (!entry.variants?.length) errors.push(`${entry.id}: no variants`)
  for (const v of entry.variants || []) {
    try {
      const html = renderToStaticMarkup(wrap(v.node))
      renderedVariants += 1
      if (html.length < 20) errors.push(`${entry.id}/${v.id}: empty render output`)
    } catch (e) {
      errors.push(`${entry.id}/${v.id}: ${e.message}`)
    }
  }
}

const perCategory = CATEGORIES.map((c) => `${c.id}=${CATALOG.filter((x) => x.category === c.id).length}`).join(' ')
console.log(`catalog entries: ${CATALOG.length}`)
console.log(`variants rendered: ${renderedVariants}`)
console.log(`categories: ${perCategory}`)
if (errors.length) {
  console.error('SMOKE FAILURES:')
  errors.forEach((e) => console.error(' -', e))
  process.exit(1)
}
console.log('SMOKE OK')
