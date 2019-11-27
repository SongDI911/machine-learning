import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report
from sklearn import tree
import graphviz
data = np.genfromtxt("./LR-testSet.csv",delimiter=',')
x_data = data[:,:2]
y_data = data[:,2]
# print(x_data)
# print(y_data)
fig = plt.figure(figsize=(6,6))
plt.scatter(x_data[:,0],x_data[:,1],c=y_data)
plt.show()

model = tree.DecisionTreeClassifier()
model.fit(x_data,y_data)

# 画决策树图
dot_data = tree.export_graphviz(model,
                                out_file=None,
                                feature_names=['x','y'],
                                class_names=['label1','label2'],
                                filled=True,
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("./double")


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



# 判断预测的程度好不好
y_train = model.predict(x_data)
print(classification_report(y_train,y_data))