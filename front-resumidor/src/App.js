import React, { useState } from 'react';
import './App.css';

function App() {
  const [texto, setTexto] = useState('');
  const [resumen, setResumen] = useState('');
  const [error, setError] = useState(null);

  const handleChange = (event) => {
    setTexto(event.target.value);
  };

  const handleSubmit = () => {
    fetch('http://localhost:5000/api/resumir', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ texto: texto }),
    })
      .then((response) => {
        if (!response.ok) {
          return response.json().then((data) => {
            throw new Error(data.error || 'Error al resumir el texto');
          });
        }
        return response.json();
      })
      .then((data) => {
        setResumen(data.resumen);
        setError(null);
      })
      .catch((error) => {
        setError(error.message);
        console.error('Error:', error);
        alert(error.message);
      });
  };

  return (
    <div className="App">
      <h1>Resumidor de Textos</h1>
      <textarea
        className="textarea"
        rows="10"
        cols="50"
        value={texto}
        onChange={handleChange}
        placeholder="Ingrese su texto aquí..."
      ></textarea>
      <br />
      <button className="button" onClick={handleSubmit}>Resumir</button>
      <br />
      {error && <p className="error">{error}</p>}
      <h2>Resumen:</h2>
      <pre className="resumen">{resumen}</pre>
    </div>
  );
}

export default App;
