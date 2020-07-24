import unittest

from testcase.base_testcase import BaseTestCase
from page.client_page import ClientPage


class ClientDeleteTestCase(BaseTestCase):

    def test_client_delete(self):
        '''删除客户'''

        lp = ClientPage(self.driver)
        lp.client_server()
        actual_a = lp.delete()
        print(actual_a)
        self.assertIn("删除成功",actual_a)


if __name__ == '__main__':
    unittest.main()
