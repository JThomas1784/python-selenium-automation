from pages.base_page import Page


class MainPage(Page):

    def __init__(self, driver):
        self.driver = driver
        self.header_menu = HeaderMenu(driver)
        self.product_page = ProductPage(driver)

    def open(self, url):
        self.driver.get(url)

    def click_sign_in(self):
        self.header_menu.click_sign_in()

    def open_main(self):
        self.open('https://www.target.com')

    def select_product(self, product_index):
        product_selector = f"locator_for_product_{product_index}"
        self.driver.find_element_by_css_selector(product_selector).click()