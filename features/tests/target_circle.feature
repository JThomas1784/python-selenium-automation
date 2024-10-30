# Created by jamontethomas at 10/30/24
Feature: Verify Target Circle Benefit Cells

  Scenario: Check number of benefit cells
    Given I open the Target Circle page
    When I check the benefit cells
    Then I should see 10 benefit cells