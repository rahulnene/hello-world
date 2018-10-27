from timeit import default_timer
start = default_timer()
long = 0
dList = []
for j in range(3,999):
    if (j&2)&(j%5):dList.append(j)
for d in dList:
    oF = 1/d
    for i in range(1,1000):
        if not(10**i - 1)%d:
            if (i > long):long = i
            break
print(long,"in",(default_timer()-start),"s")