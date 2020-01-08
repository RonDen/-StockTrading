from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import UserTable, StockInfo, HistoryTradeTable, StockComment, CommentReply, News
from .utils import get_top10, get_news, get_buy_in_out
from utils import getAstock, getHistoryData, cram_news


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
    buy_in, buy_out = get_buy_in_out(phone_number)

    context = {
        'user': user,
        'buy_in': buy_in,
        'buy_out': buy_out
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

    if (choosenStock[0].stock_type == "上证"):
        hold_vol = getAstock.getAstock(stock_id + ".SH")
        hisData = getHistoryData.getHistoryData(stock_id + ".SH")
    else:
        hold_vol = getAstock.getAstock(stock_id + ".SZ")
        hisData = getHistoryData.getHistoryData(stock_id + ".SZ")
    stock = StockInfo.objects.get(stock_id=stock_id)
    comments = StockComment.objects.filter(stock_id=stock)
    context = {
        "sid": choosenStock[0].stock_id,
        "sname": choosenStock[0].stock_name,
        "issuance_time": choosenStock[0].issuance_time,
        "closing_price_y": choosenStock[0].closing_price_y,
        "open_price_t": choosenStock[0].open_price_t,
        "stock_type": choosenStock[0].stock_type,
        "block": choosenStock[0].block,
        "change_extent": choosenStock[0].change_extent,
        "hold_vold": hold_vol,
        "hisData": hisData,
        "comments": comments
    }
    return render(request, 'adm_stock_info.html', context)


def adm_trading(request):
    all_trading = HistoryTradeTable.objects.all()
    context = {
        'all_trading': all_trading,
    }
    # print(all_trading[0].)

    return render(request, "adm_trading.html", context)


def adm_delete_trading(request, trading_id):
    trading = HistoryTradeTable.objects.get(id=trading_id)
    trading.delete()
    return redirect('tradingSystem:adm_trading')


def adm_news(request):
    all_news = News.objects.all()
    results = []
    for news in all_news:
        results.append({
            'news_title': news.title[:30],
            'content': news.content[:30],
            'news_id': news.id,
            'read': news.read,
            'news_time': str(news.news_time)
        })
    context = {
        'results': results,
    }
    return render(request, "adm_news.html", context)


def spy_news(request):
    news_list = cram_news.gen_news()
    for news in news_list:
        title = news['title']
        content = news['content']
        n = News.objects.create(
            title=title,
            content=content,
            read=0
        )
        n.save()
    return redirect('tradingSystem:adm_news')


def adm_news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    context = {
        'news': news,
    }
    return render(request, "adm_news_detail.html", context)


def adm_add_news(request):
    if request.POST:
        title = request.POST.get('news_title')
        content = request.POST.get('news_content')
        news = News.objects.create(
            title=title,
            content=content,
            read=0
        )
        news.save()
    return redirect('tradingSystem:adm_news')


def adm_delete_news(request, news_id):
    news = News.objects.get(id=news_id)
    print(news, "被删除了")
    news.delete()
    return redirect('tradingSystem:adm_news')


def adm_edit_news(request):
    if request.POST:
        news_id = request.POST.get('news_id')
        news_title = request.POST.get('news_title')
        news_content = request.POST.get('news_content')
        news = News.objects.get(id=news_id)
        news.title = news_title
        news.content = news_content
        news.save()
        return redirect('tradingSystem:adm_news_detail', news_id=int(news_id))
    return redirect('tradingSystem:adm_news')


def adm_comment(request):
    comments = StockComment.objects.all()
    results = []
    for comment in comments:
        results.append({
            'stock_id': comment.stock_id.stock_id,
            'comment_id': comment.id,
            'phone_number': comment.user_id.phone_number,
            'stock_name': comment.stock_id.stock_name,
            'title': comment.title,
            'content': comment.content[:30],
            'comment_time': comment.comment_time,
            'reply_nums': CommentReply.objects.filter(comment=comment).count(),
        })
    context = {
        'results': results,
    }
    return render(request, "adm_comment.html", context)


def adm_comment_detail(request, comment_id):
    comment = StockComment.objects.get(id=comment_id)
    replys = CommentReply.objects.filter(comment=comment)
    context = {
        'comment': comment,
        'replys': replys,
    }
    return render(request, 'adm_comment_detail.html', context)


def adm_delete_comment(request, comment_id):
    comment = StockComment.objects.get(id=comment_id)
    comment.delete()
    return redirect('tradingSystem:adm_comment')


def freeze_user(request):
    phone_number = request.GET.get('phone_number')

    user = UserTable.objects.get(phone_number=phone_number)
    user.freeze = True
    user.save()
    return JsonResponse({})


def unfreeze_user(request):
    phone_number = request.GET.get('phone_number')

    user = UserTable.objects.get(phone_number=phone_number)
    user.freeze = False
    user.save()
    return JsonResponse({})


def delete_user(request):
    phone_number = request.GET.get('phone_number')
    user = UserTable.objects.get(phone_number=phone_number)
    user.delete()
    return JsonResponse({})


def change_user(request):
    if request.POST:
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        phone_number = request.POST['phone_number']
        user_sex = request.POST['user_sex']
        id_no = request.POST['id_no']
        user_email = request.POST['user_email']
        account_type = request.POST['account_type']
        account_number = request.POST['account_num']

        user = UserTable.objects.get(user_id=user_id)
        user.phone_number = phone_number
        user.user_sex = user_sex
        user.user_name = user_name
        user.user_email = user_email
        user.account_type = account_type
        user.account_num = account_number
        user.id_no = id_no
        user.save()
    return redirect('tradingSystem:adm_user')
