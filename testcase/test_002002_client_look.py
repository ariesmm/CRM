import unittest
from testcase.base_testcase import BaseTestCase
from page.client_page import ClientPage

class ClientLookTestCase(BaseTestCase):
    def test_client_look(self):
        '''查看客户'''
        lp = ClientPage(self.driver)
        lp.client_server()
        lp.check()



if __name__ == '__main__':
    unittest.main()
