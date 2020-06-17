# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Report.py
# @Time     :2020/5/28 14:10

from HTMLTestRunner import HTMLTestRunner
import time
from Common import FilePath


class Report:
    '''
        HTMLTestRunner测试报告二次封装
    '''

    def __init__(self):
        now = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
        self.re_path = FilePath.fatherpath() + '/Output/report_' + now + '.html'

    def run(self, suite):
        with open(self.re_path, 'wb') as fp:
            runner = HTMLTestRunner(stream=fp, title='title', description='desc')
            runner.run(suite)
