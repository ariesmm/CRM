import unittest


from testcase.base_testcase import BaseTestCase
from page.business_page import BusinessPage

class BusinessAddTestCase(BaseTestCase):

    def test_business_add(self):
        '''新增商机'''
        bg = BusinessPage(self.driver)
        result = bg.business_add('美好的一天开始了','100000')
        self.assertIn('添加商机成功',result)
if __name__ == '__main__':
    unittest.main()
