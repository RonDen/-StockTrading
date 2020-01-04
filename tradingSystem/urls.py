from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'tradingSystem'

urlpatterns = [
    path('', views.goto_login, name='goto_login'),
    path('mylogin', views.mylogin, name='mylogin'),
    path('base', views.base, name='base'),
    path('register', views.register, name='register'),
    path('index', views.index, name='index'),
    path('stockdetails',views.stockDetails,name='stockdetails'),
    path('stockcomments', views.stockComments, name='stockcomments'),
    path('stockList', views.stockList, name='stockList'),
]


