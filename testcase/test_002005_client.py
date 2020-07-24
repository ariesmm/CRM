import unittest
from testcase.base_testcase import BaseTestCase
from page.client_page import ClientPage

class ClientTestCase(BaseTestCase):
    def test_client(self):
        '''新增客户-查看客户--删除'''

        lp = ClientPage(self.driver)
        actual = lp.add("lisa8832188","621601","niannian")
        print(actual)
        self.assertIn("添加客户成功", actual)

        lp.check()
        lp.modification()
        actual_result_delete = lp.delete()
        print(actual_result_delete)
        self.assertIn("删除成功",actual_result_delete)


if __name__ == '__main__':
    unittest.main()
