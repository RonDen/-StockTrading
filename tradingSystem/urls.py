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

    # 查看上市股票，股票交易，个人股票管理,获取实时股票信息
    path('stockdetails',views.stockdetails,name='stockdetails'),
    path('stock_info/<str:stock_id>/', views.stock_info, name='stock_info'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('buy_in_stock', views.buy_in_stock, name='buy_in_stock'),
    path('sold_stock',views.sold_stock,name= 'sold_stock'),
    path('get_real_quotes', views.get_real_quotes, name='get_real_quotes'),
    path('out/<str:stock_id>/', views.out, name='out'),
    path('sold_out_stock', views.sold_out_stock, name='out'),
    path('get_real_holdon', views.get_real_holdon, name='get_real_holdon'),
    #股票信息维护
    path('updateEveDayOC', views.updateEveDayOC, name='updateEveDayOC'),
    path('updateDayData', views.updateDayData, name='updateDayData'),
    path('updateTickData', views.updateTickData, name='updateTickData'),
    

    #股票评论
    path('add_stock_comment', views.add_stock_comment, name='add_stock_comment'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('log_out', views.log_out, name='log_out'),
    path('do_register', views.do_register, name='do_register'),
    path('deal_user_change', views.deal_user_change, name='deal_user_change'),
    path('add_stock_comment', views.add_stock_comment, name='add_stock_comment'),

    # 管理员视图与URL
    path('a', admin_view.adm_index, name='adm_index'),
    path('a/base', admin_view.adm_base, name='adm_base'),
    path('a/user', admin_view.adm_user, name='adm_user'),
    path('a/stock', admin_view.adm_stock, name='adm_stock'),
    path('a/trading', admin_view.adm_trading, name='adm_trading'),
    path('a/news', admin_view.adm_news, name='adm_news'),
    path('a/comments', admin_view.adm_comment, name='adm_comment'),
    path('adm_view_user/<str:phone_number>', admin_view.user_detail, name='adm_view_user'),
    path('adm_view_stock/<str:stock_id>', admin_view.adm_stock_info, name='adm_view_stock'),
    # 管理员冻结用户
    path('freeze_user', admin_view.freeze_user, name='freeze_user'),
    path('unfreeze_user', admin_view.unfreeze_user, name='unfreeze_user'),
    # 管理员删除用户
    path('delete_user', admin_view.delete_user, name='delete_user'),
    # 管理员修改用户信息
    path('change_user', admin_view.change_user, name='change_user'),
    # 管理员查看新闻详情
    path('adm_news_detail/<int:news_id>', admin_view.adm_news_detail, name='adm_news_detail'),
    # 管理员编辑新闻内容
    path('adm_edit_news', admin_view.adm_edit_news, name='adm_edit_news'),
    # 管理员新建新闻
    path('adm_add_news', admin_view.adm_add_news, name='adm_add_news'),
    # 管理员调用爬虫接口获取每天新闻
    path('spy_news', admin_view.spy_news, name='spy_news'),
    # 管理员删除新闻
    path('adm_delete_news/<int:news_id>', admin_view.adm_delete_news, name='adm_delete_news'),
    # 管理员查看评论详情
    path('adm_comment_detail/<int:comment_id>', admin_view.adm_comment_detail, name='adm_comment_detail'),
    # 管理员删除评论
    path('adm_delete_comment/<int:comment_id>', admin_view.adm_delete_comment, name='adm_delete_comment'),

    # 管理员删除交易记录
    path('adm_delete_trading/<int:trading_id>', admin_view.adm_delete_trading, name='adm_delete_trading'),

    path('update_img', views.update_img, name='update_img'),

    # 查看评论
    path('comment_detail/<int:comment_id>', views.comment_detail, name='comment_detail'),

    # 为评论添加回复
    path('add_reply', views.add_reply, name='add_reply'),

    path('view_user_profile/<int:phone_number>', views.view_user_profile, name='view_user_profile'),
    # 删除评论
    path('comment_delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('comment_list', views.comment_list, name='comment_list'),

    # 新闻路由
    path('news_detail/<int:news_id>', views.news_detail, name='news_detail'),
    path('change_news', views.change_news, name='change_news'),

    #维护每日股票信息
    path('uphold', views.uphold, name='uphold'),

]

