import { NavLink } from 'react-router-dom'
import { Icon } from '../ui/icons/Icons.jsx'
import { CATEGORIES } from '../../data/categories'
import { CATALOG } from '../../data/catalog'
import { useFavorites, useRecent } from '../../state/AppState'
import './AppSidebar.css'

const countFor = (cat) => CATALOG.filter((c) => c.category === cat).length

export default function AppSidebar({ onNavigate }) {
  const { count: favCount } = useFavorites()
  const { ids: recentIds, clearRecent } = useRecent()
  const recentItems = recentIds.map((id) => CATALOG.find((c) => c.id === id)).filter(Boolean).slice(0, 5)

  return (
    <aside className="app-sidebar" aria-label="Library navigation">
      <div className="app-sidebar__section">
        <p className="app-sidebar__heading">Library</p>
        <NavLink to="/" end className="app-sidebar__link" onClick={onNavigate}>
          <Icon name="home" size={17} /> Home
        </NavLink>
        <NavLink to="/components" className="app-sidebar__link" onClick={onNavigate}>
          <Icon name="grid" size={17} /> All components
          <span className="app-sidebar__count">{CATALOG.length}</span>
        </NavLink>
        <NavLink to="/favorites" className="app-sidebar__link" onClick={onNavigate}>
          <Icon name="heart" size={17} /> Favorites
          <span className="app-sidebar__count">{favCount}</span>
        </NavLink>
        <NavLink to="/recent" className="app-sidebar__link" onClick={onNavigate}>
          <Icon name="clock" size={17} /> Recently viewed
        </NavLink>
      </div>

      <div className="app-sidebar__section">
        <p className="app-sidebar__heading">Categories</p>
        <nav>
          {CATEGORIES.map((cat) => (
            <NavLink
              key={cat.id}
              to={`/category/${cat.id}`}
              className="app-sidebar__link"
              onClick={onNavigate}
            >
              <Icon name="layers" size={16} />
              <span className="app-sidebar__cat">{cat.label}</span>
              <span className="app-sidebar__count">{countFor(cat.id)}</span>
            </NavLink>
          ))}
        </nav>
      </div>

      {recentItems.length > 0 && (
        <div className="app-sidebar__section">
          <p className="app-sidebar__heading">
            Recent
            <button type="button" className="app-sidebar__clear" onClick={clearRecent}>Clear</button>
          </p>
          {recentItems.map((c) => (
            <NavLink key={c.id} to={`/component/${c.id}`} className="app-sidebar__link app-sidebar__link--sm" onClick={onNavigate}>
              <Icon name="clock" size={14} /> {c.title}
            </NavLink>
          ))}
        </div>
      )}
    </aside>
  )
}
