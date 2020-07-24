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
        self.locator_compile = (By.LINK_TEXT,'编辑')
        self.locator_remarks = (By.ID,'description')
        self.locator_cancel = (By.XPATH, '//form[@id="form1"]/table/tfoot/tr/td/input[2]')
        #删除
        self.locator_checkbox = (By.NAME,'customer_id[]')
        self.locator_bulk_operation = (By.CSS_SELECTOR,'.btn.dropdown-toggle')
        self.locator_delete_in_batches = (By.ID,'delete')
        self.locator_recycle_bin = (By.XPATH,'/html/body/div[5]/p/a[10]/img')
        self.locator_check_all = (By.ID,'check_all')
        self.locator_batch = (By.CSS_SELECTOR, ".btn.dropdown-toggle")
        self.locator_Batch_Remove = (By.ID,'delete')
        self.locator_assert_delete = (By.CSS_SELECTOR,'.alert.alert-success')



    '''新建客户'''
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
    def ele_compile(self):
        self.driver.find_element(*self.locator_compile).click()
    def ele_remarks(self):
        self.driver.find_element(*self.locator_remarks).send_keys("喜欢青青草原的包包大人哦")
        time.sleep(1)
    def ele_cancel(self):
        self.driver.find_element(*self.locator_cancel).click()
    #删除
    def checkbox(self):
        self.driver.find_elements(*self.locator_checkbox)[0].click()
    def bulk_operation(self):
        self.driver.find_element(*self.locator_bulk_operation).click()
    def delete_in_batches (self):
        self.driver.find_element(*self.locator_delete_in_batches).click()
        time.sleep(1)
    def Confirm_the_deletion(self):
        self.driver.switch_to.alert.accept()
        time.sleep(1)
    def recycle_bin(self):
        self.driver.find_element(*self.locator_recycle_bin).click()
    def check_all(self):
        self.driver.find_elements(*self.locator_check_all)[0].click()
    def batch(self):
        self.driver.find_element(*self.locator_batch).click()
        time.sleep(1)
    def Batch_Remove(self):
        self.driver.find_element(*self.locator_Batch_Remove).click()
    def confirm(self):
        self.driver.switch_to.alert.accept()
    #断言是否删除成功
    def assert_result_delete(self):
        actual_result = self.driver.find_element(*self.locator_assert_delete).text
        return actual_result

###
    def client_server(self):
        self.ele_client()

    def add(self,name,postcode,Keycontact): #添加
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
    def check(self): #查看
        self.ele_check()
        self.ele_back()
        time.sleep(1)
    def modification(self): #编辑
        self.ele_compile()
        self.ele_remarks()
        self.ele_cancel()
        time.sleep(1)
    def delete(self): #删除
        self.checkbox()
        self.bulk_operation()
        self.delete_in_batches()
        self.Confirm_the_deletion()
        self.recycle_bin()
        self.check_all()
        self.batch()
        self.Batch_Remove()
        self.confirm()
        time.sleep(1)
        actual_result_delete = self.assert_result_delete()
        time.sleep(2)
        # self.driver.quit()
        self.driver.quit()
        return actual_result_delete