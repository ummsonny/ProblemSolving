n = int(input())

ugly = [0] * n 
ugly[0] = 1 # 첫 번째 못생긴 수는 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈 값을 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수들을 찾기
for l in range(1, n):
    # 1. 인덱스를 증가하면서 각각 계산해둔 2,3,5 곱한 결과를 next2~5에 담아둔다.(2.로 이어짐)
        # 2,3,5 각각 곱하고 있는 인덱스가 제각각 다를 수도 있다. **중요**
        # 예를들어 2는 2번 인덱스 값에 대한 곱을 next2에 담고 있는데
        # 3,5는 아직 1번 인덱스 값에 대한 곱을 next3,next5에 담고 있을 수 있다.
    # 2. 또한 작은 인덱스부터 오름차순으로 넣어야 함으로 min()을 통해 자기 차례기다리고 있다.
    ugly[l] = min(next2, next3, next5)  
    # 인덱스에 따라서 곱셈 결과를 증가
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

# n번째 못생긴 수를 출력
print(ugly[n - 1])