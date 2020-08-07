__author__ = 'wangxiao'


from appium import webdriver

caps = {}

caps["platformName"] = "android"
caps["deviceName"] = "emulator-5554"
caps["appPackage"] = "com.shoumi.shoumi"
caps["appActivity"] = ".activity.startActivity"
caps["autoGrantPermissions"] = True


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

driver.implicitly_wait(1000)

driver.quit()
