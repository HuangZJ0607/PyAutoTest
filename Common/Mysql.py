# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Mysql.py
# @Time     :2020/6/11 15:38
import pymysql
import re
from Common.config import Get_Config

# 获取数据库的地址host(string类型)、端口port(number类型)、用户名user(string类型)、密码password(string类型)
host = Get_Config().get_config('mysql', 'host')
port = int(Get_Config().get_config('mysql', 'port'))
user = Get_Config().get_config('mysql', 'user')
password = Get_Config().get_config('mysql', 'password')
database=Get_Config().get_config('mysql','database')
con = pymysql.connect(host=host, port=port, user=user, password=password, charset='utf8', database=database)
cursor = con.cursor()
# cur.execute('show databases')
# for x in cur:
#     print(x)

cursor.execute("select * from test limit 5")
res = cursor.fetchall()
for x in res:
    print(x)
# cursor.close()
