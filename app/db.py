from connection import MongoConnection
import json


PATH = '../data/employee_data_advanced'

def init_db():
    col = MongoConnection().get_collection('employees')
    if col.count_documents({"init": True}) == 0:
        with open(PATH) as f:
            data = json.load(f)

        col.insert_many(data)
        col.insert_one({"init": True})

        print("DB initialized")
    else:
        print("DB already initialized")