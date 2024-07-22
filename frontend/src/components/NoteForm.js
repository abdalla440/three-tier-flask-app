import React, { useState } from 'react';
import axios from 'axios';
import { Box, Button, TextField } from '@mui/material';

const NoteForm = ({ setNotes }) => {
  const [note, setNote] = useState('');

  const addNote = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/notes', { note });
      setNotes((prevNotes) => [...prevNotes, { _id: response.data, note }]);
      setNote('');
    } catch (error) {
      console.error("There was an error adding the note!", error);
    }
  };

  return (
    <Box component="form" onSubmit={addNote} sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
      <TextField
        variant="outlined"
        label="Add a new note"
        value={note}
        onChange={(e) => setNote(e.target.value)}
        fullWidth
      />
      <Button variant="contained" color="primary" type="submit">
        Add Note
      </Button>
    </Box>
  );
};

export default NoteForm;
