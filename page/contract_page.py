
import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ContractPage(BasePage):
    def __init__(self, driver):

        self.loc_ele_contract = (By.XPATH, '//ul[@class="nav"]/li[7]/a')
        self.loc_ele_btn = (By.CLASS_NAME, "btn-primary")
        self.loc_ele_number = (By.ID, 'number')
        self.loc_ele_rnumber = (By.ID, 'number')
        self.loc_ele_bus1 = (By.ID, 'business_name')
        self.loc_ele_bus2 = (By.NAME, "business")
        self.loc_ele_bus3 = (By.XPATH, '/html/body/div[7]/div[3]/div/button[1]/span')
        self.loc_ele_start = (By.ID, "start_date")
        self.loc_ele_due = (By.ID, "due_time")
        self.loc_ele_price = (By.ID, "price")
        self.loc_ele_end = (By.ID, "end_date")
        self.loc_ele_back = (By.XPATH, '//table[@class="table"]/tfoot/tr/td[2]/input[2]')
        self.loc_ele_check = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[1]/td[10]/a[1]')
        self.loc_ele_outcheck = (By.XPATH, '//div[@id="tab1"]/div[1]/div/a[3]')
        self.loc_ele_comp = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[1]/td[10]/a[2]')
        self.loc_ele_outcomp = (By.XPATH, '//div[@id="tab1"]/form/table/thead/tr/td[2]/input[2]')



    def ele_contract(self):
        self.driver.find_element(*self.loc_ele_contract).click()

    # 合同编号设置添加
    def ele_btn(self):
        self.driver.find_element(*self.loc_ele_btn).click()

    # 合同编号
    def ele_number(self):
        self.driver.find_element(*self.loc_ele_number).clear()

    def ele_rnumber(self):
        date = time.strftime("%Y%m%d%H%M%S")
        self.driver.find_element(*self.loc_ele_rnumber).send_keys(date)

    # 来源商机
    def ele_bus1(self):
        self.driver.find_element(*self.loc_ele_bus1).click()
        time.sleep(2)
    def ele_bus2(self):
        self.driver.find_element(*self.loc_ele_bus2).click()
    def ele_bus3(self):
        self.driver.find_element(*self.loc_ele_bus3).click()

    # 输入合同生效时间
    def ele_start(self,stime):

        self.driver.find_element(*self.loc_ele_start).send_keys(stime)

    # 合同签约时间
    def ele_due(self,dtime):

        self.driver.find_element(*self.loc_ele_due).send_keys(dtime)

    # 合同金额
    def ele_price(self,price):

        self.driver.find_element(*self.loc_ele_price).send_keys(price)

    # 合同到期时间
    def ele_end(self,etime):

        self.driver.find_element(*self.loc_ele_end).send_keys(etime)

    # 退出新建合同
    def ele_back(self):
        self.driver.find_element(* self.loc_ele_back).click()

    # 点击查看
    def ele_check(self):
        self.driver.find_element(*self.loc_ele_check).click()

    # 退出查看
    def ele_outcheck(self):
        self.driver.find_element(*self.loc_ele_outcheck).click()

    # 点击编辑
    def ele_comp(self):
        self.driver.find_element(*self.loc_ele_comp).click()

    # 退出编辑
    def ele_outcomp(self):
        self.driver.find_element(*self.loc_ele_outcomp).click()

    def contract(self, stime,dtime,price,etime):
        self.ele_contract()
        self.ele_btn()
        self.ele_number()
        self.ele_rnumber()
        self.ele_start(stime)
        self.ele_due(dtime)
        self.ele_price(price)
        self.ele_end(etime)
        self.ele_back()
        self.ele_check()
        self.ele_outcheck()
        self.ele_comp()
        self.ele_outcomp()

        return self.contract()
        self.driver.quit()
