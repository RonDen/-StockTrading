from .models import UserTable, StockInfo, OptionalStockTable, HistoryTradeTable, StockComment, CommentReply
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, JsonResponse, Http404
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from config.createUser import gen_photo_url, banks
from django.core.serializers import serialize
from django.contrib.auth.models import User
from django.http import JsonResponse
from datetime import date, datetime
from django.shortcuts import render
from django.core.paginator import Paginator
from utils import getHistoryData
from .utils import get_top10
import tushare as ts
import uuid
import os

from tradingSystem import models
from .models import UserTable, StockInfo, OptionalStockTable, HistoryTradeTable, StockComment, CommentReply, News
from .utils import get_top10, get_news
from utils import getAstock, cram_news
import numpy as np
from utils import getHistoryData
from config.createUser import gen_photo_url, banks
from utils import getRtQuotes
from tradingSystem import models
import pymysql
import tushare as ts
import numpy as np
import time
import uuid
import os


def goto_login(request):
    return render(request, 'login.html')


def mylogin(request):
    # 10030370820
    # 222222
    if request.POST:
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        print(phone_number)
        print(password)
        message = ''
        try:
            adm = User.objects.get(username=phone_number)
            login(request, adm)
            user_num = UserTable.objects.count()
            stock_num = StockInfo.objects.count()
            request.session['user_name'] = phone_number
            request.session['username'] = adm.username
            request.session['online'] = True
            request.session['user_num'] = user_num
            request.session['stock_num'] = stock_num
            request.session['photo_url'] = '../static/img/head.jpg'

            return redirect('tradingSystem:adm_index')
        except ObjectDoesNotExist:
            try:
                user = UserTable.objects.get(phone_number=phone_number)
                if user.password == password:
                    login(request, user)
                    request.session['user_name'] = user.user_name
                    request.session['photo_url'] = user.photo_url
                    request.session['user_id'] = user.user_id
                    request.session['user_email'] = user.user_email
                    request.session['account_num'] = user.account_num
                    request.session['account_type'] = user.account_type
                    request.session['account_balance'] = user.account_balance
                    request.session['id_no'] = user.id_no
                    request.session['phone_number'] = user.phone_number
                    return redirect('tradingSystem:index')
                else:
                    message = "您的密码错误"
            except ObjectDoesNotExist:
                message = "用户不存在"
    return render(request, 'login.html', locals())


def log_out(request):
    logout(request)
    request.session.flush()
    return redirect('tradingSystem:goto_login')


# 19959008351 48494877


def index(request):
    try:
        if request.session['phone_number']:
            phone_number = request.session['phone_number']
            user = UserTable.objects.get(phone_number=phone_number)
            comments = StockComment.objects.filter(user_id=user)
            all_news = News.objects.all()
            page = request.GET.get('page', 1)
            paginator = Paginator(all_news, 8)
            if page > paginator.num_pages:
                page = 1
            news_list = paginator.get_page(page)
            # news_list = get_news()
            top10stock = get_top10()
            context = {
                'top10stock': top10stock,
                'comments': comments,
                'user': user,
                'news_list': news_list,
                'page': page
            }
            return render(request, 'index.html', context)
        else:
            return redirect("tradingSystem:goto_login")
    except Exception:
        return redirect("tradingSystem:goto_login")


def change_news(request):
    news_list = cram_news.gen_news()[:8]
    return JsonResponse({"news_list": news_list})


def user_profile(request):
    try:
        if request.session['phone_number']:
            phone_number = request.session['phone_number']
            user = UserTable.objects.get(phone_number=phone_number)
            context = {
                'banks': banks,
                'user': user
            }
            return render(request, 'tradingSystem/user_profile.html', context)
        else:
            return redirect("tradingSystem:goto_login")
    except Exception:
        return redirect("tradingSystem:goto_login")


