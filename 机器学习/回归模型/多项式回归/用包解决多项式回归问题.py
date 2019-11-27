import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# 提取数据
data = np.genfromtxt('./job.csv',delimiter = ",")
xdata = data[1:,1]
ydata = data[1:,2]
xlist =[]
ylist = []
for i in xdata:
    xlist.append(i)
for i in ydata:
    ylist.append(i)
xdata = np.array(xlist)
ydata = np.array(ylist)
xdata = xdata[:,np.newaxis]
ydata = ydata[:,np.newaxis]


def y(k, b, x):
    y = k * x + b
    return y
def function1():
    model = LinearRegression()
    model.fit(xdata,ydata)
    k,b = model.coef_,model.intercept_
    print('一元线性回归系数:',k)
    print('一元线性回归截距:',b)
    x = np.linspace(1,10)
    fig = plt.figure(figsize=(6,6))
    plt.scatter(xlist,ylist)
    plt.plot(x,y(k[0][0],b[0],x))
    plt.show()

def function2():
    # 定义多项式回归,degree的值可以调节多项式的特征
    poly_reg  = PolynomialFeatures(degree=5)
    # 特征处理
    x_poly = poly_reg.fit_transform(xdata)
    # 定义回归模型
    lin_reg = LinearRegression()
    # 训练模型
    lin_reg.fit(x_poly, ydata)
    k,b = lin_reg.intercept_,lin_reg.coef_
    print('多项式回归截距：',k)
    print('多项式回归系数：',b)

    predictlist=[[10],[11]]
    print('多项式回归预测：',lin_reg.predict(poly_reg.fit_transform(predictlist)))
    fig2 = plt.figure(figsize=(6,6))
    plt.scatter(xlist, ylist)
    plt.plot(xlist, lin_reg.predict(x_poly), c='r')
    plt.title('Truth or Bluff (Polynomial Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()

if __name__ == '__main__':
    function1()
    function2()