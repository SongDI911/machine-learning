from sympy import *
x = [1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2362]
y = [14.905, 14.745, 14.51, 14.365, 14.005, 13.69, 13.46, 13.14, 12.94, 12.63, 12.24, 11.99, 11.92]
'''
K = （x*y 的平均值  - x的平均值 * y的平均值）/ （x的平方的平均值 - x平均值的平方）
'''
On1 =0
for i in range(len(x)):
    On1 = On1+x[i]*y[i]
On1 = On1/len(x)
print(On1)


On2 =0
rept1 = 0
rept2 =0
for i in range(len(x)):
    rept1 = x[i]+rept1
    rept2 = y[i]+rept2
On2 = (rept1/len(x))*(rept2/len(x))
print(On2)


low1 =0
rept3=0
for i in range(len(x)):
    rept3 =x[i]**2+rept3
low1 =rept3/len(x)
print(low1)


low2 =0
rept4=0
for i in range(len(x)):
    rept4 =x[i]+rept4
low2 = (rept4/len(x))**2
print(low2)

k = (On1-On2)/(low1-low2)
print(k)


rept5=0
rept6=0
for i in range(len(x)):
    rept5 = rept5+x[i]
    rept6 = rept6+y[i]
xmean =rept5/len(x)
ymean = rept6/len(y)


b = ymean-k*xmean
print(b)


print("y = "+str(k)+"*x+"+str(b))