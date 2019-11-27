import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
import graphviz
data = np.genfromtxt("./data.csv",delimiter=',')
x_data = data[:,0]
y_data = data[:,1]
x_data = x_data[:,np.newaxis]
y_data = y_data[:,np.newaxis]
fig = plt.figure(figsize=(6,6))
plt.scatter(x_data,y_data)
plt.show()

model = tree.DecisionTreeRegressor()
model.fit(x_data,y_data)

dot_data = tree.export_graphviz(model,
                                out_file=None,
                                feature_names=['x'],
                                class_names=['label1'],
                                filled=True,
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('./tree_model')



x_test = np.linspace(20,80,100)
x_test = x_test[:,np.newaxis]
print(x_test)
y_test = model.predict(x_test)
fig = plt.figure(figsize=(6,6))
plt.scatter(x_data,y_data)
plt.plot(x_test,y_test,'r')
plt.show()
