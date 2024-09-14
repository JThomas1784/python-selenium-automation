from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


    @when('Search for a product')
    def search_product(context):
        context.driver.find_element(By.ID, 'search').send_keys('tea')
    # Search button => click
        context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click
        sleep(6)


    @then('Verify that correct search results shown')
    def verify_results(context):
        actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
        expected_result = 'tea'

        assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
        print('Test case passed')

