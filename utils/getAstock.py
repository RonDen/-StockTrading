import tushare as ts

def getAstock():
    
    pro = ts.pro_api('17649607a4e92be1fe38fb52b2ff2e044ac6301f665e98b278ab14a7')
    # data = pro.stock_basic(exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_date')
    data = pro.query('stock_basic', exchange='', list_status='L', fileds='ts_code,symbol,name,area,industry,list_data')
    
    return data




