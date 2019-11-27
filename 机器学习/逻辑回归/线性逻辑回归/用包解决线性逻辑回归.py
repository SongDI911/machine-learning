import numpy as np
import matplotlib.pyplot as plt
# 用于做评估
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
import warnings
# 提取数据
data = np.genfromtxt("./LR-testSet.csv",delimiter=',')
xdata = data[:,0:2]
ydata = data[:,2]
x1 =[]
y1 =[]
x2 =[]
y2 =[]
for i in range(len(ydata)):
    if ydata[i] == 0:
        x1.append(xdata[i][0])
        y1.append(xdata[i][1])
    else:
        x2.append(xdata[i][0])
        y2.append(xdata[i][1])

model = LogisticRegression()
warnings.filterwarnings("ignore")
model.fit(xdata,ydata)
print(model.intercept_)
print(model.coef_)
print(xdata[:,0]*model.coef_[0][0]+model.coef_[0][1]*xdata[:,1]+model.intercept_[0])

fig = plt.figure(figsize=(6,6))
plt.scatter(x1,y1,marker='x')
plt.scatter(x2,y2,marker='o')
x_test = np.array([[-4],[3]])
y_test = (-model.intercept_ - x_test*model.coef_[0][0])/model.coef_[0][1]
plt.plot(x_test, y_test, 'k')
plt.show()



fig = plt.figure(figsize=(6,6))
plt.scatter(y1,x1,marker='x')
plt.scatter(y2,x2,marker='o')
x_test2 = np.array([[-2.5],[15]])
y_test2 = (-model.intercept_ - x_test2*model.coef_[0][1])/model.coef_[0][0]
plt.plot(x_test2, y_test2, 'k')
plt.show()
