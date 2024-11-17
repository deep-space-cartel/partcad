@version @cli
Feature: Version Command
  As a user
  I want to run the version command
  So that I can see the PartCAD and PartCAD CLI versions

  @format
  Scenario: Version command output format
    Given I am in the command line interface
    When I run the command "version"
    Then  command takes less than "30" seconds
    Then the output should contain "PartCAD version: "
    # And the output should contain "PartCAD CLI version: "
    And the command should exit with a status code of 0
