'''
    封装发送http请求的类
'''
import requests
from Common.Log import Log
from Conf.Config import Config
from Common.Mysql import connect_mysql
import json
from Common.Yaml_Operation import read_yaml_extract

log = Log().logger


class HTTPClient:
    index = 0

    def __init__(self):
        '''
            一个项目的url，headers前缀一样的，参数类型也一样
            init方法每次实例化的时候，自动调用init方法
        '''
        self.init_url_headers()

    def get_mysql_data(self, sql):
        return connect_mysql(sql)

    def init_url_headers(self):
        '''
            初始化url和headers
        '''
        self.url = Config().get('url', 'api_url')
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.re_list = []

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

        try:
            # python反射机制，这里相当于requests.method()，如requests.get()
            res = getattr(requests, method.lower())(url=self.url, headers=self.headers, data=data, files=files)
            log.info(f'>>>-----接口测试用例<{HTTPClient.index}>')
            log.info(f'接口地址：{self.url}')
            log.info(f'请求方法：{method}')
            log.info(f'接口参数：{data}')
            # 将接口返回值转换成python字典格式并打印日志
            log.info('接口响应值：{}'.format(res.json()))
            return res.json()
        except Exception as error:
            log.error('接口请求异常：{}'.format(error))
        finally:
            self.init_url_headers()

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
                # 将sql语句转换成数据库数据。如select * from token where id = 1 这个格式判断为一个数据库语句 select, update....
                if isinstance(value, str):
                    if value.startswith('select') and 'from' in value or (
                            value.startswith('update') and 'set' in value):
                        # 从数据库中读取value
                        value = self.get_mysql_data(value)
                # 预期结果与实际结果进行比较
                try:
                    assert value == actual[key]
                    log.debug(f'接口实际结果与预期结果比对一致-->实际结果为[{key}:{actual[key]}]预期结果为[{key}:{value}]')
                    self.re_list.append('True')
                except AssertionError:
                    log.error(f'接口的实际结果与预期结果不一致-->实际结果为[{key}:{actual[key]}]预期结果为[{key}:{value}]')
                    self.re_list.append('False')
            else:
                for _key, _value in actual.items():
                    if isinstance(_value, dict) and (key in _value):
                        expect_new = {}
                        expect_new[key] = value
                        self.vaildate(expect_new, _value)
                        # 递归，重新走判断逻辑
                    elif isinstance(_value, list):
                        for i in _value:
                            if key in i:
                                expect_new = {}
                                expect_new[key] = value
                                self.vaildate(expect_new, i)
        if self.re_list.count('False') > 0:
            return False
        else:
            return True


if __name__ == '__main__':
    HTTPClient().send_request(method='get', name='demo')
#
#     para = {
#         "username": "admin",
#         "password": "123456"
#     }
#     HTTPClient().send_request(method='post', name='login', data=para)
#     log.info('RESULT_LIST：', RESULT_LIST)
