# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Log.py
# @Time     :2020/6/7 20:50
import logging, datetime, os
import config
from Common import FilePath


class Log:
    '''
        封装了logging模块，调用后回生成控制台日志&日志文件
    '''

    switch = config.logging_switch

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # # 以下三行为清空上次文件
        # # 这为清空当前文件的logging 因为logging会包含所有的文件的logging
        # logging.Logger.manager.loggerDict.pop(__name__)
        # # 将当前文件的handlers 清空
        # self.logger.handlers = []
        #
        # # 然后再次移除当前文件logging配置
        # self.logger.removeHandler(self.logger.handlers)

        # logger 配置等级
        self.logger.setLevel(logging.DEBUG)

        # logger 输出格式
        self.formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y/%m/%d %H:%M:%S")

        #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志

        if not self.logger.handlers:
            self.consolelogging()
            if self.switch == '0':
                self.filelogging()
            elif self.switch == '1':
                pass

    def consolelogging(self):
        # 创建控制台处理器
        sh = logging.StreamHandler()
        # 控制台处理器指定格式
        sh.setFormatter(self.formatter)
        # 把控制台处理器添加到日志器中
        self.logger.addHandler(sh)

    def filelogging(self):
        file_path = FilePath.fatherpath() + '/log/log.txt'
        if os.path.exists(file_path):
            os.remove(file_path)
        # 创建文件处理器
        # fh = logging.FileHandler(filename="../log/log_{}.txt".format(time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())))

        # loggger 文件配置路径
        fh = logging.FileHandler(file_path)
        # 文件处理器设置格式
        fh.setFormatter(self.formatter)
        # 添加文件处理器到日志器
        self.logger.addHandler(fh)
        fh.close()

    # 以下皆为重写方法 并且每次记录后清除logger
    def log_info(self, message=None):
        # self.__init__()
        self.logger.info(message)
        # self.logger.removeHandler(self.logger.handlers)

    def log_debug(self, message=None):
        # self.__init__()
        self.logger.debug(message)
        # self.logger.removeHandler(self.logger.handlers)

    def log_warning(self, message=None):
        # self.__init__()
        self.logger.warning(message)
        # self.logger.removeHandler(self.logger.handlers)

    def log_error(self, message=None):
        # self.__init__()
        self.logger.error(message)
        # self.logger.removeHandler(self.logger.handlers)

    def log_critical(self, message=None):
        # self.__init__()
        self.logger.critical(message)
        # self.logger.removeHandler(self.logger.handlers)


if __name__ == '__main__':
    log = Log()
    log.log_info('info')
