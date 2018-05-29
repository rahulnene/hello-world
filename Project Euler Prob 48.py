import time
start = time.clock()
sum = 0
for i in range (1,1001):
    sum += i**i

print (sum%10000000000)
print (time.clock() - start)