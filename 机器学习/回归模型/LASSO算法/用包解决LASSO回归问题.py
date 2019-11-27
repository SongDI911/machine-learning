import numpy as np
from sklearn.linear_model import LassoCV
import warnings

data =np.genfromtxt("./longley.csv",delimiter=',')
datax = data[1:,2:]
datay = data[1:,1]
print(datax)
print(datay)
# 创建模型
model = LassoCV()
# 消除其警告错误
warnings.filterwarnings("ignore")
# 训练数据集
model.fit(datax,datay)
# LASSO系数
print(model.alpha_)
# 矩阵相关系数
print(model.coef_)
# 模型预测
print(model.predict(datax[-2,np.newaxis]))
