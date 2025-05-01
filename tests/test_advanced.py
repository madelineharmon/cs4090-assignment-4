import pytest
from src.tasks import filter_tasks_by_category

@pytest.mark.parametrize("category,expected_count", [
    ("Work", 2),
    ("School", 1),
])
def test_category_filter_param(category, expected_count):
    tasks = [
        {"id": 1, "category": "Work"},
        {"id": 2, "category": "Work"},
        {"id": 3, "category": "School"},
    ]
    result = filter_tasks_by_category(tasks, category)
    assert len(result) == expected_count
