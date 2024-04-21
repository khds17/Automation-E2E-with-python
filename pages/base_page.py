import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import expected_conditions as EC 
from selenium.webdriver import *

class BasePage:
    def __init__(self):
        self.driver = conftest.driver
        
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def send(self, locator, text):
        self.find_element(locator).send_keys(text)
        
    def click(self, locator):
        self.find_element(locator).click()
        
    def check_if_element_exist(self, locator):
        self.wait_element_appear(locator)
        assert self.find_element(locator).is_displayed(), f"The element '{locator}' was not found."
    
    def get_text(self, locator):
        self.wait_element_appear(locator)
        return self.find_element(locator).text
    
    def wait_element_appear(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))
    
    def verify_if_element_exist(self, locator):
        assert self.find_element(locator), f"Error: The element '{locator} doesn't exist'"
        
    def verify_if_element_not_exist(self, locator):
        assert len(self.find_elements(locator)) == 0, f"Error: The element '{locator} exist'"
        
    def double_click(self, locator):
        element = self.wait_element_appear(locator)
        ActionChains(self.driver).double_click(element).perform()
        
    def right_click(self, locator):
        element = self.wait_element_appear(locator)
        ActionChains(self.driver).context_click(element).perform()
        
    def press_key(self, locator, key):
        element = self.find_element(locals)
        
        if key == "ENTER":
            element.send_keys(Keys.ENTER)
        elif key == "SPACE":
            element.send_keys(Keys.SPACE)
            
        