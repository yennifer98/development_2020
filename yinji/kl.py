import os
import pandas as pd
import datetime


def kl(date, data, out):
    # data是要进行处理的数据文件名，out是要得到的k线数据的csv文件名
    path = 'F:\\intern\\yinji\\data\\data\\' + 'Delta' + date[0:4] + date[6:10]  # 修改为原始数据存储的路径
    os.chdir(path)
    fp = open(data, 'r')
    # 读取文件生成dataframe
    line = fp.readline()
    if line != "":
        a = line.split(",")
        time = a[0]
        price = a[1]
        df = pd.DataFrame([[time, price]], columns=['time', 'price'])
    while line != "":
        line = fp.readline()
        if line != "":
            a = line.split(",")
            time = a[0]
            price = a[1]
            df = df.append({
                'time': time,
                'price': price
            }, ignore_index=True)
    fp.close()
    # 把第一列转化为指定时间格式
    temp = df.time
    temp1 = df.price
    final = pd.DataFrame(columns=['time'])
    for d in temp:
        data_min = (int(d) % 10000000) // 100000
        data_hour = int(d) // 10000000
        # 删除时间段外的数据
        if (data_hour >= 9) and (data_hour <= 15) and (data_hour != 9 or data_min >= 30):
            data_milisecond = int(d) % 1000
            data_second = (int(d) % 100000) // 1000
            a = datetime.time(hour=data_hour, minute=data_min, second=data_second, microsecond=data_milisecond)
            final = final.append({
                'time': a
            }, ignore_index=True)
        else:
            continue
    final = pd.concat([final, temp1], axis=1)
    final = final.dropna(axis=0, how='any')
    # 提取k线数据
    new = pd.DataFrame(columns=['time', 'price'])
    lines = final.iloc[:, 0].size - 1
    line = 0
    b = datetime.time(hour=final.iloc[0].time.hour, minute=final.iloc[0].time.minute)
    new = new.append({
        'time': b,
        'price': final.iloc[0].price
    }, ignore_index=True)
    kline = pd.DataFrame(columns=['time', 'open', 'high', 'low', 'close'])
    while line < lines:
        b = datetime.time(hour=final.iloc[line + 1].time.hour, minute=final.iloc[line + 1].time.minute)
        if final.iloc[line].time.minute == final.iloc[line + 1].time.minute:
            new = new.append({
                'time': b,
                'price': final.iloc[line + 1].price
            }, ignore_index=True)
        else:
            si = new.iloc[:, 0].size - 1
            ma = new.price.max()
            mi = new.price.min()
            kline = kline.append({
                'time': new.iloc[0].time,
                'open': new.iloc[0].price,
                'high': ma,
                'low': mi,
                'close': new.iloc[si].price
            }, ignore_index=True)
            new = pd.DataFrame(columns=['time', 'price'])
            new = new.append({
                'time': b,
                'price': final.iloc[line + 1].price
            }, ignore_index=True)
        line = line + 1
    if line == lines:
        si = new.iloc[:, 0].size - 1
        ma = new.price.max()
        mi = new.price.min()
        kline = kline.append({
            'time': new.iloc[0].time,
            'open': new.iloc[0].price,
            'high': ma,
            'low': mi,
            'close': new.iloc[si].price
        }, ignore_index=True)
    outputpath = 'F:\\intern\\yinji\\data\\kline_data'  # 修改为存储k线数据的路径
    os.chdir(outputpath)
    kline.to_csv(out, columns=['time', 'open', 'high', 'low', 'close'], header=True, index=True, mode='w')


# kl('future2019001227_IH2001.log', 'kline_IH2001.csv')
# kl('2020000106', 'option2020000106_10001909.log', 'kline_1909.csv')
