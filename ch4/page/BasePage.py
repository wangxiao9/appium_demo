__author__ = 'wangxiao'

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ch4.utils import logger


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element_by_android_component(self, locator):
        return self.driver.find_element(*locator)

    def find_element(self, locator):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((locator)))
        return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        ele = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((locator)))
        ele.click()

    def find_element_and_send_keys(self, locator, param):
        ele = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((locator)))
        ele.send_keys(param)

    def get_element_and_text(self, locator):
        ele = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((locator)))
        return ele.text
