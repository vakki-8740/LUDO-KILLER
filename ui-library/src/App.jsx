import { Suspense } from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { ThemeProvider, FavoritesProvider, RecentProvider } from './state/AppState'
import { ToastProvider } from './components/ui/feedback/Toast.jsx'
import AppLayout from './components/layout/AppLayout'
import ErrorBoundary from './components/layout/ErrorBoundary'
import PageLoader from './components/layout/PageLoader'
import { ErrorPage } from './components/ui/marketing/Marketing'
import {
  HomePage,
  AllComponentsPage,
  CategoryRoute,
  DetailRoute,
  SearchPage,
  FavoritesPage,
  RecentPage,
} from './pages/lazyPages.jsx'

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
                      <Route path="/components" element={<AllComponentsPage />} />
                      <Route path="/category/:catId" element={<CategoryRoute />} />
                      <Route path="/component/:id" element={<DetailRoute />} />
                      <Route path="/search" element={<SearchPage />} />
                      <Route path="/favorites" element={<FavoritesPage />} />
                      <Route path="/recent" element={<RecentPage />} />
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
