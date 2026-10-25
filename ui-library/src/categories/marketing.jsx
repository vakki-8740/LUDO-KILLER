import { PricingSection, TestimonialCard, FeatureSection, CtaBanner, ErrorPage, FaqSection } from '../components/ui/marketing/Marketing.jsx'
import marketingJsx from '../components/ui/marketing/Marketing.jsx?raw'
import marketingCss from '../components/ui/marketing/Marketing.css?raw'

export default [
  {
    id: 'pricing', title: 'Pricing Section', category: 'marketing',
    description: 'Three-tier pricing cards with a featured plan ribbon and feature lists.',
    keywords: ['plans', 'tiers', 'subscription'],
    source: { jsx: marketingJsx, css: marketingCss },
    props: [],
    variants: [{ id: 'tiers', title: 'Plan comparison', node: <PricingSection /> }],
  },
  {
    id: 'testimonial', title: 'Testimonial', category: 'marketing',
    description: 'Quote card with author identity and a verified badge.',
    keywords: ['review', 'quote', 'social proof'],
    source: { jsx: marketingJsx, css: marketingCss },
    props: [],
    variants: [{ id: 'quote', title: 'Customer quote', node: <TestimonialCard /> }],
  },
  {
    id: 'features', title: 'Feature Section', category: 'marketing',
    description: 'Icon feature grid explaining product capabilities.',
    keywords: ['feature grid', 'highlights', 'benefits'],
    source: { jsx: marketingJsx, css: marketingCss },
    props: [],
    variants: [{ id: 'grid', title: 'Feature grid', node: <FeatureSection /> }],
  },
  {
    id: 'cta-banner', title: 'Call to Action Banner', category: 'marketing',
    description: 'Gradient conversion banner with primary and outline actions.',
    keywords: ['cta', 'conversion', 'banner'],
    source: { jsx: marketingJsx, css: marketingCss },
    props: [],
    variants: [{ id: 'banner', title: 'Conversion banner', node: <CtaBanner /> }],
  },
  {
    id: 'faq', title: 'FAQ Section', category: 'marketing',
    description: 'Multi-open accordion wrapped in a marketing section header.',
    keywords: ['questions', 'help', 'accordion'],
    source: { jsx: marketingJsx, css: marketingCss },
    props: [],
    variants: [{ id: 'faq', title: 'Frequently asked questions', node: <FaqSection /> }],
  },
  {
    id: 'error-404', title: 'Error Page (404)', category: 'marketing',
    description: 'Friendly not-found state with a recovery action.',
    keywords: ['not found', 'error', 'lost'],
    source: { jsx: marketingJsx, css: marketingCss },
    props: [
      { name: 'code', type: 'string', default: '404', desc: 'Error code shown prominently' },
    ],
    variants: [{ id: '404', title: 'Not found', node: <ErrorPage code="404" /> }],
  },
]
