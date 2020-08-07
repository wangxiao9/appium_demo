__author__ = 'wangxiao'

import pytest

from appium import webdriver
from hamcrest import assert_that, equal_to


class TestSOUMi:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.shoumi.shoumi"
        caps["appActivity"] = ".activity.startActivity"
        caps["unicodeKeyboard"] = "true"
        caps["resetKeyboard"] = "true"
        caps["autoGrantPermissions"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    @pytest.mark.parametrize('key, res', [('2334', '关于 2334 的搜索结果'), ('455' , '关于 455 的搜索结果')])
    def test_search(self, key, res):
        self.driver.find_element_by_id('com.shoumi.shoumi:id/ivSearch').click()
        search_test = self.driver.find_element_by_id('com.shoumi.shoumi:id/etSearch')
        search_test.send_keys(key)
        self.driver.press_keycode(66)
        result = self.driver.find_element_by_id('com.shoumi.shoumi:id/tvSearchResult').text
        assert_that(result, equal_to(res))
        search_test.clear()
        # 取消
        self.driver.find_element_by_id('com.shoumi.shoumi:id/tvClose').click()
        self.driver.implicitly_wait(10)


    def teardown_class(self):
        self.driver.quit()
