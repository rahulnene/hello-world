from time import perf_counter

from sympy import *

t0 = perf_counter()
x,y = symbols('x,y')

xarr = [1, 2, 3, 4]
yarr = [6, 9, 2, 5]

table = yarr
coefficients = [yarr[0]]
column = 1
points = len(xarr)


while column < points:
    scratch = []
    # print(table)
    # size = len(table)
    for i in range(0, (points - column)):
        scratch.append((table[i + 1] - table[i]) / (xarr[i + column] - xarr[i]))
    table = scratch
    coefficients.append(table[0])
    column += 1

y = coefficients[0]

for i in range(1,points):
    temp = coefficients[i]
    for k in range(0,i):
        temp *= (x - xarr[k])
    # print(temp)
    print(y)
    y += temp

print(coefficients)
print(expand(y))



tf = perf_counter()
print(tf - t0, "seconds")