def deal_user_change(request):
    message = ""
    try:
        if request.POST:
            user_id = request.POST['user_id']
            user_name = request.POST['user_name']
            phone_number = request.POST['phone_number']
            user_sex = request.POST['user_sex']
            id_no = request.POST['id_no']
            user_email = request.POST['user_email']
            password = request.POST['password']
            conf_password = request.POST['conf_password']
            account_type = request.POST['account_type']
            account_number = request.POST['account_num']
            if conf_password != password:
                message = "确认密码不符"
            else:
                try:
                    user = UserTable.objects.get(user_id=user_id)
                    user.phone_number = phone_number
                    user.user_sex = user_sex
                    user.user_name = user_name
                    user.user_email = user_email
                    user.password = password
                    user.account_type = account_type
                    user.account_num = account_number
                    user.id_no = id_no
                    user.save()
                except Exception:
                    message = "修改信息失败，请仔细检查，或稍后重试"
    except Exception:
        message = "您的信息有误，请仔细检查"
    context = {
        'message': message,
        'banks': banks
    }
    return render(request, "tradingSystem/user_profile.html", context)


def stock_info(request, stock_id):
    print("aasdasdasd")
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()
    # print(ts.get_hist_data('600848'))

    # 获取当天交易数据
    f = ""
    tick_datax = ""
    tick_datay = ""
    tick_name = ""
    tick_data = ""
    print(stock_id)
    f = getRtQuotes.getworkday()
    # f, tick_datax, tick_datay = getRtQuotes.getRtQuotes(stock_id)



    print(tick_datay)
    # 获取当天交易数据
    print("seekroung")

    # 伪造数据接口
    # f = 1
    # tick_data = ""
    # df = ts.get_tick_data("000001", date="2020-01-03", src='tt')
    # print(df)
    # tick_data  = np.array(df)
    # tick_datax = tick_data[:, [0]]
    # tick_datay = tick_data[:, [1]]
    # tick_datax = tick_datax.reshape(-1)
    # tick_datay = tick_datay.reshape(-1)
    # tick_datax = tick_datax.tolist()
    # tick_datay = tick_datay.tolist()

    choosenStock = models.StockInfo.objects.filter(stock_id=stock_id)

    hisData = []
    hold_vol = ""

    if (choosenStock[0].stock_type == "上证"):
        sql = "SELECT * FROM `%s`"

        seaname = stock_id + "_"+"SH"
        # print(seaname)
        cursor.execute(sql,[seaname])
        hisData = cursor.fetchall()
        hisData = np.array(hisData)
        hisData = hisData.tolist()
        hold_vol = getAstock.getAstock(stock_id + ".SH")
        #抓取每日实时数据，4分钟一个时刻
        if(f):
            f = 1
            tick_name = "dailyticks"+"_"+seaname
            cursor.execute(sql,[tick_name])
            tick_data = cursor.fetchall()
            tick_data = np.array(tick_data)
            print(tick_data)
            print(type(tick_data))
            print("suck")
            tick_datax = tick_data[:,[0]]
            tick_datay = tick_data[:, [1]]
            print("fuck",tick_datax)
            print(type(tick_datax))
            tick_datax = tick_datax.reshape(-1)
            tick_datay = tick_datay.reshape(-1)
            tick_datax = tick_datax.tolist()
            tick_datay = tick_datay.tolist()
        else:
            f = 0
    else:
        sql = "SELECT * FROM `%s`"
        seaname = stock_id + "_"+"SZ"
        # print(seaname)
        cursor.execute(sql,[seaname])
        hisData = cursor.fetchall()
        hisData = np.array(hisData)
        hisData = hisData.tolist()
        # print(hisData)
        if(f):
            f = 1
            tick_name = "dailyticks"+"_"+seaname
            cursor.execute(sql,[tick_name])
            tick_data = cursor.fetchall()
            tick_data = np.array(tick_data)
            print(tick_data)
            print(type(tick_data))
            print("suckdirc")
            tick_datax = tick_data[:,[0]]
            tick_datay = tick_data[:, [1]]
            tick_datax = tick_datax.reshape(-1)
            tick_datay = tick_datay.reshape(-1)
            tick_datax = tick_datax.tolist()
            tick_datay = tick_datay.tolist()
            print("fuck",tick_datax)
            print(type(tick_datax))
        else:
            f = 0
        hold_vol = getAstock.getAstock(stock_id + ".SZ")
    cursor.close()
    conn.close()
        # hisData = getHistoryData.getHistoryData(stock_id + ".SZ")
    # hold_vol = lhold_vol)
    # print(":asdad")
    # print(hisData)

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
        "f": f,
        "tick_datax": tick_datax,
        "tick_datay": tick_datay
    }
    return render(request, 'stock_details.html', context)


