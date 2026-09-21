import { useState } from "react";
import { Card, Row, Col, Form, Button, InputGroup } from "react-bootstrap";
import { QRCodeSVG } from "qrcode.react";
import { Link } from "react-router-dom";
import { HOME, LINKS } from "../routes";
import { PageCard, DataTable } from "../components";

// Mock links table
const LINKS_DATA = [
  { timestamp: "18-09-2026 11:51:45 PM", linkId: "7j6LEL48", purpose: "Ludo killer deposit", amount: 100 },
  { timestamp: "17-09-2026 12:23:44 PM", linkId: "caOoEROu", purpose: "Ludo club deposite", amount: 100 },
  { timestamp: "15-09-2026 07:10:45 PM", linkId: "2pTqgDM9", purpose: "Deposite", amount: 100 },
];

export default function LinksPage() {
  const [purpose, setPurpose] = useState("");
  const [amount, setAmount] = useState("");
  const [redirect, setRedirect] = useState("");
  const [created, setCreated] = useState(null);
  const [defaultLink, setDefaultLink] = useState("https://zerotize.in/7j6LEL48");
  const [copied, setCopied] = useState(false);

  const handleCreate = () => {
    if (!purpose || !amount) return;
    const newId = Math.random().toString(36).slice(2, 10).toUpperCase();
    setCreated({ id: newId, purpose, amount: parseInt(amount), redirect });
    setPurpose("");
    setAmount("");
    setRedirect("");
  };

  const handleCopy = () => {
    navigator.clipboard?.writeText(defaultLink).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    });
  };

  return (
    <>
      <h2 className="zt-page-heading">Links</h2>

      {/* Create Link card */}
      <PageCard title="Create Link">
        <Form.Control
          type="text"
          className="mb-2"
          placeholder="Enter purpose"
          value={purpose}
          onChange={(e) => setPurpose(e.target.value)}
        />
        <Form.Control
          type="number"
          className="mb-2"
          placeholder="Enter amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <Form.Control
          type="url"
          className="mb-3"
          placeholder="Enter redirect URL"
          value={redirect}
          onChange={(e) => setRedirect(e.target.value)}
        />
        <Button variant="primary" className="w-100" onClick={handleCreate}>
          Create
        </Button>
        {created && (
          <div className="alert alert-success mt-3 py-2 px-3" style={{ borderRadius: 12, fontWeight: 500 }}>
            Link created: <span className="zt-id">{created.id}</span>
          </div>
        )}
      </PageCard>

      {/* Search */}
      <Card className="p-3 mt-3 mb-3">
        <Form.Control
          type="text"
          className="zt-search"
          placeholder="Search..."
        />
      </Card>

      {/* Links table */}
      <DataTable
        columns={[
          { key: "timestamp", label: "Timestamp" },
          { key: "linkId", label: "Link ID", cellType: "zt-id" },
          { key: "purpose", label: "Purpose" },
          { key: "amount", label: "Amount", cellType: "rupee", render: (row) => `${row.amount}` },
        ]}
        rows={LINKS_DATA.map((row) => ({
          key: row.linkId,
          timestamp: row.timestamp,
          linkId: row.linkId,
          purpose: row.purpose,
          amount: row.amount,
        }))}
      />

      {/* Default Link card */}
      <PageCard title="Default Link" className="mt-3">
        <InputGroup className="mb-3">
          <Form.Control
            readOnly
            value={defaultLink}
            className="font-monospace text-break"
            onChange={() => {}}
          />
          <Button variant="primary" onClick={handleCopy}>
            {copied ? "Copied" : "Copy"}
          </Button>
        </InputGroup>

        {/* Share buttons: WhatsApp green, Facebook blue, X black, Telegram light blue */}
        <div className="d-flex justify-content-around flex-wrap gap-2 mt-2">
          <Button variant="whatsapp" className="share-btn rounded-pill px-3" href={`https://wa.me/?text=${encodeURIComponent(defaultLink)}`} target="_blank">
            WhatsApp
          </Button>
          <Button variant="facebook" className="share-btn rounded-pill px-3" href={`https://facebook.com/sharer/sharer.php?u=${encodeURIComponent(defaultLink)}`} target="_blank">
            Facebook
          </Button>
          <Button variant="x" className="share-btn rounded-pill px-3" href={`https://x.com/intent/tweet?url=${encodeURIComponent(defaultLink)}`} target="_blank">
            X
          </Button>
          <Button variant="telegram" className="share-btn rounded-pill px-3" href={`https://t.me/share/url?url=${encodeURIComponent(defaultLink)}&text=Pay%20via%20Zerotize`} target="_blank">
            Telegram
          </Button>
        </div>
      </PageCard>

      {/* Link QR card */}
      <PageCard
        title="Link QR"
        headerRight={<Link to={HOME} className="zt-id small text-decoration-none">Download</Link>}
        className="mt-3 d-flex flex-column align-items-center"
      >
        <div className="py-3">
          <QRCodeSVG value={defaultLink} size={220} level="M" />
        </div>
        <p className="text-center mb-0" style={{ fontSize: "1rem" }}>
          Scan QR code to pay
        </p>
        <p className="text-center mt-3 mb-0" style={{ color: "var(--zt-muted)", fontSize: "0.85rem" }}>
          Powered by{" "}
          <span className="zt-logo-box d-inline-flex align-items-center gap-1" style={{ fontSize: "0.75rem", padding: "4px 6px" }}>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden>
              <path
                d="M4 6L10 12L4 18"
                stroke="#fff"
                strokeWidth="2.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
              <path
                d="M10 6H20C21.1 6 22 6.9 22 8V16C22 17.1 21.1 18 20 18H10"
                stroke="#fff"
                strokeWidth="2.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
            Zerotize
          </span>
        </p>
      </PageCard>

      <div className="mt-3">
        <Link to={HOME} className="text-decoration-none text-muted small">← Back to dashboard</Link>
      </div>
    </>
  );
}
