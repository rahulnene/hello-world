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
    k1 = f(xcurrent, ycurrent)
    k2 = f(xcurrent + (h / 2), ycurrent + (h * k1) / 2)
    k3 = f(xcurrent + (h / 2), ycurrent + (h * k2) / 2)
    k4 = f(xcurrent + h, ycurrent + h * k3)
    ycurrent += (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    yarr.append(ycurrent)
    print(N(k1),N(k2),N(k3),N(k4),N(ycurrent))
    xcurrent += h

print(xcurrent, N(ycurrent))

tf = perf_counter()
print(tf - t0, "seconds")
