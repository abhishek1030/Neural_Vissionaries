import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [username, setUsername] = useState('');
  const [submitMessage, setSubmitMessage] = useState('');
  const [recommendation, setRecommendation] = useState('');

  const handleSubmit = () => {
    axios.post('http://localhost:5000/submit', { username })
      .then(res => setSubmitMessage(res.data.message))
      .catch(err => setSubmitMessage('Error: ' + err.response.data.message));
  };

  const handleRecommendation = () => {
    axios.get(`http://localhost:5000/recommendation?username=${username}`)
      .then(res => setRecommendation(res.data.recommendation))
      .catch(err => setRecommendation('Error: ' + err.response.data.error));
  };

  return (
    <div style={{ padding: '30px' }}>
      <h2>Hyper-Personalization</h2>
      <input
        type="text"
        placeholder="Enter username"
        value={username}
        onChange={e => setUsername(e.target.value)}
      />
      <br /><br />
      <button onClick={handleSubmit}>Submit</button>
      <p>{submitMessage}</p>
      <button onClick={handleRecommendation}>Recommendations</button>
      <h3>{recommendation}</h3>
    </div>
  );
}

export default App;
