from django.db import models


class UserTable(models.Model):
    # 用户信息表
    # 用户ID，
    user_id = models.CharField(max_length=12)
    # 身份证号码
    id_no = models.CharField(max_length=18)
    # 用户名，用于显示和评论
    user_name = models.CharField(max_length=45)
    # 用户密码
    password = models.CharField(max_length=45)
    # 用户性别
    user_sex = models.CharField(max_length=5)
    # 用户电话号码，用于注册，开户，联系，PK
    phone_number = models.CharField(max_length=45,primary_key=True)
    # 用户邮箱
    user_email = models.EmailField()
    # 用户头像路径
    photo_url = models.CharField(max_length=45)
    # 银行卡号
    account_num = models.CharField(max_length=45)
    # 银行卡类型
    account_type = models.CharField(max_length=45)
    # 银行卡余额
    account_balance = models.FloatField()

    def __str__(self):
        return '-'.join([self.user_name, self.phone_number])

    class Meta:
        db_table = 'user_table'


class StockInfo(models.Model):
    # 股票信息表，记录股票系统中的股票信息
    # 股票ID，固定6位，PK
    stock_id = models.CharField(max_length=6, primary_key=True)
    # 股票名称
    stock_name = models.CharField(max_length=45)
    # 股票发行时间
    issuance_time = models.CharField(max_length=45)
    # 股票昨日收盘价
    closing_price_y = models.FloatField()
    # 股票今日开盘价
    open_price_t = models.FloatField()
    # 股票今日收盘价
    closing_price_n = models.FloatField()
    # 股票类型，上证/深证
    stock_type = models.CharField(max_length=15)
    # 股票所在版块，科创、金融。。
    block = models.CharField(max_length=45)
    # 涨跌幅，用于筛选牛股推荐
    change_extent = models.FloatField()

    def __str__(self):
        return '-'.join([self.stock_id, self.stock_name])

    class Meta:
        db_table = 'stock_info'


class HistoryTradeTable(models.Model):
    # 历史交易记录表
    # 交易ID，PK
    trade_id = models.CharField(max_length=20, primary_key=True)
    # 交易用户ID，FK
    user_id = models.ForeignKey(to=UserTable, on_delete=models.CASCADE)
    # 交易股票ID，FK
    stock_id = models.ForeignKey(to=StockInfo, on_delete=models.CASCADE)
    # 交易价格
    trade_price = models.FloatField()
    # 成交时间
    trade_time = models.CharField(max_length=40)

    def __str__(self):
        return '-'.join([self.trade_id, self.user_id.phone_number, self.stock_id])

    class Meta:
        db_table = 'history_trade_table'


class OptionalStockTable(models.Model):
    # 自选股票表
    user_id = models.ForeignKey(to=UserTable, on_delete=models.CASCADE)
    stock_id = models.ForeignKey(to=StockInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'optional_stock_table'
        unique_together = (
            'user_id', 'stock_id'
        )


class ForumTopic(models.Model):
    # 股吧帖子表
    # 帖子标题
    post_title = models.CharField(max_length=45)
    # 帖子ID
    post_id = models.IntegerField(auto_created=True)
    # 帖子内容，PK
    post_text = models.CharField(max_length=100, primary_key=True)
    # 帖子发表时间，前端JS获取时间，后端存储字符串
    post_time = models.CharField(max_length=100)
    # 帖子发起用户，FK
    user_id = models.ForeignKey(to=UserTable, on_delete=models.CASCADE)
    # 帖子阅读数量
    post_read = models.CharField(max_length=100)
    # 帖子涉及股票
    stock_id = models.ForeignKey(to=StockInfo,on_delete=models.CASCADE)
    # 股票评论
    stock_comment = models.IntegerField(max_length=6)

    def __str__(self):
        return '-'.join([str(self.post_id), self.post_title])

    class Meta:
        db_table = 'forum_topic'


class ForumTopicBack(models.Model):
    # 论坛帖子回复表
    reply_id = models.CharField(max_length=6, primary_key=True)
    # 帖子ID，FK
    post_id = models.ForeignKey(to=ForumTopic, on_delete=models.CASCADE)
    # 用户名，发起回复的用户的姓名，在前端获得
    user_name = models.CharField(max_length=20)
    # 用户回复时间，在前端获得
    reply_time = models.CharField(max_length=40)
    # 用户回复的内容
    reply_Text = models.CharField(max_length=100)

    def __str__(self):
        return "-".join([self.reply_id, self.reply_Text])

    class Meta:
        db_table = 'forum_topic_back'




