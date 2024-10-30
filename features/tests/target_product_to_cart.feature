# Created by jamontethomas at 10/30/24
Feature: Add product to cart on Target

  Scenario: Add a product to the cart and verify it's there
    Given I open the Target homepage
    When I search for a product
    And I add the product to the cart
    Then I should see the product in the cart