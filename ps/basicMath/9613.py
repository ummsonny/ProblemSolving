import sys
import itertools

def gcd(a,b):
    if(b==0):
        return a;
    else:
        return gcd(b, a%b)

n = int(input())

#그냥 풀이 
# for i in range(n):
#     sum=0
#     ans = list(map(int,sys.stdin.readline().split()))
#     arr = ans[1:]
#     for i in range(ans[0])://조합을 for문으로 구하는 공식
#         for j in range(ans[0]):
#             if i<j:
#                 sum+=gcd(arr[i],arr[j])
#     print(sum)



#파이썬의 조합 모듈 사용! 센스
for i in range(n):
    sum=0
    ans = list(map(int,sys.stdin.readline().split()))
    arr = ans[1:]
    for a, b in itertools.combinations(arr, 2):
        sum+=gcd(a,b)
    print(sum)
