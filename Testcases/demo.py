# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :demo.py
# @Time     :2020/6/24 1:27
from Common.HTTPClient import HTTPClient

h = HTTPClient()
parmars = '{"username":"admin","password":"123456"}'
res = h.send_request('posT', 'login', parmars)
token = res['token']
print(token)
