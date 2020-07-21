# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :run.py.py
# @Time     :2020/6/18 12:51
import pytest, sys, os
from Common.Email import Email
'''
# 使用pytest自带的测试报告生成方法
# pytest.main(['-s', './TestCases', '--html=./Report/pytest.html'])

# pytest+allure生成测试报告
# pytest.main(['-s', './TestCases', '--alluredir', './Report/xml'])

# 生成xml后在命令行使用以下语句，生成HTML文件
allure generate --clean ./Report/xml/ -o ./Report/html
'''

if __name__ == '__main__':
    args = ['-s', '--alluredir', './Report/xml']
    pytest.main(args)
    Email().sendemail()
    os.system('allure generate --clean ./Report/xml/ -o ./Report/html')
    os.system('start chrome.exe H:/PyAutoTest/Report/html/index.html')
