# def ans(x):
#     import math
#     i=1
#     sum2=0
#     sum5=0

#     while math.pow(5,i)<=x:
#         sum5+=(x//math.pow(5,i))
#         i+=1
#     i=1
#     while math.pow(2,i)<=x:
#         sum2+=(x//math.pow(2,i))
#         i+=1

#     return [int(sum2),int(sum5)]

# n,m = map(int, input().split())


# cnt2 = ans(n)[0]-ans(m)[0]-ans(n-m)[0]
# cnt5 = ans(n)[1]-ans(m)[1]-ans(n-m)[1]
# #print(cnt2) if cnt2<=cnt5 else print(cnt5)
# print(min(cnt2,cnt5))

def ans(x):
    n=x
    sum2=0

    while(n!=0):
        n = n//2
        sum2+=n
    n=x
    sum5=0
    while(n!=0):
        n = n//5
        sum5+=n


    return [sum2,sum5]

n,m = map(int, input().split())


cnt2 = ans(n)[0]-ans(m)[0]-ans(n-m)[0]
cnt5 = ans(n)[1]-ans(m)[1]-ans(n-m)[1]
print(min(cnt2,cnt5))

#https://tmdrl5779.tistory.com/95 : while문을 바로 위와같이 쓸 수 있는 이유 





