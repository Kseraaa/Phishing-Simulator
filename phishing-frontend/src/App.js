import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import PhishingSimulator from './pages/PhishingSimulator';
import BruteForceAttack from './pages/BruteForceAttack';
import Ransomeware from './pages/Ransomeware';
import PasswordTest from './pages/PasswordTest';
import SocialEngineer from './pages/SocialEngineer';
import Home from './Home';

import './App.css'; // Import CSS for styling

function App() {
    return (
        <Router>
            <div className="App">
                <nav className="navbar">
                    <ul>
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/phishing-simulator">Phishing</Link></li>
                        <li><Link to="/brute-force-attack">Brute Force</Link></li>
                        <li><Link to="/Ransomeware-simulator">Ransomeware</Link></li>
                        <li><Link to="/SocialEngineer">Social Engineer</Link></li>
                    </ul>
                </nav>

                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/phishing-simulator" component={PhishingSimulator} />
                    <Route path="/brute-force-attack" component={BruteForceAttack} />
                    <Route path="/Ransomeware-simulator" component={Ransomeware} />
                    <Route path="/SocialEngineer" component={SocialEngineer} />
                    <Route path="/Password-test" component={PasswordTest} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;
