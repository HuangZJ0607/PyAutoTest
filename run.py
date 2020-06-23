# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :run.py.py
# @Time     :2020/6/18 12:51
import pytest
from Common.Email import Email
pytest.main(['-s', './Testcases', '--html=./Report/pytest.html'])
Email()