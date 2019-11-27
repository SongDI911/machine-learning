import numpy as np
data = np.loadtxt("./Delivery.csv",delimiter =',')
datax = np.array(data[:,:2])
datay = np.array(data[:,2])
print(datax)
print(datay)
result = np.dot( np.dot( np.linalg.inv(np.dot(datax.T,datax)),datax.T),datay)
print(result[0])
print(result[1])
