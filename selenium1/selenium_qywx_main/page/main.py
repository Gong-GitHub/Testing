# Gong
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium1.selenium_qywx_main.page.add_menber import AddMenber


class Main:
    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self._driver = webdriver.Chrome(options=options)
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')
    def goto_add_member(self):
        self._driver.find_element(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        return AddMenber(self._driver)