def base(request):
    return render(request, 'base.html')


def register(request):
    return render(request, 'register.html')


def do_register(request):
    user_name = request.GET['user_name']
    phone_number = request.GET['phone_number']
    user_sex = request.GET['user_sex']
    id_no = request.GET['id_no']
    user_email = request.GET['user_email']
    password = request.GET['password']
    account_type = request.GET['account_type']
    account_number = request.GET['account_number']
    photo_url = gen_photo_url()
    message = ""
    try:
        user = UserTable.objects.create(
            user_name=user_name,
            user_email=user_email,
            user_sex=user_sex,
            user_id=str(uuid.uuid4())[:8],
            id_no=id_no,
            password=password,
            account_type=account_type,
            account_num=account_number,
            phone_number=phone_number,
            account_balance=0,
            photo_url=photo_url
        )
        user.save()
        print("success register user")
        print(user)
    except Exception:
        print(Exception)
        message = "注册失败，请检查或稍后再试！"
        return render(request, 'register.html', locals())
    return redirect('tradingSystem:goto_login')


def stockdetails(request):
    return render(request, 'stock_details.html')


def stock_list(request):
    # aStockData = getAstock()

    # lis=[]
    # for  index,row in aStockData.iterrows():
    #     lis.append(row)
    # print(lis[0])
    # queryset = []
    # for i in lis:
    #     queryset.append(models.StockInfo(stock_id = i[1],stock_name = i[2],issuance_time=i[6],closing_price_y=0,open_price_t=0,stock_type="",block=i[5],change_extent=0))
    # models.StockInfo.objects.bulk_create(queryset)

    stockl = models.StockInfo.objects.all()
    # all_years = [y['teaching__mcno__year'] for y in CourseScore.objects.values("teaching__mcno__year").distinct()]
    # print(queryset)
    context = {
        "stock": stockl
    }
    # print(type(queryset))
    return render(request, 'stock_list.html', context)


def stock_comment(request):
    return render(request, 'stock_comments.html')


def buy_in_stock(request):
    print("ss")
    if request.is_ajax():
        if request.method == 'GET':
            price = float(request.GET.get("price"))
            shares = int(request.GET.get("shares"))
            s_id = request.GET.get("s_id")
            fare = price * shares
            print(price)
            print(shares)
            print(fare)
            print(request.session['phone_number'])
            buyer = models.UserTable.objects.filter(phone_number=request.session['phone_number'])
            print("asdasdads",buyer[0].phone_number,request.session['phone_number'])
            stock_in = models.StockInfo.objects.filter(stock_id=s_id)
            money = 0
            if (buyer[0].account_balance >= fare and buyer[0].freeze == False and buyer[0].account_opened == True):
                money = 1
                models.UserTable.objects.filter(phone_number=request.session['phone_number']).update(
                    account_balance=buyer[0].account_balance - fare)
                option_stock  = models.OptionalStockTable.objects.filter(user_id=buyer[0],stock_id = stock_in[0])
                if(len(option_stock)==0):
                    models.OptionalStockTable.objects.create(
                        user_id=buyer[0],
                        stock_id=stock_in[0],
                        num_of_shares = shares
                    )
                else:
                    models.OptionalStockTable.objects.filter(user_id=buyer[0],stock_id = stock_in[0]).update(
                        num_of_shares = option_stock[0].num_of_shares+shares
                    )
                models.HistoryTradeTable.objects.create(
                    user_id=buyer[0],
                    stock_id=stock_in[0],
                    trade_price=price,
                    trade_shares=shares,
                    trade_time=time.strftime('%Y-%m-%d', time.localtime(time.time()))
                )
                return JsonResponse({"flag": 1,"money":money})
            else:
                if(buyer[0].account_balance >= fare):
                    money = 1
                else:
                    money = 0

                return JsonResponse({"flag": 0,"money":money})


