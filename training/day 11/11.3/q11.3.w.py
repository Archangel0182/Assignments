for i in range(1,6):
    st=''
    n=6
    for j in range(1,2*i):
        if j<=i:
            n=n-1
        else:
            n=n+1
        st=st+str(n)
    print(st.center(10))