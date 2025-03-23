import json

from abc_persistence import ABCPersistence


class JsonPersistence(ABCPersistence):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def append(self, data) -> None:
        new_data = self.load()
        retval = None

        if not new_data:
            retval = data
        else:
            retval = new_data + data

        with open(self.file_path, 'w') as file:
            json.dump(retval, file)

    def save(self, data) -> None:
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def load(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
