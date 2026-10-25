import { Component } from 'react'
import Button from '../ui/button/Button.jsx'

export default class ErrorBoundary extends Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false }
  }

  static getDerivedStateFromError() {
    return { hasError: true }
  }

  componentDidCatch(error, info) {
    console.error('OWN Library error:', error, info)
  }

  render() {
    if (!this.state.hasError) return this.props.children
    return (
      <div style={{ minHeight: '70vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 12, textAlign: 'center', padding: 24 }}>
        <h1 style={{ color: 'var(--no)' }}>Something went wrong</h1>
        <p className="own-muted" style={{ maxWidth: 420 }}>
          An unexpected error occurred while rendering this view. Reload the page to recover.
        </p>
        <Button onClick={() => window.location.reload()}>Reload</Button>
      </div>
    )
  }
}
