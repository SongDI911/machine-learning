import numpy as np
import matplotlib.pyplot as plt
#输入数据
X = np.array([[1,0,0],
              [1,0,1],
              [1,1,0],
              [1,1,1]])
#标签
Y = np.array([[1],
              [1],
              [-1],
              [-1]])
# 异或过程的Y
# Y = np.array([[-1],
#               [1],
#               [1],
#               [-1]])
# [0,1]-0.5 = [-0.5,0.5] *2 =[-1,1]
W = (np.random.random([3,1]) -0.5)*2
# 定义学习率
lr =0.01
print(W)
O =0


def update():
    global W,X,Y,lr
    O = np.sign(np.dot(X,W))
    W_U = lr*np.dot(X.T,Y-O)/len(X)
    W =W+W_U

for i in range(100):
    update()#更新权值
    print(W)#打印当前权值
    print(i)#打印迭代次数
    O = np.dot(X,W)#计算当前输出
    if(O == Y).all(): #如果实际输出等于期望输出，模型收敛，循环结束
        print('Finished')
        print('epoch:',i)
        break
#正样本
x1 = [0,1]
y1 = [1,0]
#负样本
x2 = [0,1]
y2 = [0,1]

#计算分界线的斜率以及截距
k = -W[1]/W[2]
d = -W[0]/W[2]
print('k=',k)
print('d=',d)

xdata = (-2,3)

plt.figure()
plt.plot(xdata,xdata*k+d,'r')
plt.scatter(x1,y1,c='b')
plt.scatter(x2,y2,c='y')
plt.show()