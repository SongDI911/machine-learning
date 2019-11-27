import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
import warnings
def plotshow():
    data = np.genfromtxt("./LR-testSet2.txt",delimiter=',')
    x1 =[]
    y1 =[]
    x2 =[]
    y2 =[]
    for i in range(len(data)):
        if data[i][2] ==1:
            x1.append(data[i][0])
            y1.append(data[i][1])
        else:
            x2.append(data[i][0])
            y2.append(data[i][1])
    fig = plt.figure(figsize=(6,6))
    plt.scatter(x1,y1,marker='o')
    plt.scatter(x2,y2,marker='x')
    plt.show()
def linearLogistic():
    data = np.genfromtxt("./LR-testSet2.txt",delimiter=',')
    xdata = data[:,0:2]
    ydata = data[:,2]
    model = LogisticRegression()
    warnings.filterwarnings("ignore")
    model.fit(xdata,ydata)
    print(model.coef_)
    print(model.intercept_)
if __name__ == '__main__':
    linearLogistic()
    plotshow()

    data = np.genfromtxt("./LR-testSet2.txt",delimiter=',')
    xdata = data[:,0:2]
    ydata = data[:,2]
    Logmodel = LogisticRegression()
    warnings.filterwarnings("ignore")
    poly = PolynomialFeatures(degree=2)
    xdata = poly.fit_transform(xdata)
    Logmodel.fit(xdata,ydata)
    print(Logmodel.coef_)
    print(Logmodel.intercept_)

    prdecit =[[-0.75,1],[-0.5,0.75],[-0.25,0.5],[0,0.25],[0.25,0],[0.5,-0.25],[0.75,-0.5]]
    prdecitdata = poly.fit_transform(prdecit)
    print(Logmodel.predict(prdecitdata))
    # Logdata =Logmodel.predict(prdecitdata)
    # Logxdata =[]
    # Logydata = []
    # for i in range(len(Logdata)):
    #     if Logdata[i] ==1:
    #         Logxdata.append(prdecit[i][0])
    #         Logydata.append(prdecit[i][1])
    # fig = plt.figure(figsize=(6,6))
    # plt.plot(Logxdata,Logydata)
    # plt.show()