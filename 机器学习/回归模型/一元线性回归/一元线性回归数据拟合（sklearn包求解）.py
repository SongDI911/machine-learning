from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
# 导入需要拟合的数据
x = np.array([1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2362])
y = np.array([14.905, 14.745, 14.51, 14.365, 14.005, 13.69, 13.46, 13.14, 12.94, 12.63, 12.24, 11.99, 11.92])
# 我们将数据放入包中拟合会出现维度问题，所以在使用过程中要该维度如下：（不可以使用reshape（1，-1）是原则性错误）
datax = x[:,np.newaxis]
datay = y[:,np.newaxis]
print(datax)
model = LinearRegression()
model.fit(datax,datay)
# 求斜率为,coef_  求截距.intercept_
a, b = model.coef_, model.intercept_
print('一元线性回归系数:',a[0][0])
print('一元线性回归截距:',b[0])
def y1(a,b,x):
    y = a[0][0]*x+b[0]
    return y
x1= np.linspace(1800,2300)
fig = plt.figure(figsize=(6,6))
ax1 = fig.add_subplot(2,1,1)
plt.plot(x,y,'b.')
ax2 = fig.add_subplot(2,1,2)
plt.plot(x1,y1(a,b,x1))
plt.show()

# 值预测
precit = [[11]]
print(model.predict(precit))

print("y = "+str(a[0][0])+"*x+"+str(b[0]))

