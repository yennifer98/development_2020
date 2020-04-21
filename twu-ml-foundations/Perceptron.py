#!/usr/bin/env python       增强代码可移植性
#-*- coding:utf-8 -*-       统一字符集
# @Time : 2020/4/11 下午10:15   创建脚本时间
# @Author :  JIN            申明作者
# @File   :  Perceptron.py     申明文件名称

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import random

def sign(x):
    if x > 0:
        return 1
    else:
        return -1

# def sign(x):
#     vfunc = np.vectorize(lambda t: 1 if t > 0 else -1)
#     return vfunc(x)

def verify(x, y, w):
    m, n = x.shape
    flag = False
    for xs in range(m):
        if sign(x[xs].dot(w.transpose())) != y[xs]:
            flag = True
    if flag:
        print("Mistake Happens!")
        return False
    return True

def testmistake(x, y, w):
    m,n = x.shape
    mistakes = []
    for i in range(m):
        if (sign(x[i].dot(w)) != y[i]):
            mistakes.append(i)
    return mistakes

def choosePocket(x, y, w1, w2):
    mistake1 = testmistake(x, y, w1)
    mistake2 = testmistake(x, y, w2)

    # print("Mistake 1 size: ", len(mistake1))
    # print("Mistake 2 size: ", len(mistake2))

    if len(mistake1) > len(mistake2):
        # print("Alter!")
        return w2.copy()
    else:
        return w1

def load_xy(data):
    m, n = data.shape
    features = data[:, :-1]
    labels = data[:, -1]

    # set x0 = 1 for each xn
    x = np.hstack((np.ones((m, 1)), features))
    y = labels.astype(float)

    return x,y


def load_data(target_URL):
    # Load in the DataFrame
    df = pd.read_csv(target_URL, sep = "\s+", header = None)
    print("+++++ The DataFrame is +++++")
    print(df)

    # Converting into the numpy array
    print("+++++ The NumpyArray is +++++")
    data = df.to_numpy()
    print(data)
    return data

def PLA_cyclic(data, randomness, yita = 1.0, verbalize = False):
    '''
    :param data:
    :param randomness: naive cycle if False, precomputed random cycle if True
    :param verbalize: Print the detailed of the updates if True
    :param yita: the coefficient when correcting
    :return:
    '''
    x, y = load_xy(data)
    m, n = x.shape

    # initialize the index set
    indexes = np.arange(m)
    if randomness:
        random.shuffle(indexes)

    # initialize the accumulator
    steps = 0
    i = 0

    # initialize weights to zero
    ## notice we shall manually add in the w0 = 0
    w = np.zeros(shape=(1, x.shape[1]))

    correct_x = 0
    correct_total = []
    while (correct_x < m):
        ii = indexes[i]
        if sign(x[ii].dot(w.transpose())) != y[ii]: # mistake here
            # update
            if(verbalize):
                print("+++++ Update {} +++++".format(steps))
                np.set_printoptions(precision=3, suppress=True)
                print("The Weights before update is ", w)
                verify(x, y, w)
            correct_total.append(correct_x)
            correct_x = 0
            w = w + yita * y[ii] * x[ii]
            steps += 1
        else:
            correct_x += 1
        # cycle generate
        if i < m-1:
            i += 1
        else:
            i = 0
    if verbalize:
        print("+++++ Update {} +++++".format(steps))
        if verify(x, y, w):
            print("Finally No Mistake Detected!")
        correct_total.append(correct_x)
        update = np.arange(0, steps + 1)
        plt.plot(update, correct_total)
        plt.xlabel('updates')
        plt.ylabel('correct x identified in total')
        plt.show()

    return steps

def Pocket(data, iteration, yita = 1.0, verbalize = False):
    '''
    :param data:
    :param iteration:
    :param yita:
    :param verbalize:
    :return:
    '''
    x,y = load_xy(data)
    w = np.zeros(shape=(x.shape[1]))
    w_pocket = w.copy()

    for t in range(iteration):
        ## return the mistakes list
        mistakes = testmistake(x, y, w)
        # print("+++++ The mistakes are +++++")
        # print(mistakes)
        if not mistakes:
            # print("break!")
            break
        else:
            i = random.choice(mistakes)
            # print("Choose Mistake ", i)
            w = w + y[i] * x[i]
            # print("w in pocket:", w_pocket)
            # print("w after alternating, ", w)
            w_pocket = choosePocket(x, y, w_pocket, w)
    return w_pocket, w


