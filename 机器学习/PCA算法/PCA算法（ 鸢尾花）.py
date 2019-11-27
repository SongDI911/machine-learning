from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np
import  matplotlib.pyplot as plt
'''
数据集说明
Id: 鸢尾花编号
SepaLengthCm: 花萼长度, 单位cm
SepalWidthCm: 花萼宽度, 单位cm
PetalLengthCm: 花瓣长度, 单位cm
PetalWidthCm; 花瓣宽度, 单位cm
Species: 鸢尾花种类.
'''
# 1.首先将鸢尾花的数据集标准
# 思路：一行代表一个数据集，取出每个数据集的各个属性值
def standardization(data):
    attribute1=[]
    attribute2=[]
    attribute3=[]
    attribute4=[]
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    for i in data:
        attribute1.append(i[0])
        sum1 = sum1+i[0]
        attribute2.append(i[1])
        sum2 = sum2+i[1]
        attribute3.append(i[2])
        sum3 = sum3 + i[2]
        attribute4.append(i[3])
        sum4 = sum4+i[3]
    for i in range(len(attribute1)):
        attribute1[i] = attribute1[i]-sum1/len(attribute1)
        attribute2[i] = attribute2[i] - sum2 / len(attribute1)
        attribute3[i] = attribute3[i] - sum3 / len(attribute1)
        attribute4[i] = attribute4[i] - sum4/ len(attribute1)
    standardizationdata=[]
    for i in range(len(attribute1)):
        standardizationdata.append([attribute1[i],attribute2[i],attribute3[i],attribute4[i]])
    return np.array(standardizationdata).reshape((150, 4)).T


def PCAA(n,data):
    pca = PCA(n_components=n)
    newX = pca.fit_transform(data)
    print(pca.explained_variance_ratio_)
    print("降维后的数据\n",newX)


if __name__ == '__main__':
    load_data = datasets.load_iris()
    data = load_data.data
    target = load_data.target
    # 使用PCA算法降到一维的值
    PCAA(1,data)

    print("包PCA降到2维".center(50, "="))
    PCAA(2, data)


    standardizationdata= standardization(data)
    print(standardizationdata)
    # 2.求协方差矩阵
    # 公式 1/m（A）*（A）.T
    covariance = 1 / 150 * np.dot(standardizationdata, standardizationdata.T)
    print(covariance)
    # 用包计算协方差
    cov1 = np.cov(standardizationdata)
    print("cov",covariance)

    # 3.求特征值和特征向量
    value,vector = np.linalg.eig(covariance)
    print("特征值：",value)
    print("特征向量：", vector)
    # 4.取出最大的那一列
    list1=[]
    for data in vector:
        list1.append(data[0])
    # 取出最大的两列
    list2 = []
    for data in vector:
        list2.append(data[1])
    list3 =[]
    list3.append(list1)
    list3.append(list2)
    print(list3)
    # 最后我们用P的第一行乘以数据矩阵，就得到了降维后的表示
    print(np.dot(list1,standardizationdata))

    print("自写PCA降到2维".center(50,"="))
    PCA2 = np.dot(list3, standardizationdata)
    print(PCA2)

    # 画图展示将数据降到二维
    fig =plt.figure(figsize=(6,6))
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = 'False'
    plt.scatter(PCA2[0],PCA2[1])
    plt.show()

