import time
import unittest

from selenium.webdriver.common.by import By

from page.base_page import BasePage
class BusinessPage(BasePage):
    def __init__(self,driver):
        self.driver = driver
        # self.url = 'http://192.168.1.36/index.php?m=user&a=login'
        '''新增商机'''
        self.loc_ele_collapse = (By.XPATH, '//div[@class="nav-collapse collapse"]/ul[1]/li[3]/a')# 商机菜单
        self.loc_ele_primary = (By.CLASS_NAME, 'btn-primary')# 添加商机按钮
        self.loc_ele_owner_name = (By.ID, 'owner_name')# 选择负责人
        self.loc_ele_owner_content = (By.XPATH, '//tbody[@id="d_content"]/tr[1]/td[1]/input')#进行选择
        self.loc_ele_owner_name_Ok = (By.CSS_SELECTOR, 'div[id="dialog-role-list"]+div>div :nth-child(1)')# 点击OK
        self.loc_ele_customer_name = (By.ID, 'customer_name')# 选择客户
        self.loc_ele_customer_content = (By.XPATH, '//*[@id="datas"]/tr[1]/td[1]/input[1]')
        self.loc_ele_customer_Ok = (By.CSS_SELECTOR, 'div[id="dialog-message"]+div>div :nth-child(1)')# 点击OK
        self.loc_ele_name = (By.ID, 'name')
        self.loc_ele_estimate_price = (By.ID, 'estimate_price')# 商机名
        self.loc_ele_product_name = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[12]/th/input')# 预计成交价
        self.loc_ele_product_content = (By.XPATH, '//tbody[@id="data"]/tr[1]/td[1]/input[1]')# 添加产品
        self.loc_ele_product_OK = (By.CSS_SELECTOR, 'div[id="dialog-product-list"]+div>div :nth-child(1)') # 点击OK
        self.loc_ele_business_submit = (By.XPATH, '//form[@id="form1"]/table/tfoot/tr/td/input[1]')# 点击保存
        self.loc_ele_result = (By.CLASS_NAME,'alert-success')#断言，提示添加商机成功
        '''修改商机'''
        self.loc_ele_business_update = (By.XPATH,'//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[3]')
        self.loc_ele_business_update_submit =(By.NAME,'submit')
        '''推进商机'''
        self.loc_ele_business_push = (By.CLASS_NAME, 'advance')
        self.loc_ele_business_push_submit = (By.XPATH,'//div[@id="dialog-advance"]/form/table/tbody/tr[5]/td[2]/input[1]')
        '''删除商机'''
        self.loc_ele_business_delete_click = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[1]/td[1]/input')
        self.loc_ele_business_delete = (By.ID, 'delete')
        '''查看商机'''
        self.loc_ele_business_view = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[1]')
        self.loc_ele_business_view_assert = (By.XPATH, '//ul[@id="left_list"]/li[1]/span')
    def ele_collapse(self):
        self.driver.find_element(*self.loc_ele_collapse).click()  # 商机菜单
    def ele_primary(self):
        self.driver.find_element(*self.loc_ele_primary).click()  # 添加商机按钮
    def ele_owner_name(self):
        self.driver.find_element(*self.loc_ele_owner_name).click()  # 选择负责人
        time.sleep(2)
        self.driver.find_element(*self.loc_ele_owner_content).click()#进行选择
        self.driver.find_element(*self.loc_ele_owner_name_Ok).click()  # 点击OK
    def ele_customer_name(self):
        self.driver.find_element(*self.loc_ele_customer_name).click()  # 选择客户
        time.sleep(2)
        self.driver.find_element(*self.loc_ele_customer_content).click()
        self.driver.find_element(*self.loc_ele_customer_Ok).click()  # 点击OK
    def ele_business_name(self,businessname):
        self.driver.find_element(*self.loc_ele_name).clear()
        self.driver.find_element(*self.loc_ele_name).send_keys(businessname)  # 商机名
    def ele_estimate_price(self,estimate_price):
        self.driver.find_element(*self.loc_ele_estimate_price).clear()
        self.driver.find_element(*self.loc_ele_estimate_price).send_keys(estimate_price)  # 预计成交价
    def ele_product(self):
        self.driver.find_element(*self.loc_ele_product_name).click()  # 添加产品
        time.sleep(2)
        self.driver.find_element(*self.loc_ele_product_content).click()
        self.driver.find_element(*self.loc_ele_product_OK).click()  # 点击OK
    def ele_business_submit(self):
        self.driver.find_element(*self.loc_ele_business_submit).click()  # 点击保存
    def ele_result(self):
        result = self.driver.find_element(*self.loc_ele_result).text #断言，提示添加商机成功
        return result
    '''修改商机'''
    def ele_business_update(self):
        self.driver.find_element(*self.loc_ele_business_update).click()
    def ele_business_update_submit(self):
        self.driver.find_element(*self.loc_ele_business_update_submit).click()

    '''推进'''
    def ele_business_push(self):
        self.driver.find_element(*self.loc_ele_business_push).click()#点击推进
    def ele_business_push_submit(self):
        self.driver.find_element(*self.loc_ele_business_push_submit).click()#提交推进
    '''删除'''
    def ele_business_delete(self):
        self.driver.find_element(*self.loc_ele_business_delete_click).click()
        self.driver.find_element(*self.loc_ele_business_delete).click()
        self.driver.switch_to.alert.accept()
    '''查看'''
    def ele_business_view(self):
        self.driver.find_element(*self.loc_ele_business_view).click()
        result_view = self.driver.find_element(*self.loc_ele_business_view_assert).text
        return result_view

    '''逻辑处理'''
    def business_add(self,businessname,estimate_price):
        '''新增商机业务处理'''
        self.ele_collapse()# 商机菜单
        self.ele_primary()# 添加商机按钮
        self.ele_owner_name()# 选择负责人
        self.ele_customer_name()# 选择客户
        self.ele_business_name(businessname)# 商机名称
        self.ele_estimate_price(estimate_price) # 预计成交价
        self.ele_product() #添加产品
        self.ele_business_submit()# 点击保存
        results = self.ele_result()#断言
        return results
    def business_view(self):
        '''查看商机业务处理'''
        self.ele_collapse()  # 商机菜单
        results = self.ele_business_view()#点击查看
        return results
    def business_update(self):
        '''修改商机业务处理'''
        self.ele_collapse()# 商机菜单
        self.ele_business_update()#点击编辑
        time.sleep(2)
        self.ele_owner_name()# 选择负责人
        self.ele_customer_name()# 选择客户
        self.ele_business_update_submit()# 点击保存
        results = self.ele_result()  # 断言
        return results

    def business_push(self):
        '''商机推进业务处理'''
        self.ele_collapse()# 商机菜单
        self.ele_business_push()
        self.ele_business_push_submit()
        results = self.ele_result()  # 断言
        return results

    def business_delete(self):
        '''商机删除业务处理'''
        self.ele_collapse()# 商机菜单
        self.ele_business_delete()
        results = self.ele_result()  # 断言
        return results

    def business_all(self,businessname,estimate_price):
        '''新增商机-查看商机-修改商机-查看商机-推进商机'''
        lst = []
        result_add = self.business_add(businessname,estimate_price)
        result_view_one = self.business_view()
        result_update = self.business_update()
        result_view_two = self.business_view()
        result_push = self.business_push()

        lst.append(result_add)
        lst.append(result_view_one)
        lst.append(result_update)
        lst.append(result_view_two)
        lst.append(result_push)
        return lst

