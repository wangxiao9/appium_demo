__author__ = 'wangxiao'

import logging

from selenium.webdriver.common.by import By

logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%d-%b-%y %H:%M:%S')
def waring(message):
    logging.warning(message)


def error(message):
    logging.error(message)


def func(locatory):
    print(locatory)

if __name__ == '__main__':
    main_locator = (By.ID, 'com.shoumi.shoumi:id/llTab1')
    func((main_locator))