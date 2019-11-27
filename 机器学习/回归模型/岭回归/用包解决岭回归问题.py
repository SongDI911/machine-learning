import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression,RidgeCV
import  matplotlib.pyplot as plt
'''
该数据中第二列数据是真实值y
第二列到最后倒是属性值
'''
data = np.genfromtxt("./longley.csv",delimiter=',')
xdata = data[1:,2:]
ydata = data[1:,1]



def y(xdata,k,b):
   y=  k[0]*xdata[:,0]+k[1]*xdata[:,1]+k[2]*xdata[:,2]+k[3]*xdata[:,3]+k[4]*xdata[:,4]+k[5]*xdata[:,5]+b
   return y
# 用多元线性回归拟合该数据
def mode_LinearRe():
    model = LinearRegression()
    model.fit(xdata,ydata)
    k = model.coef_
    b = model.intercept_
    print(model.coef_,model.intercept_)
    fig = plt.figure(figsize=(6,6))
    plt.plot(ydata,ydata)
    plt.plot(ydata,y(xdata,k,b))
    plt.show()
def model_ridge():
    # 生成测试值，找λ值，所以从0.001到1随机生成50个数
    alphas_to_test = np.linspace(0.001,1)
    # 生成岭回归的模型，store_cv_values指是否划分数据对其计算损失函数
    model = RidgeCV(alphas=alphas_to_test,store_cv_values=True)
    # 训练数据
    model.fit(xdata,ydata)
    # 岭系数
    print(model.alpha_)
    # Loss值
    print(model.cv_values_)

    fig = plt.figure(figsize=(6,6))
    # 对于cv_values_即LOSS值，函数计算的是单个数据的LOSS值，对整个测试集的LOSS取均值
    plt.plot(alphas_to_test,model.cv_values_.mean(axis=0))
    # 找到最适合的岭系数画图
    plt.plot(model.alpha_,min(model.cv_values_.mean(axis=0)),'ro')
    plt.show()
    # 岭系数进行预测
    datapredict = [[234.289,235.6,159,107.608,1947,60.323],[259.426,232.5,145.6,108.632,1948,61.122]]
    print(xdata[2,np.newaxis])
    print(model.predict(xdata[2,np.newaxis]))
    print(model.predict(datapredict))
if __name__ == '__main__':
    mode_LinearRe()
    model_ridge()