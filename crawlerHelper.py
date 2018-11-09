import urllib.request
import re
from bs4 import BeautifulSoup  # 用于解析网页


class CrawlerHelper:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def __init__(self):
        self.url = "https://www.gamersky.com/ent/wp/"

    # 移除多余内容
    def replace(self, x):
        # x = re.sub(self.removeImg, "", x)
        # x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()

    def viewPage(self):
        request = urllib.request.Request(self.url)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        self.getContent(content)

    def getContent(self, content):
        soup = BeautifulSoup(content)
        #查找所有超文本链接
        content = soup.find_all('a')
        # print(soup.find_all('a'))
        # print(self.replace(content))


crawlerhelper = CrawlerHelper()
crawlerhelper.viewPage()
