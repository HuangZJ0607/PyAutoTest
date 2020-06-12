# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :TestCase_API_demo.py
# @Time     :2020/6/11 14:50
import unittest
from Common.HTTPClient import HttpClient


class test_API(unittest.TestCase):

    def setUp(self) -> None:
        self.h = HttpClient()

    def tearDown(self) -> None:
        pass

    def test_demo(self):
        data = {
            "username": "admin",
            "password": "123456"
        }
        headers = {
            'Content-Type': 'application/json'
        }
        # data = json.dumps(data)  # 转换成json字符串
        res = self.h.sent_request(method='get', name='demo', data=data, headers=headers)
        self.assertEqual(200, res[0], msg='状态码不是200')


if __name__ == '__main__':
    unittest.main()
