import time

import xlrd

from driver.browser import chrome_driver

class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.url = 'http://192.168.1.36/index.php?m=user&a=login'
        self.driver.get(url)
        time.sleep(3)

    def quit(self):
        self.driver.quit()
