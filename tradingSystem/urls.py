from django.urls import path
from django.conf.urls import include
from . import views
from . import admin_view

app_name = 'tradingSystem'

urlpatterns = [
    path('', views.goto_login, name='goto_login'),
    path('mylogin', views.mylogin, name='mylogin'),
    path('base', views.base, name='base'),
    path('register', views.register, name='register'),
    path('index', views.index, name='index'),
    path('stockdetails',views.stockdetails,name='stockdetails'),
    path('stock_info/<str:stock_id>/', views.stock_info, name='stock_info'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock_comment', views.stock_comment, name='stock_comment'),
    path('buy_in_stock', views.buy_in_stock, name='buy_in_stock'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('log_out', views.log_out, name='log_out'),
    path('do_register', views.do_register, name='do_register'),
    path('deal_user_change', views.deal_user_change, name='deal_user_change'),
    path('get_real_quotes',views.get_real_quotes,name = 'get_real_quotes'),

    # 管理员视图与URL
    path('a', admin_view.adm_index, name='adm_index'),
    path('a/base', admin_view.adm_base, name='adm_base'),
    path('a/user', admin_view.adm_user, name='adm_user'),
    path('a/stock', admin_view.adm_stock, name='adm_stock'),
    path('a/trading', admin_view.adm_trading, name='adm_trading'),
    path('a/news', admin_view.adm_news, name='adm_news'),
    path('a/comments', admin_view.adm_comment, name='adm_comment'),
    path('adm_view_user/<int:phone_number>', admin_view.user_detail, name='adm_view_user'),
    path('adm_view_stock/<str:stock_id>', admin_view.adm_stock_info, name='adm_view_stock'),

    path('update_img', views.update_img, name='update_img'),

    # 查看评论
    path('comment_detail/<int:comment_id>', views.comment_detail, name='comment_detail'),
    path('view_user_profile/<int:phone_number>', views.view_user_profile, name='view_user_profile'),
    # 删除评论
    path('comment_delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('comment_list', views.comment_list, name='comment_list'),

    # 新闻路由
    path('news_detail/<int:news_id>', views.news_detail, name='news_detail'),
    path('change_news', views.change_news, name='change_news'),
]

