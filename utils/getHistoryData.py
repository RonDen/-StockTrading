import tushare as ts
import numpy as np
import time
def getHistoryData(t):
    pro = ts.pro_api('17649607a4e92be1fe38fb52b2ff2e044ac6301f665e98b278ab14a7')
    strt = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # print(strt)
    strt = strt.split("-")
    # print(t)
    df = pro.daily(ts_code=t, start_date='20190101', end_date=strt[0] + strt[1] + strt[2])
    print(df)
    # print("asd")
    res = np.array(df)
    res = res[:,[1,2,5,4,3]]#日期，开盘，最高，最低,收盘
    res = res.tolist()

    # print("asdasda")
    # print(res)
    return res
# print(getHistoryData("000001.SZ"))

print(getHistoryData("000002.SH"))
