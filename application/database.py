import pymongo
from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient('localhost')
        self.db = self.client['piease']
        self.collection = self.db['example']

    def add_example(self, name):
        try:
            self.collection.insert_one(name)
            return True
        except Exception as e:
            print(e)
            return False

    def get_examples(self):
        try:
            data = self.collection.find()
            return data
        except Exception as e:
            print(e)
            return False
