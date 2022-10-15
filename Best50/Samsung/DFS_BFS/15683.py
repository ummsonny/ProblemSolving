n,m = map(int, input().split())
graph = []
cctv = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if 0<graph[i][j]<=5:
            cctv.append((i,j,graph[i][j]))

# 동남서북
dx = [0,1,0,-1]
dy = [1,0,-1,0]
ccDirection=[[],
             [[0],[1],[2],[3]],
             [[0,2],[1,3]],
             [[0,1],[1,2],[2,3],[3,0]],
             [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
             [[0,1,2,3]]
             ]

def watch(x,y,direction,graph):

    for d in direction:
        nx,ny = x,y
        while True:
            nx,ny = nx+dx[d],ny+dy[d]
            if not(0<=nx<n and 0<=ny<m) or graph[nx][ny]==6:
                break
            if graph[nx][ny]==0:
                graph[nx][ny]=-1


answer = 1e9
length = len(cctv)
def dfs(i,graph):
    global answer

    if i == length:
        count = 0
        for x in range(n):
            for y in range(m):
                if graph[x][y]==0:
                    count+=1
        answer = min(answer,count)
        return

    # 재귀함수 상태 기억! -> graph 원본 보존
    copy_graph = [[0]*m for _ in range(n)]
    for a in range(n):
        for b in range(m):
            copy_graph[a][b]=graph[a][b]


    for d_list in ccDirection[cctv[i][2]]:
        watch(cctv[i][0],cctv[i][1],d_list,copy_graph)
        dfs(i+1,copy_graph)
        #밑에 3줄 복구 코드가 핵심이다
        copy_graph = [[0] * m for _ in range(n)]
        for a in range(n):
            for b in range(m):
                copy_graph[a][b] = graph[a][b]

dfs(0,graph)
print(answer)

# cctvdirection 을 딕셔너리로 한 코드
n,m = map(int, input().split())
graph = []
cctv = []
cctvdir = {}
cctvdir[1] = [[0],[1],[2],[3]]
cctvdir[2] = [[0,2],[1,3]]
cctvdir[3] = [[0,1],[1,2],[2,3],[3,0]]
cctvdir[4] = [[0,1,2],[1,2,3],[2,3,0],[3,0,1]]
cctvdir[5] = [[0,1,2,3]]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if 1<=graph[i][j]<=5:
            cctv.append((i,j,graph[i][j]))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def watch(x,y,candi,temp):

    for d in candi:
        cx,cy = x,y
        while True:
            nx,ny = cx+dx[d],cy+dy[d]
            if not(0<=nx<n and 0<=ny<m):
                break
            if temp[nx][ny]==6:
                break
            cx,cy = nx,ny
            temp[cx][cy]=-1

answer = int(1e9)
length = len(cctv)
def dfs(idx,graph):
    global answer

    if idx == length:
        cnt = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j]==0:
                    cnt+=1
        answer = min(answer,cnt)
        return

    temp = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            temp[x][y]=graph[x][y]

    a,b,num = cctv[idx]
    for candi in cctvdir[num]:
        #감시
        watch(a,b,candi,temp)
        dfs(idx+1,temp)
        for x in range(n):
            for y in range(m):
                temp[x][y] = graph[x][y]

dfs(0,graph)
print(answer)