import random

pyramid = [1,2,3,4]
cubic = [1,2,3,4,5,6]
sumPyr = 0
sumCub = 0
favorable = 0
total = 100000

for i in range (0,total):
    for throw in range(0, 9):
        sumPyr += random.choice(pyramid)
    for throw in range(0, 6):
        sumCub += random.choice(cubic)
    #print(sumPyr,sumCub)
    if sumPyr > sumCub:
        favorable += 1
    sumCub = 0
    sumPyr = 0

print(favorable)