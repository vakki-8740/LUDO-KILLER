import { Card } from "react-bootstrap";

/**
 * StatCard
 * One of the four stat blocks on the Payments dashboard.
 * - Label (muted, medium weight)
 * - Large bold amount preceded by ₹
 * - Purple "View all" link on the right
 */
export default function StatCard({ label, amount, viewAllLabel = "View all" }) {
  return (
    <Card className="p-3 stat-card">
      <div className="d-flex justify-content-between align-items-start">
        <div>
          <div className="stat-label">{label}</div>
          <div className="stat-amount mt-1">{amount}</div>
        </div>
        {viewAllLabel && (
          <div className="stat-view-all">{viewAllLabel}</div>
        )}
      </div>
    </Card>
  );
}
