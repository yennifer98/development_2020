import sympy
# *是通配符，这样就不用numpy.啥啥
from numpy import *

# # Q3
# # 定义变量
# x = sympy.Symbol('x')
# fx = 4*(2*x)**10 * sympy.exp(-1/8*0.05*0.05*x) - 0.05
# # 使用evalf函数传值
# y1 = sympy.solve(fx, x)
# print(y1)

# x=random.uniform(-1,1,2)
# print(array(x))
# print(type(x))

w1 = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
w2 = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
for i in range(11):
    print(sqrt((10**2)*(w1[i]**2)+(15**2)*(w2[i]**2)+2*0.3*10*15*w1[i]*w2[i]))

