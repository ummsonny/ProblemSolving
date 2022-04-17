from collections import deque

n, m = map(int, input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int, input())))
visited = [[-1]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
q.append((0,0))
visited[0][0]=1

while q:

    x,y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))

print(visited[n-1][m-1])
