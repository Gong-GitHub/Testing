# Gong
import selenium
from selenium import webdriver

class Base():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
