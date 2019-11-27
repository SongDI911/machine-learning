'''
迭代循环取找梯度的最小值：其结束条件为：
1.根据迭代的次数来决定是否达到了找到的条件
2.根据如果两个值之间的差值小于10的-6次方，就说明迭代的结果已经不受影响了
其公式为：
    O(1) = O(0) -aJ(O)
    其中a为步长值  J(O)是原函数的导数，并将O(0)带入进J(O)中
'''
import numpy as np
from sympy import *
import random
import matplotlib.pyplot as plt

# 定义目标方程求导
def fangcheng():
    x = Symbol('x')
    y = x*x+1
    return y


#求解J(O) 即：原函数的导数
def solve(y):
    x = Symbol('x')
    result = diff(y,"x")
    return result

# 定义整个O(0) -aJ(O)
def content(y):
    y = fangcheng()
    result = solve(y)
    x = Symbol('x')
    # result.subs(x, 1)
    # 设定步长为0.2
    final = o-0.2*result.subs(x,o)
    return final


# 定义目标方程画图
def fangcheng1(x):
    y = x*x+1
    return y
if __name__ == '__main__':
    o = random.randint(3, 5)
    list1 = []
    list1.append(o)
    while True:
        final = content(o)
        if o - final < np.exp(-6):
            o = final
            list1.append(o)
            print(o)
            break
        else:
            o = final
            list1.append(o)
            print(o)



    # 画图
    x = Symbol('x')
    y = fangcheng()
    data1  = []
    for i in list1:
        data1.append(y.subs(x,i))
    print(data1)
    x = np.linspace(-5,5)
    fig = plt.figure(figsize=(6,6))
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = 'False'
    plt.xticks()
    plt.yticks()
    plt.plot(x,fangcheng1(x))
    plt.plot(np.array(list1),np.array(data1), linestyle='--', marker='o',drawstyle='steps-post')
    plt.title('梯度下降')
    plt.grid()
    plt.show()
