__author__ = 'wangxiao'

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from ch4.config import config
from ch4.driver.platforms import PlatformSet
from ch4.page.MainPage import MainPage

"""
封装启动app
"""


class App:
    driver: WebDriver = None

    @classmethod
    def start(cls):
        caps = PlatformSet('android', 'shoumi').run()
        cls.driver = webdriver.Remote(config.APPIUM_URL, caps)
        cls.driver.implicitly_wait(10)
        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()
