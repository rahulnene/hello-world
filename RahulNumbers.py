import math
import time
import numpy as np
from matplotlib import pyplot as plt

def prod_digits(n):
    s = 1
    while n:
        if n%10 != 0:
            s *= n % 10
        n //= 10
    return s

largestIn = np.arange(1,500)
outputAve = np.arange(1,500)
for item1 in largestIn:
    totalSum = 0
    largest = item1
    output1 = np.arange(1,largest)
    input1 = np.arange(1,largest)
    for x in input1:
        inFact = math.factorial(x)
        #print(inFact)
        ans = inFact
        while math.log10(ans) > 1:
            ans = prod_digits(ans)
        #print(ans)
        output1[x-1] = ans
        totalSum += ans

    #plt.plot(input1,output1)
    average = totalSum/largest
    outputAve[item1-1] = average

plt.plot(outputAve)


plt.plot(largestIn,outputAve)
plt.show()