import React, { useState } from 'react';

function App() {
  const [texto, setTexto] = useState('');
  const [resumen, setResumen] = useState('');

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
      .then((response) => response.json())
      .then((data) => setResumen(data.resumen))
      .catch((error) => console.error('Error:', error));
  };

  return (
    <div>
      <textarea
        rows="10"
        cols="50"
        value={texto}
        onChange={handleChange}
        placeholder="Ingrese su texto aquí..."
      ></textarea>
      <br />
      <button onClick={handleSubmit}>Resumir</button>
      <br />
      <h2>Resumen:</h2>
      <p>{resumen}</p>
    </div>
  );
}

export default App;
