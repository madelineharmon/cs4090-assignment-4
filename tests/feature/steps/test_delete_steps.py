import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from pytest_bdd import scenarios, given, when, then
from tasks import load_tasks, save_tasks

scenarios('../delete_task.feature')

TASK_TITLE = "Old task"

@pytest.fixture
def task_list_with_old(tmp_path):
    file_path = tmp_path / "tasks.json"
    tasks = [{"id": 1, "title": TASK_TITLE, "description": "Outdated", "category": "Work", "priority": "Low", "due_date": "2025-04-10", "completed": False, "created_at": "2025-04-10"}]
    save_tasks(tasks, file_path)
    return file_path

@given(f'a task with the title "{TASK_TITLE}" exists')
def step_task_exists(task_list_with_old):
    tasks = load_tasks(task_list_with_old)
    assert any(task["title"] == TASK_TITLE for task in tasks)

@when('the user deletes the task')
def step_delete_task(task_list_with_old):
    tasks = load_tasks(task_list_with_old)
    tasks = [t for t in tasks if t["title"] != TASK_TITLE]
    save_tasks(tasks, task_list_with_old)

@then(f'the task list should not contain "{TASK_TITLE}"')
def step_check_task_deleted(task_list_with_old):
    tasks = load_tasks(task_list_with_old)
    assert all(task["title"] != TASK_TITLE for task in tasks)
