import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import PlayerLoginSignup from "./pages/PlayerLoginSignup";
import AdminLoginSignup from "./pages/AdminLoginSignup";
import "./App.css";
import courtIllustration from './assets/court-illustration.png';

function App() {
  return (
    <Router>
      <Routes>
        {/* Landing Page */}
        <Route
          path="/"
          element={
            <div className="container">
              <div className="hero">
                <img
                  src={courtIllustration}
                  alt="Football Court Illustration"
                  className="hero-image"
                />
                <div className="hero-text">
                  <h1>Tegy Hagz</h1>
                  <p>Your Football Court Connection</p>
                  <p>
                    Tegy Hagz is a web platform designed for football enthusiasts.
                    Whether you're a player, court owner, or administrator, Tegy Hagz
                    provides a seamless and intuitive experience for booking and
                    managing football courts.
                  </p>
                  <div className="buttons">
                    {/* Navigate to Login/Signup pages */}
                    <Link to="/player" className="btn">Player</Link>
                    <Link to="/admin" className="btn">Admin</Link>
                  </div>
                </div>
              </div>
            </div>
          }
        />

        {/* Login/Signup pages for Player and Admin */}
        <Route path="/player" element={<PlayerLoginSignup />} />
        <Route path="/admin" element={<AdminLoginSignup />} />
      </Routes>
    </Router>
  );
}

export default App;