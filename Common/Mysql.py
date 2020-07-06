# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Mysql.py
# @Time     :2020/6/11 15:38
'''
    封装连接mysql数据库的方法
'''
import pymysql
from Conf.Config import Config

# 获取数据库的地址host(string类型)、端口port(number类型)、用户名user(string类型)、密码password(string类型)
host = Config().get('mysql', 'host')
port = int(Config().get('mysql', 'port'))
user = Config().get('mysql', 'user')
password = Config().get('mysql', 'password')
database = Config().get('mysql', 'database')


def connect_mysql(sql):
    # con = pymysql.connect(host=host, port=port, user=user, password=password, charset='utf8', database=database)
    # cursor = con.cursor()
    # cursor.execute(sql)
    # res = cursor.fetchall()
    # return res
    return 200


def close_mysql():
    pass
