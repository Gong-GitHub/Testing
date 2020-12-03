# Gong
from time import sleep

import pytest
from appium import  webdriver


class TestDw:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.main.view.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        #desired_caps['dontStopAppOnRests'] ='true'
        desired_caps['unicodekeyBoard'] = 'true'
        desired_caps['resetkeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        '''
            1.打开雪球app
            2.点击搜索框
            3.向搜索狂输入’阿里巴巴‘
            4.在搜索结果里面选择’阿里巴巴‘，然后点击
            5.获取这只上香港阿里巴巴的股价，判断价格>200
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        sleep(5)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price=float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        assert current_price > 200
    def test_attr(self):
        '''
            1.打开‘雪球’app
            2.定位首页的搜索框
            3。判断搜索框是否可用，并查看搜索框name的属性值
            4.打印搜索框的左上角坐标和 他得宽高
            5.搜索框输入：alibaba
            6.判断‘阿里巴巴’是否可见
            7.如果可见，打印搜索成功， 否则打印搜索失败
        '''
        element=self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        search_enabled=element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled==True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('alibaba')
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            element_display = alibaba_element.get_attribute('displayed')
            if element_display=='true':
                print('搜索成功')
            else:
                print('搜索失败')

if __name__ == '__main__':
    pytest.main()

