from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Target main page')
def open_main(context):
      context.app.main_page.open_main()


@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart()

@when('Search for {item}')
def search_product(context, item):
    context.app.header.search_product(item)


@when('Search for {product}')
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

@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart()

@when('Search for {item}')
def search_product(context, item):
    context.app.header.search_product(item)

@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader']")
    assert len(links) == expected_amount, f'Expected {expected_amount} links, got {len(links)}'

@then('Verify header is shown')
def verify_header(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_utilityHeaderContainer']")

@then('Verify header has links')
def verify_header_links_shown(context):
    context.driver.find_element(By.CSS_SELECTOR, )