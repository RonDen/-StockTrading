# 管理员每天收盘后进行维护给数据库增加当天的数据
import tushare as ts
import numpy as np
import time
import pymysql


def getTodayData(t):
    pro = ts.pro_api('17649607a4e92be1fe38fb52b2ff2e044ac6301f665e98b278ab14a7')
    strt = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(strt)
    strt = strt.split("-")
    print(t)
    df = pro.daily(ts_code=t, start_date=strt[0] + strt[1] + strt[2], end_date=strt[0] + strt[1] + strt[2])

    res = np.array(df)
    res = res[:, [1, 2, 5, 4, 3]]  # 日期，开盘，最高，最低,收盘
    res = res.tolist()
    return res


def InsertTodayDay(t):
    res = getTodayData(t)
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()

    sql = "INSERT INTO `%s`(TRADING_DAY,OPEN_PRICE,HIGHEST,LOWEST,CLOSE_PRICE) VALUES(%s, %s, %s, %s,%s)"
    t = t.split(".")
    print(t)

    for i in res:
        i.insert(0, t[0] + "_" + t[1])
        print(i)
        cursor.execute(sql, i)

        conn.commit()
    cursor.close()
    conn.close()


def upHold():
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()
    sql = "select stock_id,stock_type  from stock_info"
    cursor.execute(sql)
    stoinfo = cursor.fetchall()
    for i in range(0, len(stoinfo)):
        if (stoinfo[i][1] == "上证"):
            tmp = stoinfo[i][0] + "." + "SH"

        else:
            tmp = stoinfo[i][0] + "." + "SZ"
        InsertTodayDay(tmp)
    cursor.close()
    conn.close()

# 接口供收盘时维护每日数据
# upHold()


