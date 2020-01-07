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
    comment = StockComment.objects.create(
        title=title,
        content=choice(dim_sentences),
        user_id=user,
        stock_id=stock,
    )
    cnt += 1

phone_number = '10071539640'
user = UserTable.objects.get(phone_number=10071539640)

comment = StockComment.objects.create(
    title='你好',
    content='今天天气真好',
    user_id=user,
    stock_id=choice(stocks)
)
comment.save()


for user in UserTable.objects.all():
    comment = StockComment.objects.create(
        title='你好',
        content='今天天气真好',
        user_id=user,
        stock_id=choice(stocks)
    )
    comment.save()


for comment in StockComment.objects.all():
    tao_ha = ['您说的真对', '您说的对', '您说的也对', "哈哈哈", "赶快买", "卖了房也要买", "小心被割韭菜"]
    for ha in tao_ha:
        reply = CommentReply.objects.create(
            user_id=choice(users),
            comment=comment,
            content=ha
        )
        reply.save()

for i in range(4, 9):
    stock_id = '00000' + str(i)
    stock = StockInfo.objects.get(stock_id=stock_id)
    tao_ha = ['您说的真对', '您说的对', '您说的也对', "哈哈哈", "赶快买", "卖了房也要买", "小心被割韭菜"]
    for hua in tao_ha:
        comment = StockComment.objects.create(
            stock_id=stock,
            user_id=choice(users),
            title=hua,
            content=','.join([choice(tao_ha), choice(tao_ha), choice(tao_ha), choice(tao_ha), choice(tao_ha)])
        )
        comment.save()
