from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

@given("I am on the Target homepage")
def open_target(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com/")

@when("I click on the cart icon")
def click_cart_icon(context):
    cart_icon = context.driver.find_element(By.CSS_SELECTOR, ".header__cart-icon")
    cart_icon.click()

@then("I see the message 'Your cart is empty'")
def verify_empty_cart(context):
    empty_message = context.driver.find_element(By.XPATH, "//div[contains(text(), 'Your cart is empty')]")
    assert empty_message.is_displayed()
    assert empty_message.text == "Your cart is empty"

@then("I close the browser")
def close_browser(context):
    context.driver.quit()