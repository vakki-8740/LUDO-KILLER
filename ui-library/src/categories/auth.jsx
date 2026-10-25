import { LoginForm, SignupForm, ForgotPasswordForm, TwoFactorForm } from '../components/ui/auth/AuthForms.jsx'
import authJsx from '../components/ui/auth/AuthForms.jsx?raw'
import authCss from '../components/ui/auth/AuthForms.css?raw'

export default [
  {
    id: 'login-form', title: 'Login Form', category: 'auth',
    description: 'Sign-in card with validation-ready fields, remember me and loading submit.',
    keywords: ['signin', 'log in', 'credentials'],
    source: { jsx: authJsx, css: authCss },
    props: [],
    variants: [{ id: 'login', title: 'Sign in', node: <LoginForm /> }],
  },
  {
    id: 'signup-form', title: 'Signup Form', category: 'auth',
    description: 'Account creation with password guidance and terms agreement.',
    keywords: ['register', 'create account', 'join'],
    source: { jsx: authJsx, css: authCss },
    props: [],
    variants: [{ id: 'signup', title: 'Create account', node: <SignupForm /> }],
  },
  {
    id: 'forgot-password', title: 'Forgot Password', category: 'auth',
    description: 'Reset request flow with a success confirmation state.',
    keywords: ['recovery', 'reset', 'email'],
    source: { jsx: authJsx, css: authCss },
    props: [],
    variants: [{ id: 'reset', title: 'Reset request', node: <ForgotPasswordForm /> }],
  },
  {
    id: 'two-factor', title: 'Two-Factor Verification', category: 'auth',
    description: 'OTP-based two-step verification built on the OTP input component.',
    keywords: ['2fa', 'otp', 'authenticator', 'security'],
    source: { jsx: authJsx, css: authCss },
    props: [],
    variants: [{ id: '2fa', title: 'Two-step verification', node: <TwoFactorForm /> }],
  },
]
