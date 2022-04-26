from collections import deque
import copy
n,m =  map(int, input().split())
graph = []

array = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            array.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():

    visit = copy.deepcopy(graph)
    #처음 시작부분 visited처리해줘야되지만 안해줘도 됨
    q = deque(array)
    
    while q:

        x,y = q.popleft()
        visit[x][y]=2
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny]==0:
                    q.append((nx,ny))

    return visit
def check_safe(visit):

    count = 0
    for a in range(n):
        for b in range(m):
            if visit[a][b]==0:
                count+=1

    return count

result = -10
def dfs(sx,sy,count):
    global result

    if count == 3:
        result = max(result, check_safe(bfs()))
        return

    for a in range(sx,n): # 이차원 조합 
        sy = sy if a == sx else 0
        for b in range(sy,m):
            if graph[a][b]==0:
                graph[a][b]=1
                dfs(sx,sy+1,count+1)
                graph[a][b]=0

dfs(0,0,0)
print(result)


