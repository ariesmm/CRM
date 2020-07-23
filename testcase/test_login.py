import unittest

from data.read_data import read_excel
from driver.browser import chrome_driver
from page.login_page import LoginPage

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()
        self.driver = driver

    def test_login(self):
        lp = LoginPage(self.driver)
        lst_user = read_excel(r"D:\workspace\webAutoCRM\data\user.xlsx","user")
        result = lp.login(lst_user[0][0],lst_user[0][1])
        self.assertIn(lst_user[0][0],result)
if __name__ == '__main__':
    unittest.main()
