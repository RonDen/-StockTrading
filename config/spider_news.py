import os
import re
import sys
import urllib
import urllib.request  # 在python3.x中没有urllib2，必须使用此语句
from urllib import request
from bs4 import BeautifulSoup
import requests  # Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
referer = 'https://tushare.pro/login?next=%2Fnews%2Fnews_sina'
headers = {
    'User-Agent': user_agent,
    'Host': 'tushare.pro',
    'Origin': 'https://tushare.pro',
    'Referer': referer
}

# downpicture = urllib.request.urlopen('http://guba.eastmoney.com/list,603121.html').read()

stockPageRequest = urllib.request.urlopen('http://finance.eastmoney.com/news/cdfsd.html')
htmlTitleContent = str(stockPageRequest.read(), 'utf-8')
# 正则匹配标题
titlePattern = re.compile('<span class="l3 a3">title="(.*?)"</span>', re.S)
p_title = 'title="(.*?)"(.*?)'
title = re.findall(p_title, htmlTitleContent)
# 循环输出对应的标题
for i in range(len(title)):
    if not title[i][0].find("【"):
        print(title[i][0])


