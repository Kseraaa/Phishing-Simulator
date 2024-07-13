import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import PhishingSimulator from './PhishingSimulator';
import BruteForceAttack from './BruteForceAttack';
import Home from './Home';

function App() {
    return (
        <Router>
            <div className="App">
                
                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/phishing-simulator" component={PhishingSimulator} />
                    <Route path="/brute-force-attack" component={BruteForceAttack} />
                </Switch>

                <nav>
                    <ul>
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/phishing-simulator">Phishing Simulator</Link></li>
                        <li><Link to="/brute-force-attack">Brute Force Attack</Link></li>
                    </ul>
                </nav>
            </div>
        </Router>
    );
}

export default App;
