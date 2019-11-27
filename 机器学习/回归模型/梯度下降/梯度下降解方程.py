'''
sin(30)
方程：90*np.sin(2 * np.pi * a / 180) + 2/np.tan(np.pi * a)
'''
from sympy import *
import random
def fangcheng():
    a = Symbol('a')
    y = -(90*sin(2*3.14*(1/(180/a))) + 2/tan((3.14*(1/(180/a)))))
    return y
def solve(y):
    a = Symbol('a')
    result = diff(y,'a')
    return result
def solution(O1):
    a = Symbol('a')
    y = fangcheng()
    result = solve(y)
    O2 = O1-0.01*result.subs(a,O1)
    print(O2)
    return O2
if __name__ == '__main__':
    O1 = random.randint(30,31)
    while True:
        temp = solution(O1)
        if temp-O1<exp(-6):
            print(temp)
            break
        else:
            O1 = temp
