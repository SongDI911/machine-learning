from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
# 读入数据
Dtree = open(r'./AllElectronics.csv', 'r')
reader = csv.reader(Dtree)
print(reader)