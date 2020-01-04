import tushare as ts
from tradingSystem.models import StockInfo

my_token = '6f6ee0533e28c2bde19102cccfc95de79fe56fc16633f5267fa0985c'

pro = ts.pro_api('6f6ee0533e28c2bde19102cccfc95de79fe56fc16633f5267fa0985c')
# data = pro.stock_basic(exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_date')
data = pro.query('stock_basic', exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_date')


cnt = 0
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
