import tushare as ts
import numpy as np
import time
from datetime import date, datetime
from chinese_calendar import is_workday, is_holiday
import getRtQuotes
import pymysql
def clearTodayData():
    conn = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="stocktrading")
    cursor = conn.cursor()

    sql = "DELETE FROM `%s`"
    stoinfo = getTscode()
    for i in range(0,len(stoinfo)):
        cursor.execute(sql,["daily_ticks"+"_"+stoinfo[i][0]+"_"+stoinfo[i][0]])
def getTodayRealTimeData():
    conn = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="stocktrading")
    cursor = conn.cursor()
    

def getTscode():
    conn = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="stocktrading")
    cursor = conn.cursor()
    sql = "select stock_id,stock_type  from stock_info"
    cursor.execute(sql)
    stoinfo = cursor.fetchall()
    cursor.close()
    conn.close()
    return stoinfo
