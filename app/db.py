from connection import MongoConnection
import json


PATH = "/data/employee_data_advanced.json"

def init_db():
    col = MongoConnection().get_collection()

    if col.estimated_document_count() > 0:
        print("DB already initialized")
        return

    with open(PATH) as f:
        data = json.load(f)

    col.insert_many(data, ordered=False)

    print("DB initialized")
