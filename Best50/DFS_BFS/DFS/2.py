import sys
sys.setrecursionlimit(10**6)

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):

    visit[x][y]=1

    for j in range(4):
        nx = x+dx[j]
        ny = y+dy[j]

        if 0<=nx<n and 0<=ny<n and graph[nx][ny]>i:
            if visit[nx][ny]==-1:
                dfs(nx,ny)

max_answer = 1 #어떤 경우든 비가 안 올 경우를 고려해야하므로 안전한 영역의 최대 개수 >=1
for i in range(1,101):

    visit = [[-1]*n for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(n):
            if visit[x][y]==-1 and graph[x][y]>i:
                count+=1
                dfs(x,y)
    max_answer = max(max_answer, count)

print(max_answer)
    