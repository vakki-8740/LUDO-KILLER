import Button from '../components/ui/button/Button.jsx'
import IconButton from '../components/ui/button/IconButton.jsx'
import ButtonGroup from '../components/ui/button/ButtonGroup.jsx'
import Fab from '../components/ui/button/Fab.jsx'
import buttonJsx from '../components/ui/button/Button.jsx?raw'
import buttonCss from '../components/ui/button/Button.css?raw'
import iconJsx from '../components/ui/button/IconButton.jsx?raw'
import iconCss from '../components/ui/button/IconButton.css?raw'
import groupJsx from '../components/ui/button/ButtonGroup.jsx?raw'
import groupCss from '../components/ui/button/ButtonGroup.css?raw'
import fabJsx from '../components/ui/button/Fab.jsx?raw'
import fabCss from '../components/ui/button/Fab.css?raw'

const Row = ({ children }) => <div style={{ display: 'flex', flexWrap: 'wrap', gap: 12, alignItems: 'center' }}>{children}</div>

export default [
  {
    id: 'button',
    title: 'Button',
    category: 'interactive',
    description: 'Primary action control with variants, sizes, loading and disabled states.',
    keywords: ['cta', 'action', 'submit', 'loading'],
    source: { jsx: buttonJsx, css: buttonCss },
    props: [
      { name: 'variant', type: 'string', default: 'primary', desc: 'primary | secondary | outline | ghost | danger | success' },
      { name: 'size', type: 'string', default: 'md', desc: 'sm | md | lg' },
      { name: 'icon / iconRight', type: 'string', default: '—', desc: 'Icon name from the inline icon set' },
      { name: 'loading', type: 'boolean', default: 'false', desc: 'Shows a spinner and blocks interaction' },
      { name: 'disabled', type: 'boolean', default: 'false', desc: 'Disables the button' },
      { name: 'fullWidth', type: 'boolean', default: 'false', desc: 'Stretches to 100% width' },
    ],
    variants: [
      { id: 'variants', title: 'Variants', node: <Row><Button>Primary</Button><Button variant="secondary">Secondary</Button><Button variant="outline">Outline</Button><Button variant="ghost">Ghost</Button><Button variant="danger">Danger</Button><Button variant="success">Success</Button></Row> },
      { id: 'sizes', title: 'Sizes & states', node: <Row><Button size="sm">Small</Button><Button>Medium</Button><Button size="lg">Large</Button><Button disabled>Disabled</Button><Button loading>Loading</Button><Button icon="heart">With icon</Button></Row> },
    ],
  },
  {
    id: 'icon-button',
    title: 'Icon Button',
    category: 'interactive',
    description: 'Compact square action button with filled, soft and ghost styles plus notification badges.',
    keywords: ['icon', 'badge', 'action', 'toolbar'],
    source: { jsx: iconJsx, css: iconCss },
    props: [
      { name: 'icon', type: 'string', default: 'bell', desc: 'Icon name from the icon set' },
      { name: 'variant', type: 'string', default: 'plain', desc: 'plain | filled | soft | ghost' },
      { name: 'size', type: 'string', default: 'md', desc: 'sm | md | lg' },
      { name: 'badge', type: 'number', default: '—', desc: 'Optional count bubble' },
    ],
    variants: [
      { id: 'styles', title: 'Styles', node: <Row><IconButton icon="bell" label="Notifications" /><IconButton icon="heart" variant="filled" label="Favorites" /><IconButton icon="settings" variant="soft" label="Settings" /><IconButton icon="bookmark" variant="ghost" label="Bookmark" /></Row> },
      { id: 'badges', title: 'Badges & sizes', node: <Row><IconButton icon="cart" badge={3} label="Cart" /><IconButton icon="message" variant="soft" badge={12} label="Messages" /><IconButton icon="bell" size="sm" variant="filled" label="Small" /><IconButton icon="user" size="lg" label="Large" /></Row> },
    ],
  },
  {
    id: 'button-group',
    title: 'Button Group & Segmented Control',
    category: 'interactive',
    description: 'Connected controls for single-choice segmented views and grouped actions.',
    keywords: ['segmented', 'toggle group', 'options'],
    source: { jsx: groupJsx, css: groupCss },
    props: [
      { name: 'options', type: 'array', default: 'Day/Week/Month', desc: '[{ id, label }] choices' },
      { name: 'defaultSelected', type: 'string', default: 'week', desc: 'Initially active option id' },
      { name: 'segmented', type: 'boolean', default: 'true', desc: 'Segmented pill vs separated buttons' },
      { name: 'onChange', type: 'function', default: '—', desc: 'Called with the selected id' },
    ],
    variants: [
      { id: 'segmented', title: 'Segmented control', node: <ButtonGroup /> },
      { id: 'separated', title: 'Separated button group', node: <ButtonGroup segmented={false} /> },
    ],
  },
  {
    id: 'fab',
    title: 'Floating Action Button',
    category: 'interactive',
    description: 'Circular or extended elevated action for primary screen actions.',
    keywords: ['fab', 'floating', 'create', 'plus'],
    source: { jsx: fabJsx, css: fabCss },
    props: [
      { name: 'icon', type: 'string', default: 'plus', desc: 'Icon name' },
      { name: 'size', type: 'string', default: 'md', desc: 'sm | md | lg (lg renders extended label)' },
      { name: 'color', type: 'string', default: 'accent', desc: 'accent | success | danger | soft' },
      { name: 'label', type: 'string', default: '—', desc: 'Accessible label / extended text' },
    ],
    variants: [
      { id: 'sizes', title: 'Sizes & colors', node: <Row><Fab size="sm" label="Small action" /><Fab label="Create" /><Fab size="lg" icon="plus" label="New project" /><Fab color="success" icon="check" label="Approve" /><Fab color="soft" icon="edit" label="Draft" /></Row> },
    ],
  },
]
