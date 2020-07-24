import unittest

from data.read_data import read_excel
from testcase.base_testcase import BaseTestCase
from page.login_page import LoginPage
from page.business_page import BusinessPage

class BusinessDeleteTestCase(BaseTestCase):

    def test_business_delete(self):
        '''删除商机'''
        bg = BusinessPage(self.driver)
        result = bg.business_delete()
        self.assertIn('删除成功',result)
if __name__ == '__main__':
    unittest.main()
