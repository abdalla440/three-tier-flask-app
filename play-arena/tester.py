
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = MongoClient("mongodb+srv://ahannora:12345@notes-cluster.erkitpg.mongodb.net/?retryWrites=true&w=majority&appName=notes-Cluster")

db = uri['db1']
collection = db['test']

document = {'name':'table', 'city':'pune'}

insert_document = collection.insert_one(document)
print('insertion id: ', insert_document.inserted_id)

uri.close()

