import { useState } from 'react'
import CodePanel from './CodePanel.jsx'
import './ComponentStage.css'

const SIZES = [
  { id: 'desktop', label: 'Desktop', width: '100%' },
  { id: 'tablet', label: 'Tablet', width: '768px' },
  { id: 'mobile', label: 'Mobile', width: '375px' },
]

export default function ComponentStage({ entry }) {
  const [size, setSize] = useState('desktop')
  const [showCode, setShowCode] = useState(false)
  const width = SIZES.find((s) => s.id === size).width

  return (
    <div className="stage">
      {entry.variants.map((v) => (
        <section key={v.id} className="stage__block" aria-labelledby={`${entry.id}-${v.id}-t`}>
          <div className="stage__head">
            <h2 id={`${entry.id}-${v.id}-t`}>{v.title}</h2>
            <div className="stage__tools">
              <div className="stage__seg" role="group" aria-label="Preview size">
                {SIZES.map((s) => (
                  <button
                    key={s.id}
                    type="button"
                    data-size={s.id}
                    aria-pressed={size === s.id}
                    onClick={() => setSize(s.id)}
                  >
                    {s.label}
                  </button>
                ))}
              </div>
              <button
                type="button"
                className={`stage__code-btn${showCode ? ' is-on' : ''}`}
                aria-expanded={showCode}
                onClick={() => setShowCode((v2) => !v2)}
              >
                {showCode ? 'Hide Code' : 'View Code'}
              </button>
            </div>
          </div>
          <div className="stage__area own-stage">
            {size !== 'desktop' && <p className="stage__size-tag">{size} preview · {width}</p>}
            <div className="stage__frame" style={{ maxWidth: width }}>
              <div className="stage__render">{v.node}</div>
            </div>
          </div>
          {showCode && <CodePanel source={entry.source} />}
        </section>
      ))}
    </div>
  )
}
