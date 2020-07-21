'''
    基于关键字驱动的，unittest + HTMLTestRunner + DDT的UI自动化测试用例demo
'''
from Common.Driver import Driver
from ddt import ddt, file_data
from Common.Email import Email
import unittest, time
from HTMLTestRunner import HTMLTestRunner


@ddt
class Test_biTab(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.driver = Driver('Chrome')

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quite()

    def setUp(self) -> None:
        self.driver.visit('http://www.bilibili.com')

    @file_data('../DataFile/tab_content.yaml')
    def test_tab(self, **c):
        title = c.get('title')
        name = c.get('name')
        value = c.get('value')
        self.driver.click(name, value)
        self.driver.sleep(2)
        status = self.driver.assert_title(title)
        self.assertEqual(status, True)


if __name__ == '__main__':
    s = unittest.TestSuite()
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_biTab))
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    filename = '../Report/' + now + '_report.html'
    with open(filename, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title='标题', description='内容')
        runner.run(s)
        report.close()
    Email().sendemail(filename)
