import pytest
from pytest_bdd import scenarios, given, when, then
from src.tasks import load_tasks, save_tasks

scenarios('../complete_task.feature')

TASK_TITLE = "Buy groceries"

@pytest.fixture
def task_list_with_unfinished(tmp_path):
    file_path = tmp_path / "tasks.json"
    task = {
        "id": 1,
        "title": TASK_TITLE,
        "description": "Milk and eggs",
        "priority": "Medium",
        "category": "Personal",
        "due_date": "2025-05-02",
        "completed": False,
        "created_at": "2025-04-30 12:00:00"
    }
    save_tasks([task], file_path)
    return file_path

@given(f'the task "{TASK_TITLE}" is not completed')
def step_task_incomplete(task_list_with_unfinished):
    tasks = load_tasks(task_list_with_unfinished)
    assert tasks[0]["title"] == TASK_TITLE
    assert not tasks[0]["completed"]

@when(f'the user marks the task as completed')
def step_mark_complete(task_list_with_unfinished):
    tasks = load_tasks(task_list_with_unfinished)
    tasks[0]["completed"] = True
    save_tasks(tasks, task_list_with_unfinished)

@then(f'the task "{TASK_TITLE}" should be marked as completed')
def step_check_task_complete(task_list_with_unfinished):
    tasks = load_tasks(task_list_with_unfinished)
    assert tasks[0]["completed"]
