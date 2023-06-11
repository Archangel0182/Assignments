i=1
while i<=5:
    if i%2:
        f=1
    else:
        f=0
    j=1
    while j<=i:
        print(f"{f} ",end=' ')
        if f==1:
            f=0
        else:
            f=1
        j=j+1
    print()
    i=i+1