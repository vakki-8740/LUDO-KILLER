import Card from '../components/ui/layout/Card.jsx'
import Accordion from '../components/ui/layout/Accordion.jsx'
import Hero from '../components/ui/layout/Hero.jsx'
import ListLayout from '../components/ui/layout/ListLayout.jsx'
import { Divider, SectionHeader, SplitLayout, GridLayout } from '../components/ui/layout/LayoutExtras.jsx'
import cardJsx from '../components/ui/layout/Card.jsx?raw'
import cardCss from '../components/ui/layout/Card.css?raw'
import accordionJsx from '../components/ui/layout/Accordion.jsx?raw'
import accordionCss from '../components/ui/layout/Accordion.css?raw'
import heroJsx from '../components/ui/layout/Hero.jsx?raw'
import heroCss from '../components/ui/layout/Hero.css?raw'
import listJsx from '../components/ui/layout/ListLayout.jsx?raw'
import listCss from '../components/ui/layout/ListLayout.css?raw'
import extrasJsx from '../components/ui/layout/LayoutExtras.jsx?raw'
import extrasCss from '../components/ui/layout/LayoutExtras.css?raw'

export default [
  {
    id: 'card', title: 'Card', category: 'layout',
    description: 'Base surface card with media, body and actions — the core container of the library.',
    keywords: ['surface', 'panel', 'tile'],
    source: { jsx: cardJsx, css: cardCss },
    props: [
      { name: 'title / text', type: 'string', default: '—', desc: 'Card content' },
      { name: 'footer', type: 'boolean', default: 'true', desc: 'Action row' },
      { name: 'elevated', type: 'boolean', default: 'false', desc: 'Stronger shadow' },
    ],
    variants: [{ id: 'grid', title: 'Card variants', node: <GridLayout columns={2}><Card /><Card elevated title="Elevated card" text="Same component with the elevated shadow token." /></GridLayout> }],
  },
  {
    id: 'hero', title: 'Hero / Banner', category: 'layout',
    description: 'Centered or split marketing hero built on the original library gradient treatment.',
    keywords: ['banner', 'landing', 'cta header'],
    source: { jsx: heroJsx, css: heroCss },
    props: [
      { name: 'split', type: 'boolean', default: 'false', desc: 'Two-column split with visual tile' },
    ],
    variants: [
      { id: 'centered', title: 'Centered hero', node: <Hero /> },
      { id: 'split', title: 'Split hero', node: <Hero split /> },
    ],
  },
  {
    id: 'list-layout', title: 'List Layout', category: 'layout',
    description: 'People / settings rows with avatars and status badges.',
    keywords: ['rows', 'list group', 'directory'],
    source: { jsx: listJsx, css: listCss },
    props: [],
    variants: [{ id: 'rows', title: 'Member rows', node: <ListLayout /> }],
  },
  {
    id: 'accordion', title: 'Accordion', category: 'layout',
    description: 'Single-open or multi-open collapsible sections with aria-expanded state.',
    keywords: ['collapse', 'faq', 'disclosure'],
    source: { jsx: accordionJsx, css: accordionCss },
    props: [
      { name: 'multiple', type: 'boolean', default: 'false', desc: 'Allow several panels open at once' },
    ],
    variants: [
      { id: 'single', title: 'Single open', node: <Accordion /> },
      { id: 'multi', title: 'Multi open', node: <Accordion multiple /> },
    ],
  },
  {
    id: 'section-primitives', title: 'Divider & Section Header', category: 'layout',
    description: 'Horizontal, vertical and labelled separators plus a reusable section header.',
    keywords: ['separator', 'spacer', 'heading', 'section'],
    source: { jsx: extrasJsx, css: extrasCss },
    props: [
      { name: 'label', type: 'string', default: '—', desc: 'Labelled divider text' },
      { name: 'vertical', type: 'boolean', default: 'false', desc: 'Vertical separator' },
      { name: 'align', type: 'string', default: 'left', desc: 'Section header alignment' },
    ],
    variants: [
      { id: 'dividers', title: 'Divider types', node: <div style={{ display: 'flex', flexDirection: 'column', gap: 14, maxWidth: 460, width: '100%' }}><Divider /><Divider label="OR" /><div style={{ display: 'flex', gap: 16, height: 44 }}><Divider vertical /><span className="own-muted" style={{ fontSize: 'var(--fs-sm)' }}>Vertical separator between panes</span></div></div> },
      { id: 'header', title: 'Section header', node: <SectionHeader eyebrow="Getting started" title="Build interfaces faster" text="A short descriptor explaining what this section contains and why it matters." /> },
    ],
  },
  {
    id: 'split-grid', title: 'Split & Grid Layouts', category: 'layout',
    description: 'Responsive two-pane split and auto-fit grid primitives.',
    keywords: ['columns', 'grid', 'split screen', 'responsive'],
    source: { jsx: extrasJsx, css: extrasCss },
    props: [
      { name: 'columns', type: 'number', default: '3', desc: 'GridLayout column count (collapses responsively)' },
      { name: 'left / right', type: 'ReactNode', default: '—', desc: 'SplitLayout panes' },
    ],
    variants: [
      { id: 'split', title: 'Split layout', node: <SplitLayout left={<h3>Left pane</h3>} right={<h3>Right pane</h3>} /> },
      { id: 'grid', title: 'Auto grid', node: <GridLayout columns={3}>{[1, 2, 3].map((n) => <div key={n} className="own-card" style={{ padding: 22, textAlign: 'center' }}>Tile {n}</div>)}</GridLayout> },
    ],
  },
]
