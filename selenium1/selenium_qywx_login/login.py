# Gong
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium1.selenium_qywx_login.register import Register


class Login:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def scanf(self):
        pass
    def goto_register(self):
        self._driver.find_element(By.XPATH, '//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        return Register(self._driver)