import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from pytest_bdd import scenarios, given, when, then
from tasks import load_tasks, save_tasks

scenarios('../add_task.feature')

@pytest.fixture
def empty_task_list(tmp_path):
    file_path = tmp_path / "tasks.json"
    save_tasks([], file_path)
    return file_path

@given("the task list is initially empty")
def step_task_list_empty(empty_task_list):
    assert load_tasks(empty_task_list) == []

@when('the user adds a task with title "Finish assignment"')
def step_user_adds_task(empty_task_list):
    tasks = load_tasks(empty_task_list)
    new_task = {
        "id": 1,
        "title": "Finish assignment",
        "description": "Test description",
        "priority": "High",
        "category": "School",
        "due_date": "2025-05-01",
        "completed": False,
        "created_at": "2025-04-30 12:00:00"
    }
    tasks.append(new_task)
    save_tasks(tasks, empty_task_list)

@then("the task list should contain 1 task")
def step_task_list_has_one(empty_task_list):
    tasks = load_tasks(empty_task_list)
    assert len(tasks) == 1

@then('the task title should be "Finish assignment"')
def step_check_task_title(empty_task_list):
    tasks = load_tasks(empty_task_list)
    assert tasks[0]["title"] == "Finish assignment"
