import React, { useState } from 'react';
import axios from 'axios';
import Dashboard from '../Dashboard_Social_Engineer';


function SocialEngineering() {
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    };

    const handleEmailSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/send_social_engineering/', { email })
            .then(response => {
                setMessage('Social engineering email sent successfully');
            })
            .catch(error => {
                setMessage('Failed to send social engineering email');
                console.error('There was an error processing the social engineering test!', error);
            });
    };

    function refreshPage() {
        window.location.reload(false);
      }

    return (
        <div className="SocialEngineering">
            <h1>Social Engineering Test</h1>
            <form onSubmit={handleEmailSubmit}>
                <label>
                    Enter email:
                    <input type="email" value={email} onChange={handleEmailChange} required />
                </label>
                <button type="submit">Send Social Engineering Email</button>
                <button onClick={refreshPage}>Refresh</button>

            </form>
            {message && <p>{message}</p>}

            <Dashboard />
        </div>
    );
}

export default SocialEngineering;
