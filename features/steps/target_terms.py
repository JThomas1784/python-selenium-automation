from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:

    driver.get('https://www.target.com/login')

    time.sleep(2)

    original_window = driver.current_window_handle

    terms_link = driver.find_element(By.LINK_TEXT, "Terms and Conditions")
    terms_link.click()

    time.sleep(2)

    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break


    assert "Terms and Conditions" in driver.title, "Terms and Conditions page did not open as expected."


    driver.close()
    driver.switch_to.window(original_window)

    assert "Sign In" in driver.title, "Did not return to Sign In page as expected."

finally:

    driver.quit()