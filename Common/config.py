# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :config.py
# @Time     :2020/5/28 15:29
'''
    这里是配置文件
'''
from configparser import ConfigParser
from Common import FilePath


class Get_Config:

    def __init__(self):
        self.cp = ConfigParser()
        # self.cp.read("../config.ini", encoding='utf-8')
        self.cp.read(FilePath.fatherpath() + '/config.ini', encoding='utf-8')

    def get_Url(self, url_name):
        return self.cp.get('url', url_name)

    def get_Switch(self,switch_name):
        '''
        :return: 返回日志开关的值
        '''
        return self.cp.get('switch', switch_name)

    def get_Email_Sender(self):
        '''
        :return: 返回邮件发送者的地址
        '''
        return self.cp.get('email', 'email_sender')

    def get_Email_Receiver(self):
        '''
        :return: 返回邮件接收者的地址(列表类型)
        '''
        receiver = self.cp.get('email', 'email_receiver')
        receiver_list = receiver.split(",")
        return receiver_list

    def get_Email_Host(self):
        '''
        :return: 返回邮箱服务器地址
        '''
        return self.cp.get('email', 'email_host')

    def get_Email_Port(self):
        '''
        :return: 返回邮箱服务器端口
        '''
        return self.cp.get('email', 'email_port')

    def get_Email_Psw(self):
        '''
        :return: 返回邮箱的授权码
        '''
        return self.cp.get('email', 'email_psw')


if __name__ == '__main__':
    # r =Get_Config().get_Switch_Logging()
    # print(r)
    Get_Config()
