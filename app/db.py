from connection import MongoConnection
import os
import json

def get_db():
    db_name = os.getenv("MONGO_DB", "employees")
    client = MongoConnection().get_client()
    return client[db_name]

def get_collection(collection_name: str):
    return get_db()[collection_name]


def init_db():

    col = get_collection('employees')
    if col.count_documents({"init": True}) == 0:
        with open("app/init_data.json") as f:
            data = json.load(f)

        col.insert_many(data)
        col.insert_one({"init": True})

        print("DB initialized")
    else:
        print("DB already initialized")