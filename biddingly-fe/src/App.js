import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import Header from "./Header";
import Login from "./Login";

function App() {
  return (
    <div className="container">

    <Router>
      <Header />
        <Routes>
          <Route exact path="/Login" element={<Login />} />            
          <Route exact path="/" element={<Login />} />
        </Routes>
      </Router>
      </div>
  );
}

export default App;
