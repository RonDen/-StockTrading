from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


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
    phone_number = models.CharField(max_length=45, primary_key=True)
    # 用户邮箱
    user_email = models.EmailField()
    # 用户头像路径
    photo_url = models.CharField(max_length=45)
    # 银行卡号
    account_num = models.CharField(max_length=45)
    # 银行卡类型
    account_type = models.CharField(max_length=45)
    # 账户余额
    account_balance = models.FloatField(null=True)
    # 是否冻结
    freeze = models.BooleanField(default=False)
    # 是否成功开户
    account_opened = models.BooleanField(default=True)
    # last_login
    last_login = models.CharField(max_length=45,null=True)

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
    closing_price_y = models.FloatField(null=True)
    # 股票今日开盘价
    open_price_t = models.FloatField(null=True)
    # 股票类型，上证/深证
    stock_type = models.CharField(max_length=15, null=True)
    # 股票所在版块，科创、金融。。
    block = models.CharField(max_length=45, null=True)
    # 涨跌幅，用于筛选牛股推荐
    change_extent = models.FloatField(null=True)

    def __str__(self):
        return '-'.join([self.stock_id, self.stock_name])

    class Meta:
        db_table = 'stock_info'


class HistoryTradeTable(models.Model):
    # 历史交易记录表
    # 交易ID，PK
    user_id = models.ForeignKey(to=UserTable, on_delete=models.CASCADE)
    # 交易股票ID，FK
    stock_id = models.ForeignKey(to=StockInfo, on_delete=models.CASCADE)
    # 交易价格
    trade_price = models.FloatField()
    #成交股数
    trade_shares = models.IntegerField()
    # 成交时间
    trade_time = models.CharField(max_length=40)

    def __str__(self):
        return '-'.join([ self.user_id.phone_number, self.stock_id])

    class Meta:
        db_table = 'history_trade_table'


class OptionalStockTable(models.Model):
    # 自选股票表
    user_id = models.ForeignKey(to=UserTable, on_delete=models.CASCADE)
    stock_id = models.ForeignKey(to=StockInfo, on_delete=models.CASCADE)
    num_of_shares = models.IntegerField(null=True)

    class Meta:
        db_table = 'optional_stock_table'
        unique_together = (
            'user_id', 'stock_id'
        )


class News(models.Model):
    # 新闻标题
    title = models.CharField(max_length=100)
    # 新闻所在URL
    url = models.URLField(null=True)
    # 新闻内容
    content = models.TextField()
    # 新闻阅读数
    read = models.IntegerField(null=True, default=0)
    # 发生时间
    news_time = models.DateField(auto_now=True)

    def __str__(self):
        return '-'.join([str(self.id), self.title])

    class Meta:
        db_table = 'news'
        ordering = ['news_time']


class StockComment(models.Model):
    # 股票标题
    title = models.CharField(max_length=50)
    # 股票内容
    content = models.TextField("股票内容")
    # 发表时间
    comment_time = models.DateTimeField(auto_now=True)
    # 发起用户
    user_id = models.ForeignKey(to=UserTable, on_delete=models.CASCADE)
    # 关联股票
    stock_id = models.ForeignKey(to=StockInfo, on_delete=models.CASCADE)

    def __str__(self):
        return '-'.join([str(self.id), self.title])

    class Meta:
        db_table = 'stock_comment'
        ordering = ['comment_time']


class CommentReply(models.Model):
    # 发起用户
    user_id = models.ForeignKey(to=UserTable, on_delete=models.CASCADE)
    # 所回复的评论
    comment = models.ForeignKey(to=StockComment, on_delete=models.CASCADE)
    reply = models.ForeignKey(to='self', null=True, blank=True, on_delete=models.CASCADE)
    # 回复内容
    content = models.TextField()
    reply_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '-'.join([str(self.id)])

    class Meta:
        db_table = 'comment_reply'
        ordering = ['reply_time']


class Comment(MPTTModel):
    stock_id = models.ForeignKey(
        StockInfo,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user_id = models.ForeignKey(
        UserTable,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    # 新增，mptt树形结构
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    # 新增，记录二级评论回复给谁, str
    reply_to = models.ForeignKey(
        UserTable,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replyers'
    )

    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    # 替换 Meta 为 MPTTMeta
    # class Meta:
    #     ordering = ('created',)

    def __str__(self):
        return self.body[:20]

    class MPTTMeta:
        order_insertion_by = ['created']

