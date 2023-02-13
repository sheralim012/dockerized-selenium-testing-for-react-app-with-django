import React, { useState } from "react";
import axios from 'axios';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = async event => {
    event.preventDefault();
    let resp = await axios.post(`http://django:8001/users/token/`, { username, password });
    const { token } = resp.data;
    const config = {
      headers: { Authorization: `Token ${token}` }
    };
    resp = await axios.get('http://django:8001/users/profile/', config);
    const { email } = resp.data;
    setEmail(email);
  };

  return (
    <>
      <form onSubmit={handleSubmit} className="mb-3">
        <div className="row mb-3">
          <label htmlFor="username" className="col-sm-2 col-form-label">Username</label>
          <div className="col-sm-4">
            <input type="text" className="form-control" id="username" value={username} onChange={e => setUsername(e.target.value)} />
          </div>
        </div>
        <div className="row mb-3">
          <label htmlFor="password" className="col-sm-2 col-form-label">Password</label>
          <div className="col-sm-4">
            <input type="password" className="form-control" id="password" value={password} onChange={e => setPassword(e.target.value)} />
          </div>
        </div>
        <button type="submit" className="btn btn-primary">Login</button>
      </form>
      {email && <div id="user-info">Email: {email}</div>}
    </>
  );
}

export default Login;
