Feature: Filter tasks by category

  Scenario: User filters tasks to only show "Work"
    Given there are tasks in multiple categories
    When the user filters tasks by category "Work"
    Then only tasks in the "Work" category should be displayed
