# Gong
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appnium1.weixin.page.add_resslist import AddressList
from appnium1.weixin.page.base_page import BasePage


class Main(BasePage):
    def goto_massage(self):
        pass

    def goto_addresslist(self):
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return AddressList(self._driver)
