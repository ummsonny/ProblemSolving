from collections import deque

n, k = map(int, input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph = []
virus = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j],0, i, j))

second, x1, y1 = map(int, input().split())

virus.sort()
q = deque(virus)

while q:

    node, s, x, y = q.popleft()
    if s == second:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = node
                q.append((graph[nx][ny], s+1, nx, ny))
print(graph, x1, y1)
print(graph[x1-1][y1-1])

