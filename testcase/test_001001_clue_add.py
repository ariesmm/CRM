import unittest

from data.read_data import read_excel
from driver.browser import chrome_driver
from page.basetest_page import BaseTestCase
from page.clue_page import CluePage
from page.login_page import LoginPage

class ClueAddTestCase(BaseTestCase):

    def test_clue(self):
        #调用登录
        lp = LoginPage(self.driver )#实例化登录page的LoginPage类
        lst_user = read_excel(r"../data/user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        # self.assertIn(lst_user[0][0], result)

        #添加线索
        cp=CluePage(self.driver)
        result1=cp.clue_add('阿里公司','李女士')
        self.assertIn('添加成功',result1)

if __name__ == '__main__':
    unittest.main()
