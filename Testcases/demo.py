# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :demo.py
# @Time     :2020/6/24 1:27
from Common.Driver import Driver

driver = Driver('Chrome')
driver.visit('http://www.baidu.com')
driver.wait_y(10)
driver.input('id', 'kw', '林丹')
driver.click('id', 'su')
driver.sleep(3)
title = driver.title()
driver.quite()
print(title)
