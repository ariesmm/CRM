import unittest
from driver.browser import chrome_driver
from data.read_data import read_excel
from page.contract_page import ContractPage
from page.login_page import LoginPage

'''
登录
合同操作
'''

class ContractTestCase(unittest.TestCase):
    # def setUp(self):
    #     driver = chrome_driver()
    #     self.driver = driver
    # # def test_login(self):


    def test_contract(self):
        driver = chrome_driver()
        self.driver = driver

        lp = LoginPage(self.driver)
        lst_user = read_excel(r"E:\海德41\python\CRM\data\user.xlsx", "user")  # 读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])  # 调用登录login方法
        self.assertIn(lst_user[0][0], result)

        cp = ContractPage(self.driver)
        actual = cp.contract("2020-07-22","2020-08-23","100","2021-07-02")
        self.assertEqual(True, actual)


if __name__ == '__main__':
    unittest.main()
