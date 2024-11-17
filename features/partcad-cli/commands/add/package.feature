# {partcad-cli/src/partcad_cli/cli_add.py}
@cli @add
Feature: Test cli_add function
  As a user
  I want to add an import to a project
  So that I can use the imported package

  Scenario: Add import to project
    Given a project exists
    And the project is initialized
    When I run the cli_add command with alias and location
    Then the import is added to the project

  Scenario: Add import to project with invalid alias
    Given a project exists
    And the project is initialized
    When I run the cli_add command with invalid alias and location
    Then an error is raised

  Scenario: Add import to project with invalid location
    Given a project exists
    And the project is initialized
    When I run the cli_add command with alias and invalid location
    Then an error is raised