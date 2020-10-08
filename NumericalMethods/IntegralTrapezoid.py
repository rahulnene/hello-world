from time import perf_counter

from sympy import *

t0 = perf_counter()
x,y = symbols('x,y')

xarr = [0,0.5,1]

print(xarr)
funcy = x**2

def y(x0):
    return funcy.subs(x,x0)

points = len(xarr)

integral = 0
for i in range(1,points):
    integral += 0.5 * (y(xarr[i]) + y(xarr[i - 1])) * (xarr[i] - xarr[i - 1])

print(integral)



tf = perf_counter()
print(tf - t0, "seconds")
