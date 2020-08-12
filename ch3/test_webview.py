__author__ = 'wangxiao'

import pytest

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from hamcrest import assert_that, equal_to
import os

class TestWebView:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "tiantianjijin"
        caps["appPackage"] = "com.hupu.games"
        caps["appActivity"] = ".launcher.StartUpActivity"
        caps["unicodeKeyboard"] = "true"
        # caps["resetKeyboard"] = "true"
        caps["autoGrantPermissions"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10000)

    def test_webview(self):
        self.driver.implicitly_wait(10000)
        self.driver.find_element_by_id('com.hupu.games:id/btn_bbs').click()
        self.driver.find_element_by_android_uiautomator(
            'UiSelector().className("android.view.View").enabled(true).index(0);').click()
        self.driver.implicitly_wait(10000)
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("这些回复亮了").instance(0));')

    def teardown_class(self):
        self.driver.quit()
