# Gong
import shelve

import selenium
from requests import cookies
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class TestBase():
    def setup(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9333'
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_chrome(self):
        self.driver.get('http://www.baidu.com')
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db = shelve.open("")
        #db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('http://www.baidu.com')
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(5)
        db.close()
        self.driver.find_element_by_id('menu_contacts').click()
        sleep(3)
