n = int(input()) # 남은 일수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
# 근데 어차피 마지막 인덱스는 쓰지도 않으면서 왜 이렇게 만들엇는지 몰름 
# 맨 밑에 dp출력하는 것 보면 알 수잇다. 
# 근데 이유를 찾았다. n = 10이고 1,1 1,2 1,3 ... 1,10 TC에서 
# 두번 째 FOR문의 n-1이 9일때 time은 10이므로 dp크기를 n으로 하면 index out of bound에러남
# 그래서 n+1로 한 거임
dp = [0] * (n + 1) 
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = i + t[i] # (i+1) + t]i] -1
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
print(dp)