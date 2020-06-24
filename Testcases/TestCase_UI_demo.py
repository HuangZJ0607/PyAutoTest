# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :TestCase_UI_demo.py
# @Time     :2020/5/25 10:16
import os, sys

sys.path.append(os.getcwd())
from Common.Driver import Driver
from ddt import ddt, file_data
from Config.config import Get_Config
import pytest, allure

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@ddt
class Test_biTab:
    def setup(self) -> None:
        self.driver = Driver('Chrome')
        self.driver.visit(Get_Config().get_config('url', 'bili_url'))

    def teardown(self) -> None:
        self.driver.quite()

    @allure.feature('B站导航栏的用例')
    @file_data(path + '/DataFile/tab_content.yaml')
    def test_tab(self, **c):
        title = c.get('title')
        name = c.get('name')
        value = c.get('value')
        self.driver.click(name, value)
        self.driver.sleep(2)
        assert self.driver.title() == title, '实际的标签页标题与预期不一致'


if __name__ == '__main__':
    pytest.main(['-s', 'TestCase_UI_demo.py', '--alluredir', '../Report/xml'])
