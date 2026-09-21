import { useState } from "react";
import { Card, Form, Button, InputGroup } from "react-bootstrap";
import { Link } from "react-router-dom";
import { HOME, CHECKOUT } from "../routes";
import { PageCard, UploadInput } from "../components";

const SELECT_OPTIONS = [
  { value: "Enable", label: "Enable" },
  { value: "Disable", label: "Disable" },
];

export default function CheckoutPage() {
  // User Input
  const [purposeInput, setPurposeInput] = useState("Disable");
  const [nameInput, setNameInput] = useState("Disable");
  const [phoneInput, setPhoneInput] = useState("Disable");
  const [emailInput, setEmailInput] = useState("Disable");

  // Checkout Message
  const [message, setMessage] = useState("LUDO CLUB DEPOSITE");

  // Checkout Advertisement
  const [adLink, setAdLink] = useState("");

  const handleUserInputUpdate = () => {
    // Mock update
    alert("User input updated");
  };

  const handleMessageUpdate = () => {
    // Mock update
    alert("Checkout message updated");
  };

  const handleAdUpdate = () => {
    // Mock update
    alert("Advertisement updated");
  };

  return (
    <>
      <h2 className="zt-page-heading">Checkout Settings</h2>

      {/* User Input card */}
      <PageCard title="User Input">
        <Form.Select
          className="mb-2"
          value={purposeInput}
          onChange={(e) => setPurposeInput(e.target.value)}
        >
          {SELECT_OPTIONS.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </Form.Select>
        <div className="mb-2">
          <div className="d-flex justify-content-between mb-1">
            <span className="zt-field-label">Purpose</span>
          </div>
          <Form.Select value={purposeInput} onChange={(e) => setPurposeInput(e.target.value)} />
        </div>
        <div className="mb-2">
          <div className="d-flex justify-content-between mb-1">
            <span className="zt-field-label">Name</span>
          </div>
          <Form.Select value={nameInput} onChange={(e) => setNameInput(e.target.value)}>
            {SELECT_OPTIONS.map((opt) => (
              <option key={opt.value} value={opt.value}>
                {opt.label}
              </option>
            ))}
          </Form.Select>
        </div>
        <div className="mb-2">
          <div className="d-flex justify-content-between mb-1">
            <span className="zt-field-label">Phone</span>
          </div>
          <Form.Select value={phoneInput} onChange={(e) => setPhoneInput(e.target.value)}>
            {SELECT_OPTIONS.map((opt) => (
              <option key={opt.value} value={opt.value}>
                {opt.label}
              </option>
            ))}
          </Form.Select>
        </div>
        <div className="mb-2">
          <div className="d-flex justify-content-between mb-1">
            <span className="zt-field-label">Email</span>
          </div>
          <Form.Select value={emailInput} onChange={(e) => setEmailInput(e.target.value)}>
            {SELECT_OPTIONS.map((opt) => (
              <option key={opt.value} value={opt.value}>
                {opt.label}
              </option>
            ))}
          </Form.Select>
        </div>
        <Button variant="primary" className="w-100 mt-2" onClick={handleUserInputUpdate}>
          Update
        </Button>
      </PageCard>

      {/* Checkout Message card */}
      <PageCard
        title="Checkout Message"
        headerRight={<button className="btn btn-link zt-reset" onClick={() => setMessage("")}>Reset</button>}
      >
        <div className="mb-2">
          <div className="zt-field-label">Message</div>
          <Form.Control
            as="textarea"
            rows={4}
            className="mb-3"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </div>
        <Button variant="primary" className="w-100" onClick={handleMessageUpdate}>
          Update
        </Button>
      </PageCard>

      {/* Checkout Advertisement card */}
      <PageCard title="Checkout Advertisement">
        <UploadInput
          label="Advertisement image"
          placeholder="Upload image..."
          name="adImage"
        />
        <div className="mb-3">
          <div className="zt-field-label">Advertisement link</div>
          <Form.Control
            type="url"
            placeholder="Enter advertisement link"
            value={adLink}
            onChange={(e) => setAdLink(e.target.value)}
            className="mb-3"
          />
        </div>
        <Button variant="primary" className="w-100" onClick={handleAdUpdate}>
          Update
        </Button>
      </PageCard>

      <div className="mt-3">
        <Link to={HOME} className="text-decoration-none text-muted small">← Back to dashboard</Link>
      </div>
    </>
  );
}
