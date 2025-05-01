import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from tasks import edit_task

def test_edit_task_title_and_description():
    tasks = [
        {
            "id": 1,
            "title": "Old Title",
            "description": "Old Description",
            "priority": "Medium",
            "category": "Work",
            "due_date": "2025-05-01",
            "completed": False
        }
    ]

    updated = edit_task(
        tasks,
        task_id=1,
        new_title="New Title",
        new_description="Updated Description"
    )

    assert updated[0]["title"] == "New Title"
    assert updated[0]["description"] == "Updated Description"
