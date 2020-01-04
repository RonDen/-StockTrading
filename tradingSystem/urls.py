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
    path('stockdetails',views.stockdetails,name='stockdetails'),
    path('stock_info/<int:stock_id>/', views.stock_info, name='stock_info'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock_comment', views.stock_comment, name='stock_comment'),
    path('buy_in_stock', views.buy_in_stock, name='buy_in_stock'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('log_out', views.log_out, name='log_out'),
]


