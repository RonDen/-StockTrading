import pymysql
import tushare as ts
import numpy as np
import time
import sys


def portinStockInfo(t):
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()
    sql = "INSERT INTO stock_info(stock_id,stock_name,issuance_time,block,stock_type) VALUES(%s, %s, %s, %s,%s)"
    data = getStockInfo(t)
    for i in data:
        i.append("上证")
        print(i)
        cursor.execute(sql, i)
    conn.commit()
    cursor.close()
    conn.close()


def getStockInfo(t):
    pro = ts.pro_api('17649607a4e92be1fe38fb52b2ff2e044ac6301f665e98b278ab14a7')
    data = pro.stock_basic(exchange=t, list_status='L', fileds='ts_code,symbol,name,list_date,market')
    data = np.array(data)
    data = data[:, [1, 2, 6, 5]]  # 代号，名称，上市日期，板块
    data = data.tolist()
    return data


def getEveDayPrice(t):
    pro = ts.pro_api('17649607a4e92be1fe38fb52b2ff2e044ac6301f665e98b278ab14a7')
    strt = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    strt = strt.split("-")
    df = pro.daily(ts_code=t, start_date=strt[0] + strt[1] + strt[2], end_date=strt[0] + strt[1] + strt[2])
    df = np.array(df)
    df = df[:, [2, 6, 8]]
    df = df.tolist()
    return df


def updateEveryday(t):
    df = getEveDayPrice(t)
    if (len(df) != 0):
        df = df[0]
        print(df)
        conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
        cursor = conn.cursor()
        sql = "update stock_info set closing_price_y='%s' ,open_price_t='%s',change_extent='%s' where stock_id=%s"
        symbol = t.split(".")
        df.append(symbol[0])
        cursor.execute(sql, df)
        conn.commit()
        cursor.close()
        conn.close()


def getTscode():
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()
    sql = "select stock_id,stock_type  from stock_info"
    cursor.execute(sql)
    stoinfo = cursor.fetchall()
    for i in range(0, 500):
        if (stoinfo[i][1] == "上证"):
            tmp = stoinfo[i][0] + "." + "SH"
        else:
            tmp = stoinfo[i][0] + "." + "SZ"
        updateEveryday(tmp)
    time.sleep(120)
    for i in range(500, 1000):
        if (stoinfo[i][1] == "上证"):
            tmp = stoinfo[i][0] + "." + "SH"
        else:
            tmp = stoinfo[i][0] + "." + "SZ"
        updateEveryday(tmp)
    time.sleep(120)
    for i in range(1000, 1500):
        if (stoinfo[i][1] == "上证"):
            tmp = stoinfo[i][0] + "." + "SH"
        else:
            tmp = stoinfo[i][0] + "." + "SZ"
        updateEveryday(tmp)
    time.sleep(120)
    for i in range(1500, 2000):
        if (stoinfo[i][1] == "上证"):
            tmp = stoinfo[i][0] + "." + "SH"
        else:
            tmp = stoinfo[i][0] + "." + "SZ"
        updateEveryday(tmp)
    time.sleep(120)
    for i in range(1500, 2000):
        if (stoinfo[i][1] == "上证"):
            tmp = stoinfo[i][0] + "." + "SH"
        else:
            tmp = stoinfo[i][0] + "." + "SZ"
        updateEveryday(tmp)

    time.sleep(120)
    for i in range(2000, 2500):
        if (stoinfo[i][1] == "上证"):
            tmp = stoinfo[i][0] + "." + "SH"
        else:
            tmp = stoinfo[i][0] + "." + "SZ"
        updateEveryday(tmp)

    time.sleep(120)
    for i in range(2500, 3000):
        if (stoinfo[i][1] == "上证"):
            tmp = stoinfo[i][0] + "." + "SH"
        else:
            tmp = stoinfo[i][0] + "." + "SZ"
        updateEveryday(tmp)

    time.sleep(120)
    for i in range(3000, 3500):
        if (stoinfo[i][1] == "上证"):
            tmp = stoinfo[i][0] + "." + "SH"
        else:
            tmp = stoinfo[i][0] + "." + "SZ"
        updateEveryday(tmp)

    time.sleep(120)
    for i in range(3500, 3754):
        if (stoinfo[i][1] == "上证"):
            tmp = stoinfo[i][0] + "." + "SH"
        else:
            tmp = stoinfo[i][0] + "." + "SZ"
        updateEveryday(tmp)

    cursor.close()
    conn.close()


# if __name__ == '__main__':
#     # portinStockInfo('SSE')
#     # getEveDayPrice('SSE')
#     getTscode()

# conn = pymysql.connect(host="127.0.0.1", user="root",password="123456",database="stocktrading")
# cursor = conn.cursor()
#
# sql = "select * from stock_info"
#
# cursor.execute(sql)
#
# res = cursor.fetchall()
#
#
# print(res)
# print(type(res))
# cursor.close()
#
# conn.close()
# getEveDayPrice("000001.SZ")
