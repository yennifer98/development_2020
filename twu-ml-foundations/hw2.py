#!/usr/bin/env python       增强代码可移植性
#-*- coding:utf-8 -*-       统一字符集
# @Time : 2020/4/15 下午12:30   创建脚本时间
# @Author :  Kitatine            申明作者
# @File   :  hw2_3.py     申明文件名称
import sympy
import numpy as np
from numpy import *


def Nsolver(dvc = 10, e = 0.05, ci = 0.95):
    d = dvc
    epsilon = e
    threshold = 1-ci
    N = sympy.symbols('N')
    delta = 4 * ((2 * N) ** d) * sympy.exp((-(epsilon ** 2) * N) / 8) - threshold
    sol_lst = sympy.solve(delta, N)
    sol = [s for s in sol_lst if sympy.im(s) == 0 and s > 10*d]
    print("The resulting N is ", sol)
    return sol


# since mH(N) = N^dvc + 1
def mH(N, dvc):
    return N**dvc

def logmH(N, dvc):
    # Avoid the overflow when calculating Dev bound
    return dvc * np.log(N)

def VCbound(N, dvc, delta):
    return np.sqrt(8.0/N*np.log(4*((2*N)**(dvc))/delta))

def RPbound(N, dvc, delta):
    return np.sqrt(2*np.log(2*N*(N**dvc))/N) + np.sqrt(2/N*np.log(1/delta)) + 1/N

def PVdbound(N, dvc, delta):
    return (sqrt(N*log(mH(2*N, dvc)/delta) + N*log(6) + 1) + 1)/N

def Devbound(N, dvc, delta):
    return (np.sqrt(2)*np.sqrt(N*logmH(N**2, dvc) - np.log(delta) + N*np.log(4) - 2*logmH(N**2, dvc) - np.log(delta) - np.log(16) + 2) + 2)/(2*(N - 2))

def varVCbound(N, dvc, delta):
    return np.sqrt(16.0/N*np.log(2*(N**dvc)/np.sqrt(delta)))

# print(__name__)



