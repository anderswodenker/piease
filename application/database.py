import pymongo
from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient('localhost')
        self.db = self.client['pawsome']
        self.collection = self.db['names']

    def add_name(self, name):
        try:
            self.collection.insert_one(name)
            return True
        except Exception as e:
            print(e)
            return False

    def get_all_names(self):
        try:
            data = self.collection.find()
            return data
        except Exception as e:
            print(e)
            return False

    def get_statistics(self):
        try:
            open_content = 0
            general_content = 0
            statistics = {'test': 'test'}
            data = self.collection.find()
            for item in data:
                try:
                    general_content += 1
                    if item['char'] == '' or item['sex'] == '' or item['pet'] == '':
                        open_content += 1
                        item['is_open'] = True
                except Exception as e:
                    open_content += 1
                    item['is_open'] = True

            statistics['open'] = open_content
            statistics['general'] = general_content

            return statistics

        except Exception as e:
            print(e)
            return False

    def get_name_by_filter(self, name_filter):
        try:
            return self.collection.find(name_filter)
        except Exception as e:
            print(e)
            return False

    def update_name(self, name, value):
        try:
            name_filter = {'name': name}
            self.collection.update_one(name_filter, value)
            return True
        except Exception as e:
            print(e)
            return False

    def delete_name(self, name):
        try:
            name_filter = {'name': name}
            self.collection.delete_one(name_filter)
            return True
        except Exception as e:
            print(e)
            return False
