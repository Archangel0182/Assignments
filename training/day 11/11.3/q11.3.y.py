n=5
for i in range(5,0,-1):
    s=''
    for j in range(1,2*i):
        s=s+str(n)
    print(s.center(10))
    n=n-1