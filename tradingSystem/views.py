from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from tradingSystem import models
from utils.getAstock import getAstock
import tushare as ts
from .models import UserTable, StockInfo, OptionalStockTable, ForumTopic, ForumTopicBack, HistoryTradeTable


def goto_login(request):
    return render(request, 'login.html')


def mylogin(request):
    if request.POST:
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        print(phone_number, password)
        return render(request, 'index.html')
        find = False
        data = {'find': '1'}
        if find:
            return JsonResponse(data)
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')


def register(request):
    return render(request, 'register.html')
def stockComments(request):
    return render(request,'stock_comments.html')
def stockDetails(request):
    return render(request,'stock_details.html')
def stockList(request):
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
        "stock":stockl
    }
    # print(type(queryset))
    return render(request,'stock_list.html',context)
