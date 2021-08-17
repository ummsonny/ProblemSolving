n = int(input())

for i in range(1,n+1):
    print(' '*(n-i), end='')
    print('*'*i)
    #print(' '*(n-i)+'*'*i) 한번에 적는것도 좋다.