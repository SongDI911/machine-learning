from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
def KMeansdivide(data,n):
    model = KMeans(n_clusters=n)
    model.fit(data)
    centers = model.cluster_centers_
    print('中心点坐标',centers)
    result = model.predict(data)
    print('预测结果',result)
    result = model.labels_
    print('分类结果',result)
    print('平方误差和',model.inertia_)
    # 画出各个数据点，用不同颜色表示分类
    mark = ['or', 'ob', 'og', 'oy']
    for i, d in enumerate(data):
        plt.plot(d[0], d[1], mark[result[i]])

    # 画出各个分类的中心点
    mark = ['*r', '*b', '*g', '*y']
    for i, center in enumerate(centers):
        plt.plot(center[0], center[1], mark[i], markersize=20)

    plt.show()
if __name__ == '__main__':
    data = np.genfromtxt("./kmeans.txt",delimiter=' ')
    KMeansdivide(data, 4)