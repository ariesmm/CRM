import time

from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from page.base_page import BasePage

class ClewPage(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.url = 'http://192.168.1.36/index.php?m=user&a=login'
        self.loc_ele_clew = (By.XPATH,'//div[@class="nav-collapse collapse"]/ul[1]/li[1]/a')
        self.loc_ele_clew_add = (By.CLASS_NAME, 'btn-primary')
        self.loc_ele_clew_username = (By.ID, 'contacts_name')
        self.loc_ele_clew_submit = (By.NAME, 'submit')

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



