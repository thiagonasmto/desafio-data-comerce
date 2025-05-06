import React, { useEffect, useState } from 'react';
import './App.css';
import Dashboard from './Dashboard';

function App() {
  const [message, setMessage] = useState('');
  useEffect(() => {
    fetch('http://localhost:8000/')
      .then(response => {
        console.log(response);  // Logando a resposta
        return response.json();
      })
      .then(data => setMessage(data.message))
      .catch(error => console.error('Error fetching data: ', error));
  }, []);

  return (
    <div className="App">
      <Dashboard />
    </div>
  );
}

export default App;
