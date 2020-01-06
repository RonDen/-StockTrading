from tradingSystem.models import StockInfo, UserTable,StockComment, CommentReply
from random import choice

dim_sentences = [
    'I would like to meet you to discuss the latest news about the arrival of the new theme. They say it is going to be one the best themes on the market.',
]


users = UserTable.objects.all()
stocks = StockInfo.objects.all()


cnt = 0
while cnt < 100:
    user = choice(users)
    stock = choice(stocks)
    title = '评论' + str(cnt)

    cnt += 1



