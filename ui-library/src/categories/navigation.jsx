import Navbar from '../components/ui/navigation/Navbar.jsx'
import Tabs from '../components/ui/navigation/Tabs.jsx'
import Breadcrumbs from '../components/ui/navigation/Breadcrumbs.jsx'
import Pagination from '../components/ui/navigation/Pagination.jsx'
import BottomNav from '../components/ui/navigation/BottomNav.jsx'
import Stepper from '../components/ui/navigation/Stepper.jsx'
import navbarJsx from '../components/ui/navigation/Navbar.jsx?raw'
import navbarCss from '../components/ui/navigation/Navbar.css?raw'
import tabsJsx from '../components/ui/navigation/Tabs.jsx?raw'
import tabsCss from '../components/ui/navigation/Tabs.css?raw'
import crumbsJsx from '../components/ui/navigation/Breadcrumbs.jsx?raw'
import crumbsCss from '../components/ui/navigation/Breadcrumbs.css?raw'
import paginationJsx from '../components/ui/navigation/Pagination.jsx?raw'
import paginationCss from '../components/ui/navigation/Pagination.css?raw'
import bottomJsx from '../components/ui/navigation/BottomNav.jsx?raw'
import bottomCss from '../components/ui/navigation/BottomNav.css?raw'
import stepperJsx from '../components/ui/navigation/Stepper.jsx?raw'
import stepperCss from '../components/ui/navigation/Stepper.css?raw'

export default [
  {
    id: 'navbar', title: 'Navbar', category: 'navigation',
    description: 'Sticky responsive navbar with active links, CTA actions and a mobile hamburger drawer.',
    keywords: ['header', 'menu', 'top nav', 'responsive'],
    source: { jsx: navbarJsx, css: navbarCss },
    props: [
      { name: 'brand', type: 'string', default: 'OWN App', desc: 'Brand text next to the logo mark' },
    ],
    variants: [
      { id: 'desktop', title: 'Desktop & mobile (resize under 860px)', node: <Navbar /> },
    ],
  },
  {
    id: 'tabs', title: 'Tabs', category: 'navigation',
    description: 'Accessible tab list with arrow-key navigation in underline and pill styles.',
    keywords: ['tablist', 'sections', 'panels'],
    source: { jsx: tabsJsx, css: tabsCss },
    props: [
      { name: 'variant', type: 'string', default: 'underline', desc: 'underline | pill' },
    ],
    variants: [
      { id: 'underline', title: 'Underline tabs', node: <Tabs /> },
      { id: 'pill', title: 'Pill tabs', node: <Tabs variant="pill" /> },
    ],
  },
  {
    id: 'breadcrumbs', title: 'Breadcrumbs', category: 'navigation',
    description: 'Page hierarchy trail with current-page aria state.',
    keywords: ['crumb', 'hierarchy', 'path'],
    source: { jsx: crumbsJsx, css: crumbsCss },
    props: [
      { name: 'items', type: 'array', default: 'sample trail', desc: '[{ label, href? }], last item is current' },
    ],
    variants: [{ id: 'trail', title: 'Hierarchy trail', node: <Breadcrumbs /> }],
  },
  {
    id: 'pagination', title: 'Pagination', category: 'navigation',
    description: 'Numbered paging with ellipsis, prev/next controls and disabled boundaries.',
    keywords: ['pager', 'pages', 'numbers'],
    source: { jsx: paginationJsx, css: paginationCss },
    props: [
      { name: 'totalPages', type: 'number', default: '8', desc: 'Page count' },
    ],
    variants: [{ id: 'numbers', title: 'Numbered paging', node: <Pagination /> }],
  },
  {
    id: 'bottom-nav', title: 'Bottom Navigation', category: 'navigation',
    description: 'Mobile app tab bar with active indicator and notification badges.',
    keywords: ['mobile nav', 'tab bar', 'app bar'],
    source: { jsx: bottomJsx, css: bottomCss },
    props: [
      { name: 'items', type: 'array', default: 'built-in', desc: '[{ id, label, icon, badge? }]' },
    ],
    variants: [{ id: 'bar', title: 'Mobile tab bar', node: <BottomNav /> }],
  },
  {
    id: 'stepper', title: 'Stepper', category: 'navigation',
    description: 'Horizontal and vertical progress steps for multi-stage flows.',
    keywords: ['steps', 'wizard', 'progress steps'],
    source: { jsx: stepperJsx, css: stepperCss },
    props: [
      { name: 'current', type: 'number', default: '2', desc: 'Zero-based current step' },
      { name: 'vertical', type: 'boolean', default: 'false', desc: 'Vertical layout' },
    ],
    variants: [
      { id: 'horizontal', title: 'Horizontal stepper', node: <Stepper current={2} /> },
      { id: 'vertical', title: 'Vertical stepper', node: <Stepper current={1} vertical /> },
    ],
  },
]
