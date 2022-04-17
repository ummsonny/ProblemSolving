from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
visit = [[-1]*n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]
def bfs(x,y,count):

    q = deque()
    q.append((x,y))
    number = 1
    visit[x][y]=1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny] ==1:
                if visit[nx][ny] == -1:
                    visit[nx][ny] = count
                    number +=1
                    q.append((nx,ny))

    return number

count = 0
number_arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1  and visit[i][j] == -1:
            count+=1
            number_arr.append(bfs(i,j,count))

print(count)
for i in sorted(number_arr):
    print(i)