# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :config.py
# @Time     :2020/5/28 15:29
'''
    这里是配置文件
'''
from configparser import ConfigParser
import os

path = os.path.dirname(os.path.abspath(__file__))


class Get_Config:

    def __init__(self):
        # 实例化ConfigParser对象
        self.cp = ConfigParser()

        # 读取ini文件
        self.cp.read(path + '/config.ini', encoding='utf-8')

    def get_config(self, section, option):
        '''读取ini文件，并返回对应的option值
        :param section: 对应的section
        :param option:  对应的option
        :return:    option的值
        '''
        try:
            op = self.cp.get(section, option)
            return op
        except Exception as error:
            raise ('文件读取错误', error)


if __name__ == '__main__':
    print(Get_Config().get_config('email', 'switch'))
