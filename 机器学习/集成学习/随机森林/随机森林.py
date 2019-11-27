from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import  RandomForestClassifier
import graphviz
data = np.genfromtxt("./LR-testSet2.txt",delimiter=',')
x_data = data[:,:2]
y_data = data[:,2]
x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.5)
tree_model = tree.DecisionTreeClassifier(max_depth=7,min_samples_split=4)
tree_model.fit(x_train,y_train)
print(tree_model.score(x_test,y_test))

RF_model = RandomForestClassifier(n_estimators=50)
RF_model.fit(x_train,y_train)
print(RF_model.score(x_test,y_test))
dot_data = tree.export_graphviz(tree_model,
                                out_file=None,
                                feature_names=['x1','y'],
                                class_names=['label1','label2'],
                                filled=True,
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("./Random")

