import { useState } from 'react'
import { Icon } from '../ui/icons/Icons.jsx'
import { copyText } from '../../utils/clipboard'
import tokensRaw from '../../styles/tokens.css?raw'
import './CodePanel.css'

export default function CodePanel({ source }) {
  const tabs = [
    { id: 'jsx', label: 'JSX', code: source?.jsx || '' },
    { id: 'css', label: 'CSS', code: source?.css || '' },
    { id: 'tokens', label: 'Tokens', code: tokensRaw },
  ].filter((t) => t.code)
  const [active, setActive] = useState(tabs[0].id)
  const [copied, setCopied] = useState(false)
  const current = tabs.find((t) => t.id === active) || tabs[0]

  const copy = async () => {
    try {
      await copyText(current.code)
      setCopied(true)
      setTimeout(() => setCopied(false), 1600)
    } catch {
      setCopied(false)
    }
  }

  const onTabKey = (e, i) => {
    if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return
    e.preventDefault()
    const next = (i + (e.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length
    setActive(tabs[next].id)
    e.currentTarget.parentElement.children[next].focus()
  }

  return (
    <div className="code-panel">
      <div className="code-panel__bar" role="tablist" aria-label="Source code">
        {tabs.map((t, i) => (
          <button
            key={t.id}
            type="button"
            role="tab"
            aria-selected={active === t.id}
            tabIndex={active === t.id ? 0 : -1}
            className={`code-panel__tab${active === t.id ? ' is-active' : ''}`}
            onClick={() => setActive(t.id)}
            onKeyDown={(e) => onTabKey(e, i)}
          >
            {t.label}
          </button>
        ))}
        <button type="button" className={`code-panel__copy${copied ? ' is-done' : ''}`} onClick={copy}>
          {copied ? <><Icon name="check" size={14} /> Copied!</> : <><Icon name="copy" size={14} /> Copy</>}
        </button>
      </div>
      <pre className="code-panel__pre"><code>{current.code}</code></pre>
      <p className="code-panel__tip">
        Copied code is standalone — add the Tokens CSS variables to your project if they are not already present.
      </p>
    </div>
  )
}
