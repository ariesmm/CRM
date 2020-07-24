import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from driver.browser import chrome_driver
from page.base_page import BasePage
from page.login_page import LoginPage


class CluePage(BasePage):
    def __init__(self, driver):
        #初始化
        super().__init__(driver)
        self.driver = driver#调用的是testcase实例化的浏览器驱动
        self.url = 'http://192.168.1.36/index.php?m=user&a=login'

        #菜单栏线索按钮
        self.loc_openclue=(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a')
        #新增线索按钮
        self.loc_newclue=(By.XPATH, '/html/body/div[5]/div[2]/div[1]/div/a')
        #负责人按钮
        self.loc_personincharge=(By.ID, 'owner_name')
        #选择部门下拉框
        self.loc_personincharge_locator=(By.ID, 'd_department')
        #选择员工按钮
        self.loc_personincharge_locator_fuzeren=(By.NAME, 'owner')
        #提交新增按钮
        self.loc_personincharge_ok=(By.XPATH, '/html/body/div[7]/div[3]/div/button[1]')
        #公司名输入框
        self.loc_companyname=(By.ID, 'name')
        #联系人输入框
        self.loc_contacts=(By.ID, 'contacts_name')
        #提交按钮
        self.loc_submit=(By.NAME, 'submit')

        #转换按钮
        self.loc_transformation=(By.XPATH,'//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[2]')

        #登录结果定位
        self.loc_clue_addclue_result=(By.XPATH,'/html/body/div[5]/div[2]')

        #查看线索按钮
        self.loc_clue_look=(By.XPATH,'//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[1]')

        #选择线索按钮
        self.loc_clue_select=(By.XPATH,'//form[@id="form1"]/table/tbody/tr[1]/td[1]/input')

        #批量操作按钮
        self.loc_clue_batch=(By.CSS_SELECTOR,'.btn.dropdown-toggle')
        #删除线索按钮
        self.loc_clue_delete=(By.ID,'delete')
        #回收站按钮
        self.loc_clue_recycle=(By.XPATH,'/html/body/div[5]/p/a[14]')
        #回收站选择按钮
        self.loc_clue_recycle_select=(By.XPATH,'//form[@id="form1"]/table/tbody/tr[1]/td[1]/input')
        #回收站批量操作按钮
        self.loc_clue_recycle_batch=(By.XPATH,'/html/body/div[5]/div[2]/div[1]/ul/li[1]/div/a')
        #回收站批量删除按钮
        self.loc_clue_recycle_delete=(By.ID,'delete')
        #修改线索按钮
        self.loc_clue_modify=(By.XPATH,'//form[@id="form1"]/table/tbody/tr[1]/td[12]/a[3]')
        #修改公司名按钮
        self.loc_clue_modify_newcompanyname=(By.ID,'name')
        #修改联系人按钮
        self.loc_clue_modify_newperson=(By.ID,'contacts_name')
        #保存修改按钮
        self.loc_clue_modify_submit=(By.NAME,'submit')


    def ele_clue_openclue(self): #打开线索页面
        self.driver.find_element(*self.loc_openclue).click()

    def ele_clue_newclue(self): #打开新增线索页面
        time.sleep(2)
        self.driver.find_element(*self.loc_newclue).click()

    def ele_clue_personincharge(self):#选择负责人
        time.sleep(2)
        self.driver.find_element(*self.loc_personincharge).click()  # 单击负责人输入框
        time.sleep(2)
        # 弹出选择页面
        locator = self.driver.find_element(*self.loc_personincharge_locator)  # 选择部门
        select = Select(locator)
        select.select_by_value('1')  # 选择办公室
        self.driver.find_elements(*self.loc_personincharge_locator_fuzeren)[8].click()  # 选择负责人
        self.driver.find_element(*self.loc_personincharge_ok).click()  # 单击OK

    def ele_clue_companyname(self,companyname):
        # 公司名
        self.driver.find_element(*self.loc_companyname).send_keys(companyname)

    def ele_clue_contacts(self,contacts):
        # 联系人姓名
        self.driver.find_element(*self.loc_contacts).send_keys(contacts)

    def ele_clue_submit(self):
        # 提交
        self.driver.find_element(*self.loc_submit).click()
        time.sleep(2)

    def ele_clue_addclue_result(self):
        #添加线索结果验证
        result1=self.driver.find_element(*self.loc_clue_addclue_result).text
        print(result1)
        return result1

    def ele_clue_transformation(self):
        # 转换
        self.driver.find_element(*self.loc_transformation).click()
        time.sleep(2)

    def ele_clue_look(self):
        # 查看线索
        self.driver.find_element(*self.loc_clue_look).click()

    def ele_clue_lookclue_result(self):
        #查看线索结果验证
        time.sleep(2)
        result2=self.driver.find_element(By.XPATH,'//div[@id="tab1"]/div[1]/a').text
        print(result2)
        return result2

    def ele_clue_select(self):
        # 选择线索
        self.driver.find_element(*self.loc_clue_select).click()

    def ele_clue_batch(self):
        # 批量操作
        self.driver.find_element(*self.loc_clue_batch).click()

    def ele_clue_delete(self):
        # 删除线索
        self.driver.find_element(*self.loc_clue_delete).click()

    def ele_clue_deleteok(self):
        # 确定删除线索
        self.driver.switch_to.alert.accept()

    def ele_clue_recycle(self):
        # 回收站
        self.driver.find_element(*self.loc_clue_recycle).click()

    def ele_clue_recycle_select(self):
        # 回收站选择线索
        self.driver.find_element(*self.loc_clue_recycle_select).click()

    def ele_clue_recycle_batch(self):
        # 回收站批量操作
        self.driver.find_element(*self.loc_clue_recycle_batch).click()

    def ele_clue_recycle_delete(self):
        # 回收站批量删除线索
        self.driver.find_element(*self.loc_clue_recycle_delete).click()

    def ele_clue_recycle_deleteok(self):
        # 回收站确定删除线索
        self.driver.switch_to.alert.accept()

    def ele_clue_deleteclue_result(self):
        #删除线索结果验证
        result3=self.driver.find_element(By.XPATH,'/html/body/div[5]/div[2]').text
        print(result3)
        return result3

    def ele_clue_modify(self):
        # 修改线索
        self.driver.find_element(*self.loc_clue_modify).click()
        self.driver.find_element(*self.loc_clue_modify_newcompanyname).clear()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.find_element(*self.loc_clue_modify_newperson).clear()

    def ele_clue_modify_newcompanyname(self,newcompanyname):
        # 修改公司名
        self.driver.find_element(*self.loc_clue_modify_newcompanyname).send_keys(newcompanyname)

    def ele_clue_modify_newperson(self,newperson):
        #修改联系人
        self.driver.find_element(*self.loc_clue_modify_newperson).send_keys(newperson)

    def ele_clue_modify_submit(self):
        #保存修改
        self.driver.find_element(*self.loc_clue_modify_submit).click()

    def ele_clue_modifyclue_result(self):
        #修改线索结果验证
        result4=self.driver.find_element(By.XPATH,'/html/body/div[5]/div[2]').text
        print(result4)
        return result4


    def clue_add(self,companyname,contacts): #添加线索
        self.ele_clue_openclue()
        self.ele_clue_newclue()
        self.ele_clue_personincharge()
        self.ele_clue_companyname(companyname)
        self.ele_clue_contacts(contacts)
        self.ele_clue_submit()
        time.sleep(2)
        result1=self.ele_clue_addclue_result()
        return result1

    def clue_look(self): #查看线索
        self.ele_clue_look()
        time.sleep(2)
        result2 = self.ele_clue_lookclue_result()
        return result2

    def clue_transformation(self): #转换为客户
        self.ele_clue_transformation()
        time.sleep(2)

    def clue_delete(self):#删除线索
        self.ele_clue_select()
        self.ele_clue_batch()
        self.ele_clue_delete()
        self.ele_clue_deleteok()
        time.sleep(2)
        self.ele_clue_recycle()
        self.ele_clue_recycle_select()
        self.ele_clue_recycle_batch()
        self.ele_clue_recycle_delete()
        self.ele_clue_recycle_deleteok()
        time.sleep(2)
        result3 = self.ele_clue_deleteclue_result()
        return result3

    def clue_modify(self,newcompanyname,newperson):#修改线索
        self.ele_clue_modify()
        self.ele_clue_modify_newcompanyname(newcompanyname)
        self.ele_clue_modify_newperson(newperson)
        self.ele_clue_modify_submit()
        time.sleep(3)
        result4 = self.ele_clue_modifyclue_result()
        return result4





