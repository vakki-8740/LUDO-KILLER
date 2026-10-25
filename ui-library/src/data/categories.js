export const CATEGORIES = [
  { id: 'interactive', label: 'Buttons & Actions', desc: 'Buttons, icon buttons, groups and floating actions.' },
  { id: 'forms', label: 'Forms & Inputs', desc: 'Inputs, choices, pickers, uploads and entry controls.' },
  { id: 'feedback', label: 'Feedback & Status', desc: 'Alerts, toasts, loaders, modals and empty states.' },
  { id: 'navigation', label: 'Navigation', desc: 'Navbars, tabs, breadcrumbs, pagination and steppers.' },
  { id: 'layout', label: 'Layout', desc: 'Cards, heroes, lists, accordions and section primitives.' },
  { id: 'data', label: 'Data Display', desc: 'Tables, avatars, stats, timelines, charts and carousels.' },
  { id: 'overlays', label: 'Overlays', desc: 'Drawers, dropdowns, popovers and command palette.' },
  { id: 'auth', label: 'Authentication', desc: 'Login, signup, recovery and two-factor screens.' },
  { id: 'dashboard', label: 'Dashboard & Admin', desc: 'App shells, wallets, transactions and notifications.' },
  { id: 'ecommerce', label: 'E-commerce', desc: 'Products, cart, checkout, coupons and galleries.' },
  { id: 'social', label: 'Social & Communication', desc: 'Chat, comments, reactions and profile headers.' },
  { id: 'marketing', label: 'Sections & Marketing', desc: 'Pricing, testimonials, FAQ, CTAs and error pages.' },
]

export const categoryLabel = (id) => CATEGORIES.find((c) => c.id === id)?.label || id
