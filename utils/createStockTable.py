import pymysql
import tushare as ts
import numpy as np
import time
from utils import getHistoryData


def createStockTable(t):  # 建表 eg:表名为000001.SZ，字段是日期，开盘，最高，最低,收盘
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()
    sql = """CREATE TABLE `%s`(
                 TRADING_DAY VARCHAR(64) DEFAULT NULL,
                 OPEN_PRICE FLOAT DEFAULT NULL,
                 HIGHEST FLOAT DEFAULT NULL,
                 LOWEST FLOAT DEFAULT NULL,
                 CLOSE_PRICE FLOAT DEFAULT NULL)
                """
    cursor.execute(sql, [t])


def createEvedayTable(t):  # 每天实时数据
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()
    sql = """CREATE TABLE `%s`(
                 DAILY_TICKS VARCHAR(64) DEFAULT NULL,
                 REAL_TIME_QUOTES FLOAT DEFAULT NULL
                 )
                """
    cursor.execute(sql, ["dailyTicks_" + t])
    cursor.close()
    conn.close()


def InsertOldDay(t):
    res = getHistoryData.getHistoryData(t)
    print(res)
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()

    sql = "INSERT INTO `%s`(TRADING_DAY,OPEN_PRICE,HIGHEST,LOWEST,CLOSE_PRICE) VALUES(%s, %s, %s, %s,%s)"
    t = t.split(".")

    for i in res:
        i.insert(0, t[0] + "_" + t[1])
        # print(i)
        cursor.execute(sql, i)
        conn.commit()
    cursor.close()
    conn.close()


def insertTodayTickData(t):
    t = t.split(".")
    res = ts.get_today_ticks(t[0])
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()

    sql = "INSERT INTO `%s`(TRADING_DAY,OPEN_PRICE,HIGHEST,LOWEST,CLOSE_PRICE) VALUES(%s, %s, %s, %s,%s)"

    for i in res:
        i.insert(0, t[0] + "_" + t[1])
        # print(i)
        cursor.execute(sql, i)
        conn.commit()
    cursor.close()
    conn.close()


def getTscode():
    conn = pymysql.connect(host="127.0.0.1", user="trading", password="trading", database="stocktrading")
    cursor = conn.cursor()
    sql = "select stock_id,stock_type  from stock_info"
    cursor.execute(sql)
    stoinfo = cursor.fetchall()
    for i in range(959,len(stoinfo)):
        if(stoinfo[i][1] == "上证"):
            tmp=stoinfo[i][0]+"_"+"SH"
            # tmp = stoinfo[i][0] + "." + "SH"

        else:
            tmp = stoinfo[i][0] + "_" + "SZ"
            # tmp = stoinfo[i][0] + "." + "SZ"
        # createStockTable(tmp)
        # createEvedayTable(tmp)
        print(tmp)
        InsertOldDay(tmp)
        # time.sleep(1)
    cursor.close()
    conn.close()


# getTscode()
# InsertOldDay("000001.SZ")
