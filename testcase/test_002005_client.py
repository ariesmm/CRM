import unittest
from data.read_data import read_excel
from driver.browser import chrome_driver
from page.basetest_page import BaseTestCase
from page.client_page import ClientPage

from page.login_page import LoginPage

class ClientTestCase(BaseTestCase):
    def test_clew_add(self):
        '''新增客户-查看客户--删除'''
        lp = LoginPage(self.driver )#实例化登录page的LoginPage类
        lst_user = read_excel(r"../data/user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        self.assertIn(lst_user[0][0], result)

        lp = ClientPage(self.driver)
        actual = lp.add("lisa0010","621601","niannian")
        print(actual)
        self.assertIn("添加客户成功", actual)

        lp.check()
        lp.modification()
        actual_a = lp.delete()
        print(actual_a)
        self.assertIn("删除成功",actual_a)


if __name__ == '__main__':
    unittest.main()
