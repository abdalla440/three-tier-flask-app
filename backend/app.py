from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS

# Initialize Flask application
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "send_wildcard": "False"}}) # Compliant
app.config['WTF_CSRF_ENABLED'] = True 

# MongoDB URI
client = MongoClient(
            host= 'notes_mongodb',
            port= 27017, 
            username='hannora', 
            password='hannora123',
            authSource="admin"
    )

db = client['notes']
collection = db['test']


@app.route('/notes', methods=['POST'])
def add_note():
    """
    Add a new note to the MongoDB database.
    Request should contain JSON with a 'note' field.
    Returns the ID of the inserted note.
    """
    try:
        note = request.json['note']
    except KeyError:
        return jsonify({"error": "Invalid data, 'note' field is required"}), 400
    
    note_id = collection.insert_one({'note': note}).inserted_id
    return jsonify(str(note_id)), 201


@app.route('/notes', methods=['GET'])
def get_notes():
    """
    Retrieve all notes from the MongoDB database.
    Returns a list of notes.
    """
    notes = collection.find()
    result = []
    for note in notes:
        result.append({'_id': str(note['_id']), 'note': note['note']})
    return jsonify(result)

@app.route('/notes/<id>', methods=['DELETE'])
def delete_note(id):
    """
    Delete a note from the MongoDB database using its ID.
    Returns no content.
    """
    collection.delete_one({'_id': ObjectId(id)})
    return '', 204

    
# Modified route to print database info
@app.route('/ping', methods=['GET'])
def test_db_connection():
    try:
        # Get database information
        db_info = client.server_info()
        return jsonify(db_info), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# if __name__ == '__main__':
#     # Run the Flask application
#     app.run(host='0.0.0.0',port=5000)
