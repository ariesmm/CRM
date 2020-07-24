import unittest

from data.read_data import read_excel
from driver.browser import chrome_driver
from page.basetest_page import BaseTestCase
from page.clue_page import CluePage
from page.login_page import LoginPage

class ClueLookTestCase(BaseTestCase):

    def test_clue_look(self):
        #调用登录
        lp = LoginPage(self.driver )#实例化登录page的LoginPage类
        lst_user = read_excel(r"../data/user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        # self.assertIn(lst_user[0][0], result)

        #查看线索
        cp = CluePage(self.driver)
        cp.ele_clue_openclue()
        result2 = cp.clue_look()
        self.assertIn('线索详情', result2)


if __name__ == '__main__':
    unittest.main()
