'''
数据集：
1800	29.81
1850	29.49
1900	29.02
1950	28.73
200	    28.01
2050	27.38
2100	26.92
2150	26.28
2200	25.88
2250	25.26
2300	24.48
2350	23.98
2362	23.84

'''
from sympy import *
import  random
import numpy as np
def fangcheng(x,y):
    f =0
    o1 = Symbol('o1')
    o2 = Symbol('o2')
    for i in range(len(x)):
        f = f+(x[i]*o1+o2-y[i])**2
    f = 1/(2*len(x)) *f
    return f

def solve(f):
    o1 = Symbol('o1')
    o2 = Symbol('o2')
    resultx = diff(f,o1)
    resulty = diff(f,o2)
    return resultx,resulty

def final(O1,O2):
    x = [1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2362]
    y = [14.905, 14.745, 14.51, 14.365, 14.005, 13.69, 13.46, 13.14, 12.94, 12.63, 12.24, 11.99, 11.92]
    f = fangcheng(x,y)
    resultx, resulty = solve(f)
    o1 = Symbol('o1')
    o2 = Symbol('o2')
    temp0 = O1-0.001*resultx.subs({o1:O1,o2:O2})
    temp1 = O2-0.001*resulty.subs({o1:O1,o2:O2})
    print(temp0)
    print(temp1)
    return temp0,temp1


if __name__ == '__main__':
    O1 = random.randint(0,2)
    O2 = random.randint(0,3)
    O1,O2 = final(O1,O2)
    O1,O2 = final(O1, O2)

    # temp0,temp1 = final(O1,O2)
    # print(temp0)
    # print(temp1)
    # temp3, temp4 = final(temp0, temp1)
    # print(temp3)
    # print(temp4)
    # while True:
    #     temp0, temp1 = final(O1, O2)
    #     print(temp0)
    #     print(temp1)
    #     print('-----------')
    #     print(O1 - temp0 )
    #     print(O2 - temp1)
    #     if (O1 - temp0 < np.exp(-6)) & (O2 - temp1 < np.exp(-6)):
    #         print('最终O1',temp0)
    #         print('最终O2',temp1)
    #         break
    #     else:
    #         O1 = temp0
    #         O2 = temp1


