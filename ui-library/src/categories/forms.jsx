import Input from '../components/ui/input/Input.jsx'
import Textarea from '../components/ui/input/Textarea.jsx'
import SearchInput from '../components/ui/input/SearchInput.jsx'
import { Checkbox, Radio, Switch } from '../components/ui/input/Checkbox.jsx'
import Select from '../components/ui/input/Select.jsx'
import RangeSlider from '../components/ui/input/RangeSlider.jsx'
import RatingInput from '../components/ui/input/RatingInput.jsx'
import FileUpload from '../components/ui/input/FileUpload.jsx'
import OtpInput from '../components/ui/input/OtpInput.jsx'
import inputJsx from '../components/ui/input/Input.jsx?raw'
import inputCss from '../components/ui/input/Input.css?raw'
import textareaJsx from '../components/ui/input/Textarea.jsx?raw'
import searchJsx from '../components/ui/input/SearchInput.jsx?raw'
import searchCss from '../components/ui/input/SearchInput.css?raw'
import choiceJsx from '../components/ui/input/Checkbox.jsx?raw'
import choiceCss from '../components/ui/input/ChoiceControls.css?raw'
import selectJsx from '../components/ui/input/Select.jsx?raw'
import selectCss from '../components/ui/input/Select.css?raw'
import rangeJsx from '../components/ui/input/RangeSlider.jsx?raw'
import rangeCss from '../components/ui/input/RangeSlider.css?raw'
import ratingJsx from '../components/ui/input/RatingInput.jsx?raw'
import ratingCss from '../components/ui/input/RatingInput.css?raw'
import uploadJsx from '../components/ui/input/FileUpload.jsx?raw'
import uploadCss from '../components/ui/input/FileUpload.css?raw'
import otpJsx from '../components/ui/input/OtpInput.jsx?raw'
import otpCss from '../components/ui/input/OtpInput.css?raw'

const Stack = ({ children }) => <div style={{ display: 'flex', flexDirection: 'column', gap: 16, maxWidth: 420 }}>{children}</div>
const Row = ({ children }) => <div style={{ display: 'flex', flexWrap: 'wrap', gap: 14, alignItems: 'center' }}>{children}</div>

