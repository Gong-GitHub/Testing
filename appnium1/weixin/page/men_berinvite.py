# Gong
from appium.webdriver.common.mobileby import MobileBy

from appnium1.weixin.page.base_page import BasePage
from appnium1.weixin.page.contact_add import ContactAdd


class MemberInvite(BasePage):
    def addmenber_by(self):
        self.find(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        return ContactAdd(self._driver)

    def get_toast(self):
        return self.find(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
