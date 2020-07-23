import unittest

from data.read_data import read_excel
from driver.browser import chrome_driver
from page.clew_page import ClewPage
from page.login_page import LoginPage

class ClewAddTestCase(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()
        self.driver = driver

    def test_clew_add(self):
        login = LoginPage(self.driver )
        lst_user = read_excel(r"D:\workspace\webAutoCRM\data\user.xlsx","user")
        login.login(lst_user[0][0], lst_user[0][1])
        cp = ClewPage(self.driver)
        cp.clew_add("zhoulisha",)



if __name__ == '__main__':
    unittest.main()
