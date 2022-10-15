n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

tor_x,tor_y, direction = n//2, n//2, 0

dx = [0,1,0,-1] #좌하우상
dy = [-1,0,1,0]

def move(x,y,direction):
    return x+dx[direction], y+dy[direction]

def tornado():
    global dust, tor_x, tor_y

    # 3. a, out_sand
    total = 0  # a 구하기 위한 변수
    for ddx, ddy, z in total_direction[direction]:
        nx = tor_x + ddx
        ny = tor_y + ddy
        if z == 0:  # a(나머지)
            new_sand = graph[tor_x][tor_y] - total
        else:  # 비율
            new_sand = int(graph[tor_x][tor_y] * z)
            total += new_sand

        if 0 <= nx < n and 0 <= ny < n:  # 인덱스 범위이면 값 갱신
            graph[nx][ny] += new_sand
        else:  # 범위 밖이면 ans 카운트
            dust += new_sand

left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x,y,z in left]
down = [(-y, x, z) for x,y,z in left]
up = [(y, x, z) for x,y,z in left]

total_direction = [left,down,right,up]

step = 1
dust = 0
while True:

    if tor_x == 0 and tor_y == n-1:
        for _ in range(step-1):
            tor_x, tor_y = move(tor_x, tor_y, direction)
            tornado()
        direction = (direction + 1) % 4
        break
    else:
        for _ in range(2):
            for _ in range(step):
                tor_x, tor_y = move(tor_x, tor_y,direction)
                tornado()
            direction = (direction+1)%4
    step +=1

print(dust)

# 비슷하지만 나중에 또 풀어본 코드 - 확산 부분이랑, 쇼용돌이 부분이 여기가 더 낫다. 퍼센트 배열에 담는 부분은 위가 더 낫다.
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [-1,0,1,0]
cx,cy,d = n//2,n//2,0
step=0

send_pt = [[(-1,1,0.01),(1,1,0.01),(-1,0,0.07),(1,0,0.07),(-1,-1,0.1),(1,-1,0.1),(-2,0,0.02),(2,0,0.02),(0,-2,0.05)],
            [(-1,-1,0.01),(-1,1,0.01),(0,-1,0.07),(0,1,0.07),(1,-1,0.1),(1,1,0.1),(0,-2,0.02),(0,2,0.02),(2,0,0.05)],
            [(-1,-1,0.01),(1,-1,0.01),(-1,0,0.07),(1,0,0.07),(-1,1,0.1),(1,1,0.1),(-2,0,0.02),(2,0,0.02),(0,2,0.05)],
            [(1,-1,0.01),(1,1,0.01),(0,-1,0.07),(0,1,0.07),(-1,-1,0.1),(-1,1,0.1),(0,-2,0.02),(0,2,0.02),(-2,0,0.05)]]
answer = 0
def send(x,y,d):
    global answer
    sum = 0
    for a,b,per in send_pt[d]:
        nx,ny = x+a,y+b
        temp = int(graph[x][y] * per)
        if 0<=nx<n and 0<=ny<n:
            graph[nx][ny]+=temp
        else:
            answer+=temp
        sum += temp

    nx,ny = x+dx[d], y+dy[d]
    if 0<=nx<n and 0<=ny<n:
        graph[nx][ny]+=(graph[x][y]-sum)
    else:
        answer+=(graph[x][y]-sum)
    graph[x][y] = 0

while True:
    step+=1
    if step < n:
        for _ in range(2):
            for _ in range(step):
                cx,cy=cx+dx[d],cy+dy[d]
                send(cx,cy,d)
            d=(d+1)%4
    else:
        for _ in range(step-1):
            cx,cy=cx+dx[d],cy+dy[d]
            send(cx,cy,d)
        break

print(answer)