import requests
import unittest
import json
import time
import HTMLTestRunnerCN

class Interface_test(unittest.TestCase):
    #实时天气查询接口
    def test_query_weather(self):
        url = 'https://tianqiapi.com/api'
        data = 'version=v6&appid=73691227&appsecret=123456'
        response = requests.request('GET',url,params=data)
        print(json.dumps(response.json(),indent=4,ensure_ascii=False))

#文件路径
#Testcase_dir = 'C:\\Users\\EDY\PycharmProjects\\AutoTest\\api_test'
Testcase_dir ="../api_test"

#测试报告名称前加时间戳
#now=time.strftime("%Y-%m-%d %H_%M_%S")

#获取文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'Queryweather_report.py')

#存放报告的路径
filename = 'C:\\Users\\EDY\PycharmProjects\\AutoTest\\api_test\\Queryweather_report.html'
#filename ="../api_test/"+now+"Queryweather_report.html"
#filename ="../api_test/Queryweather_report.html"

fp = open(filename, 'wb')

runner = HTMLTestRunnerCN.HTMLTestRunner(
stream=fp,
title='接口测试报告',
description='用例执行情况：')

#runner.run(testunit)
runner.run(dis)
fp.close()
