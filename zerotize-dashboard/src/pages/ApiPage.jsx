import { Link } from "react-router-dom";
import { HOME, API_CREDENTIALS } from "../routes";
import { PageCard } from "../components";

const PHP_SAMPLE = `<?php
# API URL
$url = "https://zerotize.in/api_payment_init";

# Define the data
$account_id    = "";              // Required - Account ID
$secret_key    = "";              // Required - Secret key
$payment_id    = "";              // Required - Unique payment ID
$payment_purpose = "";            // Optional - Max 30 characters
$payment_amount  = "";            // Required - Amount in INR
`;

export default function ApiPage() {
  return (
    <>
      <h2 className="zt-page-heading">API & Plugins</h2>

      {/* API Credentials & Plugins card */}
      <PageCard title="API Credentials & Plugins">
        <div className="d-flex flex-column gap-3">
          {/* Account ID */}
          <div className="d-flex justify-content-between align-items-start">
            <div className="zt-field-label">Account ID</div>
            <div className="zt-field-value font-monospace">UVIRVIT5</div>
          </div>

          {/* API Access */}
          <div className="d-flex justify-content-between align-items-start">
            <div className="zt-field-label">API Access</div>
            <div className="zt-field-value">Active</div>
          </div>

          {/* Secret Key */}
          <div className="d-flex justify-content-between align-items-start">
            <div className="zt-field-label">Secret Key</div>
            <div className="zt-field-value">
              <button className="btn btn-link zt-reset small">Change</button>
            </div>
          </div>

          {/* API Keys */}
          <div className="d-flex justify-content-between align-items-start">
            <div className="zt-field-label">API Keys</div>
            <div className="zt-field-value">
              <button className="btn btn-link zt-reset small">Download</button>
            </div>
          </div>

          {/* WooCommerce Plugin */}
          <div className="d-flex justify-content-between align-items-start">
            <div className="zt-field-label">WooCommerce Plugin</div>
            <div className="zt-field-value">
              <button className="btn btn-link zt-reset small">Download</button>
            </div>
          </div>
        </div>
      </PageCard>

      {/* Create Payment Request card */}
      <PageCard title="Create Payment Request" className="mt-3">
        <div
          className="bg-light rounded-2 p-3 font-monospace small text-break"
          style={{
            borderRadius: 16,
            border: "1px solid var(--zt-border)",
            background: "#f6f7f9",
            color: "#1a1d20",
          }}
        >
          {PHP_SAMPLE.split("\n").map((line, i) => (
            <div key={i} className="mb-1">{line}</div>
          ))}
        </div>
      </PageCard>

      <div className="mt-3">
        <Link to={HOME} className="text-decoration-none text-muted small">← Back to dashboard</Link>
      </div>
    </>
  );
}
