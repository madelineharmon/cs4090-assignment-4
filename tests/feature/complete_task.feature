Feature: Mark a task as completed

  Scenario: User completes an existing task
    Given the task "Buy groceries" is not completed
    When the user marks the task as completed
    Then the task "Buy groceries" should be marked as completed
