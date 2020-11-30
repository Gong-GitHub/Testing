# Gong
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium1.selenium_qywx_main.page.add_menber import AddMenber
from selenium1.selenium_qywx_main.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_member(self):
        #self._driver.find_element(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        self.find(By.XPATH,'//*[@id="menu_contacts"]/span').click()
        locator=(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1) a:nth-child(2)')
        self.waif_for_click(locator)
        self.find(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1) a:nth-child(2)').click()
        return AddMenber(self._driver)