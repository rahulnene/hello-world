from time import perf_counter
from sympy import *

t0 = perf_counter()
x,y = symbols('x,y')
y = x**3 - 612
y1 = y.diff(x)
x0 = 10

iterations = [x0]

n = 10
for i in range(0,n):
    xi = iterations[i]
    xnext = xi
    xnext -= (y.subs(x,xi)/y1.subs(x,xi))
    iterations.append(N(xnext))

print(iterations)

tf = perf_counter()
print(tf - t0, "seconds")
