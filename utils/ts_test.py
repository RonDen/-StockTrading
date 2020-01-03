import tushare as ts


def main():
    pro = ts.pro_api('6f6ee0533e28c2bde19102cccfc95de79fe56fc16633f5267fa0985c')
    # data = pro.stock_basic(exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_date')
    data = pro.query('stock_basic', exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_data')

    print(data)


if __name__ == '__main__':
    main()


