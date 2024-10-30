# Created by jamontethomas at 10/30/24
Feature: Verify empty cart message

  Scenario: "Your cart is empty" message is shown for an empty cart
    Given I open the Target homepage
    When I click on the Cart icon
    Then I should see the "Your cart is empty" message