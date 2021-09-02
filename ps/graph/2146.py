import sys
from collections import deque
sys.setrecursionlimit(10**4)
read = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(y,x,island_num):#각 섬의 가장자리 구하기
    g[y][x]=island_num
    visited[y][x]=1
    flag=False
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<N and 0<=nx<N and g[ny][nx]==1 and visited[ny][nx]==0:
            dfs(ny,nx,island_num)
        elif 0<=ny<N and 0<=nx<N and g[ny][nx]==0 and flag==False:
            queue.append([y,x,island_num])
            flag=True

def bfs():
    global min_value
    while(queue):
        q = queue.popleft()
        for i in range(4):
            ny = q[0]+dy[i]
            nx = q[1]+dx[i]
            if 0<=ny<N and 0<=nx<N and g[ny][nx]!=g[q[0]][q[1]] and visited[ny][nx]!=0:
                min_value = min(min_value, visited[q[0]][q[1]]+visited[ny][nx])
            if 0<=ny<N and 0<=nx<N and g[ny][nx]==0 and visited[ny][nx]==0:
                queue.append([ny,nx,island_num])
                visited[ny][nx]=visited[q[0]][q[1]]+1
                g[ny][nx]=g[q[0]][q[1]]



N = int(read())
g = [list(map(int, read().split())) for _ in range(N)]
visited=[[0]*N for _ in range(N)]
queue = deque()
island_num=1
min_value = sys.maxsize

for j in range(N):
    for i in range(N):
        if g[j][i]==1 and visited[j][i]==0:
            dfs(j,i,island_num)
            island_num+=1

bfs()
# print(island_num)
# for list in visited:
#     print(list)
print(min_value-2)
