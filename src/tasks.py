import json
import os
from datetime import datetime

# File path for task storage
DEFAULT_TASKS_FILE = "tasks.json"

def load_tasks(file_path=DEFAULT_TASKS_FILE):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Warning: {file_path} contains invalid JSON. Creating new tasks list.")
        return []

def save_tasks(tasks, file_path=DEFAULT_TASKS_FILE):
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=2)

def generate_unique_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def filter_tasks_by_priority(tasks, priority):
    return [task for task in tasks if task.get("priority") == priority]

def filter_tasks_by_category(tasks, category):
    return [task for task in tasks if task.get("category") == category]

def filter_tasks_by_completion(tasks, completed=True):
    return [task for task in tasks if task.get("completed") == completed]

def search_tasks(tasks, query):
    query = query.lower()
    return [
        task for task in tasks 
        if query in task.get("title", "").lower() or 
           query in task.get("description", "").lower()
    ]

def get_overdue_tasks(tasks):
    today = datetime.now().strftime("%Y-%m-%d")
    return [
        task for task in tasks 
        if not task.get("completed", False) and 
           task.get("due_date", "") < today
    ]

def edit_task(tasks, task_id, new_title=None, new_description=None, new_priority=None, new_category=None, new_due_date=None):
    for task in tasks:
        if task["id"] == task_id:
            if new_title is not None:
                task["title"] = new_title
            if new_description is not None:
                task["description"] = new_description
            if new_priority is not None:
                task["priority"] = new_priority
            if new_category is not None:
                task["category"] = new_category
            if new_due_date is not None:
                task["due_date"] = new_due_date
    return tasks
