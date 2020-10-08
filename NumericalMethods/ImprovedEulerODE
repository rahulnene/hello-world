from time import perf_counter
from sympy import *

t0 = perf_counter()
x, y = symbols('x,y')

diffy = x
x0 = 1
y0 = 1
h = 1/10
xf = 4


ycurrent = y0
xcurrent = x0
yarr = [y0]
def f(x0,y0):
    return diffy.subs({x:x0, y: y0})

while xcurrent < xf:
    ytemp = ycurrent + h * f(xcurrent,ycurrent)
    ycurrent += (h/2) * (f(xcurrent,ycurrent) + f(xcurrent+h,ytemp))
    yarr.append(ycurrent)
    xcurrent += h

print(xcurrent, N(ycurrent))


tf = perf_counter()
print(tf - t0, "seconds")
