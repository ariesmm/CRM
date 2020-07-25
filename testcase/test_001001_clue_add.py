import unittest


from testcase.base_testcase import BaseTestCase
from page.clue_page import CluePage


class ClueAddTestCase(BaseTestCase):

    def test_clue_add(self):
        '''#添加线索'''
        cp=CluePage(self.driver)
        result1=cp.clue_add('阿里公司','李女士')
        self.assertIn('添加成功',result1)

if __name__ == '__main__':
    unittest.main()
