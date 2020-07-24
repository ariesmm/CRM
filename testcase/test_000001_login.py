import unittest

from data.read_data import read_excel
from testcase.base_testcase import BaseTestCase
from page.login_page import LoginPage

class LoginTestCase(BaseTestCase):
    '''登录'''
    def test_logs(self):
        print("登录验证")
if __name__ == '__main__':
    unittest.main()
