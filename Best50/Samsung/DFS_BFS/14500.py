n,m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visit = [[0]*m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

max_result = -1e9

#1번부터 4번 블록까지
def dfs_4(x,y,count,result):
    global max_result

    if count == 3:
        max_result = max(max_result, result)
        return

    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]

        if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            dfs_4(nx,ny,count+1,result+graph[nx][ny])
            visit[nx][ny] = 0

for i in range(n):
    for j in range(m):
        # visit = [[0] * n for _ in range(m)] --> 이렇게 하면 시간초과난다. 그래서
        visit[i][j] = 1
        dfs_4(i,j,0,graph[i][j])
        visit[i][j] = 0

#이제 5번 블록

graph2 = [[0]*(m+2) for _ in range(n+2)]
for i in range(1,n+1):
    for j in range(1,m+1):
        graph2[i][j] = graph[i-1][j-1]

max_5 = -1e9
for i in range(1,n+1):
    for j in range(1,m+1):
        sum_4 = graph2[i][j] + graph2[i+dx[0]][j+dy[0]] + graph2[i+dx[1]][j+dy[1]] + graph2[i+dx[2]][j+dy[2]] + graph2[i+dx[3]][j+dy[3]]
        for k in range(4):
            max_5 = max(max_5, sum_4-graph2[i+dx[k]][j+dy[k]])

max_result = max(max_result, max_5)
print(max_result)