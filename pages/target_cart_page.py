from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_cart_icon(self):
        cart_icon = self.driver.find_element(By.CSS_SELECTOR, 'a[data-test="cart"]')
        cart_icon.click()

    def is_empty_cart_message_displayed(self):
        message_element = self.driver.find_element(By.CSS_SELECTOR, 'h1[data-test="empty-cart-message"]')
        return "Your cart is empty" in message_element.text