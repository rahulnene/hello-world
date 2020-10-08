from time import perf_counter
from sympy import *

t0 = perf_counter()
x, y = symbols('x,y')

diffy = x * sin(x)
x0 = 0
y0 = 1
h = 1
xf = 4

ycurrent = y0
xcurrent = x0
yarr = [y0]


def f(x0, y0):
    return diffy.subs({x: x0, y: y0})


while xcurrent < xf:
    k1 = h*f(xcurrent, ycurrent)
    k2 = h*f(xcurrent + (h / 2), ycurrent + k1/2)
    k3 = h*f(xcurrent + h, ycurrent -k1 + 2*k2)
    ycurrent += (1 / 6) * (k1 + 4 * k2 + k3)
    yarr.append(ycurrent)
    xcurrent += h

print(xcurrent, N(ycurrent))

tf = perf_counter()
print(tf - t0, "seconds")
