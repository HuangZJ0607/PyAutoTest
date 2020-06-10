# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :FilePath.py
# @Time     :2020/6/9 22:38
from os.path import *


def nowpath():
    dir_path = dirname(abspath(__file__))
    return dir_path


def fatherpath():
    dir_path = dirname(dirname(abspath(__file__)))
    return dir_path
