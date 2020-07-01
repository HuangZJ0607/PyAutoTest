# 自研接口和UI一体化的自动化测试框架（持续更新中）
## 框架介绍  
语言：python  
UI自动化测试框架：selenium  
接口测试框架：requests  
用例组织框架：pytest  
测试报告：allure / pytest-html  
数据驱动：ddt / excel 
数据文件：yaml  
## 环境安装  
1.安装python版本3.x  
2.安装IDE-pycharm、Chrome浏览器   
3.git拉取本项目 `git clone https://github.com/HuangZJ0607/PyAutoTest.git`  
4.安装相关依赖包 `pip install -r install.txt`   
5.运行run.py运行测试用例 
## 项目文件层级  
./PyAutoTest  
│──Common --->存放公用类  
│   │  Chrome_Options.py   
│   │  Driver.py   
│   │  Email.py   
│   │  Excel_Driver.py   
│   │  Excel_Operation.py    
│   │  HTTPClient.py   
│   │  Log.py   
│   │  Mysql.py  
│   └Yaml_Operation.py          
│──Config --->存放配置文件及封装读取ini文件的方法  
│   │  config.ini    
│   └config.py          
│──DataFile --->存放数据文件  
│──Log --->存放日志文件  
│──Report --->存放测试报告    
│──Testcases --->存放测试用例     
│  .gitignore  
│  install.txt --->记录所有需要安装模块的文件  
│  pytest.ini --->pytest测试的配置文件，核心文件用于命令行执行测试  
│  README.md  
│  run.py --->核心文件，用于编译器执行测试  
***
#### Please wait for the next update!!!

 
