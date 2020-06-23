# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :TestCase_shop.py
# @Time     :2020/6/23 16:22
import pytest
from Common.Driver import Driver
from Config.config import Get_Config
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture()
def login():
    print('先进行登录')
    driver = Driver(Get_Config().get_config('url', 'ui_url'), 'chrome')
    login_page = (By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/a[1]')
    driver.click_element(login_page)
    username_box = (By.XPATH, '//input[@name="accounts"]')
    driver.input_text(username_box, 'huangzijian')
    pwd_box = (By.XPATH, '//input[@name="pwd"]')
    driver.input_text(pwd_box, '123456')
    login_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')
    driver.click_element(login_button)
    sleep(3)
    return driver


class Test_shop:
    def test_search(self, login):
        print("执行商品搜索")
        search_box = (By.XPATH, '//input[@id="search-input"]')
        login.input_text(search_box, '手机')
        search_button = (By.XPATH, '//input[@id="ai-topsearch"]')
        login.click_element(search_box)
        sleep(2)
        assert login.browser_title() == 'ShopXO企业级B2C电商系统提供商 - 演示站点'
        login.quite_browser()

    # def test_car(self, login):
    #     print("2")


if __name__ == '__main__':
    pytest.main(['-s', 'TestCase_shop.py', '--html=../Report/pytest.html'])
