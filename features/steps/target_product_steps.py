from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('I open the Target homepage')
def step_given_open_target_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com/")
    context.driver.implicitly_wait(10)


@when('I search for a product')
def step_when_search_for_product(context):
    search_box = context.driver.find_element(By.NAME, "search")
    search_box.send_keys("toy")
    search_box.submit()
    time.sleep(2)


@when('I add the product to the cart')
def step_when_add_product_to_cart(context):
    first_product = context.driver.find_element(By.CSS_SELECTOR,
                                                'div[data-test="product"]')
    first_product.click()
    time.sleep(2)

    add_to_cart_button = context.driver.find_element(By.XPATH, '//button[contains(@data-test, "add-to-cart")]')
    add_to_cart_button.click()
    time.sleep(2)


@then('I should see the product in the cart')
def step_then_verify_product_in_cart(context):
    cart_button = context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="cart"]')
    cart_button.click()
    time.sleep(2)


    cart_items = context.driver.find_elements(By.CSS_SELECTOR,
                                              'div[data-test="cart-item"]')
    assert len(cart_items) > 0, "The cart should have at least one item."


    product_names = [item.text for item in cart_items]
    assert any("toy" in name.lower() for name in product_names), "The cart( does not contain the expected product."


def after_scenario(context, scenario):
    context.driver.quit()