import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.inventory_item = (By.XPATH, "//*[text()='{}']")
        self.button_continue_shopping = (By.ID, "continue-shopping")
        

    def check_if_product_exist_in_cart(self, name_item):
        item = (self.inventory_item[0], self.inventory_item[1].format(name_item))
        self.check_if_element_exist(item)
        

    def continue_shopping(self):
        self.click(self.button_continue_shopping)
        