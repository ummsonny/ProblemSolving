from collections import deque
n,m,t = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(deque(list(map(int, input().split()))))
length = len(graph)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):

    visit[x][y]=1
    candidate.append((x,y))

    for d in range(4):
        nx,ny = x+dx[d],(y+dy[d])%m
        if 0<=nx<n and visit[nx][ny]==-1 and graph[x][y]==graph[nx][ny]:
            dfs(nx,ny)
def bfs(x,y):

    q = deque([(x,y)])
    visit[x][y]=1
    candidate.append((x,y))

    while q:
        cx,cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], (cy + dy[d]) % m
            if 0 <= nx < n and visit[nx][ny] == -1 and graph[x][y] == graph[nx][ny]:
                q.append((nx,ny))
                visit[nx][ny]=1
                candidate.append((nx,ny))

for _ in range(t):
    x,d,k = map(int, input().split())
    d=1 if d==0 else -1

    #회전
    for i in range(length):
        if (i+1)%x == 0:
            for _ in range(k):
                graph[i].rotate(d)

    #삭제
    visit = [[-1]*m for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(m):
            if visit[i][j]==-1 and graph[i][j]>0:
                candidate = []
                # dfs(i,j) 이것도 가능! but recursion error뜸!
                bfs(i,j)
                if len(candidate)>1:
                    flag=True
                    for x,y in candidate:
                        graph[x][y]=-10

    if not flag:
        cnt,sum = 0,0
        for i in range(n):
            for j in range(m):
                if graph[i][j]>0:
                    cnt+=1
                    sum+=graph[i][j]

        if cnt: # 다 삭제해서 남아있는 수가 아무것도 없을 수도 있으므로
            avg = sum/cnt
            for i in range(n):
                for j in range(m):
                    if graph[i][j]>avg: # graph[i][j]==-10 제외해줘야하기때문에 '0<'조건 꼭있어야함
                        graph[i][j]-=1
                    elif 0<graph[i][j]<avg:
                        graph[i][j]+=1 # graph[i][j]==-10 제외해줘야하기때문에 '0<'조건 꼭있어야함

answer = 0
for x in range(n):
    for y in range(m):
        if graph[x][y]>0:
            answer+=graph[x][y]

print(answer)