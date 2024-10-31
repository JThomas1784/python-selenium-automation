from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_TXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")

    def __init__(self, driver):
        self.driver = driver
        self.cart_item = "locator_for_cart_item"

    def is_product_in_cart(self):
        return self.driver.find_element_by_css_selector(self.cart_item).is_displayed()

    def verify_cart_empty(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_TXT)
