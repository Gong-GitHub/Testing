# Gong
from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'appPackage': 'com.xueqiu.android',
    'appActivity': '.main.view.MainActivity',
    'noReset': 'true',
    'dontStopAppOnRests':'true'
}
# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 获取页面源码
el1 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
el1.click()
