import unittest


from testcase.base_testcase import BaseTestCase
from page.clue_page import CluePage

class ClueLookTestCase(BaseTestCase):

    def test_clue_look(self):
        '''查看线索'''
        cp = CluePage(self.driver)
        cp.ele_clue_openclue()
        result2 = cp.clue_look()
        self.assertIn('线索详情', result2)


if __name__ == '__main__':
    unittest.main()
