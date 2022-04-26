import sys
sys.setrecursionlimit(10**6)
n = int(input())

graph = []

for _ in range(n):
    graph.append(list(input()))
visit = [[-1]*n for _ in range(n)]
visit2 = [[-1]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def normal_dfs(x,y):

    visit[x][y]=1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==graph[x][y]:
            if visit[nx][ny] == -1:
                normal_dfs(nx,ny)

def abnormal_dfs(x,y):
    
    visit2[x][y]=1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        #dfs의 다음 노드 후보를 현재 노드에 따라 정할 수 있도록 한다.
        #여기가 핵심코드
        #히자만 이렇게 말고 다른 사람풀이(R과G노드를 하나로 통일)를 꼭 참고하길 바란다.
        if 0<=nx<n and 0<=ny<n and visit2[nx][ny] == -1:
            if graph[x][y] == 'R' or graph[x][y] == 'G':
                if graph[nx][ny] in ['R','G']:
                    abnormal_dfs(nx,ny)
            else:
                if graph[nx][ny] == graph[x][y]:
                    abnormal_dfs(nx,ny)
count_norm = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == -1:
            normal_dfs(i,j)
            count_norm+=1

count_abnorm = 0
for i in range(n):
    for j in range(n):
        if visit2[i][j] == -1:
            abnormal_dfs(i,j)
            count_abnorm+=1


print(count_norm, count_abnorm)
