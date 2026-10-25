import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react'
import { DEFAULT_THEME, THEMES } from '../themes/themes'

function readStorage(key, fallback) {
  try {
    const raw = localStorage.getItem(key)
    return raw !== null ? JSON.parse(raw) : fallback
  } catch {
    return fallback
  }
}

/* ---------------- Theme ---------------- */
const ThemeContext = createContext(null)

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState(() => {
    const saved = readStorage('own-theme', DEFAULT_THEME)
    return THEMES.some((t) => t.id === saved) ? saved : DEFAULT_THEME
  })

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme)
    try { localStorage.setItem('own-theme', JSON.stringify(theme)) } catch { /* noop */ }
  }, [theme])

  const changeTheme = useCallback((id) => setTheme(id), [])
  const toggleTheme = useCallback(() => {
    setTheme((cur) => (cur === 'dark' || cur === 'black' ? 'light' : 'dark'))
  }, [])

  const value = useMemo(() => ({ theme, changeTheme, toggleTheme, themes: THEMES }), [theme, changeTheme, toggleTheme])
  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>
}

export function useThemeContext() {
  const ctx = useContext(ThemeContext)
  if (!ctx) throw new Error('useThemeContext must be used inside ThemeProvider')
  return ctx
}

/* ---------------- Favorites ---------------- */
const FavoritesContext = createContext(null)

export function FavoritesProvider({ children }) {
  const [ids, setIds] = useState(() => readStorage('own-favorites', []))

  useEffect(() => {
    try { localStorage.setItem('own-favorites', JSON.stringify(ids)) } catch { /* noop */ }
  }, [ids])

  const toggleFavorite = useCallback((id) => {
    setIds((cur) => (cur.includes(id) ? cur.filter((x) => x !== id) : [...cur, id]))
  }, [])
  const isFavorite = useCallback((id) => ids.includes(id), [ids])

  const value = useMemo(() => ({ ids, toggleFavorite, isFavorite, count: ids.length }), [ids, toggleFavorite, isFavorite])
  return <FavoritesContext.Provider value={value}>{children}</FavoritesContext.Provider>
}

export function useFavorites() {
  const ctx = useContext(FavoritesContext)
  if (!ctx) throw new Error('useFavorites must be used inside FavoritesProvider')
  return ctx
}

/* ---------------- Recently viewed ---------------- */
const RecentContext = createContext(null)
const MAX_RECENT = 12

export function RecentProvider({ children }) {
  const [ids, setIds] = useState(() => readStorage('own-recent', []))

  useEffect(() => {
    try { localStorage.setItem('own-recent', JSON.stringify(ids)) } catch { /* noop */ }
  }, [ids])

  const recordView = useCallback((id) => {
    setIds((cur) => [id, ...cur.filter((x) => x !== id)].slice(0, MAX_RECENT))
  }, [])
  const clearRecent = useCallback(() => setIds([]), [])

  const value = useMemo(() => ({ ids, recordView, clearRecent }), [ids, recordView, clearRecent])
  return <RecentContext.Provider value={value}>{children}</RecentContext.Provider>
}

export function useRecent() {
  const ctx = useContext(RecentContext)
  if (!ctx) throw new Error('useRecent must be used inside RecentProvider')
  return ctx
}
