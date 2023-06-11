s=int(input('Enter size: '))
for i in range(1,s+1):
    l=[]
    n=97+s
    for j in range(1,2*i):
        if j<=i:
            n=n-1
        else:
            n=n+1
        l.append(chr(n))
    st='-'.join(l)
    print(st.center(37,'-'))
for i in range(s-1,0,-1):
    l=[]
    n=97+s
    for j in range(1,2*i):
        if j<=i:
            n=n-1
        else:
            n=n+1
        l.append(chr(n))
    st='-'.join(l)
    print(st.center(37,'-'))