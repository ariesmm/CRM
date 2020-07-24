import unittest

from data.read_data import read_excel
from testcase.base_testcase import BaseTestCase
from page.client_page import ClientPage
from page.clue_page import CluePage
from page.contract_page import ContractPage
from page.login_page import LoginPage
from page.business_page import BusinessPage

class BusinessALLTestCase(BaseTestCase):

    def test_business_all(self):
        '''新增线索-添加客户-查看客户-新增商机-修改商机-合同'''
        lp = LoginPage(self.driver)  # 实例化登录page的LoginPage类
        lst_user = read_excel(r"../data/user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        self.assertIn(lst_user[0][0], result)

        cp=CluePage(self.driver)
        result1=cp.clue_add('阿里公司','李女士')
        self.assertIn('添加成功',result1)
        #添加客户
        lp = ClientPage(self.driver)
        result2 = lp.add("张三999","621601","niannian")
        self.assertIn("添加客户成功", result2)
        #查看客户
        lp.client_server()
        lp.check()
        #新增商机
        bg = BusinessPage(self.driver)
        result3 = bg.business_add('好商机A','100000')
        self.assertIn('添加商机成功',result3)
        #修改商机
        bp = BusinessPage(self.driver)
        result4 = bp.business_update()
        self.assertIn("修改商机信息成功",result4)
        #合同
        cp = ContractPage(self.driver)
        date,result5 = cp.contract("2020-07-22","2020-08-23","100","2021-07-02")
        self.assertEqual(date, result5)

if __name__ == '__main__':
    unittest.main()
