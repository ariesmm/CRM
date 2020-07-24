import unittest


from testcase.base_testcase import BaseTestCase
from page.business_page import BusinessPage

class BusinessAddTestCase(BaseTestCase):

    def test_business_view(self):
        '''查看商机'''
        bg = BusinessPage(self.driver)
        result = bg.business_view()
        self.assertIn('商机详情',result)
if __name__ == '__main__':
    unittest.main()
