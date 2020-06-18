# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :pytestrun.py.py
# @Time     :2020/6/18 12:51
import pytest

pytest.main(['-s', './Testcases', '--html=./Report/pytest.html'])
