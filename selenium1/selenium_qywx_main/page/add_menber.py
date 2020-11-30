# Gong
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium1.selenium_qywx_main.page.base_page import BasePage


class AddMenber(BasePage):

    def add_member(self):
        self.find(By.ID, 'username').send_keys('朱万')
        self.find(By.ID, 'memberAdd_acctid').send_keys('11111')
        self.find(By.ID, 'memberAdd_phone').send_keys('18673612165')
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
    def update_page(self):
        content:str = self.find(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
        # 对1/10进行分割
        return [int(x) for x in content.split('/',1)]
    def get_menber(self,value):
        self.waif_for_click((By.CSS_SELECTOR,'.ww_checkbox'))
        cur_page,total_page=self.update_page()
        while True:
            elements = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
            for element in elements:
                # get_attribute:找到该元素，并生成list列表
                if value == element.get_attribute('title'):
                    return  True
            cur_page=self.update_page()[0]
            if cur_page == total_page:
                return False
            self.find(By.CSS_SELECTOR,'.js_next_page').click()


