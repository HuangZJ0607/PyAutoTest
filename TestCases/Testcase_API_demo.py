# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Testcase_API_demo.py
# @Time     :2020/6/11 14:50
import os, sys

sys.path.append(os.getcwd())
from Common.HTTPClient import HTTPClient
from ddt import ddt, data, file_data
from Common.Yaml_Operation import write_yaml
import pytest

path = os.path.dirname(__file__)
fpath = os.path.dirname(path)


@ddt
class Test_API:
    def setup(self):
        self.r = HTTPClient()

    @file_data(fpath + './DataFile/API.yaml')
    def test_interface(self, **data):
        # 发送请求
        res = self.r.send_request(method=data['request']['method'], name=data['request']['interface_name'],
                                  data=data['request']['parmars'], headers=data['request']['headers'])
        # 提取变量
        if 'extract' in data and data['extract']:
            for key, value in data['extract'].items():
                extract = {}
                extract[key] = res[value]
                write_yaml(extract)
        self.r.vaildate(data['validate'], res)


if __name__ == '__main__':
    pytest.main(['-s', 'Testcase_API_demo.py', '--html=../Report/pytest.html'])
