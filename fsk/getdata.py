import pandas as pd


def getData(data_name):
    df = pd.read_csv(data_name, sep=' ', encoding='utf-8', header=None)
    df = df.dropna(axis='columns')
    # print(df[:3])
    return df   # 读取txt数据，返回一个dataframe，所有数据都放在一个大的dataframe里


def slice(df):
    engine_list = []
    flag = 0
    for i in range(len(df)):
        if i == len(df)-1:
            engine_list.append(df[flag:i])
        elif df[0][i+1] != df[0][i]:
            engine_list.append(df[flag:i+1])
            flag = i+1
        else:
            continue
    return engine_list   # 返回的是一个list，list里每个元素都是dataframe，一个dataframe代表一个发动机全部的飞行记录


def main():
    df = getData('train_data.txt')
    print(slice(df))


if __name__ == '__main__':
    main()

