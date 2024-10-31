class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_form = "locator_for_sign_in_form"  # Replace with actual locator

    def is_sign_in_form_opened(self):
        return self.driver.find_element_by_css_selector(self.sign_in_form).is_displayed()
