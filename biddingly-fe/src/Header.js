import React from "react";
import {
  Link
} from "react-router-dom";

function Header() {
  return (
    
      <nav className="navbar navbar-expand-lg bg-light mb-5">
  <div className="container-fluid">
          <Link to="/" className="navbar-brand">Biddingly</Link>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarSupportedContent">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
        <li className="nav-item">
                <Link to="/" className="nav-link" aria-current="page">Home</Link>
        </li>
            </ul>
            <Link to="/login" className="btn btn-outline-success">Login</Link>
    </div>
  </div>
</nav>
  );
}

export default Header;