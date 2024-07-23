import unittest
import json
from app import app, db, collection
from bson.objectid import ObjectId

class TestNoteApp(unittest.TestCase):
    """
    Unit tests for the Note App Flask application.
    """

    def setUp(self):
        """
        Set up the test client and clear the database before each test.
        """
        self.app = app.test_client()
        self.app.testing = True
        self.collection = db['test']
        self.collection.drop()
        print(f"\nStarting test: {self._testMethodName}")

    def tearDown(self):
        """
        Tear down actions after each test.
        """
        print(f"Finished test: {self._testMethodName}")

    def test_add_note_success(self):
        """
        Test adding a new note successfully.
        """
        response = self.app.post('/notes', json={'note': 'Test Note'})
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 201)
        self.assertTrue(ObjectId.is_valid(data))
        print("test_add_note_success: Passed")

    def test_add_note_invalid_data(self):
        """
        Test adding a new note with invalid data.
        """
        response = self.app.post('/notes', json={'invalid': 'Test Note'})
        self.assertEqual(response.status_code, 400)
        print("test_add_note_invalid_data: Passed")

    def test_get_notes_success(self):
        """
        Test retrieving all notes successfully.
        """
        self.collection.insert_one({'note': 'Test Note'})
        response = self.app.get('/notes')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['note'], 'Test Note')
        print("test_get_notes_success: Passed")

    def test_get_notes_empty(self):
        """
        Test retrieving notes when the collection is empty.
        """
        response = self.app.get('/notes')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 0)
        print("test_get_notes_empty: Passed")

    def test_delete_note_success(self):
        """
        Test deleting a note by ID successfully.
        """
        note_id = self.collection.insert_one({'note': 'Test Note'}).inserted_id
        response = self.app.delete(f'/notes/{note_id}')
        self.assertEqual(response.status_code, 204)
        notes = list(self.collection.find())
        self.assertEqual(len(notes), 0)
        print("test_delete_note_success: Passed")

    def test_delete_note_non_existent(self):
        """
        Test deleting a note with a non-existent ID.
        """
        response = self.app.delete('/notes/60c72b2f9af1a2c3d5f6e7d8')
        self.assertEqual(response.status_code, 204)
        print("test_delete_note_non_existent: Passed")

    def test_ping_success(self):
        """
        Test the database connection ping.
        """
        response = self.app.get('/ping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Database connection successful ... PONG ^_^')
        print("test_ping_success: Passed")

if __name__ == '__main__':
    unittest.main(verbosity=2)
 