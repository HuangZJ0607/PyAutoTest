'''
    封装了WEBUI自动化的公用方法
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Common.Chrome_Options import Options
from Common.Log import Log
from time import sleep

log = Log().logger


# 创建浏览器对象
def open_browser(browser):
    try:
        # 将传入的browser参数进行格式化，首字母大写，其余小写
        browser = browser.capitalize()
        if browser == 'Chrome':
            # 实例化对象
            driver = webdriver.Chrome(options=Options().options_conf())
        else:
            # python反射机制，browser == Chrome时相当于webdriver.Chrome()
            driver = getattr(webdriver, browser)()
        log.info('{}浏览器启动中...'.format(browser))
    except Exception as error:
        log.info('{0}浏览器启动异常，默认启动Chrome浏览器，异常信息：{1}'.format(browser, error))
        driver = webdriver.Chrome(options=Options().options_conf())
    return driver


# 关键字驱动类
class Driver:
    # -------------------------浏览器资源-------------------------
    # 初始化函数
    def __init__(self, browser):
        self.driver = open_browser(browser)

    def visit(self, url):
        '''
            访问指定URL
        :param url: 固定参数，要访问的url地址
        '''
        log.info('访问地址：{}'.format(url))
        self.driver.get(url)

    def quite(self):
        '''
            释放浏览器资源
        '''
        log.info('关闭浏览器，释放资源~')
        self.driver.quit()

    # -------------------------元素定位-------------------------
    def locator(self, name, value):
        '''
            基于字符串来实现元素定位，调用python反射机制
        :param name: 元素的属性，如id、name、class、xpath...
        :param value: 元素的属性值
        :return: 元素对象
        '''
        try:
            return self.driver.find_element(getattr(By, name.upper()), value)
        except Exception as error:
            log.error('元素定位发生错误：{}'.format(error))
            # raise ('元素定位错误：{}'.format(error))

    # -------------------------元素操作-------------------------
    def input(self, name, value, text):
        '''
            对某元素进行输入操作
        :param name: 元素的属性，如id、name、class、xpath...
        :param value: 元素的属性值
        :param text: 往元素发送的值
        '''
        self.locator(name, value).send_keys(text)
        log.info('对元素：{0}输入文本：{1}'.format((name, value), text))

    def click(self, name, value):
        '''
            对某元素进行点击操作
        :param name: 元素的属性，如id、name、class、xpath...
        :param value: 元素的属性值
        '''
        self.locator(name, value).click()
        log.info('对元素：{}进行点击操作'.format((name, value)))

    def text(self, name, value):
        '''
            获取当前元素的内容
        :param name: 元素的属性，如id、name、class、xpath...
        :param value: 元素的属性值
        '''
        text = self.locator(name, value).text
        log.info('元素：{0}的文本内容为：{1}'.format((name, value), text))
        return text

    # -------------------------标签页操作-------------------------
    def title(self):
        '''
            获取当前句柄的title
        :return: 当前句柄的title值
        '''
        title = self.driver.title
        log.info('当前标签页的标题是：{}'.format(title))
        return title

    def switch_to_new_current(self):
        '''
            切换到新标签页
        '''
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        log.info('切换到新标签页：{}'.format(handles[1]))

    def close(self):
        '''
            关闭标签页
        '''
        self.driver.close()

    def switch_to_old_current(self):
        '''
            切换到旧标签页
        '''
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        log.info('切换到新标签页：{}'.format(handles[0]))

    # -------------------------frame表单处理-------------------------
    def frame_in(self, name, value):
        '''
            进入frame表单
        :param name: 元素的属性，如id、name、class、xpath...
        :param value: 元素的属性值
        '''
        self.driver.switch_to.frame(self.locator(name, value))
        log.info('进入{}表单'.format((name, value)))

    def frame_out(self):
        '''
            退出表单，返回到最外层的页面
        :return:
        '''
        self.driver.switch_to.default_content()
        log.info('离开表单，回到最外层的页面')

    # -------------------------警告框处理-------------------------
    def alert(self):
        '''
            获取警告框，警告框有三种:alert、confirm、prompt
        :return: 警告框元素
        '''
        try:
            alert = self.driver.switch_to.alert
            log.info('警告框获取成功')
            return alert
        except Exception as error:
            log.error('警告框获取出现异常，错误提示：{}'.format(error))

    def alert_text(self):
        '''
            获取警告框提示信息
        :return: 警告框提示信息
        '''
        text = self.alert().text
        log.info('警告框的提示信息为：{}'.format(text))
        return text

    def alert_input(self, text):
        self.alert().send_keys(text)
        log.info('向警告框输入文本{}'.format(text))

    def alert_accept(self):
        '''
            接受警告框
        '''
        self.alert().accept()
        log.info('接受警告框')

    def alert_quit(self):
        '''
            关闭警告框
        '''
        self.alert().quit()
        log.info('警告框关闭')

    # -------------------------三种等待-------------------------
    def sleep(self, time):
        '''
            强制等待
        :param time: 强制等待的时间
        '''
        sleep(time)

    def wait_y(self, time):
        '''
            隐式等待
        :param time: 隐式等待的时间
        '''
        self.driver.implicitly_wait(time)
        log.info('隐式等待{}秒'.format(time))

    def wait_x(self, name, value):
        '''
            显式等待，这里写死等待10秒，每0.5秒查询一次
        :param name: 元素的属性，如id、name、class、xpath...
        :param value: 元素的属性值
        '''
        try:
            WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locator(name, value), message='没有该元素')
            # log.info('显式等待元素：{}成功'.format((name, value)))
        except Exception as error:
            log.error('元素：{0}等待失败：{1}'.format((name.value), error))
            # raise ('元素{0}等待失败：{1}'.format((name.value), error))

    # -------------------------调用JS-------------------------
    def js(self, js):
        '''
            调用JavaScript(这里写的有点简陋，还要再调整一下)
        :param js: js语句
        '''
        self.driver.execute_script(js)

    # -------------------------窗口截图-------------------------
    def screenshot(self, file):
        try:
            self.driver.save_screenshot(file)
            log.info('窗口截图成功，存放路径是：{}'.format(file))
        except Exception as error:
            log.error('截图出现异常，错误提示：{}'.format(error))

    # -------------------------断言-------------------------
    '''
        断言需要再研究研究，没有return结果
    '''

    def assert_text(self, name, value, exp):
        '''
            对元素文本内容进行断言
        :param name: 元素的属性，如id、name、class、xpath...
        :param value: 元素的属性值
        :param exp: 预期结果
        :return: 断言结果
        '''
        reality = self.text(name, value)
        try:
            assert reality == exp
            log.info('断言成功，流程正确~')
            return True
        except:
            log.info('断言失败，流程出现异常！')
            return False

    def assert_title(self, exp):
        '''
            对当前窗体的title进行断言
        :param exp: 预期结果
        :return: 断言结果
        '''
        reality = self.title()
        try:
            assert reality == exp
            log.info('断言成功，流程正确~')
            return True
        except:
            log.info('断言失败，流程出现异常！')
            return False
