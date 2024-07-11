import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [email, setEmail] = useState('');
    const [responses, setResponses] = useState([]);
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

    const fetchResponses = () => {
        axios.get('http://localhost:8000/api/responses/')
            .then(response => {
                setResponses(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the data!', error);
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

            <h2>Simulation Results</h2>
            <button onClick={fetchResponses}>Load Results</button>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>User Info</th>
                        <th>Timestamp</th>
                    </tr>
                </thead>
                <tbody>
                    {responses.map(response => (
                        <tr key={response.id}>
                            <td>{response.id}</td>
                            <td>{response.user_info}</td>
                            <td>{response.timestamp}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default App;
