'''
    基于关键字驱动，excel文件的数据驱动demo
'''
from Common.Excel_Driver import ExcelDriver
from Common.Email import Email

class excel:
    def excel(self):
        ExcelDriver().excel_driver('../DataFile/WEBUI_demo.xlsx')


if __name__ == '__main__':
    excel().excel()
    Email().sendemail()
