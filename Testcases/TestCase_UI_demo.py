# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :TestCase_UI_demo.py
# @Time     :2020/5/25 10:16
import os, sys
sys.path.append(os.getcwd())
from Common.Driver import Driver
from selenium.webdriver.common.by import By
from time import sleep
from ddt import ddt, file_data
from Config.config import Get_Config
import pytest
from os.path import *

path = dirname(dirname(abspath(__file__)))


@ddt
class Test_biTab:
    def setup(self) -> None:
        # 访问指定URL
        self.driver = Driver(Get_Config().get_config('url', 'bili_url'), 'chrome')

    def teardown(self) -> None:
        self.driver.quite_browser()

    @file_data(path + '/DataFile/tab_content.yaml')
    def test_tab(self, **c):
        xpath = c.get('xpath')
        title = c.get('title')
        locator = (By.XPATH, xpath)
        self.driver.click_element(locator)
        sleep(1)
        assert self.driver.browser_title() == title


if __name__ == '__main__':
    pytest.main(['-s', 'TestCase_UI_demo.py', '--html=../Report/pytest.html'])
