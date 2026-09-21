import { useState } from "react";
import { Card, Row, Col, Form, InputGroup } from "react-bootstrap";
import { Link } from "react-router-dom";
import { HOME, LINKS, CHECKOUT } from "../routes";
import { PageCard, StatCard, DataTable } from "../components";

// Mock data
const STATS = [
  { label: "Today", amount: 128450, viewAll: "View all" },
  { label: "Pending", amount: 23600, viewAll: "View all" },
  { label: "Success", amount: 104200, viewAll: "View all" },
  { label: "Failed", amount: 550, viewAll: "View all" },
];

const PAYMENTS = [
  { timestamp: "18-09-2026 11:51:45 PM", paymentId: "7j6LEL48", customer: "Rohan Verma", amount: 200, status: "Success" },
  { timestamp: "18-09-2026 09:20:10 PM", paymentId: "caOoEROu", customer: "Sneha Iyer", amount: 500, status: "Pending" },
  { timestamp: "17-09-2026 12:23:44 PM", paymentId: "2pTqgDM9", customer: "Amit Singh", amount: 1000, status: "Success" },
  { timestamp: "17-09-2026 08:05:33 AM", paymentId: "k3Wx9P2v", customer: "Pooja Desai", amount: 150, status: "Failed" },
  { timestamp: "16-09-2026 11:40:02 PM", paymentId: "m8Rv4TnQ", customer: "Vikram Rao", amount: 300, status: "Success" },
  { timestamp: "16-09-2026 06:12:18 PM", paymentId: "h7Yc2ZsL", customer: "Anjali Mehta", amount: 400, status: "Pending" },
];

export default function PaymentsPage() {
  const [search, setSearch] = useState("");

  const filtered = PAYMENTS.filter((row) =>
    row.customer.toLowerCase().includes(search.toLowerCase()) ||
    row.paymentId.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <>
      <h2 className="zt-page-heading">Payments</h2>

      {/* Stat cards */}
      <Row className="g-3">
        {STATS.map((stat) => (
          <Col key={stat.label} xs={12} sm={6} lg={3}>
            <StatCard label={stat.label} amount={stat.amount} viewAllLabel={stat.viewAll} />
          </Col>
        ))}
      </Row>

      {/* Search */}
      <Card className="p-3 mt-3 mb-3">
        <Form.Control
          type="text"
          className="zt-search"
          placeholder="Search by customer or payment ID..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </Card>

      {/* Table */}
      <DataTable
        columns={[
          { key: "timestamp", label: "Timestamp" },
          { key: "paymentId", label: "Payment ID", cellType: "zt-id" },
          { key: "customer", label: "Customer" },
          { key: "amount", label: "Amount", cellType: "rupee", render: (row) => `${row.amount}` },
          { key: "status", label: "Status" },
        ]}
        rows={filtered.map((row) => ({
          key: row.paymentId,
          timestamp: row.timestamp,
          paymentId: row.paymentId,
          customer: row.customer,
          amount: row.amount,
          status: row.status,
        }))}
      />

      {/* Page nav */}
      <div className="d-flex justify-content-between mt-4">
        <div className="d-flex gap-2">
          <Link to={LINKS} className="btn btn-outline-secondary btn-sm">Links</Link>
          <Link to={CHECKOUT} className="btn btn-outline-secondary btn-sm">Checkout</Link>
        </div>
        <Link to={HOME} className="text-decoration-none text-muted small">← Back to dashboard</Link>
      </div>
    </>
  );
}
