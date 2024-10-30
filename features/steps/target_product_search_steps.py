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

@then('every product on the search results page should have a name and an image')
def step_then_verify_products(context):
    products = context.driver.find_elements(By.CSS_SELECTOR, 'div[data-test="product"]')

    for product in products:
        name_element = product.find_element(By.CSS_SELECTOR, 'span[data-test="product-title"]')
        image_element = product.find_element(By.CSS_SELECTOR, 'img[data-test="product-image"]')

        assert name_element.text, "Product name is missing."
        assert image_element.get_attribute("src"), "Product image is missing."

def after_scenario(context, scenario):
    context.driver.quit()
