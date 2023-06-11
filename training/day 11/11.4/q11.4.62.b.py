for i in range(1,8):
    for j in range(1,8):
        if i in (1,7):
            print('*',end='')
        elif j in (1,7):
            print('*',end='')
        else:
            print(' ',end='')
    print()