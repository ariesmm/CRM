import unittest

from testcase.base_testcase import BaseTestCase
from page.clue_page import CluePage

class ClueUpdateTestCase(BaseTestCase):

    def test_clue_update(self):
        '''修改线索'''

        cp = CluePage(self.driver)
        cp.ele_clue_openclue()
        result4 = cp.clue_modify('百度公司','王先生')
        self.assertIn('修改成功', result4)

        #转换客户
        cp.ele_clue_openclue()
        cp.clue_transformation()


if __name__ == '__main__':
    unittest.main()
