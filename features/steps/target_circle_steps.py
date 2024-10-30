from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I open the Target Circle page')
def step_given_open_target_circle(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com/circle")
    context.driver.implicitly_wait(10)

@when('I check the benefit cells')
def step_when_check_benefit_cells(context):
    context.benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, '.BenefitCell')

@then('I should see 10 benefit cells')
def step_then_verify_benefit_cells(context):
    assert len(context.benefit_cells) == 10, f"Expected 10 benefit cells, found {len(context.benefit_cells)}."

def after_scenario(context, scenario):
    context.driver.quit()