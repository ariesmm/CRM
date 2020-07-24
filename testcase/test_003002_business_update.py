import unittest

from data.read_data import read_excel
from testcase.base_testcase import BaseTestCase
from page.login_page import LoginPage
from page.business_page import BusinessPage


class BusinessUpdateTestCase(BaseTestCase):

    def test_business_update(self):
        '''修改商机'''

        bp = BusinessPage(self.driver)
        result = bp.business_update()
        self.assertIn("修改商机信息成功",result)

if __name__ == '__main__':
    unittest.main()
