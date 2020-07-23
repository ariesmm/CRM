import unittest
from data.read_data import read_excel
from driver.browser import chrome_driver
from page.client_page import ClientPage

from page.login_page import LoginPage

class ClientTestCase(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()#初始化浏览器驱动
        self.driver = driver#保证以下方法都可以使用同一个driver
    def test_clew_add(self):
        lp = LoginPage(self.driver )#实例化登录page的LoginPage类
        lst_user = read_excel(r"E:\pycharm\CRM\data\user.xlsx","user")#读取数据
        result = lp.login(lst_user[0][0], lst_user[0][1])#调用登录login方法
        self.assertIn(lst_user[0][0], result)

        lp = ClientPage(self.driver)
        actual = lp.add("alitaxx","621601","niannian")
        print(actual)
        self.assertIn("添加客户成功", actual)


if __name__ == '__main__':
    unittest.main()
