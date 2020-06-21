# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :TestCase_API_demo.py
# @Time     :2020/6/11 14:50
import os, sys

sys.path.append(os.getcwd())
from Common.HTTPClient import HTTPClient
from ddt import ddt, data, file_data
from Common.extract_yaml import write_yaml
import pytest

path = os.path.dirname(__file__)
fpath = os.path.dirname(path)


@ddt
class Test_API:
    def setup(self):
        self.r = HTTPClient()

    @file_data(fpath + './DataFile/API.yaml')
    def test_interface(self, **data):
        '''
        所有的接口用例 ，100多组数据， 只用写一个函数的情况下，依次运行所有100接口，
        而且生成相应的100测试报告
        httprunner,用例的数据结构，yaml,json
        list of dict:字典列表
          {
            "casename":"登录",
            "method":"post",
            "int_name":"login",
            "data":{"username": "admin", "password": "123456"},
            "headers":"",
        }
        '''
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
    pytest.main(['-s', 'TestCase_API_demo.py', '--html=../Report/pytest.html'])
