import { useEffect, useRef, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Icon } from '../ui/icons/Icons.jsx'
import ThemeSwitcher from './ThemeSwitcher'
import { searchCatalog } from '../../data/catalog'
import { useDebouncedValue } from '../../hooks/useDebouncedValue'
import './AppTopbar.css'

export default function AppTopbar({ onMenu }) {
  const [q, setQ] = useState('')
  const [open, setOpen] = useState(false)
  const debounced = useDebouncedValue(q, 160)
  const results = open && debounced.trim() ? searchCatalog(debounced).slice(0, 7) : []
  const navigate = useNavigate()
  const ref = useRef(null)

  useEffect(() => {
    const onClick = (e) => { if (ref.current && !ref.current.contains(e.target)) setOpen(false) }
    const onKey = (e) => {
      if (e.key === '/' && document.activeElement?.tagName !== 'INPUT') {
        e.preventDefault()
        ref.current?.querySelector('input')?.focus()
      }
    }
    document.addEventListener('mousedown', onClick)
    document.addEventListener('keydown', onKey)
    return () => {
      document.removeEventListener('mousedown', onClick)
      document.removeEventListener('keydown', onKey)
    }
  }, [])

  const go = (id) => {
    setOpen(false)
    setQ('')
    navigate(`/component/${id}`)
  }

  const submit = (e) => {
    e.preventDefault()
    if (!q.trim()) return
    navigate(`/search?q=${encodeURIComponent(q.trim())}`)
    setOpen(false)
  }

  return (
    <header className="app-topbar">
      <button type="button" className="app-topbar__burger" aria-label="Open navigation" onClick={onMenu}>
        <Icon name="menu" size={20} />
      </button>
      <a className="app-topbar__brand" href="/" onClick={(e) => { e.preventDefault(); navigate('/') }}>
        <span className="app-topbar__mark"><Icon name="grid" size={16} /></span>
        OWN Library
      </a>

      <form className="app-topbar__search" ref={ref} onSubmit={submit} role="search">
        <Icon name="search" size={16} className="app-topbar__search-icon" />
        <input
          value={q}
          placeholder="Search components…  ( press / )"
          aria-label="Search components"
          onChange={(e) => { setQ(e.target.value); setOpen(true) }}
          onFocus={() => setOpen(true)}
        />
        {open && debounced.trim() && (
          <ul className="app-topbar__results" role="listbox">
            {results.length === 0 && <li className="app-topbar__empty">No matches for “{debounced}”</li>}
            {results.map((r) => (
              <li key={r.id}>
                <button type="button" role="option" onClick={() => go(r.id)}>
                  <Icon name="layers" size={14} />
                  <span>{r.title}</span>
                  <em>{r.category}</em>
                </button>
              </li>
            ))}
          </ul>
        )}
      </form>

      <div className="app-topbar__actions">
        <ThemeSwitcher />
      </div>
    </header>
  )
}
