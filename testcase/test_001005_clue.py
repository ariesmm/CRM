import unittest

from data.read_data import read_excel
from testcase.base_testcase import BaseTestCase
from page.clue_page import CluePage
from page.login_page import LoginPage

class ClueAddTestCase(BaseTestCase):

    def test_clue(self):
        '''线索增、查、更、删除'''

        #添加线索
        cp=CluePage(self.driver)
        result1=cp.clue_add('阿里公司','李女士')
        self.assertIn('添加成功',result1)

        #查看线索
        cp.ele_clue_openclue()
        result2 = cp.clue_look()
        self.assertIn('线索详情', result2)

        #修改线索
        cp.ele_clue_openclue()
        result4 = cp.clue_modify('百度公司','王先生')
        self.assertIn('修改成功', result4)

        #删除线索
        cp.ele_clue_openclue()
        result3 = cp.clue_delete()
        self.assertIn('删除成功', result3)

        #转换客户
        cp.ele_clue_openclue()
        cp.clue_transformation()


if __name__ == '__main__':
    unittest.main()
