import unittest


from testcase.base_testcase import BaseTestCase
from page.clue_page import CluePage

class ClueDeleteTestCase(BaseTestCase):

    def test_clue_delete(self):
        '''删除线索'''
        cp = CluePage(self.driver)
        cp.ele_clue_openclue()
        result3 = cp.clue_delete()
        self.assertIn('删除成功', result3)

if __name__ == '__main__':
    unittest.main()
