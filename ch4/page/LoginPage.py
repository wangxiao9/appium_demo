__author__ = 'wangxiao'

from selenium.webdriver.common.by import By

from ch4.page.BasePage import BasePage


class LoginPage(BasePage):
    _login_locator = (By.XPATH, '//*[@text="登录"]')
    _phone_locator = (By.XPATH, '//*[@resource-id="com.shoumi.shoumi:id/etPhone"]')
    _password_locator = (By.XPATH, '//*[@resource-id="com.shoumi.shoumi:id/etPwd"]')
    _login_toast_locator = (By.XPATH, '//*[@class="android.widget.Toast"]')

    def username_login_shoumi(self, phone, password):
        self.find_element_and_send_keys(self._phone_locator, phone)
        self.find_element_and_send_keys(self._password_locator, password)
        self.find_element_and_click(self._login_locator)

    def get_login_toast(self):
        login_toast = self.find_element_by_android_component(self. _login_toast_locator)
        return login_toast.text

