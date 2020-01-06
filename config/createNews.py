from tradingSystem.models import News
from my_fake_useragent import UserAgent
from scrapy import Spider
from urllib import request


with open('config/news.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        a = line.find('【')
        b = line.find('】')
        title = line[a+1:b]
        abstract = line[b+1:]
        print(title, '\t',abstract, '\n')

        news = News.objects.create(
            title=title,
            content=abstract,
        )
        news.save()





