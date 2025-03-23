import json

from abc_persistence import ABCPersistence
from task import Task


class JsonPersistence(ABCPersistence):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def append(self, data) -> None:
        new_data = self.load()  # returns list of tasks or empty list

        if isinstance(data, str):
            data = Task(data)
        if isinstance(data, list):
            data = [Task(item) for item in data]

        new_data.append(data.to_dict())

        with open(self.file_path, 'w') as file:
            json.dump(new_data, file, indent=2)

    def save(self, tasks: list[Task]) -> None:
        print(f"DEBUG: to save = {[task.to_dict() for task in tasks]}")
        with open(self.file_path, 'w') as file:
            dicts = [task.to_dict() for task in tasks]
            json.dump(dicts, file, indent=2)

    def load(self) -> list[Task]:
        try:
            with open(self.file_path, 'r') as file:
                raw = json.load(file)
                return [Task.from_dict(obj) for obj in raw]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
