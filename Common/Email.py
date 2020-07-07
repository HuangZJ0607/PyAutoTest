'''
    封装邮件发送的类
'''
import smtplib, os
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Common.Log import Log
from Common.ExecuteResult import RESULT_LIST
from Conf.Config import Config
import time

# 实例化日志打印模块
log = Log().logger

path = os.path.dirname(os.path.abspath(__file__))
fpath = os.path.dirname(os.path.abspath(path))


class Email:
    log.info('邮件发送准备中~')
    # ----------------从config.ini文件获取邮件相关参数----------------
    c = Config()
    # 发送人的邮箱地址
    sender = c.get('email', 'sender')
    # 接受人的邮箱地址
    receiver_list = c.get('email', 'receiver')
    # 设置邮箱服务器
    host = c.get('email', 'host')
    # 设置邮箱端口
    port = c.get('email', 'port')
    # 设置psw授权码
    password = c.get('email', 'psw')

    def sendemail(self, filepath=None):
        # --------------------------发件相关参数--------------------------
        # 实例化MIMEMultipart对象
        self.message = MIMEMultipart()
        # 设置邮件的发送者
        self.message['From'] = Header('自动化测试负责人', 'utf-8')
        # 设置邮件的接收者
        # message['To'] = Header(receiver, 'utf-8')
        self.message['To'] = Header('测试报告管理邮箱', 'utf-8')
        # 设置邮件的标题
        self.message['Subject'] = Header('自动化测试报告', 'utf-8')
        # --------------------------编辑邮件附件内容--------------------------
        t = '自动化测试已完成'
        # filepath参数非空，即要添加附件
        if filepath != None:
            # 邮件添加附件
            att = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')
            # 添加附件
            att['Content-Type'] = 'applicationt/octet-stram'
            att['Content-Disposition'] = 'attachment;filename="report.html"'
            self.message.attach(att)
            t = t + '，详细内容请查看附件中的自动化测试报告，详见附件'
        # 设置邮件主体文本内容
        now = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
        # 设置邮件文本内容
        email_text = f'''
{now} {t}
用例执行结果列表：{RESULT_LIST}
用例总数为：{len(RESULT_LIST)}  通过率为：{(RESULT_LIST.count('True') / len(RESULT_LIST)) * 100}%  失败率为：{(RESULT_LIST.count('False') / len(RESULT_LIST)) * 100}%
        '''
        # 设置邮件格式
        self.message.attach(MIMEText(email_text, _subtype='plain', _charset='utf-8'))
        # --------------------------发送邮件--------------------------
        try:
            smtpobj = smtplib.SMTP()
            # 设置邮箱的地址和端口
            smtpobj.connect(self.host, self.port)
            # 登录发送人的邮箱，user是账号；password是开启邮箱服务后的授权码，非账号的密码
            smtpobj.login(self.sender, self.password)
            # 发送邮件
            smtpobj.sendmail(self.sender, self.receiver_list, self.message.as_string())
            log.info(f'邮件发送成功~')
        except Exception as error:
            log.error(f'邮件发送出现异常\n{error}')

    # def new_report(self):
    #     '''
    #         获取Report文件夹下最新的测试报告
    #     '''
    #     try:
    #         # 列出目录下所有文件和文件夹保存到lists里面
    #         test_report = fpath + '/Report/'
    #         lists = os.listdir(test_report)
    #         # lists里的文件按照时间排序
    #         lists.sort(key=lambda fn: os.path.getmtime(test_report + fn))
    #
    #         # 获取最新的文件保存到new_file
    #         new_file = os.path.join(test_report, lists[-1])
    #         return new_file
    #     except Exception as e:
    #         raise ('邮件发送发生未知错误', e)


if __name__ == '__main__':
    Email().sendemail()
