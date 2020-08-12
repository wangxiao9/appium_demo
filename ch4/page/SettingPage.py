__author__ = 'wangxiao'

from selenium.webdriver.common.by import By

from ch4.page.BasePage import BasePage


class SettingPage(BasePage):
    _logout_locator = (By.ID, 'com.shoumi.shoumi:id/btnOutLogin')
    _logout_toast_locator = (By.XPATH, '//*[@class="android.widget.Toast"]')

    def user_logout(self):
        self.find_element_and_click(self._logout_locator)

    def user_logout_toast(self):
        logout_toast = self.find_element_by_android_component(self._logout_toast_locator)
        return logout_toast.text