from  sklearn import  svm
import numpy as np
import  matplotlib.pyplot as plt
x = [[3, 3], [4, 3], [1, 1]]
y = [1, 1, -1]
x_figure =[]
y_figure =[]
for i in x:
    x_figure.append(i[0])
    y_figure.append(i[1])
model = svm.SVC(kernel='linear')
model.fit(x,y)
# 打印支持向量
print(model.support_vectors_)
# 打印支持向量的下标
print(model.support_)
# 打支持向量的个数
print(model.n_support_)
# 模型预测值
print(model.predict([[4,2],[4,-2]]))
# 划分界面的截距
print(model.intercept_[0])
# 划分界面的斜率
print(model.coef_[0])
x_test = np.array([[-5],[5]])
d = -model.intercept_/model.coef_[0][1]
k = -model.coef_[0][0]/model.coef_[0][1]
print(d)
print(k)
y_test = d + k*x_test
fig = plt.figure(figsize=(6,6))
plt.scatter(x_figure,y_figure,c=y)
plt.scatter([4],[2])
plt.plot(x_test,y_test)
plt.show()