import { Link } from "react-router-dom";
import { HOME, PROFILE } from "../routes";
import { PageCard } from "../components";

export default function ProfilePage() {
  return (
    <>
      <h2 className="zt-page-heading">Profile</h2>

      <PageCard
        title="Profile"
        headerRight={
          <button className="btn btn-link zt-reset">
            <Link to={HOME} className="text-danger text-decoration-none" style={{ fontWeight: 600 }}>
              Logout
            </Link>
          </button>
        }
      >
        <div className="d-flex flex-column gap-3">
          {/* Created */}
          <div>
            <div className="zt-field-label">Created</div>
            <div className="zt-field-value">18 Sep 2026, 11:20 AM</div>
          </div>

          {/* Account ID */}
          <div>
            <div className="zt-field-label">Account ID</div>
            <div className="zt-field-value font-monospace">UVIRVIT5</div>
          </div>

          {/* Name */}
          <div>
            <div className="zt-field-label">Name</div>
            <div className="zt-field-value">Vaseem Ansari</div>
          </div>

          {/* Phone */}
          <div>
            <div className="zt-field-label">Phone</div>
            <div className="zt-field-value">+91 98765 43210</div>
          </div>

          {/* Email */}
          <div>
            <div className="zt-field-label">Email</div>
            <div className="zt-field-value">vaseem@example.com</div>
          </div>

          {/* Profile Picture */}
          <div>
            <div className="zt-field-label">Profile Picture</div>
            <div className="zt-field-value">
              <button className="btn btn-link zt-reset small">Upload logo</button>
            </div>
          </div>

          {/* KYC Documents */}
          <div>
            <div className="zt-field-label">KYC Documents</div>
            <div className="zt-field-value">
              <button className="btn btn-link zt-reset small">Upload document</button>
            </div>
          </div>

          {/* Validity */}
          <div>
            <div className="zt-field-label">Validity</div>
            <div className="zt-field-value">Until 18 Sep 2027</div>
          </div>

          {/* KYC Status */}
          <div>
            <div className="zt-field-label">KYC Status</div>
            <div className="zt-field-value">Verified</div>
          </div>

          {/* Password */}
          <div>
            <div className="zt-field-label">Password</div>
            <div className="zt-field-value">
              <button className="btn btn-link zt-reset small">Change now</button>
            </div>
          </div>

          {/* Status */}
          <div>
            <div className="zt-field-label">Status</div>
            <div className="zt-field-value">Active</div>
          </div>
        </div>
      </PageCard>

      <div className="mt-3">
        <Link to={HOME} className="text-decoration-none text-muted small">← Back to dashboard</Link>
      </div>
    </>
  );
}
