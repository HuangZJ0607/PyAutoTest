# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Conf.py
# @Time     :2020/5/28 15:29
'''
    封装读取配置文件的类
'''
from configparser import ConfigParser
import os

path = os.path.dirname(os.path.abspath(__file__))


class Config:

    def __init__(self):
        # 实例化ConfigParser对象
        self.cp = ConfigParser()
        self.configpath = path + '/config.ini'
        # 读取ini文件
        self.cp.read(self.configpath, encoding='utf-8')

    def get(self, section, option):
        '''读取ini文件，并返回对应的option值
        :param section: 对应的section
        :param option:  对应的option
        '''
        try:
            op = self.cp.get(section, option)
            return op
        except Exception as error:
            raise ('文件读取错误', error)

    def set(self, section, option, value):
        try:
            self.cp.set(section, option, value)
            with open(self.configpath, "r+", encoding="utf-8") as f:
                return self.cp.write(f)
        except Exception as error:
            raise ('文件写入发生错误', error)
