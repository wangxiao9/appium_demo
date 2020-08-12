__author__ = 'wangxiao'


from selenium.webdriver.common.by import By

from ch4.page.BasePage import BasePage
from ch4.page.LoginPage import LoginPage
from ch4.page.SettingPage import SettingPage


class ProfilePage(BasePage):
    _login_locator = (By.XPATH, '//*[@text="登录"]')
    _setting_locator = (By.XPATH, '//*[@text="设置"]')

    def into_login_page(self):
        self.find_element_and_click(self._login_locator)
        return LoginPage(self.driver)

    def into_setting_page(self):
        self.find_element_and_click(self._setting_locator)
        return SettingPage(self.driver)