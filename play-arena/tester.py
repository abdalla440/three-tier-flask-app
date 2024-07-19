from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = MongoClient("mongodb+srv://ahannora:AdminMONGO123@notes-cluster.erkitpg.mongodb.net/?retryWrites=true&w=majority&appName=notes-Cluster")

db = uri['notes']
collection = db['test']

document = {'note':'this note is for test 2'}

insert_document = collection.insert_one(document)
print('insertion id: ', insert_document.inserted_id)
# Retrieve all documents from the collection
all_documents = collection.find()

# Print each document
for doc in all_documents:
    print(doc)
uri.close()