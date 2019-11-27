from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt("./kmeans.txt",delimiter=' ')
SSE=[]
x =[]
# 绘制SSE,平方误差和的肘部点为分类值
for n in range(9):
    model = KMeans(n_clusters=n+1)
    model.fit(data)
    centers = model.cluster_centers_
    print('中心点坐标',centers)
    result = model.predict(data)
    print('预测结果',result)
    result = model.labels_
    print('分类结果',result)
    print('平方误差和',model.inertia_)
    SSE.append(model.inertia_)
    x.append(n+1)



    
fig = plt.figure(figsize=(6,6))
plt.plot(x,SSE)
plt.show()