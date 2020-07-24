import unittest

from data.read_data import read_excel
from driver.browser import chrome_driver
from page.login_page import LoginPage


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()
        self.driver = driver

        lp = LoginPage(self.driver)  # 实例化登录page的LoginPage类
        lst_user = read_excel(r"../data/user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        self.assertIn(lst_user[0][0], result)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
