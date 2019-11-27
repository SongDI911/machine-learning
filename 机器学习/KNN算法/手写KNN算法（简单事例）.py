import matplotlib.pyplot as plt
import numpy as np
def Mashow():
    # 已知分类的数据
    x1 = np.array([3,2,1])
    y1 = np.array([104,100,81])
    x2 = np.array([101,99,98])
    y2 = np.array([10,5,2])
    predcitx = np.array([18])
    predcity = np.array([90])
    fig = plt.figure(figsize=(6,6))
    plt.scatter(x1,y1)
    plt.scatter(x2,y2)
    plt.scatter(predcitx,predcity)
    plt.show()
def findKNN(n):
    # 已知分类的数据
    x1 = np.array([3,2,1])
    y1 = np.array([104,100,81])
    x2 = np.array([101,99,98])
    y2 = np.array([10,5,2])
    category=[1,1,1,0,0,0]

    predcitx = np.array([18])
    predcity = np.array([90])

    xdata=[]
    ydata=[]
    for i in range(len(x1)):
        xdata.append(x1[i])
        ydata.append(y1[i])
    for i in range(len(x2)):
        xdata.append(x2[i])
        ydata.append(y2[i])

    score =[]
    for i in range(len(xdata)):
        score.append(np.sqrt((predcitx[0]-xdata[i])**2+(predcity[0]-ydata[i])**2))

    sortedDistances = np.array(score).argsort()
    print(sortedDistances)
    finnallist=[]
    for i in range(n):
        finnallist.append(category[sortedDistances[i]])
    print(finnallist)
    sum1 =0
    sum0 = 0
    for i in finnallist:
        if i == 1:
            sum1 = sum1+1
        elif i ==0:
            sum0 = sum0+1


    if sum1>sum0:
        print("类别为A")
    elif sum1<sum0:
        print("类别为B")
if __name__ == '__main__':
    Mashow()
    findKNN(3)