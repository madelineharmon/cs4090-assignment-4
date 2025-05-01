import pytest
from pytest_bdd import scenarios, given, when, then
from src.tasks import load_tasks, save_tasks, filter_tasks_by_category

scenarios('../filter_by_category.feature')

@pytest.fixture
def mixed_category_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"
    tasks = [
        {"id": 1, "title": "Work task", "category": "Work", "priority": "High", "due_date": "2025-04-30", "completed": False, "created_at": "2025-04-30"},
        {"id": 2, "title": "Personal task", "category": "Personal", "priority": "Low", "due_date": "2025-04-30", "completed": False, "created_at": "2025-04-30"}
    ]
    save_tasks(tasks, file_path)
    return file_path

@given("there are tasks in multiple categories")
def step_tasks_mixed(mixed_category_tasks):
    tasks = load_tasks(mixed_category_tasks)
    categories = set(task["category"] for task in tasks)
    assert "Work" in categories and "Personal" in categories

@when('the user filters tasks by category "Work"')
def step_filter_work(mixed_category_tasks):
    tasks = load_tasks(mixed_category_tasks)
    filtered = filter_tasks_by_category(tasks, "Work")
    save_tasks(filtered, mixed_category_tasks)

@then('only tasks in the "Work" category should be displayed')
def step_check_only_work(mixed_category_tasks):
    tasks = load_tasks(mixed_category_tasks)
    assert all(task["category"] == "Work" for task in tasks)
