from collections import deque

n,m = map(int, input().split())

dx = [-1,0,1,0] #북동남서
dy = [0,1,0,-1]

x0,y0,direction = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visit = [[0]*m for _ in range(n)]
visit[x0][y0]=1

result = 1
flag = False

while True:

    for i in range(4):
        direction = (direction-1)%4
        nx = x0 + dx[direction]
        ny = y0 + dy[direction]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0 and visit[nx][ny]==0:
            x0,y0 = nx,ny
            visit[x0][y0] = 1
            result+=1
            flag = True
            break

    if flag:
        flag = False # 여기...해줘야한다.
        continue

    if graph[x0-dx[direction]][y0-dy[direction]] == 0:
        x0,y0 = x0-dx[direction], y0-dy[direction]
    elif graph[x0-dx[direction]][y0-dy[direction]] == 1:
        break

for g in visit:
    print(g)
print(result)

# 개선
n,m = map(int, input().split())
r,c,d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph[r][c]=-1
answer = 1

while True:

    flag = False
    for i in range(4):
        d = (d-1)%4
        nr, nc = r + dx[d], c + dy[d]
        if graph[nr][nc]==0:
            r,c = nr,nc
            graph[r][c]=-1
            answer+=1
            flag = True
            break

    if flag == False:
        nr,nc = r-dx[d], c-dy[d]
        if graph[nr][nc]!=1:
            r,c = nr, nc
        else:
            break

for g in graph:
    print(g)
print(answer)





