__author__ = 'wangxiao'

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
        self.driver.find_element_by_xpath('//*[@text="登录"]').click()
        phome_element = self.driver.find_element_by_xpath('//*[@resource-id="com.shoumi.shoumi:id/etPhone"]')
        phome_element.send_keys("18860918480")
        phome_pwd = self.driver.find_element_by_xpath('//*[@resource-id="com.shoumi.shoumi:id/etPwd"]')
        phome_pwd.send_keys("123456")
        self.driver.find_element_by_xpath('//*[@text="登录"]').click()
        toast = self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text
        print("toast内容是：", toast)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()
