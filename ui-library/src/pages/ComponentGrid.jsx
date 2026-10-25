import ComponentCard from '../components/layout/ComponentCard'
import EmptyState from '../components/ui/feedback/EmptyState'

export default function ComponentGrid({ items, emptyTitle = 'Nothing here yet', emptyText }) {
  if (!items.length) {
    return <EmptyState icon="search" title={emptyTitle} text={emptyText} />
  }
  return (
    <div className="component-grid">
      {items.map((entry) => <ComponentCard key={entry.id} entry={entry} />)}
    </div>
  )
}
