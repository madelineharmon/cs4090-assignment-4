import pytest
from src.tasks import load_tasks, save_tasks, filter_tasks_by_priority, filter_tasks_by_category

def test_filter_by_priority():
    tasks = [{"id": 1, "priority": "High"}, {"id": 2, "priority": "Low"}]
    result = filter_tasks_by_priority(tasks, "High")
    assert len(result) == 1
    assert result[0]["priority"] == "High"

def test_filter_by_category():
    tasks = [{"id": 1, "category": "Work"}, {"id": 2, "category": "School"}]
    result = filter_tasks_by_category(tasks, "Work")
    assert len(result) == 1
    assert result[0]["category"] == "Work"
