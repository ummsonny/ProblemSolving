import sys
input = sys.stdin.readline

n,m = map(int, input().split())

#누적합 테이블 만들기1

# 장점 : 메모리와 시간 측면에서 방법2보다 좋다.
# 단점 : 코드가 길어진다.

numbers = [[0]*(n+1)] # 0 행

for _ in range(n):
    nums = [0] + list(map(int, input().split()))
    numbers.append(nums)

#1. 행 별로 더하기
for i in range(1,n+1):
    for j in range(1,n):
        numbers[i][j+1] += numbers[i][j]

#2. 열 별로 더하기
for j in range(1,n+1):
    for i in range(1,n):
        numbers[i+1][j] += numbers[i][j]
for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())

    print(numbers[x2][y2]-numbers[x1-1][y2]-numbers[x2][y1-1]+numbers[x1-1][y1-1])


'''
#누접합 테이블 만들기2
# 장점 : 코드가 간단
# 단점 : dp테이블을 따로 만듬으로 메모리 증가 및 시간도 더 걸린다.(시간은 크게 차이없음)
numbers=[]
for _ in range(n):
    nums = list(map(int, input().split()))
    numbers.append(nums)

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = dp[i+1][j]+dp[i][j+1]-dp[i][j]+numbers[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])
'''
