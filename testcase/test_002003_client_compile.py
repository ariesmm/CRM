import unittest
from data.read_data import read_excel
from driver.browser import chrome_driver
from page.basetest_page import BaseTestCase
from page.client_page import ClientPage

from page.login_page import LoginPage

class ClientTestCase(BaseTestCase):
    def test_clew_add(self):
        '''修改客户'''
        lp = LoginPage(self.driver )#实例化登录page的LoginPage类
        lst_user = read_excel(r"D:\workspace\webAutoCRM\data\user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        self.assertIn(lst_user[0][0], result)

        lp = ClientPage(self.driver)
        lp.client_server()
        lp.modification()


if __name__ == '__main__':
    unittest.main()
