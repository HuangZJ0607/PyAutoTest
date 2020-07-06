'''
    基于关键字驱动，pytest + allure的接口自动化测试用例的demo
'''
import os, sys

sys.path.append(os.getcwd())
from Common.HTTPClient import HTTPClient
from ddt import ddt, data, file_data
from Common.Yaml_Operation import write_yaml
from Common.ExecuteResult import RESULT_LIST
import pytest
from Common.Email import Email

path = os.path.dirname(__file__)
fpath = os.path.dirname(path)


@ddt
class Test_API:
    def setup(self):
        self.r = HTTPClient()

    @file_data(fpath + './DataFile/API.yaml')
    def test_interface(self, **data):
        # 发送请求
        res = self.r.send_request(method=data['request']['method'], name=data['request']['interface_name'],
                                  data=data['request']['parmars'], headers=data['request']['headers'])
        # 提取变量
        if 'extract' in data and data['extract']:
            for key, value in data['extract'].items():
                extract = {}
                extract[key] = res[value]
                write_yaml(extract)
        status = self.r.vaildate(data['validate'], res)
        try:
            assert status == True
            RESULT_LIST.append('True')
        except:
            RESULT_LIST.append('False')

if __name__ == '__main__':
    pytest.main(['-s', 'Testcase_API_demo.py', '--html=../Report/pytest.html'])
    Email().sendemail('../Report/pytest.html')