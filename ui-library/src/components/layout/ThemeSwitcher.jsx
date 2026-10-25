import { useEffect, useRef, useState } from 'react'
import { useThemeContext } from '../../state/AppState'
import { Icon } from '../ui/icons/Icons.jsx'
import './ThemeSwitcher.css'

export default function ThemeSwitcher() {
  const { theme, changeTheme, themes } = useThemeContext()
  const [open, setOpen] = useState(false)
  const ref = useRef(null)
  const current = themes.find((t) => t.id === theme) || themes[0]

  useEffect(() => {
    const onClick = (e) => { if (ref.current && !ref.current.contains(e.target)) setOpen(false) }
    const onKey = (e) => { if (e.key === 'Escape') setOpen(false) }
    document.addEventListener('mousedown', onClick)
    document.addEventListener('keydown', onKey)
    return () => {
      document.removeEventListener('mousedown', onClick)
      document.removeEventListener('keydown', onKey)
    }
  }, [])

  return (
    <div className="theme-switch" ref={ref}>
      <button
        type="button"
        className="theme-switch__trigger"
        aria-haspopup="listbox"
        aria-expanded={open}
        aria-label="Change theme"
        title="Change theme"
        onClick={() => setOpen((o) => !o)}
      >
        <span className="theme-switch__swatch" style={{ background: current.swatch[1] }} />
        <span className="theme-switch__label">{current.label}</span>
        <Icon name="chevron-down" size={15} />
      </button>
      {open && (
        <ul className="theme-switch__menu" role="listbox" aria-label="Themes">
          {themes.map((t) => (
            <li key={t.id}>
              <button
                type="button"
                role="option"
                aria-selected={t.id === theme}
                className={`theme-switch__option${t.id === theme ? ' is-active' : ''}`}
                onClick={() => { changeTheme(t.id); setOpen(false) }}
              >
                <span className="theme-switch__dots">
                  <i style={{ background: t.swatch[0] }} />
                  <i style={{ background: t.swatch[1] }} />
                </span>
                <span>{t.label}</span>
                {t.id === theme && <Icon name="check" size={14} className="theme-switch__tick" />}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}
