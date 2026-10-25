import DashboardShell from '../components/ui/dashboard/DashboardShell.jsx'
import { WalletCard, TransactionList, NotificationFeed } from '../components/ui/dashboard/DashboardWidgets.jsx'
import shellJsx from '../components/ui/dashboard/DashboardShell.jsx?raw'
import shellCss from '../components/ui/dashboard/DashboardShell.css?raw'
import widgetsJsx from '../components/ui/dashboard/DashboardWidgets.jsx?raw'
import widgetsCss from '../components/ui/dashboard/DashboardWidgets.css?raw'

export default [
  {
    id: 'dashboard-shell', title: 'Dashboard Layout', category: 'dashboard',
    description: 'Complete app shell: sidebar nav, topbar, KPI grid and chart/goal panels.',
    keywords: ['admin', 'app shell', 'sidebar layout', 'workspace'],
    source: { jsx: shellJsx, css: shellCss },
    props: [],
    variants: [{ id: 'shell', title: 'Responsive app shell', node: <DashboardShell /> }],
  },
  {
    id: 'wallet-card', title: 'Wallet Card', category: 'dashboard',
    description: 'Gradient balance card with masked number and quick actions.',
    keywords: ['balance', 'payment', 'card', 'money'],
    source: { jsx: widgetsJsx, css: widgetsCss },
    props: [],
    variants: [{ id: 'wallet', title: 'Balance card', node: <WalletCard /> }],
  },
  {
    id: 'transactions', title: 'Transactions List', category: 'dashboard',
    description: 'Credit/debit rows with icons, metadata and signed amounts.',
    keywords: ['payments', 'history', 'ledger'],
    source: { jsx: widgetsJsx, css: widgetsCss },
    props: [],
    variants: [{ id: 'list', title: 'Recent transactions', node: <TransactionList /> }],
  },
  {
    id: 'notification-feed', title: 'Notification Panel', category: 'dashboard',
    description: 'Notification feed with tone icons, unread markers and a count badge.',
    keywords: ['notifications', 'alerts', 'feed'],
    source: { jsx: widgetsJsx, css: widgetsCss },
    props: [],
    variants: [{ id: 'notif', title: 'Notification center', node: <NotificationFeed /> }],
  },
]
