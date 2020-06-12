# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :HTTPClient.py
# @Time     :2020/6/11 15:34
import requests
from Common.Log import Log
from Common.config import Get_Config

log = Log()


class HttpClient:
    '''
        封装发送http请求的类
    '''

    def __init__(self):
        # 一个项目的url、headers的前缀都是一样的
        self.url = Get_Config().get_Url('api_url')
        self.headers = {'Content-Type': 'application/json'}

    def get(self, name, data, headers):
        '''封装一个get请求的方法

        :param name: 接口地址的后缀
        :param data: 接口参数
        :param headers: 请求头
        :return: 返回一个元组，下标为0的是状态码，下标为1的是响应值内容（字典格式）
        '''
        try:
            # 发起get请求
            res = requests.get(url=name, params=data, headers=headers)
            log.log_info(f'请求成功，响应值为{res.json()}')
            return res.status_code, res.json()
        except Exception as error:
            raise ('接口请求发生错误：', error)

    def post(self, name, data, headers):
        '''封装post请求的方法

        :param name: 接口地址的后缀
        :param data: 接口参数
        :param headers: 请求头
        :return: 返回一个元组，下标为0的是状态码，下标为1的是响应值内容（字典格式）
        '''
        try:
            # 发起post请求
            res = requests.post(url=self.url + name, data=data, headers=headers)
            log.log_info(f'请求成功，响应值为{res.json()}')
            return res.status_code, res.json()
        except Exception as error:
            raise ('接口请求发生错误：', error)

    def delete(self, name, data, headers):
        '''封装delete请求的方法

        :param name: 接口地址的后缀
        :param data: 接口参数
        :param headers: 请求头
        :return: 返回一个元组，下标为0的是状态码，下标为1的是响应值内容（字典格式）
        '''
        try:
            # 发起delete请求
            res = requests.delete(url=self.url + name, data=data, headers=headers)
            log.log_info(f'请求成功，响应值为{res.json()}')
            return res.status_code, res.json()
        except Exception as error:
            raise ('接口请求发生错误：', error)

    def sent_request(self, method, name=None, data=None, headers=None):
        '''封装发送请求的方法

        :param method: 请求的方式，分为get、post、delete等
        :param name: 接口地址的后缀
        :param data: 接口参数
        :param headers: 接口请求头
        :return: 返回一个元组，下标为0的是状态码，下标为1的是响应值内容（字典格式）
        '''
        try:
            # 请求类型转成大写
            methon = method.upper()
            # 判断是否传入headers
            if headers == None:
                headers = self.headers
            # 判断是否传入地址后缀名
            if name == None:
                name = self.url
            else:
                name = self.url + name
            log.log_info('[请求地址：{0}][请求方法：{1}] 接口参数{2} 请求头{3}'.format(name, method, data, headers))
            # 判断请求类型
            if methon == 'GET':
                res = self.get(name, data, headers)
                return res
            elif method == 'POST':
                res = self.post(name, data, headers)
                return res
            elif method == 'DELETE':
                res = self.delete(name, data, headers)
                return res
        except Exception as error:
            raise ('接口请求发生错误：', error)


if __name__ == '__main__':
    res = HttpClient().sent_request(method='get', name='demo')
    print('这里是res', res)
    print('res的类型', type(res))
    print('这里是res的第一个元素', res[0], type(res[0]))
    print('这里是res的第二个元素', res[1], type(res[1]))
    print(res[1]['data'][0])
    print(res[1]['data'][0]['from'])
