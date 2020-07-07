# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Mysql.py
# @Time     :2020/6/11 15:38
'''
    封装连接mysql数据库的方法
'''
import pymysql
from Conf.Config import Config
from Common.Log import Log

log = Log().logger


def connect_mysql(sql):
    return 200


class MyDB:
    # 获取数据库的地址host(string类型)、端口port(number类型)、用户名user(string类型)、密码password(string类型)
    global host, port, user, password, database, con
    host = Config().get('mysql', 'host')
    port = int(Config().get('mysql', 'port'))
    user = Config().get('mysql', 'user')
    password = Config().get('mysql', 'password')
    database = Config().get('mysql', 'database')
    con = {
        'host': str(host),
        'port': int(port),
        'user': user,
        'password': password,
        'database': database
    }

    def __init__(self):
        self.db = self.connectDB()
        self.cursor = self.db.cursor()

    def connectDB(self):
        try:
            self.db = pymysql.connect(**con)
            log.info(f'成功连接到数据库')
            return self.db
        except ConnectionError as e:
            log.error(f'连接数据库发生异常：\n{e}')
            raise

    def executeSQL(self, sql):

        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor

    def get_all(self, sql):
        return self.executeSQL(sql).fetchall()

    def get_one(self, sql):
        return self.executeSQL(sql).fetchone()

    def closeDB(self):
        self.db.close()
        log.info('数据库连接关闭！')

    # con = pymysql.connect(host=host, port=port, user=user, password=password, charset='utf8', database=database)
    # cursor = con.cursor()
    # cursor.execute(sql)
    # res = cursor.fetchall()
    # return res


if __name__ == '__main__':
    db = MyDB()
    value = db.get_one('select * from test')
    value1 = db.get_all('select * from test')
    db.closeDB()
    print(value)
    print(value1)
