# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Testcase_shop.py
# @Time     :2020/6/23 16:22
import pytest, allure, os
from Common.Driver import Driver
from Config.config import Get_Config


@allure.feature('电商_登录')
@pytest.fixture()
def login():
    driver = Driver('Chrome')
    driver.visit(Get_Config().get_config('url', 'ui_url'))
    driver.wait_y(10)
    driver.click('xpath', '/html/body/div[6]/div/div[1]/div[2]/a[1]')
    driver.sleep(2)
    driver.input('xpath', '//input[@name="accounts"]', 'huangzijian')

    driver.input('xpath', '//input[@name="pwd"]', '123456')

    driver.click('xpath', '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

    driver.sleep(3)
    yield driver
    driver.quite()


class Test_shop:
    # @allure.feature('电商_商品搜索的用例')
    def test_search(self, login):
        login.input('xpath', '//input[@id="search-input"]', '手机')
        login.click('xpath', '//input[@id="ai-topsearch"]')
        login.sleep(2)
        status = login.assert_title('手机 - ShopXO企业级B2C电商系统提供商 - 演示站点')
        assert status == True

    # def test_car(self, login):
    #     print("2")


if __name__ == '__main__':
    pytest.main(['-s', 'Testcase_shop.py', '--alluredir', '../Report/xml'])
    os.system('allure generate --clean ../Report/xml/ -o ../Report/html')
    # pytest.main(['-s', 'Testcase_shop.py'])
