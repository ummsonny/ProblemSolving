''' 
내 풀이
- n이 k보다 작아도 계속 n%k를 확인하는 무의미한 과정을 거친다.
- 뺄수 있는건 한 번 반복때 다 빼야 하는데 난 한 루프다 1만 빼는 비효율성을 가지고 있다.
n, k = map(int, input().split())

count=0
while n>1:
    if(n%k==0):
        n //=k
        count+=1
    else:
        n-=1
        count+=1

print(count)
'''


# - 나동빈은 n이 k일때까지만 따지고 n<k 순간부터는 계속 1을 뺀다.
# - 두 가지 버전 모두 1로 뺄 수 있는건 다 빼고 나누고 다 빼고, 나누고... 이 과정을 반복한다. 
#   하지만 나는 뺄 수 있는 건 다 빼지 않고 한 번에 1빼고 다시 루프 돌았다. 뺄때는 쫘악 빼자!!!!!!!!!!!
#1. 단순 버전
'''
n,k = map(int, input().split())
result = 0

while n>=k:
    while n%k!=0:
        n-=1
        result+=1
    n//=k
    result+=1

while n>1:
    n-=1
    result+=1
print(result)
'''

#2. 업그레이드 버전
n, k = map(int, input().split())
result = 0

while True:

    #1빼기
    target = (n//k)*k
    result += (n-target)
    n = target

    if n<k:
        print(n)
        break
    #나누기
    result +=1
    n//=k

print(result)
result += (n-1)
print(result)