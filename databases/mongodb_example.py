from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["example_db"]
collection = db["users"]
collection.insert_one({"name": "Alice"})