	这是我第一个Python自动化测试项目
./PyAutoTest  
├─Common --->存放公用类  
│  │  Chrome_Options.py --->Chrome浏览器配置  
│  │  Driver.py --->封装WEBUI自动化的Driver公共类  
│  │  Email.py --->封装邮件模块的Email公共类，用于发送邮件  
│  │  extract_yaml.py --->封装yaml文件的读写等方法  
│  │  HTTPClient.py --->封装接口请求的HTTPClient公共类  
│  │  Log.py --->封装了日志模块的Log公共类  
│  └──Mysql.py --->封装了数据库连接的方法  
│          
├─Config --->存放配置文件及封装读取ini文件的方法  
│  │  config.ini --->配置文件  
│  └──config.py --->封装读取ini文件的方法  
│          
├─DataFile --->存放数据文件  
│   
├─Log --->存放日志文件  
│   
├─Report --->存放测试报告    
│   
├─Testcases --->存放测试用例    
│  │  demo.py  
│  │  TestCase_API_demo.py  
│  │  TestCase_shop.py   
│  └──TestCase_UI_demo.py  
│  
│  .gitignore  
│  install.txt --->记录所有需要安装模块的文件
│  pytest.ini --->pytest测试的配置文件，核心文件用于命令行执行测试  
│  README.md  
│  run.py --->核心文件，用于编译器执行测试  
***
Please wait for the next update!!!

 
