import time

from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from page.base_page import BasePage

class ClewPage(BasePage):
    def __init__(self,driver):

        self.driver = driver#调用的是testcase实例化的浏览器驱动
        self.url = 'http://192.168.1.36/index.php?m=user&a=login'
        self.loc_ele_clew = (By.XPATH,'//div[@class="nav-collapse collapse"]/ul[1]/li[1]/a')#线索按钮
        self.loc_ele_clew_add = (By.CLASS_NAME, 'btn-primary')#新增线索
        self.loc_ele_clew_username = (By.ID, 'contacts_name')#线索联系人必填项
        self.loc_ele_clew_submit = (By.NAME, 'submit')#保存按钮

    def ele_clew(self):
        self.driver.find_element(*self.loc_ele_clew).click()

    def ele_clew_add(self):
        self.driver.find_element(*self.loc_ele_clew_add).click()

    def ele_clew_username(self,clew_usernam):
        self.driver.find_element(self.loc_ele_clew_username).send_keys(clew_usernam)

    def ele_clew_submit(self):
        self.driver.find_element(*self.loc_ele_clew_submit).click()

    def clew_add(self,clew_usernam):

        self.ele_clew()
        self.ele_clew_add()
        self.ele_clew_username(clew_usernam)
        self.ele_clew_submit()
        self.quit()



