import unittest

from data.read_data import read_excel
from page.basetest_page import BaseTestCase
from page.login_page import LoginPage
from page.business_page import BusinessPage

class BusinessAddTestCase(BaseTestCase):
    '''
    新增商机
    '''
    def test_business_add(self):
        lp = LoginPage(self.driver)  # 实例化登录page的LoginPage类
        lst_user = read_excel(r"D:\workspace\webAutoCRM\data\user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        self.assertIn(lst_user[0][0], result)

        bg = BusinessPage(self.driver)
        result = bg.business_delete()
        self.assertIn('删除成功',result)
if __name__ == '__main__':
    unittest.main()