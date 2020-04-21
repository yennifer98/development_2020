import pandas as pd
import re
import numpy as np
import random


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def load_data(url):
    # URL = "https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_15_train.dat"
    # url = "https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_18_train.dat"
    # data = pd.read_csv(URL, header=None)  # df
    # separator = re.compile('\t|\b| |\n')
    # result = []
    # with open('pla_data.csv', 'r') as f:
    #     line = f.readline()
    #     while line:
    #         temp = separator.split(line)[0:-1]
    #         abc = [float(x) for x in temp]
    #         result.append(abc)
    #         line = f.readline()
    df = pd.read_csv(url, sep="\s+", header=None)
    result = df.to_numpy()
    return result


def perceptron(data, randomness, nta):
    m, n = data.shape
    features = data[:, :-1]
    labels = data[:, -1]

    # set weights to zero
    w = np.zeros(shape=(1, features.shape[1] + 1))
    num = 0
    i = 0

    indexes = np.arange(m)
    if randomness:
        random.shuffle(indexes)

    # set x0 = 1 for each xn (也可在后续迭代中完成此步的操作）
    x = np.hstack((np.ones((m, 1)), features))

    correct_x = 0
    while correct_x < m:
        ii = indexes[i]
        if sign(x[ii].dot(w.transpose())) != labels[ii]:  # incorrect
            w += nta*labels[ii]*x[ii]
            correct_x = 0
            num += 1
        else:
            correct_x += 1
        if i < m-1:
            i += 1
        else:
            i = 0
    return num


def pocket(data, update, randomness):
    m, n = data.shape
    features = data[:, :-1]
    labels = data[:, -1]
    # set weights to zero
    w = np.zeros(shape=(1, features.shape[1] + 1))
    indexes = np.arange(m)
    if randomness:
        random.shuffle(indexes)

    # set x0 = 1 for each xn (也可在后续迭代中完成此步的操作）
    x = np.hstack((np.ones((m, 1)), features))
    incorrect_min = m
    w_best = w.copy()
    for j in range(update):
        incorrect = 0
        incorrect_list = []
        for i in range(m):
            ii = indexes[i]
            if sign(x[ii].dot(w.transpose())) != labels[ii]:  # incorrect
                incorrect += 1
                incorrect_list.append(ii)
        if incorrect < incorrect_min:
            w_best = w.copy()
            incorrect_min = incorrect
        a = random.choice(incorrect_list)
        w += labels[a]*x[a]
    return w_best


def manytimes(data, test, times):
    num = 0
    for i in range(times):
        w = pocket(data, 100, True)
        num += testerror(test, w)
    return num/times


def testerror(test, w):
    m, n = test.shape
    features = test[:, :-1]
    labels = test[:, -1]
    x = np.hstack((np.ones((m, 1)), features))
    count = 0
    for i in range(m):
        if sign(x[i].dot(w.transpose())) != labels[i]:
           count += 1
    return count/m


data = load_data("https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_18_train.dat")
test = load_data("https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_18_test.dat")
# num = perceptron(data, True)
times = manytimes(data, test, 2000)
# print(data)
print(times)
# print(num)
# data.to_csv('pla_data.csv', header=None, index=False, mode='w')

# 0.13296
# 0.355
# 0.115