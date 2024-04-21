import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_valid_login(self): 
        #Instance the objects used
        login_page = LoginPage()
        home_page = HomePage()
        
        #Log-in
        login_page.login("standard_user", "secret_sauce")
        
        #Check with login it's OK.
        home_page.check_login_successfully()