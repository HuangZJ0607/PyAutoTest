# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :run.py.py
# @Time     :2020/6/18 12:51
import pytest
from Common.Email import Email

# 使用pytest自带的测试报告生成方法
# pytest.main(['-s', './Testcases', '--html=./Report/pytest.html'])

# pytest+allure生成测试报告
pytest.main(['-s', './Testcases', '--alluredir', './Report/xml'])
'''
# 生成xml后在命令行使用以下语句，生成HTML文件
allure generate --clean ./Report/xml/ -o ./Report/results/html
'''
Email()
