n = int(input())
data = list(map(int, input().split()))
data.sort()

# 그리디인 이유 
# 1. 항상 target-1인 상황까지는 만들 수 있다.
# 그래서 target보다 지금 확인하는 동전이 작거나 같다면
# 여기 중요!!! : target까지는은 만들수 있다. 왜냐면 target-1까지는 만들수 있고 동전의 최소 값은 1 이므로 
# 만약 1~6까지 만들 수 있고 5원짜리 동전이 남아 있다면 1~11(1~6->(+5평행이동)->6~11) 가능
target = 1  

for x in data:
    if target<x:
        break
    target+=x

print(target)