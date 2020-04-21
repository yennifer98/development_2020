#!/usr/bin/env python       增强代码可移植性
#-*- coding:utf-8 -*-       统一字符集
# @Time : 2020/4/15 下午12:29   创建脚本时间
# @Author : Kitatine           申明作者
# @File   :  hw2_4.py     申明文件名称

from hw2 import *
import matplotlib
import matplotlib.pyplot as plt


# symbolize the parameters
e = sympy.Symbol('e')
N= sympy.Symbol('N')
m = sympy.Symbol('m')
d = sympy.Symbol('delta')

print("+++++ Solve for the implicit bound of Parrondo and Van den Broek +++++")
f_pvd = e - sympy.sqrt((2*e + sympy.log(6*m/d))/N)
print(sympy.solve(f_pvd, e)[1])
#
print("+++++ Solve for the implicit bound of Devroye +++++")
f = e - sympy.sqrt((4*e*(1+e)+sympy.log((4*m)/d))/(N*2))
# sympy.init_printing(use_latex = True) # 仅仅在jupyter kernel下有效
# print(sympy.latex(sympy.solve(f, e)[1]))
print(sympy.solve(f, e)[1])

## initialize N
N = np.linspace(start=3, stop=10000, dtype="float64")
dvc = 50
delta = 0.05
bounds = [VCbound(N, dvc, delta),
          RPbound(N, dvc, delta),
          PVdbound(N, dvc, delta),
          Devbound(N, dvc, delta),
          varVCbound(N, dvc, delta)]
labels = ["Original VC bound",
          "Rademacher Penalty Bound",
          "Parrondo and Van den Broek",
          "Devroye",
          "Variant VC bound"]

print("++++ begin to plot figure 1 +++++")
plt.title("$\epsilon$ vs $N$, $N$ = 100")
plt.xlabel("$N$")
plt.ylabel("$\epsilon$")

# 提升输出的分辨率
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率

for i in range(5):
    plt.plot(N[:], (bounds[i][:]))
    plt.legend(labels, loc="best")
# plt.show()
plt.savefig('bounds-comparison-100.png', dpi=300)
# plt.clf()  # 清图。
# plt.cla()  # 清坐标轴。
# plt.close()  # 关窗口
plt.close('all') # 关闭图

print("++++ Take log to zoom in +++++")
plt.title("$log(\epsilon)$ vs $N$, $N$ = 100")
plt.xlabel("$N$")
plt.ylabel("$log(\epsilon)$")
for i in range(5):
    plt.plot(N[:], (np.log(bounds[i][:])))
    plt.legend(labels, loc="best")
#plt.show()
plt.savefig('bounds-comparison-100-log.png', dpi=300)
plt.close('all') # 关闭图


print("++++ Take log to zoom in +++++")
plt.title("$log(\epsilon)$ vs $N$, $N$ = 5")
plt.xlabel("$N$")
plt.ylabel("$log(\epsilon)$")
for i in range(5):
    plt.plot(N[:], (np.log(bounds[i][:])))
    plt.legend(labels, loc="best")
#plt.show()
plt.savefig('bounds-comparison-100-log.png', dpi=300)
plt.close('all') # 关闭图

print("+++++ for small N +++++")
plt.title("$log(\epsilon)$ vs $N$, $N$ $\leq$ 600")
plt.xlabel("$N$")
plt.ylabel("$log(\epsilon)$")
for i in range(5):
    plt.plot(N[:4], (np.log(bounds[i][:4])))
    plt.legend(labels, loc="best")
#plt.show()
plt.savefig('bounds-comparison-100-log.png', dpi=300)
plt.close('all') # 关闭图