# Gong
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium1.selenium_qywx_login.login import Login
from selenium1.selenium_qywx_login.register import Register


class Index:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://work.weixin.qq.com/')
    def goto_login(self):
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self._driver)

    def goto_register(self):
        self._driver.find_element(By.XPATH, '//*[@id="tmp"]/div[1]/a').click()
        return Register(self._driver)
