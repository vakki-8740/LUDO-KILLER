import Drawer from '../components/ui/overlays/Drawer.jsx'
import { DropdownMenu, Popover } from '../components/ui/overlays/DropdownMenu.jsx'
import CommandPalette from '../components/ui/overlays/CommandPalette.jsx'
import drawerJsx from '../components/ui/overlays/Drawer.jsx?raw'
import drawerCss from '../components/ui/overlays/Drawer.css?raw'
import dropdownJsx from '../components/ui/overlays/DropdownMenu.jsx?raw'
import dropdownCss from '../components/ui/overlays/DropdownMenu.css?raw'
import paletteJsx from '../components/ui/overlays/CommandPalette.jsx?raw'
import paletteCss from '../components/ui/overlays/CommandPalette.css?raw'

const Row = ({ children }) => <div style={{ display: 'flex', flexWrap: 'wrap', gap: 16, alignItems: 'flex-start' }}>{children}</div>

export default [
  {
    id: 'drawer', title: 'Navigation Drawer', category: 'overlays',
    description: 'Off-canvas panel from either side with scrim and Escape close.',
    keywords: ['side panel', 'sheet', 'off-canvas'],
    source: { jsx: drawerJsx, css: drawerCss },
    props: [
      { name: 'side', type: 'string', default: 'left', desc: 'left | right' },
    ],
    variants: [
      { id: 'left', title: 'Left drawer', node: <Drawer side="left" /> },
      { id: 'right', title: 'Right drawer', node: <Drawer side="right" /> },
    ],
  },
  {
    id: 'dropdown-menu', title: 'Dropdown Menu', category: 'overlays',
    description: 'Account menu with outside-click and Escape dismissal, dividers and danger item.',
    keywords: ['menu', 'account menu', 'popover list'],
    source: { jsx: dropdownJsx, css: dropdownCss },
    props: [],
    variants: [{ id: 'menu', title: 'Account dropdown', node: <DropdownMenu /> }],
  },
  {
    id: 'popover', title: 'Popover', category: 'overlays',
    description: 'Anchored filter panel with form controls and reset/apply actions.',
    keywords: ['filter', 'popover', 'anchored panel'],
    source: { jsx: dropdownJsx, css: dropdownCss },
    props: [],
    variants: [{ id: 'filter', title: 'Filter popover', node: <Popover /> }],
  },
  {
    id: 'command-palette', title: 'Command Palette', category: 'overlays',
    description: 'Ctrl/Cmd+K quick-actions palette with fuzzy filter, arrow keys and Enter selection.',
    keywords: ['cmd k', 'quick actions', 'spotlight', 'search'],
    source: { jsx: paletteJsx, css: paletteCss },
    props: [],
    variants: [{ id: 'palette', title: 'Press Ctrl / Cmd + K', node: <CommandPalette /> }],
  },
]
