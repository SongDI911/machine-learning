import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans,DBSCAN
data = np.genfromtxt("./kmeans.txt",delimiter=' ')
print(data)
model = KMeans(n_clusters=4)
model.fit(data)
y_data = model.predict(data)
fig =plt.figure()
plt.scatter(data[:,0],data[:,1],c =y_data)
plt.show()

db_model = DBSCAN(eps=1,min_samples=4)
yy_data = db_model.fit_predict(data)
fig =plt.figure()
plt.scatter(data[:,0],data[:,1],c =yy_data)
plt.show()
