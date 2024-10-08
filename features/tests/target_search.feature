# Created by jamontethomas at 9/5/24
Feature: Tests for Target Search functionality

  @smoke @safari_only
  Scenario: User can search for coffee
    Given Open Target main page
    When  Search for coffee
    Then  Verify that correct search results shown for coffee
    Then Verify product coffee in URL

Scenario: User can search for tea
  Given Open Target main page
  When Search for tea
  Then Verify that correct search results shown for tea

  Scenario Outline: User can search for product
    Given Open Target main page
    When Search for <search_word>
    Then Verify that correct search results shown for <search_result>
    Examples:
    |search_word   | search_result |
    |coffee        | coffee        |
    |tea           | tea           |
    |mug           | mug           |
    |sugar         | sugar         |

Scenario: User can add a product to cart
  Given Open Target main page
  When Search for mug
  And Click on Add to Cart button
  And Store product name
  And Confirm Add to Cart button from side navigation
  And Open cart page
  Then Verify cart has 1 item(s)
  And Verify cart has correct product

Scenario: Verify that user can see product names
  Given Open Target main page
  When  Search for AirPods (3rd Generation)
  Then Verify that every product has a name and an image