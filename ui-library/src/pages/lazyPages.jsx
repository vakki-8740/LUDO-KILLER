import { lazy } from 'react'

// Default-export modules map directly onto React.lazy.
export const HomePage = lazy(() => import('./HomePage'))
export const ComponentDetailPage = lazy(() => import('./ComponentDetailPage'))

// CatalogPages exposes named exports only, so each route gets its own lazy
// component that resolves the named export as the module default.
const loadCatalogPages = () => import('./CatalogPages')
const lazyCatalogPage = (exportName) =>
  lazy(async () => {
    const module = await loadCatalogPages()
    const Page = module[exportName]
    if (typeof Page !== 'function') {
      throw new Error(`CatalogPages is missing the "${exportName}" export`)
    }
    return { default: Page }
  })

export const AllComponentsPage = lazyCatalogPage('AllComponentsPage')
export const CategoryRoute = lazyCatalogPage('CategoryRoute')
export const DetailRoute = lazyCatalogPage('DetailRoute')
export const SearchPage = lazyCatalogPage('SearchPage')
export const FavoritesPage = lazyCatalogPage('FavoritesPage')
export const RecentPage = lazyCatalogPage('RecentPage')
