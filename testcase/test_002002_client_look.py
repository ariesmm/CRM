import unittest
from data.read_data import read_excel
from testcase.base_testcase import BaseTestCase
from page.client_page import ClientPage

from page.login_page import LoginPage

class ClientLookTestCase(BaseTestCase):
    def test_client_look(self):
        '''查看客户'''
        lp = LoginPage(self.driver )#实例化登录page的LoginPage类
        lst_user = read_excel(r"../data/user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        self.assertIn(lst_user[0][0], result)


        lp = ClientPage(self.driver)
        lp.client_server()
        lp.check()



if __name__ == '__main__':
    unittest.main()
