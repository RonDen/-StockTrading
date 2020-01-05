from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

import tushare as ts
import uuid
import os

from tradingSystem import models
from .models import UserTable, StockInfo, OptionalStockTable, ForumTopic, ForumTopicBack, HistoryTradeTable
from .utils import get_top10
from utils import getAstock
import numpy as np
from utils import getHistoryData
from config.createUser import gen_photo_url, banks


def goto_login(request):
    return render(request, 'login.html')


def mylogin(request):
    # 10030370820
    # 222222
    if request.POST:
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        message = ''
        try:
            adm = User.objects.get(username=phone_number)
            user_num = len(UserTable.objects.all())
            stock_num = len(StockInfo.objects.all())
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
                    request.session['user_name'] = user.user_name
                    request.session['online'] = True
                    request.session['photo_url'] = user.photo_url
                    request.session['user_id'] = user.user_id
                    request.session['user_email'] = user.user_email
                    request.session['account_num'] = user.account_num
                    request.session['account_type'] = user.account_type
                    request.session['account_balance'] = user.account_balance
                    request.session['id_no'] = user.id_no
                    request.session['phone_number'] = user.phone_number
                    return redirect("tradingSystem:index")
                else:
                    message = "您的密码错误"
            except ObjectDoesNotExist:
                message = "用户不存在"
    return render(request, 'login.html', locals())


def log_out(request):
    request.session.flush()
    return redirect('tradingSystem:goto_login')


def index(request):
    try:
        if request.session['phone_number']:
            top10stock = get_top10()
            context = {
                'top10stock': top10stock
            }
            return render(request, 'index.html', context)
        else:
            return redirect("tradingSystem:goto_login")
    except Exception:
        return redirect("tradingSystem:goto_login")


def user_profile(request):
    try:
        if request.session['phone_number']:
            context = {
                'banks': banks
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
    # print(ts.get_hist_data('600848'))

    choosenStock = models.StockInfo.objects.filter(stock_id = stock_id)
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
    # hold_vol = lhold_vol)
    # print(":asdad")
    # print(hisData)

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
    return render(request, 'stock_details.html',context)

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


def buy_in_stock(request,sid):

    return render(request, 'buy_in.html')
