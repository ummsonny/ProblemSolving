n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visit = [[-1]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y,count):
    global value
    
    value += 1
    visit[x][y] = count

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
            if visit[nx][ny]==-1:
                dfs(nx,ny,count)
answer = []
num_home = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == -1 and graph[i][j] == 1:
            num_home+=1
            value = 0
            dfs(i,j,num_home)
            answer.append(value)

print(num_home)
for i in sorted(answer):
    print(i)