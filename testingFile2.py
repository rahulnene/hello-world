from time import clock as time
testanswer = 0
start = time()


for i in range(14,0,-1):              #13 red 2 blue
    for j in range(i,0,-1):
        # print(i,"*",j,"=",(i != j)*i*j)
        testanswer += (i != j)*i*j

time1 = time()-start
print(time1)
testanswer = 0

for i in range(14,0,-1):              #13 red 2 blue
    for j in range(i,0,-1):
        # print(i,"*",j,"=",(i != j)*i*j)
        testanswer += i*j*(i != j)

time2 = time()-start
print(time2)

print(time2/time1)