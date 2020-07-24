import unittest
from testcase.base_testcase import BaseTestCase
from page.client_page import ClientPage

class ClientTestCase(BaseTestCase):
    def test_clew_add(self):
        #添加客户
        lp = ClientPage(self.driver)
        actual = lp.add("alitax22x","621601","niannian")
        print(actual)
        self.assertIn("添加客户成功", actual)


if __name__ == '__main__':
    unittest.main()
