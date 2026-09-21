import { useLocation, useNavigate } from "react-router-dom";
import { Container } from "react-bootstrap";
import { HOME, LINKS, CHECKOUT, SUPPORT, PROFILE, API_CREDENTIALS } from "./routes";
import { Routes, Route } from "react-router-dom";
import "./App.css";

import AppNavbar from "./components/AppNavbar";
import PaymentsPage from "./pages/PaymentsPage";
import LinksPage from "./pages/LinksPage";
import CheckoutPage from "./pages/CheckoutPage";
import TicketsPage from "./pages/TicketsPage";
import ProfilePage from "./pages/ProfilePage";
import ApiPage from "./pages/ApiPage";

export default function App() {
  const location = useLocation();
  const navigate = useNavigate();

  // Offcanvas mirror only; real menu is rendered by AppNavbar
  const [offcanvasOpen, setOffcanvasOpen] = React.useState(false);

  // Close the offcanvas menu on route change
  React.useEffect(() => {
    setOffcanvasOpen(false);
  }, [location.pathname]);

  return (
    <div className="app-shell">
      <AppNavbar />

      <main className="app-main">
        <Container fluid className="px-3 pt-4 pb-5">
          <Routes>
            <Route path={HOME} element={<PaymentsPage />} />
            <Route path={LINKS} element={<LinksPage />} />
            <Route path={CHECKOUT} element={<CheckoutPage />} />
            <Route path={SUPPORT} element={<TicketsPage />} />
            <Route path={PROFILE} element={<ProfilePage />} />
            <Route path={API_CREDENTIALS} element={<ApiPage />} />
          </Routes>
        </Container>
      </main>

      {/* Mobile offcanvas backoff (kept in sync with AppNavbar until
          that component is the single source for the menu.) */}
      {offcanvasOpen && (
        <div
          className="offcanvas-backdrop fade show"
          style={{ position: "fixed", inset: 0, zIndex: 1040 }}
          onClick={() => setOffcanvasOpen(false)}
        />
      )}
    </div>
  );
}
