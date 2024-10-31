from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.wait_to_be_clickable(*self.CART_BTN)
        # self.driver.find_element(*self.CART_BTN).click()

    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = "locator_for_sign_in_button"

    def click_sign_in(self):
        self.driver.find_element_by_css_selector(self.sign_in_button).click()