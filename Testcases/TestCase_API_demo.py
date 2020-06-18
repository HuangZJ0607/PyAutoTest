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

    @file_data(fpath + '/DataFile/API.yaml')
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
        print(data['request']['method'])
        res = self.r.send_request(method=data['request']['method'], name=data['request']['interface_name'],
                                  data=data['request']['parmars'], headers=data['request']['headers'])
        # 提取变量
        if 'extract' in data and data['extract']:
            for key, value in data['extract'].items():
                extract = {}
                extract[key] = res[value]
                write_yaml(extract)
        self.vaildate(data['assert'], res)

    def vaildate(self, expect, actual):
        '''
        校验测试结果的函数
        :param expect: 预期结果
        :param actual: 实际结果
        :return:
        '''
        for key, value in expect.items():
            # 预期的key在实际结果返回值的key里面
            if key in actual:
                # 将select * from token where id = 1 这个格式判断为一个数据库语句 select, update....
                if value.startswith('select') and 'from' in value or (value.startswith('update') and 'set' in value):
                    value_after = self.r.get_mysql_data(value)
                    assert value_after == actual[key]
                else:
                    assert value == actual[key]
            else:  # 预期的key不在实际结果返回值的key里面
                for _key, _value in actual.items():
                    if isinstance(_value, dict) and (key in _value):
                        expect_new = {}
                        expect_new[key] = value
                        self.vaildate(expect_new, _value)


if __name__ == '__main__':
    pytest.main(['-s', 'TestCase_API_demo.py', '--html=../Report/pytest.html'])
