# Gong
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import  *

class TestTouchAction:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.main.view.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodekeyBoard'] = 'true'
        desired_caps['resetkeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()
        # self.driver.quit()
    @pytest.mark.parametrize('searchkey , expect_price',[
        ('alibaba',260),
        ('baidu',150)
    ])
    def test_search(self,searchkey,expect_price):
        '''
            1.打开雪球应用
            2.点击搜索框
            3.输入’alibabab‘ or ’xiaomi‘
            4.点击第一个搜索结果
            5。判断股票价格
        :return:
        '''
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/home_search').click()
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys(searchkey)
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/name').click()
        current_price = float(self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/current_price').get_attribute('text'))
        assert_that(current_price,close_to(expect_price,expect_price*0.1))

        #print(current_price)