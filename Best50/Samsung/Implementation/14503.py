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


print(result)





