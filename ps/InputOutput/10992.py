n = int(input())

if n==1:
    print('*'*(2*n-1))
else:
    print(' '*(n-1)+'*')
    for i in range(1,n-1):
        print(' '*(n-1-i)+'* '+' '*(2*(i-1)) +'* ')
    print('*'*(2*n-1))