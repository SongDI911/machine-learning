import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_gaussian_quantiles
from sklearn.metrics import classification_report
def plot(model):
    # 划分等高线图进行区分
    x_min, x_max = x_data[:, 0].min() - 1, x_data[:, 0].max() + 1
    y_min, y_max = x_data[:, 1].min() - 1, x_data[:, 1].max() + 1
    # 生成网格矩阵
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))
    z = model.predict(np.c_[xx.ravel(), yy.ravel()])  # ravel与flatten类似，多维数据转一维。flatten不会改变原始数据，ravel会改变原始数据
    z = z.reshape(xx.shape)
    # 等高线图
    cs = plt.contourf(xx, yy, z)
    # 样本散点图
    plt.scatter(x_data[:, 0], x_data[:, 1], c=y_data)
    plt.show()

# 生成数据
# 生成2维正态分布，生成的数据按分位数分为两类，500个样本,2个样本特征
x1, y1 = make_gaussian_quantiles(n_samples=500, n_features=2,n_classes=2)
# 生成2维正态分布，生成的数据按分位数分为两类，400个样本,2个样本特征均值都为3
x2, y2 = make_gaussian_quantiles(mean=(3, 3), n_samples=500, n_features=2, n_classes=2)
# 将两组数据合成一组数据
x_data = np.concatenate((x1, x2))
y_data = np.concatenate((y1, - y2 + 1))



model_tree = tree.DecisionTreeClassifier(max_depth=3)
model_tree.fit(x_data,y_data)
print(model_tree.score(x_data,y_data))

fig = plt.figure(figsize=(6,6))
plot(model_tree)
plt.show()


# n_estimators迭代次数
model_Ada = AdaBoostClassifier(model_tree,n_estimators=10)
model_Ada.fit(x_data,y_data)
print(model_Ada.score(x_data,y_data))
plot(model_Ada)
plt.show()