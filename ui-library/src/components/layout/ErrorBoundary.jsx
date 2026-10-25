import { Component } from 'react'
import Button from '../ui/button/Button.jsx'

export default class ErrorBoundary extends Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false }
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, message: error?.message, name: error?.name }
  }

  componentDidCatch(error, info) {
    console.error('OWN Library error:', error, info)
    this.setState({ componentStack: info?.componentStack })
  }

  render() {
    if (!this.state.hasError) return this.props.children
    return (
      <div style={{ minHeight: '70vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 12, textAlign: 'center', padding: 24 }}>
        <h1 style={{ color: 'var(--no)' }}>Something went wrong</h1>
        <p className="own-muted" style={{ maxWidth: 420 }}>
          An unexpected error occurred while rendering this view. Reload the page to recover.
        </p>
        <pre data-testid="error-detail" style={{ maxWidth: 900, whiteSpace: 'pre-wrap', wordBreak: 'break-word', textAlign: 'left', background: 'var(--code-bg)', color: 'var(--code-text)', padding: 14, borderRadius: 8, fontSize: 12 }}>
          {`${this.state.name || 'Error'}: ${this.state.message || '(no message)'}\n${this.state.componentStack || ''}`}
        </pre>
        <Button onClick={() => window.location.reload()}>Reload</Button>
      </div>
    )
  }
}
