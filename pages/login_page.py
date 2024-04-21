import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message_login = (By.XPATH, "//div[@class='error-message-container error']")
        
    def login(self, user, password):
        self.send(self.username_field, user)
        self.send(self.password_field, password)
        self.click(self.login_button)
        
    def check_error_message_login(self):
        self.check_if_element_exist(self.error_message_login)
        
    def check_text_error_message_login(self, text):
        result_text = self.get_text(self.error_message_login)
        assert  result_text == text, f"Return the text '{result_text}', but expected the text '{text}'"
        
        