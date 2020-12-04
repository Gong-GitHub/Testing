# Gong
from appium import webdriver

from appnium1.weixin.page.base_page import BasePage
from appnium1.weixin.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver==None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['deviceName'] = '127.0.0.1:62001'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
            desired_caps['noReset'] = 'true'
            desired_caps['skipServerInstallation'] = 'true'
            desired_caps['skipDeviceInitialization'] = 'true'
            # desired_caps['dontStopAppOnRests'] ='true'
            desired_caps['unicodekeyBoard'] = 'true'
            desired_caps['resetkeyBoard'] = 'true'
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(8)

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        return Main(self._driver)
