# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Log.py
# @Time     :2020/6/7 20:50
import logging, os
from Config.config import Get_Config
import time
path = os.path.dirname(__file__)
fpath = os.path.dirname(path)
switch = Get_Config().get_config('logging', 'switch')
level = Get_Config().get_config('logging', 'level').upper()


class Log:
    '''
        封装了logging模块，调用后回生成控制台日志&日志文件
    '''

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # logger 配置等级
        self.logger.setLevel(level)
        # logger 输出格式
        self.formatter = logging.Formatter(
            fmt="[%(asctime)s][%(filename)s][%(levelname)s] %(message)s", datefmt="%Y/%m/%d %H:%M:%S")
        #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
        if not self.logger.handlers:
            self.consolelogging()
            # 判断是否打印日志到日志文件
            if switch == '0':
                self.filelogging()
            elif switch == '1':
                pass

    def consolelogging(self):
        # 创建控制台处理器
        sh = logging.StreamHandler()
        # 控制台处理器指定格式
        sh.setFormatter(self.formatter)
        # 把控制台处理器添加到日志器中
        self.logger.addHandler(sh)

    def filelogging(self):
        now = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
        file_path = fpath + '/Log/log_' + now + '.txt'
        # 判断是否存在日志文件，是则删除
        if os.path.exists(file_path):
            os.remove(file_path)
        # loggger 文件配置路径
        fh = logging.FileHandler(file_path)
        # 文件处理器设置格式
        fh.setFormatter(self.formatter)
        # 添加文件处理器到日志器
        self.logger.addHandler(fh)
        fh.close()
if __name__ == '__main__':
    Log().logger.info('123123')