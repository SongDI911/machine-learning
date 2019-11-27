from sklearn import datasets
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
import numpy as np
import warnings
iris_data = datasets.load_iris()
x_data = iris_data.data
y_data = iris_data.target
x_data = x_data[:,1:3]

cf1 = LogisticRegression()
warnings.filterwarnings("ignore")
cf2 = DecisionTreeClassifier()
warnings.filterwarnings("ignore")
cf3 = KNeighborsClassifier(n_neighbors=1)
warnings.filterwarnings("ignore")

sclf = VotingClassifier([('Logist',cf1),('Tree',cf2),("KNN",cf3)])
warnings.filterwarnings("ignore")




for clf,name in zip([cf1,cf2,cf3,sclf],['Logist','Tree','KNN','Voting']):
    sorces = model_selection.cross_val_score(clf,x_data,y_data,cv=3,scoring='accuracy')
    warnings.filterwarnings("ignore")
    print(name,":",'{}'.format(sorces.mean()))