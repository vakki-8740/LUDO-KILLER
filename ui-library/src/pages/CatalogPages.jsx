import { useMemo, useState } from 'react'
import { useSearchParams, useParams, Link, useNavigate } from 'react-router-dom'
import { CATALOG, SORTS, searchCatalog } from '../data/catalog'
import { CATEGORIES } from '../data/categories'
import { useFavorites, useRecent } from '../state/AppState'
import { getComponent } from '../data/catalog'
import ComponentGrid from './ComponentGrid'
import ComponentDetailPage from './ComponentDetailPage'
import EmptyState from '../components/ui/feedback/EmptyState'
import { Icon } from '../components/ui/icons/Icons.jsx'
import './pages.css'

export function CategoryRoute() {
  const { catId } = useParams()
  return <CategoryPage catId={catId} />
}

export function DetailRoute() {
  const { id } = useParams()
  return <ComponentDetailPage id={id} />
}

function PageHeading({ title, text, count }) {
  return (
    <header className="page-head">
      <h1>{title}</h1>
      {text && <p>{text}</p>}
      {count != null && <span className="page-head__count">{count} components</span>}
    </header>
  )
}

function Toolbar({ category, setCategory, sort, setSort }) {
  return (
    <div className="toolbar">
      <label className="toolbar__filter">
        <span className="own-sr-only">Filter by category</span>
        <select value={category} onChange={(e) => setCategory(e.target.value)} aria-label="Filter by category">
          <option value="all">All categories</option>
          {CATEGORIES.map((c) => <option key={c.id} value={c.id}>{c.label}</option>)}
        </select>
        <Icon name="chevron-down" size={15} />
      </label>
      <label className="toolbar__filter">
        <span className="own-sr-only">Sort components</span>
        <select value={sort} onChange={(e) => setSort(e.target.value)} aria-label="Sort components">
          <option value="name-asc">Name A → Z</option>
          <option value="name-desc">Name Z → A</option>
          <option value="category">Category</option>
        </select>
        <Icon name="chevron-down" size={15} />
      </label>
    </div>
  )
}

export function AllComponentsPage() {
  const [category, setCategory] = useState('all')
  const [sort, setSort] = useState('name-asc')
  const items = useMemo(() => {
    const filtered = searchCatalog('', category)
    return [...filtered].sort(SORTS[sort])
  }, [category, sort])

  return (
    <div className="page">
      <PageHeading title="All components" text="Every reusable component in the library, grouped into 12 categories." count={CATALOG.length} />
      <Toolbar category={category} setCategory={setCategory} sort={sort} setSort={setSort} />
      <ComponentGrid items={items} emptyTitle="No components in this category" />
    </div>
  )
}

export function CategoryPage({ catId }) {
  const cat = CATEGORIES.find((c) => c.id === catId)
  const [sort, setSort] = useState('name-asc')
  const items = useMemo(() => CATALOG.filter((c) => c.category === catId).sort(SORTS[sort]), [catId, sort])
  if (!cat) {
    return <EmptyState icon="x-circle" title="Unknown category" text="This category does not exist." />
  }
  return (
    <div className="page">
      <nav className="page-crumbs" aria-label="Breadcrumb">
        <Link to="/components">All components</Link>
        <Icon name="chevron-right" size={13} />
        <span aria-current="page">{cat.label}</span>
      </nav>
      <PageHeading title={cat.label} text={cat.desc} count={items.length} />
      <div className="toolbar">
        <label className="toolbar__filter">
          <span className="own-sr-only">Sort components</span>
          <select value={sort} onChange={(e) => setSort(e.target.value)} aria-label="Sort components">
            <option value="name-asc">Name A → Z</option>
            <option value="name-desc">Name Z → A</option>
          </select>
          <Icon name="chevron-down" size={15} />
        </label>
      </div>
      <ComponentGrid items={items} />
    </div>
  )
}

export function SearchPage() {
  const [params] = useSearchParams()
  const q = params.get('q') || ''
  const items = useMemo(() => searchCatalog(q), [q])
  return (
    <div className="page">
      <PageHeading title={`Search results`} text={q ? `Showing matches for “${q}”` : 'Type a query in the top search bar.'} count={q ? items.length : undefined} />
      {q ? (
        <ComponentGrid
          items={items}
          emptyTitle="No components found"
          emptyText={`No title, description or keyword matches “${q}”. Try “button”, “table” or “theme”.`}
        />
      ) : (
        <EmptyState icon="search" title="Search the library" text="Find components by name, description or keyword." />
      )}
    </div>
  )
}

export function FavoritesPage() {
  const { ids } = useFavorites()
  const navigate = useNavigate()
  const items = ids.map(getComponent).filter(Boolean)
  return (
    <div className="page">
      <PageHeading title="Favorites" text="Bookmarked components, stored locally in your browser." count={items.length} />
      {items.length ? (
        <ComponentGrid items={items} />
      ) : (
        <EmptyState
          icon="heart"
          title="No favorites yet"
          text="Tap the heart on any component card to bookmark it here."
          actionLabel="Browse components"
          onAction={() => navigate('/components')}
        />
      )}
    </div>
  )
}

export function RecentPage() {
  const { ids, clearRecent } = useRecent()
  const items = ids.map(getComponent).filter(Boolean)
  return (
    <div className="page">
      <PageHeading title="Recently viewed" text="The last 12 components you opened, most recent first." count={items.length} />
      {items.length ? (
        <>
          <div className="toolbar">
            <button type="button" className="toolbar__clear" onClick={clearRecent}><Icon name="trash" size={14} /> Clear history</button>
          </div>
          <ComponentGrid items={items} />
        </>
      ) : (
        <EmptyState icon="clock" title="No history yet" text="Components you open will appear here for quick access." />
      )}
    </div>
  )
}

export { PageHeading }
