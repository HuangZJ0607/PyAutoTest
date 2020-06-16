# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :TestCase_API_demo.py
# @Time     :2020/6/11 14:50
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from Common.HTTPClient import Request
from Common.Log import Log
from ddt import ddt, data, file_data
from Common import FilePath


cases_info = [
    {
        "case_name": "例子1",
        "method": "get",
        "interface_name": "demo",
        "data": "",
        "headers": "",
        "assert": {
            'data': [{'from': 'cemaxueyuan', 'name': 'hello,yideng'}, {'from': 'cemaxueyuan', 'name': 'hello,xuzhu'},
                     {'from': 'cemaxueyuan', 'name': 'hello,susu'}], 'httpstatus': 200}
    },
    {
        "case_name": "例子2",
        "method": "get",
        "interface_name": "demo",
        "data": "",
        "headers": "",
        "assert": {'from1': 'cemaxueyuan'}
    },
    {
        "case_name": "例子3",
        "method": "get",
        "interface_name": "demo",
        "data": "",
        "headers": "",
        "assert": {"httpstatus": 100}
    }]


@ddt
class test_API(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.r = Request()

    def vaildate(self, expect, actual):
        '''
        校验测试结果的函数
        :param expect: 预期结果
        :param actual: 实际结果
        :return:
        '''
        for key, value in expect.items():
            if key in actual:  # 预期的key在实际结果返回值的key里面
                self.assertEqual(value, actual[key])
            else:  # 预期的key不在实际结果返回值的key里面
                for _key, _value in actual.items():
                    if isinstance(_value, dict) and (key in _value):
                        expect_new = {}
                        expect_new[key] = value
                        self.vaildate(expect_new, _value)

    # def test_demo(self):
    #     data = {
    #         "username": "admin",
    #         "password": "123456"
    #     }
    #     headers = {
    #         'Content-Type': 'application/json'
    #     }
    #     # data = json.dumps(data)  # 转换成json字符串
    #     res = self.r.send_request(method='get', name='demo', data=data, headers=headers)
    #     self.assertEqual(200, res['httpstatus'], msg='状态码不正确')
    @file_data(FilePath.fatherpath() + '/DataFile/API.yaml')
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
        '''方法一，使用for循环进行断言，但是一旦中间有一条用例不通过就会中断整个流程'''
        # for data in cases_info:
        #     res = self.r.send_request(method=data['method'], name=data['interface_name'], data=data['data'],
        #                               headers=data['headers'])
        #     self.vaildate(data['assert'], res)
        '''方法二，使用unittest里面的上下文管理器subTest'''
        # for data in cases_info:
        #     with self.subTest(data):
        #         res = self.r.send_request(method=data['method'], name=data['interface_name'], data=data['data'],
        #                                   headers=data['headers'])
        '''方法三，使用ddt数据驱动'''
        res = self.r.send_request(method=data['request']['method'], name=data['request']['interface_name'],
                                  data=data['request']['data'], headers=data['request']['headers'])
        self.vaildate(data['assert'], res)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_API))
    now = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    test_dir = 'report.html'
    with open(test_dir, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title='title', description='desc')
        runner.run(suite)
