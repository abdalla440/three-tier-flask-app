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

    def test_add_note(self):
        """
        Test adding a new note.
        """
        try:
            response = self.app.post('/notes', json={'note': 'Test Note'})
            data = json.loads(response.get_data())
            self.assertEqual(response.status_code, 201)
            self.assertTrue(ObjectId.is_valid(data))
            print("test_add_note: Passed")
        except AssertionError as e:
            print(f"test_add_note: Failed ({e})")
            raise

    def test_get_notes(self):
        """
        Test retrieving all notes.
        """
        try:
            self.collection.insert_one({'note': 'Test Note'})
            response = self.app.get('/notes')
            data = json.loads(response.get_data())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['note'], 'Test Note')
            print("test_get_notes: Passed")
        except AssertionError as e:
            print(f"test_get_notes: Failed ({e})")
            raise

    def test_delete_note(self):
        """
        Test deleting a note by ID.
        """
        try:
            note_id = self.collection.insert_one({'note': 'Test Note'}).inserted_id
            response = self.app.delete(f'/notes/{note_id}')
            self.assertEqual(response.status_code, 204)
            notes = list(self.collection.find())
            self.assertEqual(len(notes), 0)
            print("test_delete_note: Passed")
        except AssertionError as e:
            print(f"test_delete_note: Failed ({e})")
            raise

if __name__ == '__main__':
    unittest.main(verbosity=2)
