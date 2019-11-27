# 导入算法包以及数据集
from sklearn import neighbors
from sklearn import datasets
from sklearn.ensemble import BaggingClassifier
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
iris = datasets.load_iris()
iris_data = iris.data
iris_target = iris.target
iris_data = iris_data[:,:2]
x_train,x_test,y_train,y_test = train_test_split(iris_data, iris_target)


knn_model = neighbors.KNeighborsClassifier(n_neighbors=3)
knn_model.fit(x_train,y_train)
print("KNN-Model",classification_report(knn_model.predict(x_test),y_test))


tree_model = tree.DecisionTreeClassifier()
tree_model.fit(x_train,y_train)
print("Tree-Model",classification_report(tree_model.predict(x_test),y_test))
def plot(model):
    # 获取数据值所在的范围
    x_min, x_max = iris_data[:, 0].min() - 1, iris_data[:, 0].max() + 1
    y_min, y_max = iris_data[:, 1].min() - 1, iris_data[:, 1].max() + 1

    # 生成网格矩阵
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))
    z = model.predict(np.c_[xx.ravel(), yy.ravel()])# ravel与flatten类似，多维数据转一维。flatten不会改变原始数据，ravel会改变原始数据
    z = z.reshape(xx.shape)
    # 等高线图
    cs = plt.contourf(xx, yy, z)
plot(knn_model)
plt.scatter(iris_data[:,0],iris_data[:,1],c=iris_target)
plt.show()

plot(tree_model)
plt.scatter(iris_data[:,0],iris_data[:,1],c=iris_target)
plt.show()

bagknn = BaggingClassifier(knn_model,n_estimators=100)
bagknn.fit(x_train,y_train)
print("Bag-Model-Knn",classification_report(bagknn.predict(x_test),y_test))
plot(bagknn)
plt.scatter(iris_data[:,0],iris_data[:,1],c=iris_target)
plt.show()


bagtree = BaggingClassifier(tree_model,n_estimators=100)
bagtree.fit(x_train,y_train)
print("Bag-Model-Tree",classification_report(bagtree.predict(x_test),y_test))
plot(bagtree)
plt.scatter(iris_data[:,0],iris_data[:,1],c=iris_target)
plt.show()


ploy_model = PolynomialFeatures(degree=2)
x_train = ploy_model.fit_transform(x_train)
x_test = ploy_model.fit_transform(x_test)
log_model = LogisticRegression()
warnings.filterwarnings("ignore")
log_model.fit(x_train,y_train)
print(classification_report(log_model.predict(x_test),y_test))


baglog = BaggingClassifier(log_model,n_estimators=100)
baglog.fit(x_train,y_train)
print(classification_report(log_model.predict(x_test),y_test))