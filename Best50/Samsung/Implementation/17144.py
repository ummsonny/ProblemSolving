import sys

input = sys.stdin.readline
r,c,t = map(int, input().split())
graph = []

robot = []
for i in range(r):
    graph.append(list(map(int, input().split())))
    for j in range(c):
        if graph[i][j]==-1:
            robot.append((i,j))


dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(t):

    # 확산
    new_graph = [[0]*c for _ in range(r)]
    for x,y in robot:
        new_graph[x][y]=-1

    for i in range(r):
        for j in range(c):
            if graph[i][j]>0:
                count = 0
                for d in range(4):
                    ni,nj = i+dx[d], j+dy[d]
                    if 0<=ni<r and 0<=nj<c and graph[ni][nj]!=-1:
                        count+=1
                        new_graph[ni][nj]+=graph[i][j]//5
                new_graph[i][j]+=graph[i][j]-(graph[i][j]//5)*count
    graph=new_graph

    #공기 청정기 작동

    #위쪽
    curx,cury = robot[0][0], robot[0][1]+1
    temp = 0
    while True:
        graph[curx][cury], temp = temp, graph[curx][cury]
        if cury==c-1:
            curx-=1
            break
        cury+=1
    while True:
        graph[curx][cury], temp = temp, graph[curx][cury]
        if curx==0:
            cury-=1
            break
        curx-=1
    while True:
        graph[curx][cury], temp = temp, graph[curx][cury]
        if cury == 0:
            curx+=1
            break
        cury-=1
    while True:
        if graph[curx][cury] == -1:
            break
        graph[curx][cury], temp = temp, graph[curx][cury]
        curx+=1

    #아래쪽
    curx, cury = robot[1][0], robot[1][1] + 1
    temp = 0
    while True:
        graph[curx][cury], temp = temp, graph[curx][cury]
        if cury == c - 1:
            curx += 1
            break
        cury += 1
    while True:
        graph[curx][cury], temp = temp, graph[curx][cury]
        if curx == r-1:
            cury -= 1
            break
        curx += 1
    while True:
        graph[curx][cury], temp = temp, graph[curx][cury]
        if cury == 0:
            curx -= 1
            break
        cury -= 1
    while True:
        if graph[curx][cury] == -1:
            break
        graph[curx][cury], temp = temp, graph[curx][cury]
        curx -= 1

#남아있는 미세먼지 양 구하기
answer = 0
for i in range(r):
    for j in range(c):
        if graph[i][j]>0:
            answer+=graph[i][j]

print(answer)
# for g in graph:
#     print(g)
# print()

#==============================================================
# 개선
r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1
# 공기 청정기 위치 찾기
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지 확산
def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        tmp_arr[nx][ny] += arr[i][j] // 5
                        tmp += arr[i][j] // 5
                arr[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp_arr[i][j]

# 공기청정기 위쪽 이동
def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny


for _ in range(t):
    spread()
    air_up()
    air_down()

answer = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            answer += arr[i][j]

print(answer)