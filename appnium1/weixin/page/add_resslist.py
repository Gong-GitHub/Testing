# Gong
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from appnium1.weixin.page.base_page import BasePage
from appnium1.weixin.page.men_berinvite import MemberInvite


class AddressList(BasePage):
    def addmember(self):
        self.find(By.ID, 'com.tencent.wework:id/i6i').click()
        self.find(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        return MemberInvite(self._driver)

