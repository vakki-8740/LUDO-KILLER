import { Link } from 'react-router-dom'
import { Icon } from '../components/ui/icons/Icons.jsx'
import { CATEGORIES } from '../data/categories'
import { CATALOG, totalComponents } from '../data/catalog'
import ComponentGrid from './ComponentGrid'
import { THEMES } from '../themes/themes'
import './pages.css'

export default function HomePage() {
  const featured = CATALOG.slice(0, 8)
  return (
    <div className="page">
      <section className="home-hero own-card">
        <span className="home-hero__eyebrow"><span className="home-hero__dot" /> Personal UI Design Library</span>
        <h1>Design once. Reuse every component.</h1>
        <p>
          A complete React + Vite reference built on one token system — same colors, typography, spacing and 6px radius
          across every theme. Preview variants, switch screen sizes and copy production-ready JSX &amp; CSS.
        </p>
        <div className="home-hero__stats">
          <div><strong>{totalComponents}</strong><span>Components</span></div>
          <div><strong>{CATEGORIES.length}</strong><span>Categories</span></div>
          <div><strong>{THEMES.length}</strong><span>Themes</span></div>
          <div><strong>100%</strong><span>Responsive</span></div>
        </div>
      </section>

      <section className="home-section">
        <div className="home-section__head">
          <h2>Browse by category</h2>
          <Link to="/components" className="home-section__all">View all <Icon name="arrow-right" size={14} /></Link>
        </div>
        <div className="home-cats">
          {CATEGORIES.map((cat) => {
            const count = CATALOG.filter((c) => c.category === cat.id).length
            return (
              <Link key={cat.id} to={`/category/${cat.id}`} className="home-cat">
                <span className="home-cat__icon"><Icon name="layers" size={18} /></span>
                <strong>{cat.label}</strong>
                <span>{count} components</span>
              </Link>
            )
          })}
        </div>
      </section>

      <section className="home-section">
        <div className="home-section__head">
          <h2>Featured components</h2>
          <Link to="/components" className="home-section__all">View all <Icon name="arrow-right" size={14} /></Link>
        </div>
        <ComponentGrid items={featured} />
      </section>
    </div>
  )
}
