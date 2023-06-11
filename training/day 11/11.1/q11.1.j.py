n=5
i=0
while i<n/2:
    j=1
    while j<=(n-i):
        print(f"{i+1}",end=' ')
        j=j+1
    print()
    i=i+1
while i<n:
    j=1
    while j<=(n-i):
        print(f"{n-i}",end=' ')
        j=j+1
    print()
    i=i+1