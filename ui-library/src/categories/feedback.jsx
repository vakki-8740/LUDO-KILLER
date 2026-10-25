import { useState } from 'react'
import { Alert, Badge, Chip } from '../components/ui/feedback/Alert.jsx'
import Tooltip from '../components/ui/feedback/Tooltip.jsx'
import { Spinner, DotLoader, ProgressBar, ProgressCircle, Skeleton } from '../components/ui/feedback/Loaders.jsx'
import { ToastProvider, ToastDemoButtons } from '../components/ui/feedback/Toast.jsx'
import Modal from '../components/ui/feedback/Modal.jsx'
import EmptyState from '../components/ui/feedback/EmptyState.jsx'
import Button from '../components/ui/button/Button.jsx'
import alertJsx from '../components/ui/feedback/Alert.jsx?raw'
import alertCss from '../components/ui/feedback/Alert.css?raw'
import tooltipJsx from '../components/ui/feedback/Tooltip.jsx?raw'
import tooltipCss from '../components/ui/feedback/Tooltip.css?raw'
import loadersJsx from '../components/ui/feedback/Loaders.jsx?raw'
import loadersCss from '../components/ui/feedback/Loaders.css?raw'
import toastJsx from '../components/ui/feedback/Toast.jsx?raw'
import toastCss from '../components/ui/feedback/Toast.css?raw'
import modalJsx from '../components/ui/feedback/Modal.jsx?raw'
import modalCss from '../components/ui/feedback/Modal.css?raw'
import emptyJsx from '../components/ui/feedback/EmptyState.jsx?raw'
import emptyCss from '../components/ui/feedback/EmptyState.css?raw'

const Stack = ({ children }) => <div style={{ display: 'flex', flexDirection: 'column', gap: 12, maxWidth: 480 }}>{children}</div>
const Row = ({ children }) => <div style={{ display: 'flex', flexWrap: 'wrap', gap: 12, alignItems: 'center' }}>{children}</div>

function ModalDemo() {
  const [open, setOpen] = useState(false)
  return (
    <>
      <Button onClick={() => setOpen(true)} icon="info">Open dialog</Button>
      <Modal
        open={open}
        onClose={() => setOpen(false)}
        title="Confirm deletion"
        footer={<><Button variant="secondary" onClick={() => setOpen(false)}>Cancel</Button><Button variant="danger" onClick={() => setOpen(false)}>Delete</Button></>}
      >
        <p className="own-muted" style={{ fontSize: 'var(--fs-sm)' }}>
          This will permanently remove the selected project and all of its data. This action cannot be undone.
        </p>
      </Modal>
    </>
  )
}

function ChipsDemo() {
  const [chips, setChips] = useState(['Design', 'React', 'Tokens'])
  return (
    <Row>
      {chips.map((c) => <Chip key={c} label={c} selected={c === 'React'} onRemove={(label) => setChips((cur) => cur.filter((x) => x !== label))} />)}
      <Chip label="Add filter" icon="plus" onClick={() => setChips((c) => [...c, `Filter ${c.length + 1}`])} />
    </Row>
  )
}

