'''

'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page.login_page import LoginPage
from page.base_page import BasePage

class ClientPage():
    def __init__(self,driver):
        self.url = "http://192.168.1.36/index.php?m=user&a=login"
        self.driver = driver
        #元素定位符
        #新建
        self.locator_client = (By.LINK_TEXT, '客户')
        self.locator_addclient = (By.CLASS_NAME,'btn-primary')
        self.locator_name = (By.ID,'name')
        self.locator_trade = (By.ID, 'industry')
        self.locator_message = (By.ID, 'origin')
        self.locator_Business = (By.NAME,'ownership')
        self.locator_emial = (By.ID, 'zip_code')
        self.locator_turnover = (By.ID, 'annual_revenue')
        self.locator_grade = (By.NAME, 'rating')
        self.locator_linkman = (By.NAME, 'con_name')
        self.locator_subimit = (By.XPATH,'//form[@id="form1"]/table/tfoot/tr/td/input[1]')
        self.locator_assert_result = (By.CLASS_NAME,'alert-success')
        #查看
        self.locator_check = (By.LINK_TEXT,'查看')
        self.locator_back = (By.LINK_TEXT,'返回')
        #编辑
        self.locator_compile_a = (By.LINK_TEXT,'编辑')
        self.locator_compile_b = (By.ID,'description')
        self.locator_compile_c = (By.XPATH, '//form[@id="form1"]/table/tfoot/tr/td/input[2]')
        #删除
        self.locator_delete_a = (By.NAME,'customer_id[]')
        self.locator_delete_b = (By.CSS_SELECTOR,'.btn.dropdown-toggle')
        self.locator_delete_c = (By.ID,'delete')
        self.locator_delete_e = (By.XPATH,'/html/body/div[5]/p/a[10]/img')
        self.locator_delete_f = (By.ID,'check_all')
        self.locator_delete_g = (By.CSS_SELECTOR, ".btn.dropdown-toggle")
        self.locator_delete_h = (By.ID,'delete')
        self.locator_assert_result_a = (By.CSS_SELECTOR,'.alert.alert-success')



        #新建客户
    def ele_client(self):
        self.driver.find_element(*self.locator_client).click()

    def ele_addclient(self):
        self.driver.find_element(*self.locator_addclient).click()

    def ele_name(self,name):
        self.driver.find_element(*self.locator_name).send_keys(name)

    def ele_trade(self):
        locator = self.driver.find_element(*self.locator_trade)
        select = Select(locator)
        select.select_by_value("对外贸易")
    def ele_message(self):
        locator = self.driver.find_element(*self.locator_message)
        select = Select(locator)
        select.select_by_value("网络营销")

    def ele_Business(self):
        self.driver.find_elements(*self.locator_Business)[0].click()

    def ele_emil(self,postcode):
        self.driver.find_element(*self.locator_emial).send_keys(postcode)

    def ele_turnover(self):
        locator = self.driver.find_element(*self.locator_turnover)
        select = Select(locator)
        select.select_by_value("20-50万")

    def ele_grade(self):
        self.driver.find_elements(*self.locator_grade)[2].click()
    #首要联系人
    def ele_linkman(self,Keycontact):
        self.driver.find_element(*self.locator_linkman).send_keys(Keycontact)
    #附加
    def ele_subimit(self):
        self.driver.find_element(*self.locator_subimit).click()
    #断言是否登录成功
    def assert_result(self):
        actual_result = self.driver.find_element(*self.locator_assert_result).text
        return actual_result
    #查看
    def ele_check(self):
        self.driver.find_element(*self.locator_check).click()
        time.sleep(1)
    def ele_back(self):
        self.driver.find_element(*self.locator_back).click()
        time.sleep(1)
    #编辑
    def ele_compile_a(self):
        self.driver.find_element(*self.locator_compile_a).click()
    def ele_compile_b(self):
        self.driver.find_element(*self.locator_compile_b).send_keys("喜欢青青草原的包包大人哦")
        time.sleep(1)
    def ele_compile_c(self):
        self.driver.find_element(*self.locator_compile_c).click()
    #删除
    def delete_a(self):
        self.driver.find_elements(*self.locator_delete_a)[0].click()
    def delete_b(self):
        self.driver.find_element(*self.locator_delete_b).click()
    def delete_c(self):
        self.driver.find_element(*self.locator_delete_c).click()
        time.sleep(1)
    def delete_d(self):
        self.driver.switch_to.alert.accept()
        time.sleep(1)
    def delete_e(self):
        self.driver.find_element(*self.locator_delete_e).click()
    def delete_f(self):
        self.driver.find_elements(*self.locator_delete_f)[0].click()
    def delete_g(self):
        self.driver.find_element(*self.locator_delete_g).click()
        time.sleep(1)
    def delete_h(self):
        self.driver.find_element(*self.locator_delete_h).click()
    def delete_j(self):
        self.driver.switch_to.alert.accept()
    #断言是否删除成功
    def assert_result_a(self):
        actual_result_a = self.driver.find_element(*self.locator_assert_result_a).text
        return actual_result_a

###
    def client_server(self):
        self.ele_client()

    def add(self,name,postcode,Keycontact):
        # self.driver.get(url=self.url)
        self.ele_client()
        self.ele_addclient()
        self.ele_name(name)
        self.ele_trade()
        self.ele_message()
        self.ele_Business()
        self.ele_emil(postcode)
        self.ele_turnover()
        self.ele_grade()
        self.ele_linkman(Keycontact)
        self.ele_subimit()
        actual_result = self.assert_result()
        time.sleep(2)
        # self.driver.quit()
        return actual_result
    def check(self):
        self.ele_check()
        self.ele_back()
        time.sleep(1)
    def modification(self):
        self.ele_compile_a()
        self.ele_compile_b()
        self.ele_compile_c()
        time.sleep(1)
    def delete(self):
        self.delete_a()
        self.delete_b()
        self.delete_c()
        self.delete_d()
        self.delete_e()
        self.delete_f()
        self.delete_g()
        self.delete_h()
        self.delete_j()
        time.sleep(1)
        actual_result_a = self.assert_result_a()
        time.sleep(2)
        # self.driver.quit()
        self.driver.quit()
        return actual_result_a