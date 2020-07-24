import unittest

from data.read_data import read_excel
from testcase.base_testcase import BaseTestCase
from page.clue_page import CluePage
from page.login_page import LoginPage

class ClueDeleteTestCase(BaseTestCase):

    def test_clue_delete(self):
        '''删除线索'''
        #调用登录
        lp = LoginPage(self.driver )#实例化登录page的LoginPage类
        lst_user = read_excel(r"../data/user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        # self.assertIn(lst_user[0][0], result)

        #删除线索
        cp = CluePage(self.driver)
        cp.ele_clue_openclue()
        result3 = cp.clue_delete()
        self.assertIn('删除成功', result3)

if __name__ == '__main__':
    unittest.main()
