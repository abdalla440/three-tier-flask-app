import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import axios from 'axios';
import App from './App';

jest.mock('axios');

test('renders Note App', () => {
  render(<App />);
  const linkElement = screen.getByText(/Note App/i);
  expect(linkElement).toBeInTheDocument();
});

test('adds a note', async () => {
  axios.post.mockResolvedValue({ data: '1' });
  axios.get.mockResolvedValue({ data: [{ _id: '1', note: 'Test Note' }] });

  render(<App />);
  
  const inputElement = screen.getByRole('textbox');
  const buttonElement = screen.getByText(/Add Note/i);

  fireEvent.change(inputElement, { target: { value: 'Test Note' } });
  fireEvent.click(buttonElement);

  await waitFor(() => screen.getByText('Test Note'));
  const noteElement = screen.getByText('Test Note');
  expect(noteElement).toBeInTheDocument();
});

test('deletes a note', async () => {
  axios.delete.mockResolvedValue({});
  axios.get.mockResolvedValue({ data: [{ _id: '1', note: 'Test Note' }] });

  render(<App />);

  await waitFor(() => screen.getByText('Test Note'));
  const deleteButton = screen.getByText(/Delete/i);
  fireEvent.click(deleteButton);

  await waitFor(() => expect(screen.queryByText('Test Note')).toBeNull());
});
