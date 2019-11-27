import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans,DBSCAN
x1, y1 = datasets.make_circles(n_samples=2000, factor=0.5, noise=0.05)
x2, y2 = datasets.make_blobs(n_samples=1000, centers=[[1.2,1.2]], cluster_std=[[.1]])

x = np.concatenate((x1, x2))
plt.scatter(x[:, 0], x[:, 1], marker='o')
plt.show()

k_model = KMeans(n_clusters=3)
k_y = k_model.fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], marker='o',c=k_y)
plt.show()


db_model =DBSCAN(eps=0.2,min_samples=50)
db_y=db_model.fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], marker='o',c=db_y)
plt.show()