'''
    根据环境参数调整config.ini配置文件
'''
from Conf.Config import Config


def envset(env):
    env = env.lower()
    c = Config()
    if env == 'debug':
        c.set('env', 'env', env)
        c.set('url', 'api_url', 'http://39.98.138.157:5000/api/')
        c.set('url', 'ui_url', 'http://39.98.138.157/shopxo/')
        c.set('mysql', 'host', 'localhost')
        c.set('mysql', 'port', '3306')
        c.set('mysql', 'user', 'root')
        c.set('mysql', 'password', '000000')
        c.set('mysql', 'database', 'test')
    elif env == 'release':
        c.set('env', 'env', env)
        c.set('url', 'api_url', 'http://39.98.138.157:5000/api/')
        c.set('url', 'ui_url', 'http://39.98.138.157/shopxo/')
        c.set('mysql', 'host', 'localhost')
        c.set('mysql', 'port', '3306')
        c.set('mysql', 'user', 'root')
        c.set('mysql', 'password', '000000')
        c.set('mysql', 'database', 'test')


if __name__ == '__main__':
    envset('debug')
