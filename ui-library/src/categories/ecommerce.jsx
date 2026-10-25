import { ProductCard, PriceBreakdown, CouponField } from '../components/ui/ecommerce/ProductCard.jsx'
import { CartItems, OrderSummary } from '../components/ui/ecommerce/Cart.jsx'
import { CheckoutForm } from '../components/ui/ecommerce/CheckoutForm.jsx'
import ProductGallery from '../components/ui/ecommerce/ProductGallery.jsx'
import productJsx from '../components/ui/ecommerce/ProductCard.jsx?raw'
import productCss from '../components/ui/ecommerce/ProductCard.css?raw'
import cartJsx from '../components/ui/ecommerce/Cart.jsx?raw'
import cartCss from '../components/ui/ecommerce/Cart.css?raw'
import checkoutJsx from '../components/ui/ecommerce/CheckoutForm.jsx?raw'
import checkoutCss from '../components/ui/ecommerce/CheckoutForm.css?raw'
import galleryJsx from '../components/ui/ecommerce/ProductGallery.jsx?raw'
import galleryCss from '../components/ui/ecommerce/ProductGallery.css?raw'
import { GridLayout } from '../components/ui/layout/LayoutExtras.jsx'

export default [
  {
    id: 'product-card', title: 'Product Card', category: 'ecommerce',
    description: 'Catalog card with media, rating, price strike-through, add-to-cart and wishlist toggle.',
    keywords: ['shop', 'item', 'wishlist', 'price'],
    source: { jsx: productJsx, css: productCss },
    props: [
      { name: 'name / price / oldPrice', type: 'string', default: 'sample', desc: 'Product copy and pricing' },
      { name: 'badge', type: 'string', default: 'Bestseller', desc: 'Corner badge (null hides it)' },
    ],
    variants: [{ id: 'card', title: 'Catalog card', node: <GridLayout columns={2}><ProductCard /><ProductCard name="Mechanical Keyboard" price="₹6,999" oldPrice="₹8,499" badge="New" /></GridLayout> }],
  },
  {
    id: 'price-breakdown', title: 'Price Breakdown', category: 'ecommerce',
    description: 'Itemized totals with discount and tax rows.',
    keywords: ['totals', 'invoice math', 'cost'],
    source: { jsx: productJsx, css: productCss },
    props: [],
    variants: [{ id: 'totals', title: 'Cost breakdown', node: <PriceBreakdown /> }],
  },
  {
    id: 'coupon', title: 'Coupon Code', category: 'ecommerce',
    description: 'Promo input with success and error states — try code SAVE10.',
    keywords: ['promo', 'discount code', 'voucher'],
    source: { jsx: productJsx, css: productCss },
    props: [],
    variants: [{ id: 'apply', title: 'Apply promo (SAVE10)', node: <CouponField /> }],
  },
  {
    id: 'cart', title: 'Cart Items & Summary', category: 'ecommerce',
    description: 'Editable cart rows with quantity steppers, remove and an order summary panel.',
    keywords: ['basket', 'quantity', 'checkout prep'],
    source: { jsx: cartJsx, css: cartCss },
    props: [],
    variants: [
      { id: 'items', title: 'Cart with quantity controls', node: <CartItems /> },
      { id: 'summary', title: 'Order summary', node: <OrderSummary /> },
    ],
  },
  {
    id: 'checkout', title: 'Checkout Form', category: 'ecommerce',
    description: 'Full checkout with payment method radio cards, conditional card fields and success state.',
    keywords: ['payment', 'billing', 'place order'],
    source: { jsx: checkoutJsx, css: checkoutCss },
    props: [],
    variants: [{ id: 'form', title: 'Checkout flow', node: <CheckoutForm /> }],
  },
  {
    id: 'product-gallery', title: 'Product Gallery', category: 'ecommerce',
    description: 'Thumbnail switcher with a full-screen lightbox and Escape close.',
    keywords: ['images', 'lightbox', 'photos', 'zoom'],
    source: { jsx: galleryJsx, css: galleryCss },
    props: [],
    variants: [{ id: 'gallery', title: 'Gallery with lightbox', node: <ProductGallery /> }],
  },
]
