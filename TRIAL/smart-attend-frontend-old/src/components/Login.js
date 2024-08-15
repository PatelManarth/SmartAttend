import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { fetchFromBackend } from '../utils/api';

function Login() {
  const [role, setRole] = useState('student');
  const [id, setId] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    const endpoint = role === 'student' ? 'student/login' : 'faculty/login';
    const payload = role === 'student' ? { studentId: id, password } : { email: id, password };
    
    try {
      const response = await fetchFromBackend(endpoint, 'POST', payload);
      if (response.success) {
        sessionStorage.setItem('ROLE', role === 'student' ? '0' : '1');
        if (role === 'student') {
          navigate('/student/home');
        } else {
          navigate('/faculty/home');
        }
      } else {
        alert('Login failed');
      }
    } catch (error) {
      console.error(error);
      alert('Login failed');
    }
  };

  const handleZoomLogin = () => {
    // Integrate Zoom OAuth here
  };

  return (
    <div className="login-container">
      <h1>Login</h1>
      <select onChange={(e) => setRole(e.target.value)}>
        <option value="student">Student</option>
        <option value="faculty">Faculty</option>
      </select>
      <input
        type="text"
        placeholder={role === 'student' ? 'Student ID' : 'Email'}
        value={id}
        onChange={(e) => setId(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Login</button>
      <button onClick={handleZoomLogin}>Login with Zoom</button>
    </div>
  );
}

export default Login;
