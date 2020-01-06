from .models import StockInfo
from .models import News


def get_top10():
    return StockInfo.objects.all().order_by('-change_extent')[:10]


def get_news():
    news_list = News.objects.all().order_by('-news_time')
    return news_list[:8]