def comment_detail(request, comment_id):
    user = UserTable.objects.get(phone_number=request.session['phone_number'])
    comment = StockComment.objects.get(id=comment_id)
    replys = CommentReply.objects.filter(comment=comment)
    context = {
        'comment': comment,
        'replys': replys,
        'user': user
    }
    return render(request, 'comment_detail.html', context)


def get_real_quotes(request):
    if request.is_ajax():
        if request.method == 'GET':
            print("aa")
            sym = request.GET.get("id")
            print(sym)
            df = ts.get_realtime_quotes(symbols=sym)
            df = df[['code', 'name', 'price', 'bid', 'ask', 'volume', 'amount', 'time']]
            print(df)
            res = np.array(df)
            res = res[:, [2]]
            print(res)
            print(res[0][0])
            print(type(res[0][0]))
            return JsonResponse({"price": res[0][0]})


# 点击查看其他用户的信息
def view_user_profile(request, phone_number):
    user = UserTable.objects.get(phone_number=phone_number)
    context = {
        'user': user
    }
    return render(request, 'view_user_profile.html', context)


def news_detail(request, news_id):
    user = UserTable.objects.get(phone_number=request.session['phone_number'])

    news = News.objects.get(id=news_id)
    nx_news = news_id + 1
    pre_news = news_id - 1

    while not News.objects.filter(id=nx_news).exists():
        nx_news += 1
    while not News.objects.filter(id=pre_news).exists():
        pre_news -= 1

    context = {
        'user': user,
        'news': news,
        'nx_news': nx_news,
        'pre_news': pre_news
    }
    return render(request, 'news_detail.html', context)


def update_img(request):
    if request.method == 'POST':
        user = UserTable.objects.get(phone_number=request.session['phone_number'])
        my_file = request.FILES.get('teamFile', None)
        message = ""
        filename = os.path.splitext(my_file._name)[1]
        save_name = 'static/img/' + user.phone_number + filename
        code = 1000
        if my_file:
            with open(save_name, 'wb') as file:
                file.write(my_file.read())
            code = 0
            user.photo_url = '../' + save_name
            user.save()
            print("修改成功呢")
        else:
            filename = ''
            message = "修改失败，请稍后再试！"
        context = {
            'message': message,
            'banks': banks,
            "code": code, "msg": {"url": '../static/img/%s' % (filename), 'filename': my_file._name}
        }
        return JsonResponse(context)


def comment_list(request):
    try:
        user = UserTable.objects.get(phone_number=request.session['phone_number'])
        comments = StockComment.objects.filter(user_id=user)
        results = []
        for comment in comments:
            results.append({
                'stock_id': comment.stock_id.stock_id,
                'comment_id': comment.id,
                'stock_name': comment.stock_id.stock_name,
                'title': comment.title,
                'content': comment.content,
                'comment_time': comment.comment_time,
                'reply_nums': CommentReply.objects.filter(comment=comment).count(),
            })
        context = {
            'results': results,
            'user': user,
        }
        return render(request, 'comment_list.html', context)
    except:
        return redirect('tradingSystem:mylogin')


def comment_delete(request, comment_id):
    pass
