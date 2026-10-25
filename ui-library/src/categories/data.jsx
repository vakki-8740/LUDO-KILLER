import { Avatar, AvatarGroup } from '../components/ui/data/Avatar.jsx'
import { StatCard, StatCardGrid } from '../components/ui/data/StatCard.jsx'
import DataTable from '../components/ui/data/DataTable.jsx'
import { Timeline, ActivityFeed } from '../components/ui/data/Timeline.jsx'
import KeyValue from '../components/ui/data/KeyValue.jsx'
import { BarChart, DonutChart } from '../components/ui/data/Charts.jsx'
import { Carousel, RatingStars } from '../components/ui/data/Carousel.jsx'
import avatarJsx from '../components/ui/data/Avatar.jsx?raw'
import avatarCss from '../components/ui/data/Avatar.css?raw'
import statJsx from '../components/ui/data/StatCard.jsx?raw'
import statCss from '../components/ui/data/StatCard.css?raw'
import tableJsx from '../components/ui/data/DataTable.jsx?raw'
import tableCss from '../components/ui/data/DataTable.css?raw'
import timelineJsx from '../components/ui/data/Timeline.jsx?raw'
import timelineCss from '../components/ui/data/Timeline.css?raw'
import kvJsx from '../components/ui/data/KeyValue.jsx?raw'
import kvCss from '../components/ui/data/KeyValue.css?raw'
import chartsJsx from '../components/ui/data/Charts.jsx?raw'
import chartsCss from '../components/ui/data/Charts.css?raw'
import carouselJsx from '../components/ui/data/Carousel.jsx?raw'
import carouselCss from '../components/ui/data/Carousel.css?raw'

const Row = ({ children }) => <div style={{ display: 'flex', flexWrap: 'wrap', gap: 14, alignItems: 'center' }}>{children}</div>

export default [
  {
    id: 'avatar', title: 'Avatar & Avatar Group', category: 'data',
    description: 'Initial avatars with presence dots and stacked overlapping groups.',
    keywords: ['profile picture', 'user', 'presence', 'stack'],
    source: { jsx: avatarJsx, css: avatarCss },
    props: [
      { name: 'initials', type: 'string', default: 'AK', desc: 'Text inside the avatar' },
      { name: 'size', type: 'string', default: 'md', desc: 'sm | md | lg' },
      { name: 'tone', type: 'string', default: 'accent', desc: 'accent | success | warning | neutral' },
      { name: 'status', type: 'string', default: '—', desc: 'online | away | offline presence dot' },
    ],
    variants: [
      { id: 'sizes', title: 'Sizes and presence', node: <Row><Avatar initials="AK" size="sm" /><Avatar initials="PS" size="md" status="online" /><Avatar initials="RV" size="lg" tone="warning" status="away" /></Row> },
      { id: 'group', title: 'Stacked group', node: <AvatarGroup max={3} /> },
    ],
  },
  {
    id: 'stat-card', title: 'Stats Cards', category: 'data',
    description: 'KPI tiles with icon, value and trend deltas in a responsive grid.',
    keywords: ['kpi', 'metric', 'analytics', 'numbers'],
    source: { jsx: statJsx, css: statCss },
    props: [
      { name: 'stat', type: 'object', default: 'sample set', desc: '{ label, value, delta, up, icon }' },
    ],
    variants: [{ id: 'grid', title: 'KPI grid', node: <StatCardGrid /> }],
  },
  {
    id: 'data-table', title: 'Data Table', category: 'data',
    description: 'Responsive table that reflows into labelled cards below 600px.',
    keywords: ['table', 'rows', 'members', 'directory'],
    source: { jsx: tableJsx, css: tableCss },
    props: [],
    variants: [{ id: 'members', title: 'Team table (try mobile width)', node: <DataTable /> }],
  },
  {
    id: 'timeline', title: 'Timeline & Activity Feed', category: 'data',
    description: 'Vertical event timeline and compact activity list with tone dots.',
    keywords: ['history', 'events', 'feed', 'activity'],
    source: { jsx: timelineJsx, css: timelineCss },
    props: [
      { name: 'events', type: 'array', default: 'sample set', desc: '[{ title, time, tone }]' },
    ],
    variants: [
      { id: 'timeline', title: 'Event timeline', node: <Timeline /> },
      { id: 'feed', title: 'Activity feed', node: <ActivityFeed /> },
    ],
  },
  {
    id: 'key-value', title: 'Key-Value List', category: 'data',
    description: 'Definition rows for order details and summaries.',
    keywords: ['details', 'definition list', 'summary'],
    source: { jsx: kvJsx, css: kvCss },
    props: [
      { name: 'rows', type: 'array', default: 'order sample', desc: '[{ k, v }]' },
    ],
    variants: [{ id: 'order', title: 'Order details', node: <KeyValue /> }],
  },
  {
    id: 'charts', title: 'Chart Containers', category: 'data',
    description: 'CSS-only bar and conic-gradient donut charts — no chart library needed.',
    keywords: ['bar chart', 'donut', 'graph', 'visualization'],
    source: { jsx: chartsJsx, css: chartsCss },
    props: [],
    variants: [
      { id: 'bar', title: 'Weekly bar chart', node: <BarChart /> },
      { id: 'donut', title: 'Traffic donut', node: <DonutChart /> },
    ],
  },
  {
    id: 'carousel', title: 'Carousel', category: 'data',
    description: 'Sliding feature carousel with arrows, dots and aria roles.',
    keywords: ['slider', 'slideshow', 'gallery'],
    source: { jsx: carouselJsx, css: carouselCss },
    props: [],
    variants: [{ id: 'slides', title: 'Feature slides', node: <Carousel /> }],
  },
  {
    id: 'rating-stars', title: 'Rating Summary', category: 'data',
    description: 'Read-only fractional star rating with review count.',
    keywords: ['stars', 'review', 'score', 'rating'],
    source: { jsx: carouselJsx, css: carouselCss },
    props: [
      { name: 'value', type: 'number', default: '4.2', desc: 'Fractional score out of 5' },
      { name: 'count', type: 'number', default: '128', desc: 'Review count' },
    ],
    variants: [{ id: 'score', title: 'Product score', node: <Row><RatingStars value={4.6} count={1024} /><RatingStars value={3.4} count={42} size={15} /></Row> }],
  },
]
