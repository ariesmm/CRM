import unittest
from data.read_data import read_excel
from testcase.base_testcase import BaseTestCase
from page.client_page import ClientPage

from page.login_page import LoginPage

class ClientDeleteTestCase(BaseTestCase):

    def test_client_delete(self):
        '''删除客户'''
        lp = LoginPage(self.driver )#实例化登录page的LoginPage类
        lst_user = read_excel(r"../data/user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        self.assertIn(lst_user[0][0], result)

        lp = ClientPage(self.driver)
        lp.client_server()
        actual_a = lp.delete()
        print(actual_a)
        self.assertIn("删除成功",actual_a)


if __name__ == '__main__':
    unittest.main()
