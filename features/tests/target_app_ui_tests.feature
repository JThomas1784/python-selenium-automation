# Created by jamontethomas at 9/21/24
Feature: Tests for Target App Page

  Scenario: User is able to open Privacy Policy
    Given Open Target app page
    And Store original window
    When Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original window