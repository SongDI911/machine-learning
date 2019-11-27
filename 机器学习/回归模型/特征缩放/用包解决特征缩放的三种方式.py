from sklearn import preprocessing
import numpy as np
x = [1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2362]
y = [14.905, 14.745, 14.51, 14.365, 14.005, 13.69, 13.46, 13.14, 12.94, 12.63, 12.24, 11.99, 11.92]
xdata = np.array(x)
xdata = xdata[:,np.newaxis]


# MinMaxScaler 即：rescaling 将其缩放到（0，1）
model = preprocessing.MinMaxScaler()
x_train = model.fit_transform(xdata)
print("rescaling 将其缩放到（0，1）".center(50,"=")+'\n',x_train)


# MaxAbsScaler 即：mean normalization 将其缩放到（-1,1）
model2 = preprocessing.MaxAbsScaler()
x_train = model2.fit_transform(xdata)
print("mean normalization 将其缩放到（-1，1）".center(50,"=")+'\n',x_train)



# standardization 将其缩放至平均值为0,方差为1：特征缩放
x_scale = preprocessing.scale(xdata)
print("standardization 将其缩放至平均值为0,方差为1".center(50,"=")+'\n',x_scale)



# 标准缩放
scaler = preprocessing.StandardScaler(with_mean=False,).fit(xdata)
scaler_data = scaler.transform(xdata)
print("标准缩放".center(50,"=")+'\n',scaler_data)