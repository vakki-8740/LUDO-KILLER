import { Link } from 'react-router-dom'
import { Icon } from '../ui/icons/Icons.jsx'
import { useFavorites } from '../../state/AppState'
import { categoryLabel } from '../../data/categories'
import './ComponentCard.css'

export default function ComponentCard({ entry }) {
  const { isFavorite, toggleFavorite } = useFavorites()
  const fav = isFavorite(entry.id)

  return (
    <article className="comp-card">
      <button
        type="button"
        className={`comp-card__fav${fav ? ' is-on' : ''}`}
        aria-label={fav ? `Remove ${entry.title} from favorites` : `Add ${entry.title} to favorites`}
        aria-pressed={fav}
        onClick={() => toggleFavorite(entry.id)}
      >
        <Icon name="heart" size={15} />
      </button>
      <Link to={`/component/${entry.id}`} className="comp-card__link">
        <div className="comp-card__thumb own-stage" aria-hidden="true">
          <span className="comp-card__mini">{entry.title.slice(0, 1)}</span>
        </div>
        <div className="comp-card__body">
          <h3 className="comp-card__title">
            {entry.title}
            <Icon name="arrow-right" size={14} />
          </h3>
          <p className="comp-card__desc">{entry.description}</p>
          <span className="comp-card__cat">{categoryLabel(entry.category)}</span>
        </div>
      </Link>
    </article>
  )
}
