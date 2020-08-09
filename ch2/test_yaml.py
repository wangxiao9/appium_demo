__author__ = 'wangxiao'

import pytest

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.webdriver.webdriver import WebDriver
from hamcrest import assert_that, equal_to
import os
import yaml
# from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestSOUMi:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.shoumi.shoumi"
        caps["appActivity"] = ".activity.startActivity"
        caps["unicodeKeyboard"] = "true"
        caps["resetKeyboard"] = "true"
        caps["automationName"] = "Appium"
        caps["autoGrantPermissions"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    # @pytest.mark.parametrize('key, res', [('2334', '关于 2334 的搜索结果'), ('455' , '关于 455 的搜索结果')])
    # def test_search(self, key, res):
    #     self.driver.find_element_by_id('com.shoumi.shoumi:id/ivSearch').click()
    #     search_test = self.driver.find_element_by_id('com.shoumi.shoumi:id/etSearch')
    #     search_test.send_keys(key)
    #     self.driver.implicitly_wait(1000)
    #     os.system("adb shell ime set com.microvirt.memuime/.MemuIME")
    #     self.driver.press_keycode(AndroidKey.ENTER)
    #     result = self.driver.find_element_by_id('com.shoumi.shoumi:id/tvSearchResult').text
    #     assert_that(result, equal_to(res))
    #     search_test.clear()
    #     # 取消
    #     self.driver.find_element_by_id('com.shoumi.shoumi:id/tvClose').click()
    #     self.driver.implicitly_wait(10)

    def test_case_run(self):
        TestCaseTemplate('case.yaml').run(self.driver)

    def teardown_class(self):
        self.driver.quit()


class TestCaseTemplate:
    def __init__(self, path):
        with open(path, 'r', encoding="utf-8") as file:
            self.steps = yaml.safe_load(file)

    def method(self, driver: WebDriver, method, value):
        ele = None
        if method == 'id':
            ele = driver.find_element_by_id(value)
        elif method =='xpath':
            ele = driver.find_element_by_xpath(value)
        elif method == 'accessibility':
            ele = driver.find_element_by_accessibility_id(value)
        else:
            return 'No element'
        return ele

    def run(self, driver: WebDriver):
        for step in self.steps:
            elemet = None
            if isinstance(step, dict):
                if 'Methods' in step.keys() and 'Value' in step.keys():
                    elemet = self.method(driver, step['Methods'], step['Value'])
                else:
                    print(step.keys())
                if 'Action' in step.keys():
                    if 'click' in step['Action']:
                        elemet.click()
                    elif 'send_keys' in step['Action']:
                        if 'data' in step.keys():
                            elemet.send_keys(step['data'])
                        else:
                            print('没有输入的测试数据')
                    elif 'text' in step['Action']:
                        data = elemet.text
                        print(data)
