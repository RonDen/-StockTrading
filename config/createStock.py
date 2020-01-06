from tradingSystem.models import StockInfo
from random import randint, choice
from hashlib import sha256


def gen_issuance_time():
    return '/'.join([str(randint(1990, 2020)), str(randint(1,12)), str(randint(1, 28))])


def change_value():
    cnt = 0
    for s in StockInfo.objects.all():
        closing_price_y = randint(1, 300)
        extend = randint(-100, 200)
        open_price_t = closing_price_y + extend
        stock_type = choice(['上证', '深圳'])
        try:
            s.issuance_time = gen_issuance_time()
            s.closing_price_y = closing_price_y
            s.open_price_t = open_price_t
            s.stock_type = stock_type
            s.change_extent = 1.0 * extend / s.closing_price_y
            s.save()
            cnt += 1
            print(cnt, s)
        except Exception:
            print(Exception)


