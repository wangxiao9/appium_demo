__author__ = 'wangxiao'

from hamcrest import assert_that, equal_to

"""
https://github.com/hamcrest/PyHamcrest
pip install PyHamcrest
"""

from selenium.webdriver.common.by import By


from appium import webdriver


class TestSOUMi:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.shoumi.shoumi"
        caps["appActivity"] = ".activity.startActivity"
        caps["autoGrantPermissions"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_login(self):
        self.driver.find_element(By.ID, 'com.shoumi.shoumi:id/tvTab5').click()
        self.driver.implicitly_wait(10)

    """
    判断元素是否存在:
        get_attribute
    """
    def test_Hamcrest(self):
        task = self.driver.find_element_by_xpath('//*[contains(@resource-id, "tvName") and contains(@text, "任务中心")]')
        assert_that(task.text, equal_to('任务中心'))

    def teardown_class(self):
        self.driver.quit()
