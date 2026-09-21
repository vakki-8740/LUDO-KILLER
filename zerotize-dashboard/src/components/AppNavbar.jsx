import React from "react";
import { Navbar, Container, Offcanvas, Button } from "react-bootstrap";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { FiMenu } from "react-icons/fi";
import { HOME, LINKS, CHECKOUT, SUPPORT, PROFILE, API_CREDENTIALS } from "../routes";

/**
 * AppNavbar
 * - White top bar
 * - Purple "Zerotize" logo on the left (rect + Z mark + wordmark)
 * - Purple hamburger icon on the right (mobile only)
 * - Opens an Offcanvas menu on mobile
 */
export default function AppNavbar() {
  const location = useLocation();
  const navigate = useNavigate();
  const [open, setOpen] = React.useState(false);

  // Close the menu when the route changes
  React.useEffect(() => {
    setOpen(false);
  }, [location.pathname]);

  const menu = [
    { label: "Payments", to: HOME },
    { label: "Links", to: LINKS },
    { label: "Checkout", to: CHECKOUT },
    { label: "Tickets", to: SUPPORT },
    { label: "Profile", to: PROFILE },
    { label: "API & Plugins", to: API_CREDENTIALS },
  ];

  return (
    <>
      <Navbar fixed="top" expand="lg" className="zt-navbar">
        <Container fluid className="px-3">
          {/* Zerotize logo */}
          <Link
            to={HOME}
            className="navbar-brand d-flex align-items-center text-decoration-none me-auto"
          >
            <span className="zt-logo-box">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden>
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
                <path
                  d="M10 6L4 12M10 6L16 6"
                  stroke="#ffffff"
                  strokeWidth="2.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  opacity="0.9"
                />
              </svg>
              <span style={{ fontWeight: 700, color: "#fff", fontSize: "1.05rem" }}>
                Zerotize
              </span>
            </span>
          </Link>

          {/* Hamburger menu (mobile only) */}
          <Button
            variant="link"
            className="zt-hamburger d-lg-none"
            onClick={() => setOpen(true)}
            aria-label="Open menu"
          >
            <FiMenu size={24} color="#5222d8" />
          </Button>
        </Container>
      </Navbar>

      {/* Mobile offcanvas */}
      <Offcanvas show={open} onHide={() => setOpen(false)} placement="end" className="zt-offcanvas">
        <Offcanvas.Header closeButton className="p-3">
          <Offcanvas.Title className="d-flex align-items-center text-decoration-none">
            <span className="zt-logo-box me-2">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden>
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
                <path
                  d="M10 6L4 12M10 6L16 6"
                  stroke="#ffffff"
                  strokeWidth="2.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  opacity="0.9"
                />
              </svg>
              <span style={{ fontWeight: 700 }}>Zerotize</span>
            </span>
          </Offcanvas.Title>
        </Offcanvas.Header>
        <Offcanvas.Body className="py-2">
          {menu.map((item) => (
            <Button
              key={item.to}
              variant="ghost"
              className="zt-menu-item w-100 text-start mb-1"
              onClick={() => navigate(item.to)}
            >
              {item.label}
            </Button>
          ))}
        </Offcanvas.Body>
      </Offcanvas>
    </>
  );
}
