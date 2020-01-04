import tushare as ts
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from tradingSystem import models


my_token = '17649607a4e92be1fe38fb52b2ff2e044ac6301f665e98b278ab14a7'


def main():
    # print(ts.get_today_all())
    df = ts.get_realtime_quotes('000581') #Single stock symbol
    # data = pro.stock_basic(exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_date')
    # data = pro.query('stock_basic', exchange='SSE', list_status='L', fileds='ts_code,symbol,name,area,industry,list_data')
    # lis=[]
    # for  index,row in data.iterrows():
    #     lis.append(row)
    # print(lis[0])
    
    print(df)
    
        
        


if __name__ == '__main__':
    main()


