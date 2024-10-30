Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown

Feature: Search for products on Target

  Scenario: Verify product details on search results page
    Given I open the Target homepage
    When I search for a product
    Then every product on the search results page should have a name and an image