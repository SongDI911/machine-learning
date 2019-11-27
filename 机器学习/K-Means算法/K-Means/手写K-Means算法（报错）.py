import numpy as np
import matplotlib.pyplot as plt
import random
def getrandom(data,n):
    x_data = data[:, 0]
    y_data = data[:, 1]
    data_list = []
    for i, q in zip(x_data, y_data):
        data_list.append([i, q])
    choicelist = []
    num = 0
    while num < n:
        temp = random.choice(data_list)
        if temp not in choicelist:
            choicelist.append(temp)
            num = num + 1
    return choicelist,data_list
def scattershow(data):
    fig = plt.figure(figsize=(6,6))
    plt.scatter(data[:,0],data[:,1])
    plt.show()
def getdistance(choicelist,data_list,n):
    distancelist = []
    for i in range(n):
        sumlist = []
        for value in data_list:
            sumlist.append(np.sqrt(((value[0]-choicelist[i][0])**2+(value[1]-choicelist[i][1])**2)))
        distancelist.append(sumlist)
    return distancelist
def get_attrlist(distancelist):
    attr1list =[]
    attr2list =[]
    for attr1,attr2 in zip(distancelist[0],distancelist[1]):
        if attr1>=attr2:
            attr1list.append(1)
            attr2list.append(0)
        elif attr1<attr2:
            attr1list.append(0)
            attr2list.append(1)
    attrlist = []
    attrlist.append(attr1list)
    attrlist.append(attr2list)
    return attrlist
def rot(data,attrlist):
    x_data = data[:,0]
    y_data =data[:,1]
    x_sum = 0
    y_sum = 0
    for i in range(len(attrlist[0])):
        if attrlist[0][i] ==1:
            x_sum = x_sum+x_data[i]
            y_sum = y_sum+y_data[i]
    x_sum1 = 0
    y_sum1 = 0
    for i in range(len(attrlist[1])):
        if attrlist[0][i] ==1:
            x_sum1 = x_sum+x_data[i]
            y_sum1 = y_sum+y_data[i]
    x1 = [x_sum/np.array(attrlist[0]).sum(),y_sum/np.array(attrlist[0]).sum()]
    x2 = [x_sum1 / np.array(attrlist[0]).sum(), y_sum1/ np.array(attrlist[0]).sum()]
    return x1,x2
if __name__ == '__main__':
    data = np.genfromtxt("./kmeans.txt", delimiter=' ')
    scattershow(data)
    choicelist,data_list = getrandom(data,2)
    distancelist = getdistance(choicelist, data_list, 2)
    attrlist = get_attrlist(distancelist)
    x1, x2 = rot(data,attrlist)
    while True:
        choicelist = [x1, x2]
        distancelist = getdistance(choicelist,data_list,2)
        attrlist = get_attrlist(distancelist)
        temp1, temp2 = rot(data, attrlist)
        if x1 == temp1 and x2== temp2:
            print(temp1)
            print(temp2)
            break
        x1,x2 = temp1,temp2
        print(temp1)
        print(temp2)
