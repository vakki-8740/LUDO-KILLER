import { useState } from 'react'
import { Outlet } from 'react-router-dom'
import AppTopbar from './AppTopbar'
import AppSidebar from './AppSidebar'
import './AppLayout.css'

export default function AppLayout() {
  const [drawer, setDrawer] = useState(false)

  return (
    <div className="app-layout">
      <AppTopbar onMenu={() => setDrawer(true)} />
      <div className="app-layout__body">
        <div className="app-layout__sidebar" data-open={drawer}>
          <AppSidebar onNavigate={() => setDrawer(false)} />
        </div>
        {drawer && <button type="button" className="app-layout__scrim" aria-label="Close navigation" onClick={() => setDrawer(false)} />}
        <main className="app-layout__main" id="main-content">
          <Outlet />
        </main>
      </div>
    </div>
  )
}
