import urllib.request
import re
import string
import os
import time
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
        # 全局file变量，文件写入操作对象
        self.file = open("wallpaperTotal.txt", "wb")
        self.urlList = []

    # 移除多余内容
    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()  # 写入所有壁纸链接到文件

    def selectContent(self, x):
        print(type(x))
        for link in x:
            if link.get('title') != None:
                url = link.get('href')
                if ("https://www.gamersky.com" not in link.get('href')):
                    url = "https://www.gamersky.com" + link.get('href')
                wallpaperbean = WallpaperBean(link.get('title'), url)
                self.urlList.append(wallpaperbean)
                # print(link.get('title'))
                # print(link.get('href'))
                self.file.write("\n".encode())
                self.file.write(link.get('title').encode('utf-8'))
                self.file.write("\n".encode())
                self.file.write(url.encode('utf-8'))
        print(self.urlList)
        return self.urlList

    # 打开链接
    def viewPage(self):
        request = urllib.request.Request(self.url)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        return self.getContent(content)

    # 查找总目录
    def getContent(self, content):
        soup = BeautifulSoup(content)
        # 查找所有超文本链接
        content = soup.find_all('a')
        return self.selectContent(content)


class WallpaperBean(object):
    def __init__(self, title, url):
        self.title = title
        self.url = url

    # python的toString方法
    def __repr__(self):
        return "title, " + self.title + "url, " + self.url


# 每一期的解析
class GamerSkyParsePhase:
    def __init__(self, title, url):
        self.url = url
        self.title = title
        self.file = open("wallPaperList.txt", "wb")
        self.urlList = []

    # 打开子链接
    def viewPageUrl(self):
        request = urllib.request.Request(self.url)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        return self.getContentUrl(content)

    # 查找子目录
    def getContentUrl(self, content):
        soup = BeautifulSoup(content)
        # 查找所有超文本链接
        content = soup.find_all('a')
        return self.selectContentUrl(content)

    def selectContentUrl(self, x):
        # 截取字符串最后一个"/"后面的内容（包含最后一个"/"）：/1122337.shtml
        self.url = self.url[self.url.rfind("/"):]
        print(self.url)
        # 截取第1位到倒数第6位的内容
        self.url = self.url[1:-6]
        print(self.url)
        for tag in x:
            # print(type(tag))
            # bs4.element.tag类型转换成String
            wallpaperUrl = str(tag)
            if (self.url in wallpaperUrl) & ("href" in wallpaperUrl):
                if ("_" in tag['href']):
                    wallpaperbean = WallpaperBean(tag.text, tag['href'])
                    self.urlList.append(wallpaperbean)
                    # print(tag['href'])
                    # print(tag.text)
                    self.file.write("\n".encode())
                    self.file.write(tag['href'].encode('utf-8'))
                    self.file.write("\n".encode())
                    self.file.write(tag.text.encode('utf-8'))
        return self.urlList


# 每期中每页的解析
class GamerSkyParsePage:
    def __init__(self, url):
        self.url = url
        self.list =[]
        self.saveUrl = "/Users/a1234/parse"

    # 打开子链接
    def viewPageUrl(self):
        request = urllib.request.Request(self.url)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        self.parsePage(content)

    # 该页中壁纸链接以picact类为标示的<img>标签
    def parsePage(self, content):
        soup = BeautifulSoup(content)
        # 查找所有以picact类为标示超文本链接
        content = soup.find_all("img", class_="picact")
        for url in content:
            self.list.append(url['src'])
            print(self.list)
            # 使用Python中的urllib类中的urlretrieve()函数，直接从网上下载资源到本地
            try:
                # 是否有这个路径
                if not os.path.exists(self.saveUrl):
                    # 创建路径
                    os.makedirs(self.saveUrl)
                # 拼接图片名（包含路径）

                filename = self.saveUrl+"/"+url['src'].split('/')[-1]
                print(filename)
                # 下载图片，并保存到文件夹中
                urllib.request.urlretrieve(url['src'], filename=filename)

            except IOError as e:
                print("IOError")
            except Exception as e:
                print("Exception")

crawlerhelper = CrawlerHelper()
url = crawlerhelper.viewPage()
gamerSkyParsePhase = GamerSkyParsePhase(url[0].title, url[0].url)
urllist = gamerSkyParsePhase.viewPageUrl()
for wallpaper in urllist:
    gamerSkyParsePage = GamerSkyParsePage(wallpaper.url)
    gamerSkyParsePage.viewPageUrl()
