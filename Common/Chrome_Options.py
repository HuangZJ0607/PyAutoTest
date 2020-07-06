'''
    Chrome浏览器的配置文件
'''
from selenium import webdriver


class Options:
    def options_conf(self):
        # 创建chromeOptions对象
        options = webdriver.ChromeOptions()

        # 窗体最大化
        options.add_argument('start-maximized')

        # 无头模式，启动浏览器进程，但不展示到前台
        # options.add_argument('--headless')

        # 去掉开发者警告
        options.add_experimental_option('useAutomationExtension', False)

        # 去掉黄条
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        # 去掉密码管理弹窗
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)

        # 无头模式： 启动浏览器进程，但是不会显示出来
        # options.add_argument('--headless')
        # 启动隐身模式
        # options.add_argument('incognito')
        return options

        # 读取本地缓存，这个操作非常不推荐使用


'''
            1. 找到本地缓存的位置：通过chrome://version查看
            2. 传入本地缓存，应用参数 --user-data-dir=
            3. 加载之前，请关闭所有的浏览器
            4. 适用在记住登录状态下的URL的访问
            5. 当输入这个参数后，读取和加载的时间会延长很久，没有很好的办法处理。只有手动先输入一个url让它运行
'''
# options.add_argument(r'--user-data-dir=C:\Users\15414\AppData\Local\Google\Chrome\User Data')
# 去掉警告
# options.add_argument('disable-infobars')  # 这是老版本的chrome浏览器采用的去掉警告的形式
