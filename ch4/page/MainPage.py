__author__ = 'wangxiao'

from selenium.webdriver.common.by import By

from ch4.page.BasePage import BasePage
from ch4.page.MatchPage import MatchPage
from ch4.page.ProfilePage import ProfilePage


class MainPage(BasePage):
    _main_locator = (By.ID, 'com.shoumi.shoumi:id/llTab1')
    _match_locator = (By.ID, 'com.shoumi.shoumi:id/ivTab2')
    _profile_locator = (By.ID, 'com.shoumi.shoumi:id/tvTab5')

    def into_mian_page(self):
        self.find_element_and_click(self._main_locator)
        return MainPage(self.driver)

    def into_match_page(self):
        self.find_element_and_click(self._main_locator)
        return MatchPage(self.driver)

    def into_profile_locator(self):
        self.find_element_and_click(self._profile_locator)
        return ProfilePage(self.driver)