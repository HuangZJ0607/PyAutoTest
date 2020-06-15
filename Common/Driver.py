# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Driver.py
# @Time     :2020/5/25 10:09
from selenium import webdriver
from Common.Log import Log


# 关键字驱动类
class Driver(object):
    '''
        封装了部分webdriver方法
    '''
    log = Log().logger

    # 初始化函数
    def __init__(self, url, browser):
        self.open_browser(browser)
        self.driver.implicitly_wait(10)
        self.visit_url(url)

    # 打开指定浏览器
    def open_browser(self, browser):
        '''
        按照传参调用不同的浏览器驱动
        :param browser:固定参数，表示浏览器的类型
        :return:浏览器的driver驱动
        '''
        try:
            # 将参数browser转成大写
            browser = browser.upper()
            # 判断参数是哪种浏览器
            if browser == 'CHROME':
                self.driver = webdriver.Chrome()
                self.log.log_info('调用Chrome浏览器')
            elif browser == 'FIREFOX':
                self.driver = webdriver.Firefox()
                self.log.log_info('调用Firefox浏览器')
            elif browser == 'IE':
                self.driver = webdriver.Ie()
                self.log.log_info('调用ie浏览器')
        except Exception as error:
            self.log.log_error(f'浏览器启动失败')
            raise error

    # 访问指定URL
    def visit_url(self, url):
        '''
        访问指定URL
        :param url:固定参数，表示要访问的URL地址
        :return:访问URL
        '''
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            self.log.logger.log_info(f'访问url：{url}')
        except Exception as error:
            self.log.log_error(f'地址访问错误：{error}')
            raise error

    # 定位元素
    def locator(self, locator):
        '''
        定位页面上面的Element，以元组的形式传入，主要用来为其它方法服务
        :param locator: 元组的形式，见例子：（By.XPATH, xpath路径）   (By.ID, "kw")
        :return: 对应WebElement
        '''
        # 不需要在其他部分添加*号，因为*表示将变量作为元组进行解析，只需要在解析时标注即可
        try:
            el = self.driver.find_element(*locator)
            self.log.info(f'定位到元素：{locator}')
            return el
        except BaseException as error:
            self.log.error(f'元素定位失败,{error}')
            raise ('元素定位发生错误', error)

    # 输入操作
    def input_text(self, locator, text):
        '''对指定元素输入文本内容
        :param locator: 元素元组
        :param text: 文本内容
        '''
        try:
            el = self.locator(locator)
            el.send_keys(text)
            self.log.info(f'输入内容：{text}')
        except BaseException as error:
            self.log.error(f'内容输入操作失败,{error}')
            raise ('输入内容操作发生错误', error)

    # 点击操作
    def click_element(self, locator):
        '''对指定元素进行点击操作
        :param locator: 元素元组
        '''
        try:
            el = self.locator(locator)
            el.click()
            self.log.info('点击元素')
        except BaseException as error:
            self.log.error(f'元素点击失败,{error}')
            raise ('点击操作发生错误', error)

    # 获取当前元素的内容
    def get_text(self, locator):
        '''
        :param locator: 元素元组
        :return: 该元素的文本内容
        '''
        try:
            el = self.locator(locator)
            text = el.text
            self.log.info(f'当前元素的内容为：{text}')
            return text
        except Exception as error:
            self.log.error(f'元素内容获取失败,{error}')

    # 切换句柄，关闭旧的页面
    def switch_handle(self, num):
        '''按照参数切换到对应的句柄
        :param num: 对应句柄的索引值
        '''
        try:
            handles = self.driver.window_handles
            self.driver.close()
            self.driver.switch_to.window(handles[num])
            self.log.info(f'切换到页面：{handles[num]}')
        except Exception as error:
            self.log.error(f'句柄切换失败,{error}')

    # 获取当前句柄的title
    def browser_title(self):
        '''返回当前页面的title
        :return: 页面title内容
        '''
        try:
            self.log.info(f'当前页面的title：{self.driver.title}')
            return self.driver.title
        except Exception as error:
            self.log.error(f'页面标题获取失败,{error}')

    # 关闭标签页
    def close_tag(self):
        '''
        关闭当前标签页
        '''
        try:
            self.driver.close()
            self.log.info('关闭标签页')
        except Exception as error:
            self.log.error(f'标签页关闭失败,错误提示：{error}')

    # 释放浏览器资源
    def quite_browser(self):
        '''
        关闭浏览器，释放资源
        '''
        self.driver.quit()
        self.log.info('关闭浏览器，释放资源')
