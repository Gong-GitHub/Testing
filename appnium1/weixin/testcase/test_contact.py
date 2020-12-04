# Gong
import pytest
from appium import  webdriver
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.common.by import By


class TestWeiXin:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipServerInstallation'] = 'true'     # 跳过server的安装
        desired_caps['skipDeviceInitialization'] = 'true'   # 跳过设备的初始化（安装），提高速度
        # desired_caps['dontStopAppOnRests'] ='true'
        desired_caps['unicodekeyBoard'] = 'true'
        desired_caps['resetkeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass
        #self.driver.quit()

    def test_weixin(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        self.driver.find_element(By.ID,'com.tencent.wework:id/i6i').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys('朱万SB')
        self.driver.find_element(MobileBy.XPATH,'//*[@text="性别"]/..//*[@class="android.widget.LinearLayout"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手机　"]/..//*[@class="android.widget.EditText"]').send_keys('18373621572')
        self.driver.find_element(By.ID,'com.tencent.wework:id/i6k').click()

if __name__ == '__main__':
    pytest.main()

