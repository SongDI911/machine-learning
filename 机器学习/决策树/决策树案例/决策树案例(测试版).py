import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
import graphviz
def getfeatureList():
    data = pd.read_csv("./AllElectronics.csv",delimiter=',')
    # 取出data中的数据放进datalist中
    datalist=[]
    for i in data:
        list1 =[]
        for value in data[i]:
            list1.append(value)
        datalist.append(list1)


    datalist = np.array(datalist)
    trainlist = datalist[1:5]
    valuelist=[]
    for i in range(len(trainlist[0])):
        valuelist.append([trainlist[0][i],trainlist[1][i],trainlist[2][i],trainlist[3][i]])
    valuelist = np.array(valuelist)
    print(valuelist)
    featureList=[]
    headers=[]
    for i in data:
        headers.append(i)
    print(headers)
    # 获取每个对象对应的属性下的值   例如：第一个对象 1,youth,high,no,fair,no
    # 获取到的dict为：{'age': 'youth', 'income': 'high', 'student': 'no', 'credit_rating': 'fair'}
    for i in range(len(valuelist)):
        rowDict = {}
        rowDict[headers[1]] = valuelist[i][0]
        rowDict[headers[2]] = valuelist[i][1]
        rowDict[headers[3]] = valuelist[i][2]
        rowDict[headers[4]] = valuelist[i][3]
        featureList.append(rowDict)
    labellist =datalist[-1]
    print(featureList)
    return featureList,labellist
if __name__ == '__main__':
    featureList,labellist = getfeatureList()

    # 把数据转换成01表示
    vec = DictVectorizer()
    x_data = vec.fit_transform(featureList).toarray()
    print("x_data: " + str(x_data))
    # 打印属性名称
    print(vec.get_feature_names())
    # 把标签转换成01表示
    lb = preprocessing.LabelBinarizer()
    y_data = lb.fit_transform(labellist)
    print(lb.classes_)
    print(y_data)
    # 创建决策树模型  entropy为ID3算法
    model = tree.DecisionTreeClassifier(criterion='entropy')
    # 输入数据建立模型
    model.fit(x_data, y_data)



    # 测试
    x_test = x_data[0]
    print("x_test: " + str(x_test))
    predict = model.predict(x_test.reshape(1, -1))
    print("predict: " + str(predict))

    # 导出决策树
    # pip install graphviz
    # http://www.graphviz.org/
    # 名称：get_feature_names,分类名称：classes_
    dot_data = tree.export_graphviz(model,
                                    out_file=None,
                                    feature_names=vec.get_feature_names(),
                                    class_names=lb.classes_,
                                    filled=True,
                                    rounded=True,
                                    special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.render('./computer')

    with open("./computer") as f:
        dot_graph = f.read()
    dot = graphviz.Source(dot_graph)
    dot.view()