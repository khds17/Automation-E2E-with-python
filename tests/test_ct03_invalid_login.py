import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct03_invalid_login(self): 
         
        erro_message = "Epic sadface: Username and password do not match any user in this service"
        
        #Instance the objects used
        login_page = LoginPage()
        home_page = HomePage()
        
        #Log-in
        login_page.login("standard_user", "xxxxx")
        
        #Check the login error message.
        login_page.check_error_message_login()
        login_page.check_text_error_message_login(erro_message)