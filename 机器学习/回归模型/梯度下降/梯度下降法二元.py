import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sympy import *
import random
import matplotlib.pyplot as plt

# 定义目标方程求导
def fangcheng():
    x = Symbol('x')
    y = Symbol('y')
    z = x*x+y*y
    return z


#求解J(O) 即：原函数的导数
def solve(z):
    x = Symbol('x')
    y = Symbol('y')
    resultx = diff(z,x)
    resulty = diff(z,y)
    return resultx,resulty

# 定义整个O(0) -aJ(O)
def content(ox,oy):
    z = fangcheng()
    resultx,resulty = solve(z)
    x = Symbol('x')
    y = Symbol('y')
    resultx.subs('x', 1)
    resulty.subs('y', 1)
    # 设定步长为0.2
    finalx = ox-0.2*resultx.subs('x',ox)
    finaly = oy-0.2*resulty.subs('y',oy)
    return finalx,finaly
if __name__ == '__main__':
    ox = random.randint(3, 5)
    oy = random.randint(3, 5)
    list1 = []
    list2 = []
    list1.append(ox)
    list2.append(oy)
    while True:
        finalx,finaly = content(ox,oy)
        if (ox - finalx < np.exp(-6)) & (oy - finaly < np.exp(-6)):
            ox = finalx
            list1.append(ox)
            print("x的值为{}".format(ox))
            oy = finaly
            list2.append(oy)
            print("y的值为{}".format(oy))
            break
        else:
            ox = finalx
            list1.append(ox)
            print("x的值为{}".format(ox))
            oy = finaly
            list2.append(oy)
            print("y的值为{}".format(oy))

    # print(len(list1))
    # print(len(list2))

    # 画图
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i]*list1[i]+list2[i]*list2[i])
    print(list3)
    x = np.arange(-4, 4, 0.25)
    y = np.arange(-4, 4, 0.25)
    x, y = np.meshgrid(x, y)
    # z = np.sqrt(x**2+y**2)
    z = x ** 2 + y ** 2
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = 'False'
    ax.grid()
    ax.set_xlabel('测试数据1')
    ax.set_ylabel('测试数据2')
    ax.set_zlabel('测试数据3')
    ax.contourf(x, y, z, zdir='z', offset=-2, cmap='rainbow')
    # x1 = np.array([list1])
    # y1 = np.array([list2])
    # z1 = np.array([list3])
    # xx, y1 = np.meshgrid(x1, y1)
    # x1, z1 = np.meshgrid(x1, z1)
    ax.plot(list1, list2, list3, "bo--")
    plt.show()