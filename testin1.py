n = 1
counter = 0
for b in range(1,500):
    for a in range(1,b+1):
        LHS = (1/a)+ (1/b)
        p = (LHS)*(10**n)
        if not p%1:
            counter += 1
            print(a,b,p,counter)