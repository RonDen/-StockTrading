from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import UserTable, StockInfo, OptionalStockTable, ForumTopic, ForumTopicBack, HistoryTradeTable


def goto_login(request):
    return render(request, 'login.html')


def mylogin(request):
    return redirect('tradingSystem:goto_login')


def base(request):
    return render(request, 'base.html')



