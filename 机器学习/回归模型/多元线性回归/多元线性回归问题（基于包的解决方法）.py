import numpy as np
from sklearn.linear_model import LinearRegression
data = np.loadtxt("./Delivery.csv",delimiter =',')
datax1 = data[:,0]
datax2 = data[:,1]
datax = []
for i in range(len(datax1)):
    datax.append([datax1[i],datax2[i]])

# 二维的提取方式（1）
datax = np.array(datax)
# 二维的提取方式（2）
datax = data[:,:2]
print(data)
print(datax)

datay = data[:,2,np.newaxis]
model = LinearRegression()
model.fit(datax,datay)
a, b = model.coef_, model.intercept_
print('多元线性回归系数:',a)
print('多元线性回归系数:',b)
print('y={}*x1+{}*x2{}'.format(a[0][0],a[0][1],b[0]))


# 值预测
precit = [[11,4],[12,7]]
print(model.predict(precit))
