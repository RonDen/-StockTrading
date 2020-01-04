from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import UserTable, StockInfo, OptionalStockTable, ForumTopic, ForumTopicBack, HistoryTradeTable
from django.core.exceptions import ObjectDoesNotExist


def goto_login(request):
    return render(request, 'login.html')


def mylogin(request):
    # 10030370820
    # 50342411
    if request.POST:
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        message = ''
        try:
            user = UserTable.objects.get(phone_number=phone_number)
            if user.password == password:
                request.session['user_name'] = user.user_name
                request.session['photo_url'] = user.photo_url
                request.session['user_id'] = user.user_id
                request.session['user_email'] = user.user_email
                request.session['account_num'] = user.account_num
                request.session['account_type'] = user.account_type
                request.session['account_balance'] = user.account_balance
                request.session['id_no'] = user.id_no

                return redirect("tradingSystem:index")
            else:
                message = "您的密码错误"
        except ObjectDoesNotExist:
            message = "用户不存在"
    return render(request, 'login.html', locals())


def index(request):

    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')


def register(request):
    return render(request, 'register.html')

def stockdetails(request):
    return render(request,'stock_details.html')

