# Gong

from selenium import webdriver
class Index:
    def init(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://www.baidu.com/')