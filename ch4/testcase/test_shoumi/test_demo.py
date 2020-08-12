__author__ = 'wangxiao'

from selenium.webdriver.common.by import By


from appium import webdriver

from ch4.page.MainPage import MainPage
from ch4.page.app import App


class TestSOUMi:
    def setup_class(self):
        mainPage = App.start()
        self.match_page = mainPage.into_match_page()

    def test_match(self):
        print("完成")

    def teardown_class(self):
        App.quit()
