# Created by jamontethomas at 10/30/24
Feature: Select product colors on Target

  Scenario: Verify color selection for a product
    Given I open the product page
    When I select each available color
    Then the selected color should be displayed