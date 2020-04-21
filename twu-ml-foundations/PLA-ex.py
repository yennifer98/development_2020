#!/usr/bin/env python       增强代码可移植性
#-*- coding:utf-8 -*-       统一字符集
# @Time : 2020/4/11 下午4:15   创建脚本时间
# @Author :  JIN            申明作者
# @File   :  PLA-ex.py     申明文件名称
from Perceptron import *

# data = load_data("https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_15_train.dat")
# updates = PLA_cyclic(data, randomness = False)
# print("+++++ The final updates of naive cycle are +++++")
# print(updates)
#
# updates_intotal = 0
# for i in range(2000):
#     random.seed(i)
#     updates = PLA_cyclic(data, randomness = True, yita = 1.0)
#     updates_intotal += updates
#
#
# updates_intotal = 0
# for i in range(2000):
#     random.seed(i)
#     updates = PLA_cyclic(data, randomness = True, yita = 0.5)
#     updates_intotal += updates
#
# print("The updates in average is:")
# print(updates_intotal/2000)

train_data = load_data("https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_18_train.dat")
test_data = load_data("https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_18_test.dat")

x, y = load_xy(test_data)
pocket_error = []
pocket_error_100 = []
PLA_error = []
T = 2000
it = 50
it2 = 100
for t in range(T):
    w_p, w = Pocket(train_data, it)
    w_p_2, w_2 = Pocket(train_data, it2)
    mistakes = testmistake(x, y, w_p)
    PLA_mistakes = testmistake(x, y, w)
    pocket_mistakes_100 = testmistake(x, y, w_p_2)
    pocket_error.append(len(mistakes)/len(y))
    PLA_error.append(len(PLA_mistakes)/len(y))
    pocket_error_100.append(len(pocket_mistakes_100)/len(y))

print("+++++ The average error rate of pocket vector for {} iterations after {} experiments is +++++".format(it, T))
print(np.mean(pocket_error))

print("+++++ The average error rate of PLA vector for {} iterations after {} experiments is +++++".format(it, T))
print(np.mean(PLA_error))

print("+++++ The average error rate of pocket vector for {} iterations after {} experiments is +++++".format(it2, T))
print(np.mean(pocket_error_100))