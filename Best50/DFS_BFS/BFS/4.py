from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def find_dist(x,y):

    q = deque()

    q.append((x,y))
    visit[x][y]=0

    while q:
        cx,cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny]<=ssize:
                if visit[nx][ny]==-1:
                    q.append((nx,ny))
                    visit[nx][ny]=visit[cx][cy]+1

def ate_feed():

    feedx,feedy = 0,0
    dist = 1e9
    for i in range(n):
        for j in range(n):
            if 0<visit[i][j]<dist and 0<graph[i][j]<ssize: #지나갈수 없는 경우도 있으므로 0<visit~
                feedx,feedy = i,j
                dist = visit[i][j]

    return feedx, feedy, dist

n = int(input())
graph = []

sx, sy = 0,0
ssize = 2
s_eat = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j]==9:
            sx,sy = i,j
graph[sx][sy]=0

answer = 0
while True:

    visit = [[-1]*n for _ in range(n)]
    find_dist(sx,sy)
    fx,fy,fdist = ate_feed()

    if fdist == 1e9:
        print(answer)
        break
    else:
        sx,sy = fx,fy
        # print(sx,sy)
        graph[sx][sy] = 0
        answer+=fdist
        s_eat+=1
        
        if s_eat==ssize:
            ssize+=1
            s_eat=0