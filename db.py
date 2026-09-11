import json
import os


class Database:
    def __init__(self):
        self.path = "database.json"
        self.data = self.load_data()

    def load_data(self):
        if os.path.isfile(self.path):
            with open(self.path, "r") as file:
                return json.load(file)
        else:
            self.create_db()

    def create_db(self):
        self.data = {"accounts": [], "transactions": {}}
        with open(self.path, "w") as file:
            json.dump(self.data, file)

    def dump_data(self):
        with open(self.path, "w") as file:
            json.dump(self.data, file, indent=4)


if __name__ == "__main__":
    db = Database()
