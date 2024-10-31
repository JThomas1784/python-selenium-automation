import unittest
from selenium import webdriver
from MainPage import MainPage
from CartPage import CartPage

class TestAddProductToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def test_add_product_to_cart(self):
        self.main_page.open("https://target.com/products")
        self.main_page.select_product(1)
        self.main_page.product_page.add_to_cart()


        self.main_page.open("https://target.com/cart")
        self.assertTrue(self.cart_page.is_product_in_cart(), "Product was not added to the cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
