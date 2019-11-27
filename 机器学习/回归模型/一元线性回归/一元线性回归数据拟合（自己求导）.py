from sympy import *
import  random
import numpy as np


def result(O0,O1):
    x = [1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2362]
    y = [14.905, 14.745, 14.51, 14.365, 14.005, 13.69, 13.46, 13.14, 12.94, 12.63, 12.24, 11.99, 11.92]

    for i in range(len(x)):
        resultx = O1*x[i]+O0-y[i]
        resulty = (O1*x[i]+O0-y[i])*x[i]
    O0 = O0-0.2*(1/len(x))*resultx
    O1 = O1-0.2*(1/len(x))*resulty
    return O0,O1


if __name__ == '__main__':
    O0 = random.randint(-1,1)
    O1 = random.randint(1, 3)
    while True:
        temp0,temp1=result(O0,O1)
        if (O0-temp0 <np.exp(-6)) & (O1-temp1<np.exp(-6)):
            print('最后的O0',temp0)
            print('最后的O1',temp1)
            break
        else:
            O0 =temp0
            O1 =temp1