import unittest

from data.read_data import read_excel
from page.basetest_page import BaseTestCase
from page.login_page import LoginPage
from page.business_page import BusinessPage

class BusinessALLTestCase(BaseTestCase):

    def test_business_all(self):
        '''新增商机-修改商机-推进商机-删除商机'''
        lp = LoginPage(self.driver)  # 实例化登录page的LoginPage类
        lst_user = read_excel(r"../data/user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        self.assertIn(lst_user[0][0], result)

        bg = BusinessPage(self.driver)
        results = bg.business_all('lisa020','10000')#有四个返回值，返回的是一个列表

        self.assertIn('添加商机成功',results[0])
        self.assertIn('修改商机信息成功', results[1])
        self.assertIn('推进成功', results[2])
        self.assertIn('删除成功', results[3])


if __name__ == '__main__':
    unittest.main()
