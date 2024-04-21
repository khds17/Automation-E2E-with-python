import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage



@pytest.mark.usefixtures("setup_teardown")
class TestCT01: 
    def test_ct01_add_produt_in_cart(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        
        product_1 = "Sauce Labs Backpack"
        product_2 = "Sauce Labs Bolt T-Shirt"
        
        #Login
        login_page.fazer_login("standard_user", "secret_sauce")

        #Add backpack in cart 
        home_page.add_product_to_cart(product_1)

        # #Check if the backpack was add in cart
        home_page.go_to_cart()
        cart_page.check_if_product_exist_in_cart(product_1)
        
        # #Back to the products 
        cart_page.continue_shopping()

        # #Add t-shirt in cart 
        home_page.add_product_to_cart(product_2)

        # #Check if the t-shirt was add in cart
        home_page.go_to_cart()
        cart_page.check_if_product_exist_in_cart(product_2)
        



