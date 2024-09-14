class Page:
    def __init__(self, driver):

    def click(self):
        print('Clicking')

    def input_text(self, text):
        print(f'Entering text {text}')

    def find_element(self):
        print('Searching for element')




    class LoginPage(Page):
        def login(self):
            self.find_element()
            self.click()


    login_page = LoginPage()
    login_page.input_text('login...')