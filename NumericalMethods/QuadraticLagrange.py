from time import perf_counter
from sympy import *

t0 = perf_counter()
x,y = symbols('x,y')

x0,x1,x2 = -1,2,5
y0,y1,y2 = 6,3,9

y = (((x-x1)*(x-x2))/((x0-x1)*(x0-x2)))*y0 +\
    (((x-x0)*(x-x2))/((x1-x0)*(x1-x2)))*y1 +\
    (((x-x0)*(x-x1))/((x2-x0)*(x2-x1)))*y2

print(expand(y))

tf = perf_counter()
print(tf - t0, "seconds")
