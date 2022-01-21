n, m = map(int, input().split())
coin_type=[]
for i in range(n):
    coin_type.append(int(input()))

d=[10001]*(m+1)

d[0]=0
for i in range(n):
    for j in range(coin_type[i], m+1):
        if d[j-coin_type[i]]!=10001:
            d[j] = min(d[j], d[j-coin_type[i]]+1)

if d[m]==10001:
    print('-1')
else:
    print(d[m])
