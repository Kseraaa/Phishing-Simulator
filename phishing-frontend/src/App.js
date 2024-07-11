import React, { useState } from 'react';
import axios from 'axios';
import Dashboard from './Dashboard';

function App() {
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    };

    const handleEmailSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/send_phishing_email/', { email })
            .then(response => {
                setMessage('Phishing email sent successfully');
            })
            .catch(error => {
                setMessage('Failed to send phishing email');
            });
    };

    return (
        <div className="App">
            <h1>Phishing Simulation</h1>
            
            <form onSubmit={handleEmailSubmit}>
                <label>
                    Enter email to phish:
                    <input type="email" value={email} onChange={handleEmailChange} required />
                </label>
                <button type="submit">Send Phishing Email</button>
            </form>
            {message && <p>{message}</p>}

            <Dashboard />
        </div>
    );
}

export default App;
