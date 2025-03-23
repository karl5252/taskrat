import json

from abc_persistence import ABCPersistence


class JsonPersistence(ABCPersistence):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def append(self, data) -> None:
        new_data = self.load()
        retval = None

        if not new_data:
            retval = [data]
        else:
            new_data.append(data)
            retval = new_data

        with open(self.file_path, 'w') as file:
            json.dump(retval, file, indent=2)

    def save(self, data: list) -> None:
        if not isinstance(data, list):
            raise ValueError("save() expects a list of tasks, not a single item")
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def load(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
