from sklearn import datasets
import  numpy as np
def findirs(n,target,argsortlist):
    targetlist =[]
    for i in range(n):
        targetlist.append(target[argsortlist[i]])
    sum0 =0
    sum1 =0
    sum2 =0
    for i in targetlist:
        if i == 0:
            sum0 = sum0+1
        elif i ==1:
            sum1 =sum1+1
        elif i==2:
            sum2 = sum2+1
    sortlsit =np.array([sum0,sum1,sum2])
    num = sortlsit.argsort()[-1]
    if num ==0:
        print("分类0")
    elif num ==1:
        print("分类1")
    elif num ==2:
        print("分类2")

if __name__ == '__main__':
    data1 = datasets.load_iris()
    data = data1.data
    target = data1.target
    xtest = [5, 3, 1.5, 0.3]
    score = []
    for content in data:
        score.append(np.sqrt((content[0] - xtest[0]) ** 2 + (content[1] - xtest[1]) ** 2 + (content[2] - xtest[2]) ** 2
                             + (content[3] - xtest[3]) ** 2))
    argsortlist = np.array(score).argsort()
    findirs(3,target,argsortlist)