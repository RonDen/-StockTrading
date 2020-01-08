import tushare as ts
import numpy as np
import time
from datetime import date, datetime
from chinese_calendar import is_workday, is_holiday
from utils import getRtQuotes
import pymysql


def judje(stock_start, stock_end):
    n_time = datetime.now()  # 获取当前时间
    start = datetime.strptime(str(datetime.now().date()) + stock_start, '%Y-%m-%d%H:%M')
    end = datetime.strptime(str(datetime.now().date()) + stock_end, '%Y-%m-%d%H:%M')

    if n_time > start and n_time < end:
        return True
    else:
        return False


def clearTodayData():
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()

    sql = "DELETE FROM `%s`"
    stoinfo = getTscode()
    for i in range(0, len(stoinfo)):
        cursor.execute(sql, ["daily_ticks" + "_" + stoinfo[i][0] + "_" + stoinfo[i][0]])


def getTodayRealTimeData():
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()
    stoinfo = getTscode()
    sql = "INSERT INTO `%s`(DAILY_TICKS,REAL_TIME_QUOTES) VALUES(%s, %s)"
    while(1):
        if(judje("09:30","11:30") or judje("13:00","15:00")):

            for i in range(0, len(stoinfo)):
                if (i != 2190):
                    df = ts.get_realtime_quotes(symbols=stoinfo[i][0])
                    df = df[['code', 'name', 'price', 'bid', 'ask', 'volume', 'amount', 'time']]
                    print(df)
                    res = np.array(df)
                    res = res[:, [2, 7]]
                    # res = res.tolist()
                    if (len(res) != 0):
                        if (stoinfo[i][1] == "深证"):

                            cursor.execute(sql, ["dailyticks_" + stoinfo[i][0] + "_" + "SZ", res[0][1], res[0][0]])
                        else:
                            cursor.execute(sql, ["dailyticks_" + stoinfo[i][0] + "_" + "SH", res[0][1], res[0][0]])
                    conn.commit()
        n_time = datetime.now()
        end = datetime.strptime(str(datetime.now().date()) + "15:00", '%Y-%m-%d%H:%M')
        if( n_time>end ):#超过晚上15：00自动终止获取
            break
    cursor.close()
    conn.close()
    # stoinfo = getTscode()
    # for i in range(0,len(stoinfo)):
    #     cursor.execute(sql,["daily_ticks"+"_"+stoinfo[i][0]+"_"+stoinfo[i][0]])


def getTscode():
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()
    sql = "select stock_id,stock_type  from stock_info"
    cursor.execute(sql)
    stoinfo = cursor.fetchall()
    cursor.close()
    conn.close()
    return stoinfo


# getTodayRealTimeData()
# judje("09:30","11:30")