export default [
  {
    id: 'input', title: 'Input Field', category: 'forms',
    description: 'Labelled text input with icon, hint, validation error and password visibility toggle.',
    keywords: ['text', 'email', 'password', 'form', 'validation'],
    source: { jsx: inputJsx, css: inputCss },
    props: [
      { name: 'label / hint / error', type: 'string', default: '—', desc: 'Caption, helper text and validation message' },
      { name: 'icon', type: 'string', default: '—', desc: 'Leading icon name' },
      { name: 'type', type: 'string', default: 'text', desc: 'Any input type; password gets an eye toggle' },
      { name: 'allowPasswordToggle', type: 'boolean', default: 'false', desc: 'Show/hide password button' },
      { name: 'disabled', type: 'boolean', default: 'false', desc: 'Disables the field' },
    ],
    variants: [
      { id: 'states', title: 'Default, filled and error states', node: <Stack><Input label="Email" type="email" icon="mail" placeholder="you@example.com" /><Input label="Username" defaultValue="aman.kumar" hint="Your public profile name." /><Input label="Coupon" defaultValue="SAVED" error="This coupon has expired." /></Stack> },
      { id: 'password', title: 'Password with toggle', node: <Stack><Input label="Password" type="password" icon="lock" allowPasswordToggle placeholder="Min. 8 characters" /><Input label="Disabled field" defaultValue="Read only value" disabled /></Stack> },
    ],
  },
  {
    id: 'textarea', title: 'Textarea', category: 'forms',
    description: 'Multi-line input sharing the same field tokens and validation styles.',
    keywords: ['multiline', 'message', 'form'],
    source: { jsx: textareaJsx, css: inputCss },
    props: [
      { name: 'rows', type: 'number', default: '4', desc: 'Visible line count' },
      { name: 'label / hint / error', type: 'string', default: '—', desc: 'Same caption API as Input' },
    ],
    variants: [{ id: 'basic', title: 'Multiline entry', node: <Stack><Textarea label="Project description" placeholder="Tell us what you are building…" /><Textarea label="With error" defaultValue="Too short" error="Minimum 40 characters required." rows={3} /></Stack> }],
  },
  {
    id: 'search-input', title: 'Search Input', category: 'forms',
    description: 'Pill search with live filtered suggestions, clear button and keyboard hint.',
    keywords: ['search', 'autocomplete', 'suggestions', 'filter'],
    source: { jsx: searchJsx, css: searchCss },
    props: [
      { name: 'items', type: 'array', default: 'built-in list', desc: 'Suggestion strings' },
      { name: 'placeholder', type: 'string', default: 'Search components...', desc: 'Field placeholder' },
    ],
    variants: [{ id: 'basic', title: 'Live suggestions', node: <SearchInput /> }],
  },
  {
    id: 'checkbox', title: 'Checkbox', category: 'forms',
    description: 'Tri-state capable checkbox with checked, indeterminate and disabled states.',
    keywords: ['check', 'select all', 'choice', 'form'],
    source: { jsx: choiceJsx, css: choiceCss },
    props: [
      { name: 'label', type: 'string', default: '—', desc: 'Visible label' },
      { name: 'checked / defaultChecked', type: 'boolean', default: '—', desc: 'Controlled or uncontrolled state' },
      { name: 'indeterminate', type: 'boolean', default: 'false', desc: 'Shows a dash for partial selection' },
    ],
    variants: [{ id: 'states', title: 'Checkbox states', node: <Stack><Checkbox label="Email notifications" defaultChecked /><Checkbox label="Indeterminate select-all" indeterminate /><Checkbox label="Disabled option" disabled /><Checkbox label="Disabled checked" defaultChecked disabled /></Stack> }],
  },
  {
    id: 'radio', title: 'Radio Buttons', category: 'forms',
    description: 'Single-choice radio group with disabled and plan-card style usage.',
    keywords: ['radio', 'single choice', 'option'],
    source: { jsx: choiceJsx, css: choiceCss },
    props: [
      { name: 'name', type: 'string', default: '—', desc: 'Group name for mutual exclusion' },
      { name: 'value', type: 'string', default: '—', desc: 'Option value' },
      { name: 'label', type: 'string', default: '—', desc: 'Option label' },
    ],
    variants: [{ id: 'group', title: 'Radio group', node: <Stack><Radio name="plan" label="Free plan" defaultChecked /><Radio name="plan" label="Pro plan" /><Radio name="plan" label="Team plan" disabled /></Stack> }],
  },
  {
    id: 'switch', title: 'Switch', category: 'forms',
    description: 'On/off toggle with proper switch role and keyboard support.',
    keywords: ['toggle', 'switch', 'boolean', 'settings'],
    source: { jsx: choiceJsx, css: choiceCss },
    props: [
      { name: 'label', type: 'string', default: '—', desc: 'Setting label' },
      { name: 'checked / defaultChecked', type: 'boolean', default: '—', desc: 'State' },
    ],
    variants: [{ id: 'settings', title: 'Settings rows', node: <Stack><Switch label="Dark mode by default" defaultChecked /><Switch label="Marketing emails" /><Switch label="Disabled lock" disabled defaultChecked /></Stack> }],
  },
  {
    id: 'select', title: 'Select Menu', category: 'forms',
    description: 'Native-styled select that inherits every theme token.',
    keywords: ['dropdown', 'select', 'choice', 'form'],
    source: { jsx: selectJsx, css: selectCss },
    props: [
      { name: 'options', type: 'array', default: 'plans list', desc: '[{ value, label }]' },
      { name: 'defaultValue', type: 'string', default: "''", desc: 'Initial value' },
      { name: 'onChange', type: 'function', default: '—', desc: 'Receives selected value' },
    ],
    variants: [{ id: 'basic', title: 'Plan selection', node: <Stack><Select label="Choose a plan" hint="You can upgrade anytime." /><Select label="Pre-selected" defaultValue="pro" /></Stack> }],
  },
  {
    id: 'range-slider', title: 'Range Slider', category: 'forms',
    description: 'Single-thumb numeric slider with live formatted value output.',
    keywords: ['slider', 'range', 'budget', 'number'],
    source: { jsx: rangeJsx, css: rangeCss },
    props: [
      { name: 'min / max / step', type: 'number', default: '0 / 100 / 1', desc: 'Numeric bounds' },
      { name: 'defaultValue', type: 'number', default: '40', desc: 'Start value' },
      { name: 'prefix', type: 'string', default: '₹', desc: 'Value formatting prefix' },
    ],
    variants: [{ id: 'budget', title: 'Budget range', node: <div style={{ maxWidth: 380 }}><RangeSlider /></div> }],
  },
  {
    id: 'rating-input', title: 'Rating Input', category: 'forms',
    description: 'Interactive star rating with hover preview and accessible radio semantics.',
    keywords: ['stars', 'rating', 'review', 'feedback'],
    source: { jsx: ratingJsx, css: ratingCss },
    props: [
      { name: 'max', type: 'number', default: '5', desc: 'Number of stars' },
      { name: 'defaultValue', type: 'number', default: '0', desc: 'Initial rating' },
    ],
    variants: [{ id: 'rate', title: 'Rate this page', node: <RatingInput defaultValue={3} /> }],
  },
  {
    id: 'file-upload', title: 'File Upload', category: 'forms',
    description: 'Drag-and-drop zone with browse fallback, file list and per-file remove.',
    keywords: ['upload', 'drag drop', 'attachment', 'file'],
    source: { jsx: uploadJsx, css: uploadCss },
    props: [
      { name: 'accept', type: 'string', default: 'image/*', desc: 'Accepted MIME pattern' },
      { name: 'multiple', type: 'boolean', default: 'true', desc: 'Allow several files' },
    ],
    variants: [{ id: 'dropzone', title: 'Dropzone with file list', node: <div style={{ maxWidth: 420 }}><FileUpload /></div> }],
  },
  {
    id: 'otp-input', title: 'OTP Input', category: 'forms',
    description: 'One-time code boxes with auto-advance, backspace navigation and paste support.',
    keywords: ['otp', 'code', 'verification', 'pin'],
    source: { jsx: otpJsx, css: otpCss },
    props: [
      { name: 'length', type: 'number', default: '6', desc: 'Digit count' },
      { name: 'label', type: 'string', default: 'Enter verification code', desc: 'Field caption' },
    ],
    variants: [{ id: 'code', title: '6-digit code', node: <OtpInput /> }],
  },
]
