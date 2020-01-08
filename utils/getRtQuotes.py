import tushare as ts
import numpy as np
import time
from datetime import date, datetime
from chinese_calendar import is_workday,is_holiday
# pro = ts.pro_api('17649607a4e92be1fe38fb52b2ff2e044ac6301f665e98b278ab14a7')

# data = pro.stock_basic(exchange='SSE', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')


def getworkday():
    strt = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    strt = strt.split("-")
    y = int(strt[0])
    m = int(strt[1])
    d = int(strt[2])

    april_last = date(y , m , d)
    print(april_last)
    print(is_workday(april_last))
    print("fuckshit",is_holiday(april_last))
    print("dick",not is_holiday(april_last))
    print("elecshit",is_workday(april_last) and (not is_holiday(april_last)))
    return is_workday(april_last) and (not is_holiday(april_last))



def getRtQuotes(t):
    f = getworkday()

    df = "0"
    resx="0"
    res = "0"
    resy="0"
    print(t)

    if(f):
        print(f)


        strt = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        print(strt)

        df = ts.get_today_ticks(t)
        print(df)
        res = np.array(df)
        resx = res[:, [0]]
        resy = res[:, [1]]
        resx = resx.reshape(-1)
        resy = resy.reshape(-1)
        resx = resx.tolist()
        resy = resy.tolist()

        return 1,resx,resy
    else:
        return 0,resx,resy