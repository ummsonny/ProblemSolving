from collections import deque

n = int(input())
graph = []
shark = [2,0,0] # 크기 x,y
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j]==9:
            shark[1],shark[2] = i,j
            graph[i][j]=0

#거리 구해
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y,visit):

    q = deque([(x,y)])
    visit[x][y]=0

    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx,ny = cx+dx[i], cy+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]<=shark[0]:
                if visit[nx][ny]==-1:
                    visit[nx][ny]=visit[cx][cy]+1
                    q.append((nx,ny))

#먹어
def eat(visit):
    feed = (1e9,-1,-1) #거리,x,y
    for i in range(n):
        for j in range(n):
            if 0<visit[i][j]<feed[0] and 0<graph[i][j]<shark[0]:
                feed = (visit[i][j],i,j)

    return feed

fish = 0 #물고기 먹은 횟수
answer = 0
while True:


    visit = [[-1]*n for _ in range(n)]
    #거리 구해
    bfs(shark[1],shark[2],visit)

    #먹어
    dist,x,y = eat(visit)
    if x==-1 and y==-1:
        break
    else:
        graph[x][y]=0
        shark[1],shark[2]=x,y
        fish+=1

        if fish>=shark[0]:
            fish = 0
            shark[0]+=1

        answer+=dist

print(answer)