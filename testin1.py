import random

dartCoordX = 0
dartCoordY = 0
inside,out = 0,0
darts = 100000

for dart in range(darts):
    dartCoordX = random.uniform(-1, 1)
    dartCoordY = random.uniform(-1, 1)
    if (dartCoordX**2 + dartCoordY**2 < 1):
        inside += 1
    else:
        out += 1

print(inside*4/darts)