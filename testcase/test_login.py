import unittest

from data.read_data import read_excel
from driver.browser import chrome_driver
from page.login_page import LoginPage

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()#初始化浏览器驱动
        self.driver = driver#保证以下方法都可以使用同一个driver

    def test_login(self):
        lp = LoginPage(self.driver )#实例化登录page的LoginPage类
        lst_user = read_excel(r"D:\workspace\webAutoCRM\data\user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        self.assertIn(lst_user[0][0], result)

if __name__ == '__main__':
    unittest.main()
