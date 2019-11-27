import numpy as np
from numpy import genfromtxt
from sklearn.linear_model import ElasticNetCV
import warnings
# 读入数据
data = genfromtxt(r"longley.csv",delimiter=',')
# 切分数据
x_data = data[1:,2:]
y_data = data[1:,1]
# 创建模型
model = ElasticNetCV()
warnings.filterwarnings("ignore")
# 训练数据集
model.fit(x_data,y_data)
# 弹性网的λ
print(model.alpha_)
# 预测值的系数w
print(model.coef_)