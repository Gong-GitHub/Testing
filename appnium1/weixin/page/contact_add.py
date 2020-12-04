# Gong
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from appnium1.weixin.page.base_page import BasePage


class ContactAdd(BasePage):
    def input_name(self):
        self.find(MobileBy.XPATH,'//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys('朱万SB')
        return self

    def input_genser(self):
        self.find(MobileBy.XPATH, '//*[@text="性别"]/..//*[@class="android.widget.LinearLayout"]').click()
        self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        return self

    def input_phone(self):
        self.find(MobileBy.XPATH,'//*[@text="手机　"]/..//*[@class="android.widget.EditText"]').send_keys('18373621572')
        return self

    def click_save(self):
        # 反复调用，采用局部导入
        from appnium1.weixin.page.men_berinvite import MemberInvite
        self.find(By.ID,'com.tencent.wework:id/i6k').click()
        return MemberInvite(self._driver)