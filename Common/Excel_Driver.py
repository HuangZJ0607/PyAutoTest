# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Excel_Driver.py
# @Time     :2020/6/29 15:56
'''
    封装excel文件驱动UI自动化测试的类
'''
import openpyxl
from Common.Driver import Driver
from openpyxl.styles import PatternFill, Font
from Common.Log import Log

log = Log().logger


def getexcel(filename):
    # 读取excel文件
    excel = openpyxl.load_workbook(filename)
    log.info('读取{}文件'.format(filename))
    return excel


class ExcelDriver:
    index = 0

    # 初始化函数
    def __init__(self, filename):
        self.excel = getexcel(filename)
        self.excel_driver(filename)

    def excel_driver(self, filename):
        # 获取所有的sheet页
        sheetnames = self.excel.sheetnames

        for sheetname in sheetnames:
            sheet = self.excel[sheetname]
            ExcelDriver.index += 1
            log.info('执行第{0}个用例：{1}'.format(ExcelDriver.index, sheetname))

            for value in sheet.values:
                if type(value[0]) is int:  # 第一列的内容是int类型，即编号
                    if value[1] == 'open_browser':
                        # 实例化driver
                        driver = Driver(value[4])
                    elif 'assert' in value[1]:  # 第二列存在assert这个字符串时，进行判断传参
                        if value[2] != None:
                            status = getattr(driver, value[1])(value[2], value[3], value[6])
                        else:
                            status = getattr(driver, value[1])(value[6])
                        # 获取断言结果，对结果进行判断
                        if status is True:
                            # 结果为True时写入pass
                            # 获取当前行数
                            row = value[0] + 1
                            sheet.cell(row=row, column=8).value = 'Pass'
                            # 填充颜色
                            sheet.cell(row=row, column=8).fill = PatternFill('solid', fgColor='00FF00')
                            # 字体加粗
                            sheet.cell(row=row, column=8).font = Font(bold=True)
                        else:
                            # 结果为False时写入false
                            row = value[0] + 1
                            sheet.cell(row=row, column=8).value = 'False'
                            sheet.cell(row=row, column=8).fill = PatternFill('solid', fgColor='FF0000')
                            sheet.cell(row=row, column=8).font = Font(bold=True)
                        # excel文件保存机制
                        self.excel.save(filename)
                    else:  # 除open_browser和断言外的其他流程，根据每列是否存在内容进行传参
                        if value[4] == None and value[2] == None:
                            getattr(driver, value[1])()
                        elif value[4] == None and value[2] != None:
                            getattr(driver, value[1])(value[2], value[3])
                        elif value[4] != None and value[2] == None:
                            getattr(driver, value[1])(value[4])
                        elif value[4] != None and value[2] != None:
                            getattr(driver, value[1])(value[2], value[3], value[4])
                        else:
                            pass
                else:
                    pass


if __name__ == '__main__':
    ExcelDriver('../DataFile/WEBUI_demo.xlsx')
