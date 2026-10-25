import { lazy, Suspense } from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { ThemeProvider, FavoritesProvider, RecentProvider } from './state/AppState'
import { ToastProvider } from './components/ui/feedback/Toast.jsx'
import AppLayout from './components/layout/AppLayout'
import ErrorBoundary from './components/layout/ErrorBoundary'
import PageLoader from './components/layout/PageLoader'
import { ErrorPage } from './components/ui/marketing/Marketing'

const HomePage = lazy(() => import('./pages/HomePage'))
const CatalogPages = lazy(() => import('./pages/CatalogPages'))
const ComponentDetailPage = lazy(() => import('./pages/ComponentDetailPage'))

export default function App() {
  return (
    <ErrorBoundary>
      <ThemeProvider>
        <FavoritesProvider>
          <RecentProvider>
            <ToastProvider>
              <BrowserRouter>
                <Suspense fallback={<PageLoader />}>
                  <Routes>
                    <Route element={<AppLayout />}>
                      <Route path="/" element={<HomePage />} />
                      <Route path="/components" element={<CatalogPages.AllComponentsPage />} />
                      <Route path="/category/:catId" element={<CatalogPages.CategoryRoute />} />
                      <Route path="/component/:id" element={<CatalogPages.DetailRoute />} />
                      <Route path="/search" element={<CatalogPages.SearchPage />} />
                      <Route path="/favorites" element={<CatalogPages.FavoritesPage />} />
                      <Route path="/recent" element={<CatalogPages.RecentPage />} />
                      <Route path="/404" element={<ErrorPage code="404" />} />
                      <Route path="*" element={<Navigate to="/404" replace />} />
                    </Route>
                  </Routes>
                </Suspense>
              </BrowserRouter>
            </ToastProvider>
          </RecentProvider>
        </FavoritesProvider>
      </ThemeProvider>
    </ErrorBoundary>
  )
}
