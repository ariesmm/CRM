import unittest

from driver.browser import chrome_driver

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        driver = chrome_driver()
        self.driver = driver
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
