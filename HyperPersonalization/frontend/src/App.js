import React, { useState } from 'react';
import './App.css';

function App() {
  const [username, setUsername] = useState('');
  const [message, setMessage] = useState('');
  const [recommendations, setRecommendations] = useState([]);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isLoadingRecommendations, setIsLoadingRecommendations] = useState(false);

  const handleSubmit = async () => {
    if (!username.trim()) {
      setMessage('Please enter a username before submitting.');
      return;
    }

    setIsSubmitting(true);
    setMessage('🔃 Submitting username...');

    try {
      const response = await fetch('http://localhost:5000/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username }),
      });

      const data = await response.json();
      setMessage(`✅ Server says: ${data.message}`);
    } catch (error) {
      console.error('❌ Error submitting username:', error);
      setMessage('❌ Server says: Something went wrong.');
    }

    setIsSubmitting(false);
  };

  const handleRecommendation = async () => {
    setIsLoadingRecommendations(true);
    setMessage('🔃 Fetching recommendations...');

    try {
      const response = await fetch('http://localhost:5000/recommend');
      const data = await response.json();

      if (Array.isArray(data)) {
        setRecommendations(data);
        setMessage('✅ Recommendations loaded.');
      } else {
        setRecommendations([]);
        setMessage(data.message || 'No recommendations found.');
      }
    } catch (error) {
      console.error('❌ Error fetching recommendation:', error);
      setMessage('❌ Something went wrong while fetching recommendations.');
    }

    setIsLoadingRecommendations(false);
  };

  return (
    <div className="App">
      <h2>Hyper Personalization</h2>

      <input
  type="text"
  placeholder="Enter username"
  value={username}
  onChange={(e) => {
    const value = e.target.value;
    setUsername(value);

    if (value.trim() === '') {
      setMessage('');
      setRecommendations([]);
    }
  }}
      />
      <br /><br />

      <button onClick={handleSubmit} disabled={isSubmitting}>
        {isSubmitting ? 'Submitting...' : 'Submit'}
      </button>

      <button
        onClick={handleRecommendation}
        style={{ marginLeft: '10px' }}
        disabled={isLoadingRecommendations}
      >
        {isLoadingRecommendations ? 'Loading...' : 'Recommendation'}
      </button>

      <br /><br />
      <p>{message}</p>

      {recommendations.length > 0 && (
        <div>
          <h3>Recommendations:</h3>
          <ul>
            {recommendations.map((rec, index) => (
              <li key={index}>
                <strong>{rec.item}</strong> — Score: {rec.score}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
