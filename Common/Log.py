import logging, os, time
from Conf.Config import Config


class Log:
    def __init__(self):
        '''日志管理器'''
        self.logger = logging.getLogger(__name__)
        # logger 配置等级
        if Config().get('logging', 'level').upper() not in ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'):
            loglevel = 'INFO'  # 默认日志等级为INFO
        else:
            loglevel = Config().get('logging', 'level').upper()
        self.logger.setLevel(loglevel)
        # logger 输出格式
        # fmt = "[%(asctime)s.%(msecs)03d][%(levelname)s][%(filename)s]%(message)s"
        fmt = "[%(asctime)s.%(msecs)03d][%(levelname)s]%(message)s"
        self.formatter = logging.Formatter(fmt=fmt, datefmt="%Y-%m-%d %H:%M:%S")
        # 判断是否存在handler，避免日志重复打印
        if not self.logger.handlers:
            self.consolelogging()
            # 判断是否打印日志到日志文件
            if Config().get('logging', 'switch') == '0':
                today = time.strftime('%Y%m%d', time.localtime())
                # 按照环境则输出日志文件，test则为服务器，debug为本地
                if Config().get('env', 'env') == 'test':
                    # 测试环境则按照服务器路径输出日志文件
                    file_path1 = 'log_' + today + '.txt'
                    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '../../../Log/', file_path1)
                    self.filelogging(file_path)
                else:
                    # 调试环境，即本地工程，则按照本地路径输出日志文件
                    file_path = os.path.dirname(os.path.dirname(__file__)) + '/Log/log_' + today + '.txt'
                    self.filelogging(file_path)

    def consolelogging(self):
        # 创建控制台处理器
        sh = logging.StreamHandler()
        # 控制台处理器指定格式
        sh.setFormatter(self.formatter)
        # 把控制台处理器添加到日志器中
        self.logger.addHandler(sh)

    def filelogging(self, filepath):
        # 创建文件处理器
        fh = logging.FileHandler(filepath)
        # 文件处理器指定格式
        fh.setFormatter(self.formatter)
        # 添加文件处理器到日志器
        self.logger.addHandler(fh)
        fh.close()


if __name__ == '__main__':
    for i in range(10):
        Log().logger.info(f'{i}')
