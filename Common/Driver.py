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
        if browser == 'Chrome':
            log.info('Chrome浏览器启动中~~')
            driver = webdriver.Chrome(options=Options().options_conf())
        else:
            log.info('{}浏览器启动中~~'.format(browser))
            # python反射机制，browser == Chrome时相当于webdriver.Chrome()
            driver = getattr(webdriver, browser)()
    except Exception as error:
        log.info('调用浏览器异常，默认启动Chrome浏览器，异常信息：{}'.format(error))
        driver = webdriver.Chrome()
    return driver


# 关键字驱动类
class Driver:

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

    # -------------------------元素定位及操作-------------------------
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

    def input(self, name, value, text):
        '''
            对某元素进行输入操作
        :param name: 元素的属性，如id、name、class、xpath...
        :param value: 元素的属性值
        :param text: 往元素发送的值
        '''
        self.locator(name, value).send_keys(text)
        log.info('对元素{0}输入{1}'.format((name, value), text))

    def click(self, name, value):
        '''
            对某元素进行点击操作
        :param name: 元素的属性，如id、name、class、xpath...
        :param value: 元素的属性值
        '''
        self.locator(name, value).click()
        log.info('对元素{}进行点击操作'.format((name, value)))

    def text(self, name, value):
        '''
            获取当前元素的内容
        :param name: 元素的属性，如id、name、class、xpath...
        :param value: 元素的属性值
        '''
        text = self.locator(name, value).text
        log.info('元素{0}的文本内容为{1}'.format((name, value), text))
        return text

    # -------------------------标签页操作-------------------------
    def title(self):
        '''
            获取当前句柄的title
        :return: 当前句柄的title值
        '''
        title = self.driver.title
        log.info('当前页面的标题是：{}'.format(title))
        return title

    def switch_to_new_current(self):
        '''
            切换到新标签页
        '''
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        log.info('切换到新窗体{}'.format(handles[1]))

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
        log.info('切换到新窗体{}'.format(handles[0]))

    # -------------------------三种等待-------------------------
    def sleep(self, time):
        '''
            强制等待
        :param num: 强制等待的时间
        '''
        sleep(time)

    def wait_y(self, time):
        '''
            隐式等待
        :param num: 隐式等待的时间
        '''
        self.driver.implicitly_wait(time)

    def wait_x(self, name, value):
        '''
            显式等待
        :param name: 元素的属性，如id、name、class、xpath...
        :param value: 元素的属性值
        '''
        try:
            WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locator(name, value), message='没有该元素')
            log.info('显式等待元素{}成功'.format((name, value)))
        except Exception as error:
            log.error('元素{0}等待失败：{1}'.format((name.value), error))
            raise ('元素{0}等待失败：{1}'.format((name.value), error))

    # -------------------------浏览器释放-------------------------
    def quite(self):
        '''
            释放浏览器资源
        '''
        log.info('关闭浏览器，释放资源~')
        self.driver.quit()

    # -------------------------元素文本断言-------------------------
    def assert_text(self, name, value, exp):
        '''
            对元素文本内容进行断言
        :param name: 元素的属性，如id、name、class、xpath...
        :param value: 元素的属性值
        :param exp: 预期结果
        '''
        reality = self.text(name, value)
        try:
            assert reality == exp
            log.info('断言成功，流程正确！')
        except Exception as error:
            log.info('出现异常，异常信息：\n{}'.format(error))

    def assert_title(self, exp):
        '''
            对当前窗体的title进行断言
        :param exp: 预期结果
        '''
        reality = self.title()
        try:
            assert reality == exp
            log.info('断言成功，流程正确！')
        except Exception as error:
            log.info('出现异常，异常信息：\n{}'.format(error))
