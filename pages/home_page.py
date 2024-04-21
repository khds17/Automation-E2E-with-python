import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
        self.inventory_item = (By.XPATH, "//*[text()='{}']")
        self.add_to_cart_button = (By.XPATH, "//*[text()='Add to cart']")
        self.cart_button = (By.XPATH, "//*[@class='shopping_cart_link']")
        
    def check_login_successfully(self):
        self.check_if_element_exist(self.page_title)
        
    def add_product_to_cart(self, name_item):
        item = (self.inventory_item[0], self.inventory_item[1].format(name_item))
        self.click(item)
        self.click(self.add_to_cart_button)
        
    def go_to_cart(self):
        self.click(self.cart_button)