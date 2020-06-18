# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Email.py
# @Time     :2020/6/9 19:31
import smtplib, os
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Common.Log import Log

from Config.config import Get_Config
import time

# 实例化日志打印模块
log = Log().logger

path = os.path.dirname(os.path.abspath(__file__))
fpath = os.path.dirname(os.path.abspath(path))


class Email:
    '''
        把邮件发送的模块封装起来
    '''
    switch = Get_Config().get_config('email', 'switch')
    # 发送人的邮箱地址
    sender = Get_Config().get_config('email', 'sender')
    # 接受人的邮箱地址
    receiver_list = Get_Config().get_config('email', 'receiver')
    # 设置邮箱服务器
    host = Get_Config().get_config('email', 'host')
    # 设置邮箱端口
    port = Get_Config().get_config('email', 'port')
    # 设置psw授权码
    password = Get_Config().get_config('email', 'psw')

    def __init__(self):
        if self.switch == '0':
            log.info('邮件发送准备中~')
            self.setemail()
        elif self.switch == '1':
            log.info('根据配置文件，邮件不发送！')
            pass

    def setemail(self):
        # 实例化MIMEMultipart对象
        self.message = MIMEMultipart()
        # 设置邮件的发送者
        self.message['From'] = Header('这里是测试报告发送者', 'utf-8')
        # 设置邮件的接收者
        # message['To'] = Header(receiver, 'utf-8')
        self.message['To'] = Header('这里是测试报告接收者', 'utf-8')
        # 设置邮件的标题
        self.message['Subject'] = Header('自动化测试报告', 'utf-8')
        # 设置邮件主体文本内容
        now = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
        # 设置邮件文本内容
        email_text = now + ' 自动化测试报告，详见附件'
        # 设置邮件格式
        self.message.attach(MIMEText(email_text, _subtype='plain', _charset='utf-8'))
        # 邮件添加附件
        att = MIMEText(open(self.new_report(), 'rb').read(), 'base64', 'utf-8')
        # 添加附件
        att['Content-Type'] = 'applicationt/octet-stram'
        att['Content-Disposition'] = 'attachment;filename="test_report.html"'
        self.message.attach(att)
        try:
            smtpobj = smtplib.SMTP()
            # 设置邮箱的地址和端口
            smtpobj.connect(self.host, self.port)
            # 登录发送人的邮箱，user是账号；password是开启邮箱服务后的授权码，非账号的密码
            smtpobj.login(self.sender, self.password)
            # 发送邮件
            smtpobj.sendmail(self.sender, self.receiver_list, self.message.as_string())
            log.info(f'邮件发送成功，附件为：{self.new_report()}')
        except Exception as error:
            log.error(f'邮件发送失败，{error}')

    def new_report(self):
        try:
            # 列出目录下所有文件和文件夹保存到lists里面
            test_report = fpath + '/Report/'
            lists = os.listdir(test_report)
            # lists里的文件按照时间排序
            lists.sort(key=lambda fn: os.path.getmtime(test_report + fn))

            # 获取最新的文件保存到new_file
            new_file = os.path.join(test_report, lists[-1])
            return new_file
        except Exception as e:
            raise ('邮件发送发生未知错误', e)


if __name__ == '__main__':
    Email()
