import pytest

from json_persistance import JsonPersistence
from task import Task


def test_append_single_task_test():
    persistence = JsonPersistence('test_file.json')
    persistence.append('Test Task')
    tasks = persistence.load()
    assert len(tasks) == 1
    assert tasks[0].description == 'Test Task'


def test_create_new_task_list():
    # Create a new task list using new_tasks command
    persistence = JsonPersistence('test_file.json')
    persistence.save([Task('Task 1'), Task('Task 2')])
    tasks = persistence.load()


def test_save_tasks():
    persistence = JsonPersistence('test_file.json')
    tasks = [Task('Task 1'), Task('Task 2')]
    persistence.save(tasks)
    loaded_tasks = persistence.load()
    assert len(loaded_tasks) == 2
    assert loaded_tasks[0].description == 'Task 1'
    assert loaded_tasks[1].description == 'Task 2'


def test_load_empty_file():
    persistence = JsonPersistence('non_existent_file.json')
    tasks = persistence.load()
    assert tasks == []




