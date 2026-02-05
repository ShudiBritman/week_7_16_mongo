from pymongo import MongoClient
from pymongo.errors import PyMongoError
import os
import time

def build_mongo_uri() -> str:
    uri = os.getenv("MONGO_URI")
    if uri:
        return uri

    host = os.getenv("MONGO_HOST", "localhost")
    port = os.getenv("MONGO_PORT", "27017")
    user = os.getenv("MONGO_USER")
    password = os.getenv("MONGO_PASSWORD")

    if user and password:
        return f"mongodb://{user}:{password}@{host}:{port}"

    return f"mongodb://{host}:{port}"


class MongoConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = cls._connect_with_retry()
        return cls._instance

    @staticmethod
    def connect_with_retry():
        uri = build_mongo_uri()
        retries = 10
        delay = 3

        last_error = None

        for attempt in range(1, retries + 1):
            try:
                client = MongoClient(uri)
                client.admin.command("ping")
                print(f"Mongo connected (attempt {attempt})")
                return client
            except PyMongoError as e:
                last_error = e
                print(f"Mongo connection failed (attempt {attempt}), retrying...")
                time.sleep(delay)

        raise RuntimeError(f"Mongo connection failed after {retries} attempts: {last_error}")

    def get_client(self):
        return self.client



#https://sandbox.redhat.com/?intcmp=7013a0000026GZMAA2