# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :Yaml_Operation.py
# @Time     :2020/6/17 13:28
'''
    封装读写yaml文件的方法
'''
import yaml, os

path = os.path.dirname(os.path.abspath(__file__))
fpath = os.path.dirname(path)
yaml_path = fpath + '/DataFile/extract.yaml'


def write_yaml(extract_dict):
    with open(yaml_path, 'w') as f:
        yaml.dump(extract_dict, f)


def read_yaml():
    with open(yaml_path, 'r', encoding='utf-8') as f:
        cfg = yaml.load(f)
        return cfg


def read_yaml_extract(data):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        cfg = yaml.load(f)
        data = cfg[data]
        # print(type(cfg),cfg)
        return data
