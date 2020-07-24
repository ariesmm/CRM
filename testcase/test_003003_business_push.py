import unittest


from testcase.base_testcase import BaseTestCase
from page.business_page import BusinessPage

class BusinessPushTestCase(BaseTestCase):

    def test_business_push(self):
        '''推进商机'''
        bg = BusinessPage(self.driver)
        result = bg.business_push()
        self.assertIn('推进成功',result)
if __name__ == '__main__':
    unittest.main()
