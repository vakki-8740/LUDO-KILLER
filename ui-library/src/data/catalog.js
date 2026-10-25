import interactive from '../categories/interactive.jsx'
import forms from '../categories/forms.jsx'
import feedback from '../categories/feedback.jsx'
import navigation from '../categories/navigation.jsx'
import layout from '../categories/layout.jsx'
import data from '../categories/data.jsx'
import overlays from '../categories/overlays.jsx'
import auth from '../categories/auth.jsx'
import dashboard from '../categories/dashboard.jsx'
import ecommerce from '../categories/ecommerce.jsx'
import social from '../categories/social.jsx'
import marketing from '../categories/marketing.jsx'

export const CATALOG = [
  ...interactive,
  ...forms,
  ...feedback,
  ...navigation,
  ...layout,
  ...data,
  ...overlays,
  ...auth,
  ...dashboard,
  ...ecommerce,
  ...social,
  ...marketing,
]

const byId = new Map(CATALOG.map((c) => [c.id, c]))

export const getComponent = (id) => byId.get(id)
export const totalComponents = CATALOG.length

export function searchCatalog(query, categoryId = 'all') {
  const q = query.trim().toLowerCase()
  return CATALOG.filter((c) => {
    const inCategory = categoryId === 'all' || c.category === categoryId
    if (!inCategory) return false
    if (!q) return true
    const haystack = [c.title, c.description, c.category, ...(c.keywords || [])].join(' ').toLowerCase()
    return haystack.includes(q)
  })
}

export const SORTS = {
  'name-asc': (a, b) => a.title.localeCompare(b.title),
  'name-desc': (a, b) => b.title.localeCompare(a.title),
  category: (a, b) => a.category.localeCompare(b.category) || a.title.localeCompare(b.title),
}
