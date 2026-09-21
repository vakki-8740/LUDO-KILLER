import { Card } from "react-bootstrap";

/**
 * PageCard
 * Reusable card shell for every dashboard section.
 * - White background, 24px radius, 1px #dee2e6 border
 * - Bold card header with bottom border
 */
export default function PageCard({ title, headerRight, children, style, className }) {
  return (
    <Card className={className || ""} style={style || {}}>
      {(title || headerRight) && (
        <Card.Header className="d-flex justify-content-between align-items-center">
          <span>{title}</span>
          {headerRight}
        </Card.Header>
      )}
      <Card.Body className="p-3">
        {children}
      </Card.Body>
    </Card>
  );
}
