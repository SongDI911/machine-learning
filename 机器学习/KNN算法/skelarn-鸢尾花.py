from  sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
data = datasets.load_iris()
x_train = data.data[40:]
y_train = data.target[40:]
x_test = data.data[:40]
y_test = data.data[:40]
model = KNeighborsClassifier(n_neighbors=3)
prediction = model.fit(x_train,y_train)
print(model.predict(x_test))