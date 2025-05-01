Feature: Display overdue tasks

  Scenario: User checks for overdue tasks
    Given there is a task due before today
    When the user views overdue tasks
    Then the task should be listed as overdue
