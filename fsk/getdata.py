import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def getData(data_name):
    title_list = []
    title_list.append("engine_num")
    title_list.append("times")
    for i in range(24):
        title_list.append("s"+str(i+1))
    # print(title_list)
    df = pd.read_csv(data_name, sep=' ', encoding='utf-8', header=None, index_col=False)  # 有names的时候header=None可省略
    df = df.dropna(axis='columns')
    df.columns = title_list
    # print(df[:3])
    return df   # 读取txt数据，返回一个dataframe，所有数据都放在一个大的dataframe里


def slice(df):
    engine_list = []
    flag = 0
    for i in range(len(df)):
        if i == len(df)-1:
            engine_list.append(df[flag:i])
        elif df["engine_num"][i+1] != df["engine_num"][i]:
            engine_list.append(df[flag:i+1])
            flag = i+1
        else:
            continue
    for i in engine_list:
        i["RUL"] = list(map(lambda x: len(i)-(x-1)-1, i.iloc[:, 1]))  # 最后一列是由第二列算出的RUL  这里可能不是deep copy
    return engine_list   # 返回的是一个list，list里每个元素都是dataframe，一个dataframe代表一个发动机全部的飞行记录


def re_slice(en_list):
    df = pd.DataFrame(data=en_list[0])
    for i in range(len(en_list)-1):
        df = df.append(en_list[i+1])
    return df


def sen_select(df, sensor):
    RUL = df['RUL']
    a, b = df.shape
    for i in range(24):   # 24 sensors
        plt.figure()
        temp = df['s'+str(i+1)].values
        # temp = temp[~np.isnan(temp)]
        plt.scatter(RUL, temp, s=1)
        plt.title('Sensor Measurement '+str(i+1)+' when '+sensor)
        plt.show(block=False)


def divide_df_s3(df, sensor):
    df_list_s3 = []
    new_df1 = df[df[sensor] == 60.0]
    new_df2 = df[df[sensor] == 100.0]
    df_list_s3.append(new_df1)
    df_list_s3.append(new_df2)
    return df_list_s3


def divide_df_s2(df):
    df_list_s2 = []
    new_df1 = df[(df['s2'] > 0.8) & (df['s2'] < 1.0)]
    new_df2 = df[(df['s2'] > 0.6) & (df['s2'] < 0.8)]
    new_df3 = df[(df['s2'] > 0.2) & (df['s2'] < 0.4)]
    new_df4 = df[df['s2'] < 0.2]
    df_list_s2.append(new_df1)
    df_list_s2.append(new_df2)
    df_list_s2.append(new_df3)
    df_list_s2.append(new_df4)
    return df_list_s2


def main():
    df = getData('train_data.txt')
    engine_list = slice(df)
    df_with_RUL = re_slice(engine_list)
    # print(df_with_RUL['s4'])
    l_s3 = divide_df_s3(df_with_RUL, 's3')
    # for i in l_s3:
    #     sen_select(i, 's3')
    # sen_select(l_s3[1], 's3')
    # sen_select(l_s3[0], 's3')
    l_s2 = divide_df_s2(l_s3[1])
    sen_select(l_s2[1], 's2')
    # print(l_s3[0]['s1'])


if __name__ == '__main__':
    main()

