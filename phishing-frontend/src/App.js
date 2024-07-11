import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [responses, setResponses] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/responses/')
            .then(response => {
                setResponses(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the data!', error);
            });
    }, []);

    return (
        <div className="App">
            <h1>Phishing Simulation Results</h1>
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
