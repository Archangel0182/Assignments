r=int(input('Enter no of rows: '))
c=int(input('Enter no of columns: '))
for i in range(1,r//2+1):
    s=''
    for j in range(1,2*i):
        s=s+'.|.'
    print(s.center(c,'-'))
print('WELCOME'.center(c,'-'))
for i in range(r//2,0,-1):
    s=''
    for j in range(1,2*i):
        s=s+'.|.'
    print(s.center(c,'-'))