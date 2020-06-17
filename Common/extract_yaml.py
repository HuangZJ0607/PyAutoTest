# -*- coding: utf-8 -*-
# @Author   :hzj
# @File     :extract_yaml.py
# @Time     :2020/6/17 13:28
import yaml
from Common.FilePath import fatherpath

yaml_path = fatherpath() + '/DataFile/extract.yaml'


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


# extract_dict = {"token": '123123','name':'hahaha'}
# write_yaml(extract_dict)
headers = {"token": '${{token_name}}'}
