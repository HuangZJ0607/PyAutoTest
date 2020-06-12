# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :TestCase_UI_biTab.py
# @Time     :2020/5/25 10:16
from Common.Driver import Driver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from ddt import ddt, file_data
from Common.config import Get_Config
from Common import FilePath

@ddt
class biTab(unittest.TestCase):
    def setUp(self) -> None:
        # 访问指定URL
        self.d = Driver(Get_Config().get_Url('ui_url'), 'chrome')

    def tearDown(self) -> None:
        self.d.quite_browser()

    @file_data(FilePath.fatherpath() + '/DataFile/tab_content.yaml')
    def test_tab(self, **c):
        xpath = c.get('xpath')
        title = c.get('title')
        self.locator = (By.XPATH, xpath)
        self.d.click_element(self.locator)
        sleep(1)
        self.assertEqual(self.d.browser_title(), title, msg="内容不相同！！！")


if __name__ == '__main__':
    unittest.main()
