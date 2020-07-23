import unittest
from data.read_data import read_excel
from page.basetest_page import BaseTestCase
from page.contract_page import ContractPage
from page.login_page import LoginPage

'''
登录
合同操作
'''

class ContractTestCase(BaseTestCase):

    def test_contract(self):
        '''合同-新增-查看-编辑'''
        lp = LoginPage(self.driver)
        lst_user = read_excel(r"D:\workspace\webAutoCRM\data\user.xlsx", "user")  # 读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])  # 调用登录login方法
        self.assertIn(lst_user[0][0], result)

        cp = ContractPage(self.driver)
        date,result = cp.contract("2020-07-22","2020-08-23","100","2021-07-02")
        self.assertEqual(date, result)


if __name__ == '__main__':
    unittest.main()
