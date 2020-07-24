import unittest
from testcase.base_testcase import BaseTestCase
from page.client_page import ClientPage

class ClientCompileTestCase(BaseTestCase):
    def test_client_compile(self):
        '''修改客户'''

        lp = ClientPage(self.driver)
        lp.client_server()
        lp.modification()


if __name__ == '__main__':
    unittest.main()
