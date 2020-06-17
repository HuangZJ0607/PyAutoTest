# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :HTTPClient.py
# @Time     :2020/6/11 15:34
import requests
from Common.Log import Log
from Common.config import Get_Config
from Common.Mysql import connect_mysql
import json
from Common.extract_yaml import read_yaml_extract

log = Log().logger


class RequestFail(Exception):
    pass


class HTTPClient:
    '''
        封装发送http请求的类
    '''
    index = 0

    def __init__(self):
        '''
            一个项目的url，headers前缀一样的，参数类型也一样
            init方法每次实例化的时候，自动调用init方法
        '''
        self.init_url_headers()

    def get_mysql_data(self, sql):
        sql = connect_mysql(sql)
        return sql

    def init_url_headers(self):
        '''
            初始化url和headers
        '''
        self.url = Get_Config().get_config('url', 'api_url')
        self.headers = {
            'Content-Type': 'application/json'
        }

    def get(self, data):
        '''封装一个get请求的方法
        :param data: 接口参数
        :return: 返回接口的返回值
        '''
        try:
            # 发起get请求
            res = requests.get(url=self.url, params=data, headers=self.headers)
            return res.json()
        except BaseException as error:
            raise RequestFail('接口请求发生错误：', error)

    def post(self, data, files):
        '''封装post请求的方法
        :param data: 接口参数
        :return: 返回接口的返回值
        '''
        try:
            # 发起post请求
            res = requests.post(url=self.url, data=data, headers=self.headers, files=files)
            return res.json()
        except BaseException as error:
            raise RequestFail('接口请求发生错误：', error)

    def delete(self, data):
        '''封装delete请求的方法
        :param data: 接口参数
        :return: 返回接口的返回值
        '''
        try:
            # 发起delete请求
            res = requests.delete(url=self.url, data=data, headers=self.headers)
            return res.json()
        except BaseException as error:
            raise RequestFail('接口请求发生错误：', error)

    def send_request(self, method, name=None, data=None, headers=None, files=None):
        '''封装发送请求的方法
        :param method: 请求的方式，分为get、post、delete等
        :param name: 接口地址的后缀
        :param data: 接口参数
        :param headers: 接口请求头
        :return: 返回接口的返回值
        '''
        # 用例执行数量
        HTTPClient.index += 1
        # headers判断逻辑
        if headers:
            # 转成字典类型
            for key, value in headers.items():
                # 若存在类似于${{get_token}}格式的，则将内容提取出来，放到self.headers里面，也就是所谓的参数化
                if value.startswith("${{") and value.endswith("}}"):
                    value = value.split("{{")[1].split("}}")[0]
                    value = read_yaml_extract(value)
                self.headers[key] = value

        # data判断逻辑
        if data:
            # 字典类型转换成json字符串
            if isinstance(data, dict):
                data = json.dumps(data)
        # 后缀不一定相同，但是前缀是一样的，拼接每次的请求的url
        self.url = self.url + name

        # 请求类型转成大写
        methon = method.upper()
        res = ''
        # 判断请求类型
        if methon == 'GET':
            res = self.get(data)
        elif method == 'POST':
            res = self.post(data, files)
        elif method == 'DELETE':
            res = self.delete(data)
        log.info(f'>>--开始测试用例{HTTPClient.index}请求接口地址：{self.url}，请求方法：{method}，接口参数：{data}')
        log.info('接口响应值：{}'.format(res))
        self.init_url_headers()
        return res


if __name__ == '__main__':
    res = HTTPClient().send_request(method='get', name='demo')
