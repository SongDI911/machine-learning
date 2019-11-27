import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import warnings
import matplotlib.pyplot as plt
data = np.genfromtxt("./LR-testSet2.txt",delimiter=',')
x_data = data[:,0:2]
y_data = data[:,2]
y_train = np.array(y_data)[:,np.newaxis]
print(x_data)
print(y_data)
model = SVC(kernel='rbf')
warnings.filterwarnings("ignore")
model.fit(x_data,y_train)
print(classification_report(model.predict(x_data),y_data))
fig = plt.figure(figsize=(6,6))
plt.scatter(x_data[:,0],x_data[:,1],c=y_data)
plt.show()

# 划分等高线图进行区分
x_min, x_max = x_data[:, 0].min() - 1, x_data[:, 0].max() + 1
y_min, y_max = x_data[:, 1].min() - 1, x_data[:, 1].max() + 1
# 生成网格矩阵
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
z = model.predict(np.c_[xx.ravel(), yy.ravel()])# ravel与flatten类似，多维数据转一维。flatten不会改变原始数据，ravel会改变原始数据
z = z.reshape(xx.shape)
# 等高线图
cs = plt.contourf(xx, yy, z)
# 样本散点图
plt.scatter(x_data[:, 0], x_data[:, 1], c=y_data)
plt.show()