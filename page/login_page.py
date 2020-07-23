import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,driver):
        #初始化
        self.driver = driver#调用的是testcase实例化的浏览器驱动
        self.url = 'http://192.168.1.36/index.php?m=user&a=login'
        self.loc_ele_username = (By.NAME,'name')
        self.loc_ele_password = (By.NAME,'password')
        self.loc_ele_autologin = (By.NAME,'autologin')
        self.loc_ele_submit = (By.NAME,'submit')
        self.loc_ele_result = (By.XPATH,'//div[@class="nav-collapse collapse"]/ul[2]/li[6]/a')
    def ele_username(self,name):
        self.driver.find_element(*self.loc_ele_username).clear()
        self.driver.find_element(*self.loc_ele_username).send_keys(name)
    def ele_password(self,pwd):
        self.driver.find_element(*self.loc_ele_password).clear()
        self.driver.find_element(*self.loc_ele_password).send_keys(pwd)
    def ele_autologin(self):
        self.driver.find_element(*self.loc_ele_autologin).click()
    def ele_submit(self):
        self.driver.find_element(*self.loc_ele_submit).click()
    def ele_result(self):
        result = self.driver.find_element(*self.loc_ele_result).text
        return result
    def login(self,name,pwd):
        self.open(self.url)
        self.ele_username(name)
        self.ele_password(pwd)
        self.ele_autologin()
        self.ele_submit()
        time.sleep(2)
        results = self.ele_result()
        return results

