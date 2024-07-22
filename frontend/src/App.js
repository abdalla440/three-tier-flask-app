import React, { useEffect, useState } from 'react';
import axios from 'axios';
import NoteTable from './components/NoteTable';
import NoteForm from './components/NoteForm';
import { Container, Typography } from '@mui/material';

const App = () => {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    const fetchNotes = async () => {
      try {
        const response = await axios.get('http://localhost:5000/notes');
        setNotes(response.data);
      } catch (error) {
        console.error("There was an error fetching the notes!", error);
      }
    };

    fetchNotes();
  }, []);

  return (
    <Container>
      <Typography variant="h3" align="center" gutterBottom>
        Note Taking App
      </Typography>
      <NoteForm setNotes={setNotes} />
      <NoteTable notes={notes} setNotes={setNotes} />
    </Container>
  );
};

export default App;
