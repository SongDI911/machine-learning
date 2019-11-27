from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
def getdata():
    data = np.genfromtxt("./LR-testSet.csv",delimiter=',')
    xdata = data[:,0:2]
    ydata = data[:,2]
    x1 =[]
    y1 =[]
    x2 =[]
    y2 =[]
    for i in range(len(ydata)):
        if ydata[i] ==0:
            x1.append(xdata[i][0])
            y1.append(xdata[i][1])
        else:
            x2.append(xdata[i][0])
            y2.append(xdata[i][1])
    return x1,x2,y1,y2
def matplot(x1,x2,y1,y2,ws):
    x_test = [[-4], [3]]
    y_test = (-ws[0] - x_test * ws[1]) / ws[2]
    fig = plt.figure(figsize=(6,6))
    plt.scatter(x1,y1,marker='x')
    plt.scatter(x2,y2,marker='o')
    plt.plot(x_test, y_test, 'k')
    plt.show()
def solve():
    data = np.genfromtxt("./LR-testSet.csv",delimiter=',')
    xdata = data[:,0:2]
    ydata = data[:,2]
    ydata = ydata[:,np.newaxis]
    # 给样本添加偏置项
    X_data = np.concatenate((np.ones((100, 1)), xdata), axis=1)
    return X_data,ydata


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def cost(xMat, yMat, ws):
    left = np.multiply(yMat, np.log(sigmoid(xMat * ws)))
    right = np.multiply(1 - yMat, np.log(1 - sigmoid(xMat * ws)))
    return np.sum(left + right) / -(len(xMat))


def gradAscent(xArr, yArr):
    xMat = np.mat(xArr)
    yMat = np.mat(yArr)

    lr = 0.001
    epochs = 10000
    costList = []
    # 计算数据行列数
    # 行代表数据个数，列代表权值个数
    m, n = np.shape(xMat)
    # 初始化权值
    ws = np.mat(np.ones((n, 1)))

    for i in range(epochs + 1):
        # xMat和weights矩阵相乘
        h = sigmoid(xMat * ws)
        # 计算误差
        ws_grad = xMat.T * (h - yMat) / m
        ws = ws - lr * ws_grad

        if i % 50 == 0:
            costList.append(cost(xMat, yMat, ws))
    return ws, costList
if __name__ == '__main__':
    x1, x2, y1, y2= getdata()
    X_data, ydata=solve()
    ws, costList=gradAscent(X_data, ydata)
    print(ws)
    matplot(x1, x2, y1, y2,ws)
    x = np.linspace(0, 10000, 201)
    plt.plot(x, costList, c='r')
    plt.title('Train')
    plt.xlabel('Epochs')
    plt.ylabel('Cost')
    plt.show()

