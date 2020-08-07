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

    """
    登录:
        xpath: 
        //*[@text='']
        //*[@resource-id='']
    """
    def test_demo(self):
        self.driver.find_element(By.ID, 'com.shoumi.shoumi:id/tvTab5').click()
        self.driver.find_element_by_xpath('//*[@text="登录"]').click()
        phome_element = self.driver.find_element_by_xpath('//*[@resource-id="com.shoumi.shoumi:id/etPhone"]')
        phome_element.send_keys("18860918480")
        phome_pwd = self.driver.find_element_by_xpath('//*[@resource-id="com.shoumi.shoumi:id/etPwd"]')
        phome_pwd.send_keys("123456")
        self.driver.find_element_by_xpath('//*[@text="登录"]').click()
        self.driver.implicitly_wait(10)

    """
    获取用户名是否正确
        xpath： contains包含
            //*[contains(@resource-id, "")] 
    """
    def test_useruname(self):
        username = self.driver.find_element_by_xpath('//*[contains(@resource-id, "tvUserName")]').text
        assert 'flury' in username

    """
    xpath： contains包含
            //*[contains(@resource-id, "") and(or) contains(@text, '')] 
    """
    def test_task_centre(self):
        task_centre = self.driver.find_element_by_xpath('//*[contains(@resource-id, "tvName") and contains(@text, "任务中心")]').text
        assert "任务中心" in task_centre

    def teardown_class(self):
        self.driver.quit()
