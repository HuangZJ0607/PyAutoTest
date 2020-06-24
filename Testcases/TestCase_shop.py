# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :TestCase_shop.py
# @Time     :2020/6/23 16:22
import pytest,allure
from Common.Driver import Driver
from Config.config import Get_Config

@allure.feature('电商_登录')
@pytest.fixture()
def login():
    driver = Driver('Chrome')
    driver.visit(Get_Config().get_config('url', 'ui_url'))
    driver.wait_y(10)
    driver.click('xpath', '/html/body/div[6]/div/div[1]/div[2]/a[1]')

    driver.input('xpath', '//input[@name="accounts"]', 'huangzijian')

    driver.input('xpath', '//input[@name="pwd"]', '123456')

    driver.click('xpath', '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

    driver.sleep(3)
    return driver


class Test_shop:
    @allure.feature('电商_商品搜索的用例')
    def test_search(self, login):
        print("执行商品搜索")

        login.input('xpath', '//input[@id="search-input"]', '手机')

        login.click('xpath', '//input[@id="ai-topsearch"]')
        login.sleep(2)
        login.assert_title('手机 - ShopXO企业级B2C电商系统提供商 - 演示站点')
        login.quite()

    # def test_car(self, login):
    #     print("2")


if __name__ == '__main__':
    pytest.main(['-s', 'TestCase_shop.py', '--html=../Report/pytest.html'])
