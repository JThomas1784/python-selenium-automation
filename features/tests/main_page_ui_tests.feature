# Created by jamontethomas at 9/7/24
Feature: Tests for main page UI

  @smoke
  Scenario: Verify header is shown
    Given Open Target main page
    Then Verify header is shown

  Scenario: Verify header has correct amount links
    Given Open Target main page
    Then Verify header is shown
    And  Verify header has 6 links