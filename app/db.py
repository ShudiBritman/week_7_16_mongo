from connection import MongoConnection
import os

def get_db():
    db_name = os.getenv("MONGO_DB", "my_db")
    client = MongoConnection().get_client()
    return client[db_name]

def get_collection(collection_name: str):
    return get_db()[collection_name]
