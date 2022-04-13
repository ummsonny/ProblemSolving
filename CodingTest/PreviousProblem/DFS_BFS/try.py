import sys
sys.setrecursionlimit(10000)
n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y,united):

    visited[x][y]=1
    united.append((x,y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
            if l<=abs(graph[x][y]-graph[nx][ny])<=r:

                dfs(nx,ny,united)                

people, country= 0,0
united = []
count = 0
while True:
    visited = [[0]*n for _ in range(n)]

    result = 0
    #flag = False
    count +=1
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:#==0:
                dfs(i,j,united)
            if len(united) > 1:
                result +=1
                #flag=True
                summary = 0
                for node in united:
                   summary+=graph[node[0]][node[1]]

                length = len(united)
                avg = summary//length
                for a,b in united:
                    graph[a][b] = avg

            people, country= 0,0
            united=[]
    
    if result == n*n:
    #if not flag:
        break

print(count-1)