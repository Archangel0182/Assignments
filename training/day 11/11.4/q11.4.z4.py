n=1
for i in range(1,6):
    s=''
    for j in range(1,2*i):
        s=s+str(n)
    print(s.center(10))
    n=n+1
n=4
for i in range(4,0,-1):
    s=''
    for j in range(1,2*i):
        s=s+str(n)
    print(s.center(10))
    n=n-1