import json
import os

class ToyDB(object):

    # in creating this database, we only need to pass the location for initialization

    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        self.db = json.load(open(self.location, "r"))

    def dumpdb(self):
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except:
            return False

    def set(self, key, value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Database: " + str(e))
            return False

    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            print("No Value Can Be Found For " + str(key))
            return false

    def delete(self, key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True

    def reset(self):
        self.db = {}
        self.dumpdb()
        return True

    def display(self):
        for x in self.db:
            print(self.db[x])