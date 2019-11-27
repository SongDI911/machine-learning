# 导入算法包以及数据集
import numpy as np
import warnings
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.naive_bayes import MultinomialNB,BernoulliNB,GaussianNB
iris_data = datasets.load_iris()
x_data = iris_data.data
y_data = iris_data.target
x_train,x_test,y_train,y_test = train_test_split(x_data,y_data)
# 多项式型
mul_model = MultinomialNB()
mul_model.fit(x_train,y_train)
print("多项式类型",classification_report(mul_model.predict(x_test),y_test))
print("多项式类型混淆矩阵\n",confusion_matrix(mul_model.predict(x_test),y_test))
# 伯努利型
ber_model = BernoulliNB()
warnings.filterwarnings("ignore")
ber_model.fit(x_train,y_train)
print("伯努利类型",classification_report(ber_model.predict(x_test),y_test))
print("伯努利类型混淆矩阵\n",confusion_matrix(ber_model.predict(x_test),y_test))
# 高斯类型
gau_model=GaussianNB()
gau_model.fit(x_train,y_train)
print("高斯类型",classification_report(gau_model.predict(x_test),y_test))
print("高斯类型混淆矩阵\n",confusion_matrix(gau_model.predict(x_test),y_test))