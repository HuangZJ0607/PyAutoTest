# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :tt.py
# @Time     :2020/6/12 14:16
from Common.Driver import Driver
from selenium.webdriver.common.by import By
import unittest
from Common.config import Get_Config


class b(unittest.TestCase):
    def setUp(self) -> None:
        # 访问指定URL
        self.d = Driver(Get_Config().get_Url('ui_url'), 'chrome')

    def tearDown(self) -> None:
        self.d.quite_browser()

    def test_01(self):
        locator = (By.XPATH, '//*[id="kw"]')
        print('111')
        self.d.click_element(locator)
        print('222')


if __name__ == '__main__':
    unittest.main()

    # def test_02(self):
    #     print('333')
    #     locator = (By.XPATH, '//*[id="kw"]')
    #     self.d.input_text(locator, 'heihei')
    #     print('444')
