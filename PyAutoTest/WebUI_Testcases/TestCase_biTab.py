# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :TestCase_biTab.py
# @Time     :2020/5/25 10:16
from Common.Driver import Driver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from ddt import ddt, file_data
import config


@ddt
class biTab(unittest.TestCase):
    def setUp(self) -> None:
        # 访问指定URL
        self.d = Driver(config.bili_url, 'chrome')

    def tearDown(self) -> None:
        self.d.quite_browser()

    @file_data(config.df_path + 'tab_content.yaml')
    def test_tab(self, **c):
        xpath = c.get('xpath')
        title = c.get('title')
        self.locator = (By.XPATH, xpath)
        self.d.click_element(self.locator)
        sleep(1)
        self.assertEqual(self.d.browser_title(), title, msg="内容不相同！！！")


if __name__ == '__main__':
    unittest.main()
