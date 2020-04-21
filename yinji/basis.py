import os
import pandas as pd


def basis_price(contract, etf, basis):
    # contract是合约的k线数据, eft是eft价格为文件名, basis是要得到的基差价格的文件名
    path_kl = 'F:\\intern\\yinji\\data\\kline_data'  # 修改为存储合约k线数据的路径
    os.chdir(path_kl)
    data1 = pd.read_csv(contract)
    path_diff = 'F:\\intern\\yinji\\data\\difference'  # 修改为存储etf价格的路径
    os.chdir(path_diff)
    data2 = pd.read_csv(etf)
    new1 = pd.DataFrame(data1, columns=['time', 'close'])
    new = pd.merge(new1, data2, how="right", on='time', sort=False)
    # new = pd.concat([new1, data2], axis=1, keys='time')
    new = new.dropna(axis=0, how='any')
    if contract[6] == 'I':
        new['basis'] = new['close'] - new['diff'] * 1000
    else:
        new['basis'] = new['close'] * 1000 - new['diff'] * 1000
    del new['close']
    del new['diff']
    outputpath = 'F:\\intern\\yinji\\data\\basis'  # 修改为存储basis price的路径
    os.chdir(outputpath)
    new.to_csv(basis, columns=['time', 'basis'], header=True, index=True, mode='w')


# basis_price('kline_IH2001.csv', 'diff_1909_1918.csv', 'basis_IH2001_1909and1918.csv')
