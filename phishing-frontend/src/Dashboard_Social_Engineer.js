import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { PieChart, Pie, Cell, Tooltip, Legend } from 'recharts';

const COLORS = ['#0088FE', '#00C49F'];

const Dashboard = () => {
    const [analysisData, setAnalysisData] = useState(null);

    useEffect(() => {
        axios.get('http://localhost:8000/api/analysis_social_engineering/')
            .then(response => {
                setAnalysisData(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the analysis data!', error);
            });
    }, []);

    if (!analysisData) {
        return <div>Loading...</div>;
    }

    const data = [
        { name: 'Clicked', value: analysisData.emails_clicked },
        { name: 'Not Clicked', value: analysisData.total_emails_sent - analysisData.emails_clicked },
    ];

    return (
        <div>
            <h2>SocialEngineer Email Analysis</h2>
            <p>Total Emails Sent: {analysisData.total_emails_sent}</p>
            <p>Emails Clicked: {analysisData.emails_clicked}</p>
            <p>Click Rate: {analysisData.click_rate.toFixed(2)}%</p>
            <PieChart width={400} height={400}>
                <Pie
                    data={data}
                    cx={200}
                    cy={200}
                    innerRadius={60}
                    outerRadius={80}
                    fill="#8884d8"
                    paddingAngle={5}
                    dataKey="value"
                >
                    {data.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                </Pie>
                <Tooltip />
                <Legend />
            </PieChart>
        </div>
    );
};

export default Dashboard;
