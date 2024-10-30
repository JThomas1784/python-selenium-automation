from behave import given, when, then
from selenium import webdriver
from pages.cart_page import CartPage

@given('I open the Target homepage')
def step_given_open_target_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com/")
    context.driver.implicitly_wait(10)
    context.cart_page = CartPage(context.driver)

@when('I click on the Cart icon')
def step_when_click_cart_icon(context):
    context.cart_page.click_cart_icon()

@then('I should see the "Your cart is empty" message')
def step_then_verify_empty_cart_message(context):
    assert context.cart_page.is_empty_cart_message_displayed(), "Empty cart message is not displayed."

def after_scenario(context, scenario):
    context.driver.quit()
