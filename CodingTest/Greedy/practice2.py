'''쉬운 풀이
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m==0:
            break
        result += first
        m-=1
    if m==0:
        break
    result+=second
    m-=1

print(result)
'''
'''조금 고급스러운 풀이
-> 수열의 활용
'''

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

#제일 큰수 개수 구하기
count = (m//(k+1))*k
count += m%(k+1)

result = count * first
result += (m-count)*second

print(result)