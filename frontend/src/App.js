import React, { useState, useEffect } from 'react';
import axios from 'axios';

/**
 * App component represents the main Note App.
 * It allows users to add, view, and delete notes.
 */
function App() {
  const [notes, setNotes] = useState([]);
  const [note, setNote] = useState('');

  // Fetch notes from the backend when the component mounts
  useEffect(() => {
    axios.get('http://localhost:5000/notes').then(response => {
      setNotes(response.data);
    });
  }, []);

  /**
   * Add a new note by sending a POST request to the backend.
   */
  const addNote = () => {
    axios.post('http://localhost:5000/notes', { note }).then(response => {
      setNotes([...notes, { _id: response.data, note }]);
      setNote('');
    });
  };

  /**
   * Delete a note by sending a DELETE request to the backend.
   * @param {string} id - The ID of the note to delete.
   */
  const deleteNote = (id) => {
    axios.delete(`http://localhost:5000/notes/${id}`).then(() => {
      setNotes(notes.filter(note => note._id !== id));
    });
  };

  return (
    <div>
      <h1>Note App</h1>
      <input 
        type="text" 
        value={note} 
        onChange={e => setNote(e.target.value)} 
      />
      <button onClick={addNote}>Add Note</button>
      <ul>
        {notes.map(note => (
          <li key={note._id}>
            {note.note} 
            <button onClick={() => deleteNote(note._id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
