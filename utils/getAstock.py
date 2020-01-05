import tushare as ts
import numpy as np
def getAstock(t):

    # data = np.array([[1, 8, 3, 3, 4],
    #                  [1, 8, 9, 9, 4],
    #                  [1, 8, 3, 3, 4]])
    # print(type(data))
    # print(data)
    # # 删除整个数组的重复元素
    # uniques = np.unique(data)
    # print(uniques)
    # # array([1, 3, 4, 8, 9])
    # # 删除重复行
    # uniques = np.unique(data,axis = 0)
    # print(uniques)
    # # array([[1, 8, 3, 3, 4],
    # #        [1, 8, 9, 9, 4]])
    # # 删除重复列
    # uniques = np.unique(data,axis = 1)
    # print(uniques)



    pro = ts.pro_api('17649607a4e92be1fe38fb52b2ff2e044ac6301f665e98b278ab14a7')
    # data = pro.stock_basic(exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_date')


    df = pro.stk_rewards(ts_code=t)
    m = df.dropna(axis=0)
    m = m[~m['hold_vol'].isin([0])]
    res = np.array(m)
    res = res[0:5,[3,6]]
    # print(res)
    # print(res)
    dic = {}
    res = list(res)
    # print(len(res))
    # print(res)
    for i in range(0,len(res)):
        # print(res[i][0])
        dic[res[i][0]]=res[i][1]

    # print(dic)
    res = []
    for key in dic:
        tmp = []
        tmp.append(key)
        print(key,dic[key])
        tmp.append(dic[key])

        res.append(tmp)
    return res



    # print(np.argmax(res[1],))

    # res.append(list(m["hold_vol"]))
    # res.append(list(m["name"]))
    # print(res)
