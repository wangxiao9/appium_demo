__author__ = 'wangxiao'

from selenium.webdriver.common.by import By

"""
id : resource-id
"""
from appium import webdriver

caps = {}

caps["platformName"] = "android"
caps["deviceName"] = "emulator-5554"
caps["appPackage"] = "com.shoumi.shoumi"
caps["appActivity"] = ".activity.startActivity"
caps["autoGrantPermissions"] = True


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(10)
# myelememt = driver.find_element_by_id('com.shoumi.shoumi:id/tvTab5')
driver.find_element_by_accessibility_id()
myelememt = driver.find_element(By.ID, 'com.shoumi.shoumi:id/tvTab5')
myelememt.click()
driver.implicitly_wait(10)
driver.quit()
