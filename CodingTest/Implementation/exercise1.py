n = int(input())
plans = input().split() # 타입은 리스트 이다.
# print(type(plans))
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx<1 or ny<1 or nx>n or ny>n:
        continue

    x,y = nx, ny

print(x, y)