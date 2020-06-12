# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :TestSuites.py
# @Time     :2020/5/28 13:56

import unittest
from Common.Report import Report
from Common.Email import Email
from Common import FilePath


class CreateSuite:
    def __init__(self):
        self.test_dir = FilePath.fatherpath() + '/Testcases/'
        self.t = Report()

    def testsuite_all(self):
        self.suite = unittest.defaultTestLoader.discover(self.test_dir, pattern='TestCase*.py')
        self.t.run(self.suite)


if __name__ == '__main__':
    CreateSuite().testsuite_all()
    Email()
