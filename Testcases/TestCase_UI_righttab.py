# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :TestCase_UI_righttab.py
# @Time     :2020/6/9 0:19
from Common import FilePath
from Common.Driver import Driver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from ddt import ddt, file_data
from Common.config import Get_Config


@ddt
class righttab(unittest.TestCase):
    def setUp(self) -> None:
        self.d = Driver(Get_Config().get_Url('ui_url'), 'chrome')

    def tearDown(self) -> None:
        self.d.quite_browser()

    @file_data(FilePath.fatherpath() + '/DataFile/righttab_content.yaml')
    def test_01(self, **c):
        xpath1 = c.get('xpath1')
        xpath2 = c.get('xpath2')
        text = c.get('text')
        self.locator1 = (By.XPATH, xpath1)
        self.d.click_element(self.locator1)
        sleep(2)
        self.locator2 = (By.XPATH, xpath2)
        self.assertEqual(self.d.get_text(self.locator2), text, msg='内容不相同')

    def test_02(self):
        self.d.log.log_info('123123')


if __name__ == '__main__':
    unittest.main()
