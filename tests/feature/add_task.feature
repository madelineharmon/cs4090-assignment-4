Feature: Add new task to the to-do list

  Scenario: User adds a valid task
    Given the task list is initially empty
    When the user adds a task with title "Finish assignment"
    Then the task list should contain 1 task
    And the task title should be "Finish assignment"
