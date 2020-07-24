import unittest

from testcase.base_testcase import BaseTestCase
from page.business_page import BusinessPage

class BusinessALLTestCase(BaseTestCase):

    def test_business_all(self):
        '''新增商机-查看商机-修改商机-查看商机-推进商机-删除商机'''

        bg = BusinessPage(self.driver)
        results = bg.business_all('lisa7780','10000')#有四个返回值，返回的是一个列表

        self.assertIn('添加商机成功',results[0])
        self.assertIn('商机详情', results[1])
        self.assertIn('修改商机信息成功', results[2])
        self.assertIn('商机详情', results[3])
        self.assertIn('推进成功', results[4])


if __name__ == '__main__':
    unittest.main()
