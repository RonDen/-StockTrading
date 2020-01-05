import tushare as ts
from tradingSystem.models import StockInfo
from random import randint, random, choice

my_token = '6f6ee0533e28c2bde19102cccfc95de79fe56fc16633f5267fa0985c'

pro = ts.pro_api(my_token)
# data = pro.stock_basic(exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_date')
data = pro.query('stock_basic', exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_date,market')


cnt = 0

for row in data.iterrows():
    # try:
    exchange = ""
    if row[1]['ts_code'].find('SH'):
        exchange = "上证"
    else:
        exchange = "深证"
    close_y = randint(5, 200)
    extend = choice([0.1, -0.1, 0.05, -0.05]) * random()
    open_t = close_y + close_y * extend
    stock = StockInfo(
        stock_id=row[1]['symbol'],
        stock_name=row[1]['name'],
        block=row[1]['market'],
        issuance_time=row[1]['list_date'],
        stock_type=exchange,
        closing_price_y=close_y,
        open_price_t=open_t,
        change_extent=extend
    )
    stock.save()
    cnt += 1
    print(cnt)
    # except Exception:
    #     print(Exception)

for row in data.iterrows():
    try:
        stock = StockInfo(
            stock_id=row[1]['symbol'],
            stock_name=row[1]['name'],
            stock_type=row[1]['market']
        )
        stock.save()
        cnt += 1
        print(cnt)
    except Exception:
        print(Exception)


def main():
    # print(ts.get_today_all())
    df = ts.get_realtime_quotes('000581') #Single stock symbol
    # data = pro.stock_basic(exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_date')
    data = pro.query('stock_basic', exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_data')

    for ts_code, symbol, name, area, industry, list_data in data['ts_code'], data['symbol'], data['name'], data['area'], \
                                                            data['industry'], data['list_data']:
        print(ts_code, symbol, name, area, industry, list_data)
    print(data)


if __name__ == '__main__':
    main()
