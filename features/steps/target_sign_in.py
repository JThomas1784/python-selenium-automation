import unittest
from selenium import webdriver
from MainPage import MainPage
from SignInPage import SignInPage

class TestSignInAccess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)

    def test_logged_out_user_can_access_sign_in(self):
        self.main_page.open("https://target.com")
        self.main_page.click_sign_in()


        self.assertTrue(self.sign_in_page.is_sign_in_form_opened(), "Sign In form did not open.")

    def tearDown(self):
        self.driver.quit()