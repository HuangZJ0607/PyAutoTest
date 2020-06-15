# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :TestCase_API_demo.py
# @Time     :2020/6/11 14:50
import unittest
from Common.HTTPClient import Request
from Common.Log import Log
cases_info = [
    {
        "case_name": "例子1",
        "method": "get",
        "interface_name": "demo",
        "data": {"username": "admin", "password": "123456"},
        "headers": "",
        "assert": {"httpstatus": 200}
    },
    {
        "case_name": "例子2",
        "method": "get",
        "interface_name": "demo",
        "data": {"username": "admin", "password": "123456"},
        "headers": "",
        "assert": {"httpstatus": 200}
    },
    {
        "case_name": "例子2",
        "method": "get",
        "interface_name": "demo",
        "data": {"username": "admin", "password": "123456"},
        "headers": "",
        "assert": {"httpstatus": 200}
    }]
log = Log()

class test_API(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.r = Request()

    def test_demo(self):
        data = {
            "username": "admin",
            "password": "123456"
        }
        headers = {
            'Content-Type': 'application/json'
        }
        # data = json.dumps(data)  # 转换成json字符串
        res = self.r.send_request(method='get', name='demo', data=data, headers=headers)
        self.assertEqual(200, res['httpstatus'], msg='状态码不正确')

    def test_interface(self):
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
        for data in cases_info:
            res = self.r.send_request(method=data['method'], name=data['interface_name'], data=data['data'],
                                      headers=data['headers'])
            vaildate = data['assert']
            for key, value in vaildate.items():
                if key in res:
                    self.assertEqual(value, res[key])


if __name__ == '__main__':
    unittest.main()
