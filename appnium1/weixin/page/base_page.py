# Gong
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    # 弹框处理的名单列表
    _black_list=[
        (By.XPATH,"//*[@text='确认']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']"),
    ]
    # 设置查找异常的次数
    _max_num= 3
    _error_num=0
    def __init__(self,driver:WebDriver=None):
        self._driver =driver

    def find(self,locator,value:str=None):
        element=WebElement
        try:
            if isinstance(locator,tuple):
                element=self._driver.find_element(*locator)
            else:
                element=self._driver.find_element(locator,value)
            return element
            # 查找之前_error_num 归 0
            self._error_num = 0
        except Exception as e:
            # 判断查找次数
            if self._error_num > self._max_num:
                raise e
            self._error_num+=1
            # 处理黑名单里面的弹框
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹框，再去查找目标元素
                    return self.find(locator,value)
            raise e