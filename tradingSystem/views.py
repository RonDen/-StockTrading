from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404


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
    return render(request,'stock_list.html')
