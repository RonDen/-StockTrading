from .models import StockInfo, StockComment
from .models import News


def get_top10():
    return StockInfo.objects.all().order_by('-change_extent')[:10]


def get_news():
    news_list = News.objects.all().order_by('-news_time')
    return news_list[:8]


def get_stock_comments(stock_id):
    stock=StockInfo.objects.get(stock_id=stock_id)
    return StockComment.objects.filter(stock_id=stock)
