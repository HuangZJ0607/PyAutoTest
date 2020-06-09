# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Email.py
# @Time     :2020/6/9 19:31
import smtplib, os, config
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Common.Log import Log
from Common import FilePath


class Email:
    '''
        把邮件发送的模块封装起来
    '''
    # 实例化日志打印模块
    log = Log()

    def __init__(self):
        self.setemail()

    def setemail(self):

        # 发送人的邮箱地址
        self.sender = config.email_sender

        # 接受人的邮箱地址
        # receiver = config.email_receiver
        self.receiver = ['*****@qq.com']

        # 设置邮箱服务器
        self.host = config.email_host

        # 设置邮箱端口
        self.port = config.email_port

        # 设置psw授权码
        self.password = config.email_psw
        self.message = MIMEMultipart()

        # 设置邮件的发送者
        self.message['From'] = Header(self.sender, 'utf-8')

        # 设置邮件的接收者
        # message['To'] = Header(receiver, 'utf-8')
        self.message['To'] = Header('*****@qq.com', 'utf-8')

        # 设置邮件的标题
        self.message['Subject'] = Header('自动化测试报告', 'utf-8')

        self.message.attach(MIMEText('邮件发送', _subtype='html', _charset='utf-8'))

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
            smtpobj.sendmail(self.sender, self.receiver, self.message.as_string())
            self.log.log_info(f'邮件发送成功，附件名称为：{self.new_report()}')
            print(self.new_report())
        except Exception as error:
            self.log.log_error(f'邮件发送失败，{error}')

    def new_report(self):
        # 列出目录下所有文件和文件夹保存到lists里面
        test_report = FilePath.fatherpath() + '/Test_Report/'
        lists = os.listdir(test_report)

        # lists里的文件按照时间排序
        lists.sort(key=lambda fn: os.path.getmtime(test_report + fn))

        # 获取最新的文件保存到new_file
        new_file = os.path.join(test_report, lists[-1])
        return new_file


if __name__ == '__main__':
    Email()
