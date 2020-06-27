# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :demo.py
# @Time     :2020/6/24 1:27
from Common.Driver import Driver

driver = Driver('chromE')
driver.visit('https://music.163.com/')
driver.frame_in("id", "g_iframe")
driver.click("id", "index-enter-default")
