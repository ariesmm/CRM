import unittest

from testcase.base_testcase import BaseTestCase


class LoginTestCase(BaseTestCase):
    '''登录'''
    def test_logs(self):
        print("登录验证")
if __name__ == '__main__':
    unittest.main()
