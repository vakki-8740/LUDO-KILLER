import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
// 1) Bootstrap CSS first
import 'bootstrap/dist/css/bootstrap.min.css'
// 2) Theme overrides after (so tokens win)
import './theme.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
