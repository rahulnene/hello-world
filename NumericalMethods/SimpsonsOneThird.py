from time import perf_counter
from sympy import *

t0 = perf_counter()
x, y = symbols('x,y')

a, b = 1, 2
n = 100
h = (b - a) / n
funcy = sin(x)


def y(x0):
    return funcy.subs(x, x0)


xarr = set()
for i in [x / (1 / h) for x in range(ceiling(a / h), ceiling(b / h + h))]:
    xarr.add(i)
xarr.add(a)
xarr.add(b)
xarr = sorted(list(xarr))
yarr = []

for i in range(0, n + 1):
    yarr.append(y(xarr[i]))


def integrate():
    ans = yarr[0] + yarr[n]
    for odd in range(1, n, 2):
        ans += 4 * yarr[odd]
    for even in range(2, n - 1, 2):
        ans += 2 * yarr[even]
    ans *= h / 3
    return ans


print(integrate())

tf = perf_counter()
print(tf - t0, "seconds")
