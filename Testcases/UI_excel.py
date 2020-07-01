# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :UI_excel.py
# @Time     :2020/6/24 1:27
from Common.Excel_Driver import ExcelDriver


class excel:
    def excel(self):
        ExcelDriver().excel_driver('../DataFile/WEBUI_demo.xlsx')


if __name__ == '__main__':
    excel().excel()
