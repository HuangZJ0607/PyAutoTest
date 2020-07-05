# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Testcase_UI_demo.py
# @Time     :2020/5/25 10:16
import os, sys

sys.path.append(os.getcwd())
from Common.Driver import Driver
from ddt import ddt, file_data
from Config.config import Get_Config
import unittest, time
# import HTMLTestRunner

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@ddt
class Test_biTab(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Driver('Chrome')
        self.driver.visit('http://www.bilibili.com')

    def tearDown(self) -> None:
        self.driver.quite()

    @file_data(path + '/DataFile/tab_content.yaml')
    def test_tab(self, **c):
        title = c.get('title')
        name = c.get('name')
        value = c.get('value')
        self.driver.click(name, value)
        self.driver.sleep(2)
        self.assertEqual(self.driver.title(), title, msg='实际的标签页标题与预期不一致')


# if __name__ == '__main__':
#     # unittest.main()
#     s = unittest.TestSuite()
#     s.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_biTab))
#     now = time.strftime('%Y_%m_%d_%H_%M_%S')
#     report_path = '../Report/'
#     filename = report_path + now + '.html'
#     with open(filename, 'wb') as report:
#         runner = HTMLTestRunner.HTMLTestRunner(stream=report, title='标题', description='内容')
#         runner.run(s)
