import pandas as pd
import os


def etf_price(kl_1, kl_2, etf, strike_price):
    # kl_1是第一个k线数据文件名，kl_2是第二个k线数据文件名
    # eft是要得到的etf的价格（diff）的文件名， strike_price是执行价
    path_kl = 'F:\\intern\\yinji\\data\\kline_data'  # 修改为存储k线数据的路径
    os.chdir(path_kl)
    data1 = pd.read_csv(kl_1)
    data2 = pd.read_csv(kl_2)
    new1 = pd.DataFrame(data1, columns=['time', 'close'])
    new2 = pd.DataFrame(data2, columns=['time', 'close'])
    new = pd.merge(new1, new2, how="right", on='time', sort=False)
    new['diff'] = new['close_x'] - new['close_y'] + strike_price
    del new['close_x']
    del new['close_y']
    outputpath = 'F:\\intern\\yinji\\data\\difference'  # 修改为存储etf价格的路径
    os.chdir(outputpath)
    new.to_csv(etf, columns=['time', 'diff'], header=True, index=True, mode='w')


# etf_price('kline_10001909.csv', 'kline_10001918.csv', 'diff_10001909_10001918.csv', 2.706)
