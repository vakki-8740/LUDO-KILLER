import { useState } from "react";
import { Card, Form, Button, InputGroup } from "react-bootstrap";
import { Link } from "react-router-dom";
import { HOME, SUPPORT } from "../routes";
import { PageCard, UploadInput, DataTable } from "../components";

// Mock tickets
const TICKETS_DATA = [
  {
    timestamp: "15-09-2026 06:40:50 PM",
    ticketId: "9sqSOyM7",
    subject: "Plan not active",
    lastMessage: "Use our support link to activate.",
  },
  {
    timestamp: "14-09-2026 11:20:00 PM",
    ticketId: "k8Rv4TnQ",
    subject: "Refund request",
    lastMessage: "Please share transaction ID.",
  },
];

export default function TicketsPage() {
  const [search, setSearch] = useState("");
  const [subject, setSubject] = useState("");
  const [message, setMessage] = useState("");
  const [attachment, setAttachment] = useState(null);

  const filterTickets = TICKETS_DATA.filter(
    (t) =>
      t.subject.toLowerCase().includes(search.toLowerCase()) ||
      t.ticketId.toLowerCase().includes(search.toLowerCase())
  );

  const handleSubmit = () => {
    if (!subject || !message) return;
    alert("Ticket submitted");
    setSubject("");
    setMessage("");
    setAttachment(null);
  };

  return (
    <>
      <h2 className="zt-page-heading">Support Tickets</h2>

      {/* Open Ticket card */}
      <PageCard title="Open Ticket">
        <div className="mb-2">
          <div className="zt-field-label">Subject</div>
          <Form.Control
            type="text"
            placeholder="Enter subject"
            value={subject}
            onChange={(e) => setSubject(e.target.value)}
            className="mb-2"
          />
        </div>
        <div className="mb-2">
          <div className="zt-field-label">Message</div>
          <Form.Control
            as="textarea"
            rows={4}
            placeholder="Enter message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            className="mb-3"
          />
        </div>
        <div className="mb-3">
          <div className="zt-field-label">Attachment</div>
          <InputGroup>
            <Form.Control
              readOnly
              placeholder="Upload image..."
              className="upload-value"
            />
            <Button variant="outline-secondary" className="upload-browse">
              Browse
            </Button>
          </InputGroup>
        </div>
        <Button variant="primary" className="w-100" onClick={handleSubmit}>
          Submit
        </Button>
      </PageCard>

      {/* Search */}
      <Card className="p-3 mt-3 mb-3">
        <Form.Control
          type="text"
          className="zt-search"
          placeholder="Search..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </Card>

      {/* Tickets table */}
      <Card className="mt-3" style={{ borderRadius: 24 }}>
        <div style={{ padding: "1.2rem 1.7rem", fontWeight: 700, borderBottom: "1px solid var(--zt-border)" }}>
          Tickets
        </div>
        <div className="table-responsive" style={{ borderRadius: "0 0 24px 24px" }}>
          <table className="table align-middle mb-0">
            <thead>
              <tr>
                <th>Timestamp</th>
                <th>Ticket ID</th>
                <th>Subject</th>
                <th>Last Message</th>
              </tr>
            </thead>
            <tbody>
              {filterTickets.map((row) => (
                <tr key={row.ticketId}>
                  <td>{row.timestamp}</td>
                  <td>
                    <span className="zt-id">{row.ticketId}</span>
                  </td>
                  <td>{row.subject}</td>
                  <td>{row.lastMessage}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        {/* Purple indicator bar at bottom of card (matches screenshot) */}
        <div
          style={{
            height: 4,
            background: "var(--zt-primary)",
            borderRadius: "0 0 24px 24px",
            marginTop: -1,
          }}
          aria-hidden
        />
      </Card>

      <div className="mt-3">
        <Link to={HOME} className="text-decoration-none text-muted small">← Back to dashboard</Link>
      </div>
    </>
  );
}
