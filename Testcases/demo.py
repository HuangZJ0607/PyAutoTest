# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :demo.py
# @Time     :2020/6/24 1:27
from Common.Excel_Driver import ExcelDriver
import pytest


class Test_excel:
    def test_excel(self):
        ExcelDriver('../DataFile/WEBUI_demo.xlsx')


if __name__ == '__main__':
    pytest.main(['-s', 'TestCase_shop.py', '--alluredir', '../Report/xml'])
