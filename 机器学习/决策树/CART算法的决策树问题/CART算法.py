import numpy as np
from sklearn import tree
import graphviz
data = np.genfromtxt("./cart.csv",delimiter=',')
x_data = data[1:,1:-1]
y_data = data[1:,-1]
print(x_data)
print(y_data)
model = tree.DecisionTreeClassifier()
model.fit(x_data,y_data)
dot_data = tree.export_graphviz(model,
                                out_file = None,
                                feature_names = ['house_yes','house_no','single','married','divorced','income'],
                                class_names = ['no','yes'],
                                filled = True,
                                rounded = True,
                                special_characters = True)
graph = graphviz.Source(dot_data)
graph.render("./cart")

# with open("./cart") as f:
#     cartdata = f.read()
# dot = graphviz.Source(cartdata)
# dot.view()