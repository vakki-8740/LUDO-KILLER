import { useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Icon } from '../components/ui/icons/Icons.jsx'
import { getComponent } from '../data/catalog'
import { categoryLabel } from '../data/categories'
import { useFavorites, useRecent } from '../state/AppState'
import ComponentStage from '../components/viewer/ComponentStage'
import EmptyState from '../components/ui/feedback/EmptyState'
import Button from '../components/ui/button/Button.jsx'
import './pages.css'

export default function ComponentDetailPage({ id }) {
  const entry = getComponent(id)
  const { isFavorite, toggleFavorite } = useFavorites()
  const { recordView } = useRecent()
  const navigate = useNavigate()

  useEffect(() => {
    if (entry) recordView(entry.id)
    window.scrollTo({ top: 0 })
  }, [entry, recordView])

  if (!entry) {
    return (
      <div className="page">
        <EmptyState
          icon="x-circle"
          title="Component not found"
          text="It may have been renamed or removed."
          actionLabel="Back to library"
          onAction={() => navigate('/components')}
        />
      </div>
    )
  }

  const fav = isFavorite(entry.id)

  return (
    <div className="page detail">
      <nav className="page-crumbs" aria-label="Breadcrumb">
        <Link to="/components">Components</Link>
        <Icon name="chevron-right" size={13} />
        <Link to={`/category/${entry.category}`}>{categoryLabel(entry.category)}</Link>
        <Icon name="chevron-right" size={13} />
        <span aria-current="page">{entry.title}</span>
      </nav>

      <header className="detail__head">
        <div>
          <h1>{entry.title}</h1>
          <p>{entry.description}</p>
          <div className="detail__meta">
            <Link to={`/category/${entry.category}`} className="detail__cat">{categoryLabel(entry.category)}</Link>
            <span className="detail__variants">{entry.variants.length} variant{entry.variants.length > 1 ? 's' : ''}</span>
          </div>
        </div>
        <button
          type="button"
          className={`detail__fav${fav ? ' is-on' : ''}`}
          aria-pressed={fav}
          onClick={() => toggleFavorite(entry.id)}
        >
          <Icon name="heart" size={16} /> {fav ? 'Saved' : 'Save'}
        </button>
      </header>

      <ComponentStage entry={entry} />

      {entry.props?.length > 0 && (
        <section className="detail__props">
          <h2>Props &amp; customization</h2>
          <div className="detail__table-wrap">
            <table className="detail__table">
              <thead>
                <tr><th scope="col">Prop</th><th scope="col">Type</th><th scope="col">Default</th><th scope="col">Description</th></tr>
              </thead>
              <tbody>
                {entry.props.map((p) => (
                  <tr key={p.name}>
                    <td data-label="Prop"><code>{p.name}</code></td>
                    <td data-label="Type"><code>{p.type}</code></td>
                    <td data-label="Default"><code>{p.default}</code></td>
                    <td data-label="Description">{p.desc}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )}

      <div className="detail__footer">
        <Button variant="secondary" icon="arrow-left" onClick={() => navigate(-1)}>Back</Button>
      </div>
    </div>
  )
}
