from django.shortcuts import render
from .models import UserTable, StockInfo, HistoryTradeTable,StockComment, CommentReply
from .utils import get_top10, get_news
from utils import getAstock, getHistoryData


def adm_base(request):
    return render(request, 'adm_base.html')


def adm_index(request):
    top10stock = get_top10
    user_num = UserTable.objects.count()
    stock_num = StockInfo.objects.count()
    comment_num = StockComment.objects.count()
    trading_num = HistoryTradeTable.objects.count()
    news_list = get_news()
    context = {
        'top10stock': top10stock,
        'user_num': user_num,
        'stock_num': stock_num,
        'comment_num': comment_num,
        'trading_num': trading_num,
        'news_list': news_list
    }
    return render(request, 'adm_index.html', context)


def adm_user(request):
    all_user = UserTable.objects.all()
    context = {
        'all_user': all_user,
    }
    return render(request, "adm_user.html", context)


def user_detail(request, phone_number):
    user = UserTable.objects.get(phone_number=phone_number)
    context = {
        'user': user
    }
    return render(request, 'adm_user_detail.html', context)


def adm_stock(request):
    all_stock = StockInfo.objects.all()[:10]
    context = {
        'all_stock': all_stock
    }
    return render(request, "adm_stock.html", context)


def adm_stock_info(request, stock_id):
    # print(ts.get_hist_data('600848'))
    choosenStock = StockInfo.objects.filter(stock_id=stock_id)
    print(choosenStock)
    print(choosenStock[0].stock_name)
    print(choosenStock[0].block)
    hisData = []
    hold_vol = ""

    if(choosenStock[0].stock_type=="上证"):
        hold_vol = getAstock.getAstock(stock_id+".SH")
        hisData = getHistoryData.getHistoryData(stock_id+".SH")
    else:
        hold_vol = getAstock.getAstock(stock_id+".SZ")
        hisData = getHistoryData.getHistoryData(stock_id+".SZ")

    context={
        "sid":choosenStock[0].stock_id,
        "sname":choosenStock[0].stock_name,
        "issuance_time":choosenStock[0].issuance_time,
        "closing_price_y":choosenStock[0].closing_price_y,
        "open_price_t":choosenStock[0].open_price_t,
        "stock_type":choosenStock[0].stock_type,
        "block":choosenStock[0].block,
        "change_extent":choosenStock[0].change_extent,
        "hold_vold":hold_vol,
        "hisData":hisData
    }
    return render(request, 'adm_stock_info.html',context)


def adm_trading(request):
    all_trading = HistoryTradeTable.objects.all()
    context = {
        'all_trading': all_trading,
    }
    return render(request, "adm_trading.html", context)


def adm_news(request):
    return render(request, "adm_news.html")


def adm_comment(request):
    return render(request, "adm_comment.html")














