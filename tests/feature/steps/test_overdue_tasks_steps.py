import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from pytest_bdd import scenarios, given, when, then
from tasks import load_tasks, save_tasks, get_overdue_tasks

scenarios('../overdue_tasks.feature')

@pytest.fixture
def overdue_task_list(tmp_path):
    file_path = tmp_path / "tasks.json"
    tasks = [{
        "id": 1,
        "title": "Late homework",
        "description": "Was due last week",
        "priority": "High",
        "category": "School",
        "due_date": "2023-01-01",
        "completed": False,
        "created_at": "2022-12-31"
    }]
    save_tasks(tasks, file_path)
    return file_path

@given("there is a task due before today")
def step_add_overdue(overdue_task_list):
    tasks = load_tasks(overdue_task_list)
    assert tasks[0]["due_date"] < "2025-04-30"

@when("the user views overdue tasks")
def step_view_overdue(overdue_task_list):
    tasks = load_tasks(overdue_task_list)
    overdue = get_overdue_tasks(tasks)
    save_tasks(overdue, overdue_task_list)

@then("the task should be listed as overdue")
def step_verify_overdue(overdue_task_list):
    tasks = load_tasks(overdue_task_list)
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Late homework"
