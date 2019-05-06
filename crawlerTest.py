import urllib.request
import time
from urllib import parse


# Accept: application/vnd.alloy+json; version=1
# Accept-Language: zh-cn
# Content-Type: application/json;charset=UTF-8
# Origin: http://www.bceasy.com
# Referer: http://www.bceasy.com/signin
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
# X-Client-Type: BROWSER
# X-Requested-With: XMLHttpRequest

# http://www.bceasy.com/api/bimage-web/user/login?_t=1541570996528
# {login: "xabws@163.com", password: "a123456"}
# login: "xabws@163.com"
# password: "a123456"


# class crawlerHelper:
#     def __init__(self, url, data):
#         self.url = url
#         self.data = data
#         self.headers = {"Accept": "application/vnd.alloy+json; version=1",
#                         "Accept-Language": "zh_cn",
#                          "Content-Type": "application/json; charset=UTF-8",
#                         "Origin": "http://www.bceasy.com",
#                         "Referer": "http://www.bceasy.com/signin",
#                         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
#                         "X-Client-Type": "BROWSER",
#                         "X-Requested-With": "XMLHttpRequest",
#                         }
#
#     def crawlerOpen(self):
#         print(self.headers)
#         request = urllib.request.Request(url=self.url, data=self.data, headers=self.headers)
#         response = urllib.request.urlopen(request).read()
#         print(response.read().decode('utf-8'))

class crawlerHelper:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    def crawlerOpen(self):
        print(self.headers)
        request = urllib.request.Request(url=self.url,headers=self.headers)
        response = urllib.request.urlopen(request)
        print(response.read().decode('utf-8'))
value = {}
# value["login"] = ["xabws@163.com"]
# value["password"] = ["123456"]
# data = urllib.parse.urlencode(value).encode('utf-8')
crawlerHelper = crawlerHelper("http://www.zhihu.com")
crawlerHelper.crawlerOpen()
