import { Spinner } from '../ui/feedback/Loaders.jsx'

export default function PageLoader() {
  return (
    <div style={{ minHeight: '50vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 14 }} role="status" aria-live="polite">
      <Spinner size={34} />
      <p className="own-muted" style={{ fontSize: 'var(--fs-sm)' }}>Loading library…</p>
    </div>
  )
}
