
# 最终只运行这个文件就可以了，需要修改一次路径，每次生成只需修改bp函数后面的接口即可

from kl import kl
from etf_price import etf_price
from basis import basis_price


def bp(date, put, call, fu, strike_price):
    data1 = 'option' + date + '_' + put + '.log'  # e.g. 'option2019001227_10001909.log'
    data2 = 'option' + date + '_' + call + '.log'
    if fu[0] == 'I':
        future = 'future' + date + '_' + fu + '.log'  # e.g. 'future2019001227_IH2001.log'
    else:
        future = 'stock' + date + '_' + fu + '.log'  # e.g. 'stock2019001227_510050.log'
    # 过程文件命名
    kl_data1 = 'kline' + '_' + put + '.csv'  # e.g. 'kline_10001909.csv'
    kl_data2 = 'kline' + '_' + call + '.csv'
    kl_datafu = 'kline' + '_' + fu + '.csv'
    etf = 'diff_' + put + '_' + call + '.csv'  # e.g. 'diff_10001909_10001918.csv'
    # 最终文件命名
    basis = 'basis_' + fu + '_' + put + 'and' + call + '_' + date + '.csv'
    kl(date, data1, kl_data1)
    kl(date, data2, kl_data2)
    kl(date, future, kl_datafu)
    etf_price(kl_data1, kl_data2, etf, strike_price)
    basis_price(kl_datafu, etf, basis)  # 现在结果是e.g. IF2001减去etf价格


bp('2020000107', '10002053', '10002062', 'IH2001', 3.0)
