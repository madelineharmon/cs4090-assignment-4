# To-Do App Testing Assignment

## Overview

This repository contains a tested and extended version of a Streamlit-based To-Do List application. The goal of this assignment was to gain hands-on experience with:

- Unit Testing
- Pytest Features (parametrize, coverage, mocking, HTML reports)
- Test-Driven Development (TDD)
- Behavior-Driven Development (BDD)
- Property-Based Testing (bonus)

The application was forked from the starter repository provided and enhanced with automated testing and new features.

---

## Application Features

- Create, edit, and delete tasks
- Set priorities, due dates, and categories
- Filter tasks by category and priority
- Mark tasks as complete or incomplete
- View overdue tasks
- Run automated tests through Streamlit UI buttons

---

## Testing Summary

### Unit Testing

- Functions tested:
  - load_tasks
  - save_tasks
  - filter_tasks_by_priority
  - filter_tasks_by_category
- Coverage achieved: over 90%
- Frameworks used: pytest, pytest-cov

### Pytest Features

- Used `@pytest.mark.parametrize` to test multiple conditions
- Generated HTML report with `pytest-html`
- Measured coverage with `pytest-cov`
- Used `mock` for file/datetime handling (if applicable)

### Test-Driven Development (TDD)

Three new features were developed using the TDD process:

1. Edit task functionality
2. Search task functionality
3. Overdue task detection

Each feature followed the TDD cycle:
- Initial failing test written
- Feature implemented in `tasks.py`
- Tests re-run until passing
- Refactoring as needed

### Behavior-Driven Development (BDD)

Implemented 5 behavior-driven scenarios using `.feature` files:

- Add a task
- Mark task as complete
- Delete task
- Filter by category
- Show overdue tasks

Used `pytest-bdd` with corresponding step definitions in Python. All scenarios were verified and connected with `scenarios()` in the step files.

### Property-Based Testing

Tested functions with randomized data using Hypothesis:

- search_tasks
- filter_tasks_by_priority
- JSON and list handling under random input conditions

All tests passed, and no crashes or edge-case failures were observed.

---

## Bugs Found and Fixed

| Bug ID | Description | Resolution |
|--------|-------------|------------|
| 001 | Filtering logic failed for lowercase priorities | Normalized priority comparison |
| 002 | Reused static task ID | Replaced with generate_unique_id function |
| 003 | search_tasks crashed on missing fields | Used .get() safely with default values |

---

## How to Run Tests

Command-line execution:

```bash
# Unit tests with coverage
pytest tests/test_basic.py --cov=src

# Run all tests
pytest tests/ --cov=src

# Run only BDD
pytest tests/feature

# Run Hypothesis property tests
pytest tests/test_property.py

# Run TDD tests
pytest tests/test_tdd.py
