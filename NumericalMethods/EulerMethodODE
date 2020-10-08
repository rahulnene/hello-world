from time import perf_counter
from sympy import *

t0 = perf_counter()
x, y = symbols('x,y')

diffy = x
x0 = 1
y0 = 2
h = 1
xf = 4


ycurrent = y0
xcurrent = x0
yarr = [y0]
def f(x0,y0):
    return diffy.subs({x:x0, y: y0})

while xcurrent < xf:
    ycurrent += h * f(xcurrent,ycurrent)
    yarr.append(ycurrent)
    xcurrent += h

print(xcurrent, N(ycurrent))


tf = perf_counter()
print(tf - t0, "seconds")
