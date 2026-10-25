import { ChatBubbles, ChatComposer, ReactionBar, CommentSection, ProfileHeader } from '../components/ui/social/Social.jsx'
import socialJsx from '../components/ui/social/Social.jsx?raw'
import socialCss from '../components/ui/social/Social.css?raw'

export default [
  {
    id: 'chat', title: 'Chat Bubbles & Composer', category: 'social',
    description: 'Two-way message bubbles with avatars and a working message input.',
    keywords: ['messaging', 'conversation', 'dm'],
    source: { jsx: socialJsx, css: socialCss },
    props: [],
    variants: [
      { id: 'bubbles', title: 'Conversation', node: <div style={{ maxWidth: 460, width: '100%' }}><ChatBubbles /><ChatComposer /></div> },
    ],
  },
  {
    id: 'reactions', title: 'Reaction Buttons', category: 'social',
    description: 'Single-choice reaction row with pressed states.',
    keywords: ['like', 'emoji reactions', 'feedback'],
    source: { jsx: socialJsx, css: socialCss },
    props: [],
    variants: [{ id: 'bar', title: 'Reaction row', node: <ReactionBar /> }],
  },
  {
    id: 'comments', title: 'Comment Section', category: 'social',
    description: 'Working comment thread — post a comment and it appears instantly.',
    keywords: ['discussion', 'thread', 'reply'],
    source: { jsx: socialJsx, css: socialCss },
    props: [],
    variants: [{ id: 'thread', title: 'Post a comment', node: <CommentSection /> }],
  },
  {
    id: 'profile-header', title: 'Profile Header', category: 'social',
    description: 'Cover, avatar, stats and follow actions for a member profile.',
    keywords: ['user profile', 'cover', 'follow'],
    source: { jsx: socialJsx, css: socialCss },
    props: [],
    variants: [{ id: 'header', title: 'Member profile', node: <ProfileHeader /> }],
  },
]
