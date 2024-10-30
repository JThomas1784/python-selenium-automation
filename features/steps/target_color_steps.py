from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PRODUCT_URL = "https://www.target.com/p/A-91511634"

@given('I open the product page')
def step_given_open_product_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get(PRODUCT_URL)
    context.driver.implicitly_wait(10)

@when('I select each available color')
def step_when_select_each_color(context):
    color_elements = context.driver.find_elements(By.CSS_SELECTOR, 'button[data-test="color"]')

    for color in color_elements:
        color.click()
        time.sleep(1)


        selected_color = context.driver.find_element(By.CSS_SELECTOR, 'span[data-test="selected-color-name"]')
        assert color.get_attribute("aria-label") == selected_color.text, f"Expected color {color.get_attribute('aria-label')} to be selected."

@then('the selected color should be displayed')
def step_then_verify_selected_color(context):

    pass

def after_scenario(context, scenario):
    context.driver.quit()