import React, { useState } from 'react';
import axios from 'axios';

function PasswordTest() {
    const [password, setPassword] = useState('');
    const [strength, setStrength] = useState('');
    const [showPassword, setShowPassword] = useState(false);

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };

    const handlePasswordSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/password_test/', { password })
            .then(response => {
                setStrength(response.data.strength);
            })
            .catch(error => {
                console.error('There was an error testing the password!', error);
            });
    };

    const toggleShowPassword = () => {
        setShowPassword(!showPassword);
    };

    return (
        <div className="PasswordTest">
            <h1>Password Strength Test</h1>
            <form onSubmit={handlePasswordSubmit}>
                <label>
                    Enter Password:
                    <input 
                        type={showPassword ? "text" : "password"} 
                        value={password} 
                        onChange={handlePasswordChange} 
                        required 
                    />
                </label>
                <button type="button" onClick={toggleShowPassword}>
                    {showPassword ? "Hide Password" : "Show Password"}
                </button>
                <button type="submit">Test Password</button>
            </form>
            {strength && <p>Password Strength: {strength}</p>}
        </div>
    );
}

export default PasswordTest;
