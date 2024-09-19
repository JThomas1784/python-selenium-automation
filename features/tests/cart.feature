# Created by jamontethomas at 9/7/24
Feature: Test for cart functionalit

  Scenario: User can see Cart Empty message
    Given Open Target main page
    When Click on cart icon
    Then Verify Cart Empty message shown