export default [
  {
    id: 'alert', title: 'Alert', category: 'feedback',
    description: 'Inline info, success, warning and danger messages with optional dismiss.',
    keywords: ['banner', 'message', 'notice', 'validation'],
    source: { jsx: alertJsx, css: alertCss },
    props: [
      { name: 'tone', type: 'string', default: 'info', desc: 'info | success | warning | danger' },
      { name: 'title', type: 'string', default: '—', desc: 'Bold heading' },
      { name: 'dismissible', type: 'boolean', default: 'true', desc: 'Shows a close button' },
    ],
    variants: [{ id: 'tones', title: 'Four tones', node: <Stack><Alert tone="info" title="Heads up">Library themes update automatically tonight.</Alert><Alert tone="success" title="Saved">Your component changes were published.</Alert><Alert tone="warning" title="Storage almost full">80% of your space is used.</Alert><Alert tone="danger" title="Payment failed">Update your billing details to keep the workspace active.</Alert></Stack> }],
  },
  {
    id: 'badge-chip', title: 'Badge & Chip', category: 'feedback',
    description: 'Status pills, counts and removable filter chips.',
    keywords: ['tag', 'pill', 'status', 'filter'],
    source: { jsx: alertJsx, css: alertCss },
    props: [
      { name: 'tone', type: 'string', default: 'accent', desc: 'accent | success | danger | warning | neutral' },
      { name: 'dot', type: 'boolean', default: 'false', desc: 'Adds a status dot' },
      { name: 'onRemove', type: 'function', default: '—', desc: 'Chip: renders a remove button when provided' },
    ],
    variants: [
      { id: 'badges', title: 'Badges', node: <Row><Badge tone="accent">New</Badge><Badge tone="success" dot>Active</Badge><Badge tone="warning" dot>Away</Badge><Badge tone="danger" dot>Failed</Badge><Badge tone="neutral">Draft</Badge></Row> },
      { id: 'chips', title: 'Removable chips', node: <ChipsDemo /> },
    ],
  },
  {
    id: 'tooltip', title: 'Tooltip', category: 'feedback',
    description: 'Hover and focus hint in four placements.',
    keywords: ['hint', 'popover hint', 'help'],
    source: { jsx: tooltipJsx, css: tooltipCss },
    props: [
      { name: 'text', type: 'string', default: 'Tooltip text', desc: 'Tooltip content' },
      { name: 'side', type: 'string', default: 'top', desc: 'top | bottom | left | right' },
    ],
    variants: [{ id: 'sides', title: 'Placements', node: <Row style={{ padding: '40px 8px' }}><Tooltip text="Top tooltip" side="top"><Button size="sm" variant="secondary">Top</Button></Tooltip><Tooltip text="Bottom tooltip" side="bottom"><Button size="sm" variant="secondary">Bottom</Button></Tooltip><Tooltip text="Left tooltip" side="left"><Button size="sm" variant="secondary">Left</Button></Tooltip><Tooltip text="Right tooltip" side="right"><Button size="sm" variant="secondary">Right</Button></Tooltip></Row> }],
  },
  {
    id: 'loaders', title: 'Loaders & Progress', category: 'feedback',
    description: 'Spinners, dots, determinate bars, progress circles and shimmer skeletons.',
    keywords: ['loading', 'spinner', 'skeleton', 'progress', 'shimmer'],
    source: { jsx: loadersJsx, css: loadersCss },
    props: [
      { name: 'value', type: 'number', default: '62 / 72', desc: 'Progress fill 0–100' },
      { name: 'tone', type: 'string', default: 'accent', desc: 'Progress bar tone' },
      { name: 'lines / circle', type: 'boolean/number', default: '3 / false', desc: 'Skeleton shape controls' },
    ],
    variants: [
      { id: 'spinners', title: 'Spinners & dots', node: <Row><Spinner size={28} /><Spinner size={20} /><DotLoader /></Row> },
      { id: 'progress', title: 'Bars & circle', node: <Stack style={{ maxWidth: 380 }}><ProgressBar label="Uploading files" value={62} /><ProgressBar value={34} tone="warning" /><Row><ProgressCircle value={72} /><ProgressCircle value={45} size={72} /></Row></Stack> },
      { id: 'skeleton', title: 'Skeleton shimmer', node: <div style={{ maxWidth: 380, width: '100%' }}><Skeleton lines={3} circle /></div> },
    ],
  },
  {
    id: 'toast', title: 'Toast Notifications', category: 'feedback',
    description: 'Stacked aria-live notifications with tones, actions and auto-dismiss.',
    keywords: ['snackbar', 'notification', 'undo', 'alert'],
    source: { jsx: toastJsx, css: toastCss },
    props: [
      { name: 'tone', type: 'string', default: 'info', desc: 'info | success | warning | danger' },
      { name: 'title / message', type: 'string', default: '—', desc: 'Toast content' },
      { name: 'action', type: 'object', default: '—', desc: '{ label, onClick } e.g. Undo' },
      { name: 'duration', type: 'number', default: '3600', desc: 'Auto-dismiss ms (0 = sticky)' },
    ],
    variants: [{ id: 'trigger', title: 'Trigger toasts', node: <ToastProvider><ToastDemoButtons /></ToastProvider> }],
  },
  {
    id: 'modal', title: 'Modal Dialog', category: 'feedback',
    description: 'Centered dialog with scrim, Escape to close, focus management and scroll lock.',
    keywords: ['dialog', 'popup', 'confirm', 'overlay'],
    source: { jsx: modalJsx, css: modalCss },
    props: [
      { name: 'open / onClose', type: 'boolean / function', default: '—', desc: 'Controlled visibility' },
      { name: 'title', type: 'string', default: '—', desc: 'Dialog heading' },
      { name: 'size', type: 'string', default: 'md', desc: 'sm | md | lg' },
      { name: 'footer', type: 'ReactNode', default: '—', desc: 'Action area' },
    ],
    variants: [{ id: 'confirm', title: 'Confirmation dialog', node: <ModalDemo /> }],
  },
  {
    id: 'empty-state', title: 'Empty State', category: 'feedback',
    description: 'Friendly placeholder for zero-data screens with an optional action.',
    keywords: ['no data', 'placeholder', 'zero results'],
    source: { jsx: emptyJsx, css: emptyCss },
    props: [
      { name: 'icon', type: 'string', default: 'search', desc: 'Icon name' },
      { name: 'title / text', type: 'string', default: '—', desc: 'Heading and helper copy' },
      { name: 'actionLabel / onAction', type: 'string / function', default: '—', desc: 'Optional CTA' },
    ],
    variants: [{ id: 'inbox', title: 'No results', node: <EmptyState icon="search" title="No components found" text="Try a different search term or clear your filters." actionLabel="Clear filters" /> }],
  },
]
