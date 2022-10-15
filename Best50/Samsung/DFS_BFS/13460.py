'''
# dfs 버전
n,m = map(int, input().split())
graph = []
rx,ry,bx,by = 0,0,0,0
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j]=='#':
            graph[i][j]=-1
        elif graph[i][j] == '.':
            graph[i][j]=0
        elif graph[i][j]=='O':
            graph[i][j]=1
        elif graph[i][j] == 'R':
            graph[i][j]=0
            rx,ry = i,j
        elif graph[i][j] == 'B':
            graph[i][j]=0
            bx,by = i,j

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def move(d,graph,rx,ry,bx,by):

    # 빨간색
    nrx,nry = rx,ry
    while True:
        nrx,nry = nrx+dx[d],nry+dy[d]
        if graph[nrx][nry]==-1:
            nrx,nry = nrx-dx[d],nry-dy[d]
            break
        elif graph[nrx][nry] == 1:
            break
    # 파란색
    nbx,nby = bx,by
    while True:
        nbx,nby = nbx+dx[d],nby+dy[d]
        if graph[nbx][nby]==-1:
            nbx,nby = nbx-dx[d],nby-dy[d]
            break
        elif graph[nbx][nby]==1:
            break

    # 둘다 빈칸
    # print(nrx,nry,nbx,nby)
    if graph[nrx][nry]==0 and graph[nbx][nby]==0:
        if nrx==nbx and nry==nby: #같은위치
            if abs(nrx-rx)+abs(nry-ry) > abs(nbx-bx)+abs(nby-by):
                nrx,nry = nrx-dx[d],nry-dy[d]
            else:
                nbx,nby = nbx-dx[d],nby-dy[d]

        graph[rx][ry],graph[nrx][nry]=graph[nrx][nry],graph[rx][ry]
        graph[bx][by],graph[nbx][nby]=graph[nbx][nby],graph[bx][by]
        return 1,nrx,nry,nbx,nby
    # 파란색 구멍
    if graph[nbx][nby]==1:
        return -1,nrx,nry,nbx,nby
    # 빨간색 구멍
    if graph[nrx][nry]==1:
        return 0,nrx,nry,nbx,nby

def dfs(count,d,graph,rx,ry,bx,by):
    global answer

    if count>10 or answer<=count:
        return

    temp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[i][j]

    # 공을 움직여서 구멍으로 빼내자
    flag,rx,ry,bx,by = move(d,temp,rx,ry,bx,by)

    if flag==1:
        for i in range(4):
            dfs(count+1,i,temp,rx,ry,bx,by)
    elif flag==-1:
        return
    else:
        answer = min(answer,count)
        return

answer = 11
for d in range(4):
    dfs(1,d,graph,rx,ry,bx,by)

if answer>10:
    print(-1)
else:
    print(answer)
'''
# bfs버전
from collections import deque

n,m = map(int, input().split())
graph = []
rx,ry,bx,by = 0,0,0,0
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j]=='#':
            graph[i][j]=-1
        elif graph[i][j] == '.':
            graph[i][j]=0
        elif graph[i][j]=='O':
            graph[i][j]=1
        elif graph[i][j] == 'R':
            graph[i][j]=0
            rx,ry = i,j
        elif graph[i][j] == 'B':
            graph[i][j]=0
            bx,by = i,j
visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]
def move(d,x,y):

    count=0
    while graph[x+dx[d]][y+dy[d]] != -1 and graph[x][y]!=1:
        x+=dx[d]
        y+=dy[d]
        count+=1

    return x,y,count

q = deque()
q.append((rx,ry,bx,by,0))
visit[rx][ry][bx][by]=True

while q:
    rx,ry,bx,by,depth = q.popleft()

    if depth>=10:
        break

    for i in range(4):
        nrx,nry,rcnt = move(i,rx,ry)
        nbx,nby,bcnt = move(i,bx,by)

        # 파란공이 구멍에 들어가!
        if graph[nbx][nby]==1:
            continue
        # 빨간공이 구멍에 들어가
        if graph[nrx][nry]==1:
            print(depth+1)
            exit(0)
        # 파란,빨간 공 둘이 같은 위치!
        if nrx==nbx and nry==nby:
            if rcnt>bcnt:
                nrx-=dx[i]
                nry-=dy[i]
            else:
                nbx-=dx[i]
                nby-=dy[i]

        if not visit[nrx][nry][nbx][nby]:
            visit[nrx][nry][nbx][nby]=True
            q.append((nrx,nry,nbx,nby,depth+1))
print(-1)

# 밑에는 내가 직접 bfs로 풀어본것!
from collections import deque
n,m = map(int, input().split())
graph = []
rx,ry,bx,by = 0,0,0,0
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j]=='#':
            graph[i][j]=-1
        elif graph[i][j]=='.':
            graph[i][j]=0
        elif graph[i][j]=='O':
            graph[i][j]=1
        elif graph[i][j]=='R':
            graph[i][j]=2
            rx,ry = i,j
        else:
            graph[i][j]=3
            bx,by = i,j

visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def moveball(x,y,d):
    count=0
    while True:
        nx,ny = x+dx[d],y+dy[d]
        if graph[nx][ny]==-1 or graph[x][y]==1:
            return x,y,count
        x,y = nx,ny
        count+=1
def makestate(rx,ry,bx,by,d):
    nrx,nry,rcnt = moveball(rx,ry,d)
    nbx,nby,bcnt = moveball(bx,by,d)

    if nrx==nbx and nry==nby and graph[nrx][nry]!=1: #만약 같은 위치에 있고 구멍이 아니라면
        # if abs(rx-nrx)+abs(ry-nry)<abs(bx-nbx)+abs(by-nby): # 빨간색이 더 빨리 도달
        if rcnt<bcnt: # 윗 줄보다 count 만들어서 하는게 더 빠르다
            nbx,nby = nbx-dx[d],nby-dy[d]
        else:
            nrx,nry = nrx-dx[d],nry-dy[d]

    return nrx,nry,nbx,nby

q = deque([(rx,ry,bx,by,0)])
visit[rx][ry][bx][by]=True

while q:
    ra,rb,ba,bb,cost = q.popleft()

    if cost>=10:
        break

    for d in range(4):
        nrx,nry,nbx,nby = makestate(ra,rb,ba,bb,d)

        if graph[nbx][nby] == 1:
            continue

        if graph[nrx][nry] == 1:
            print(cost+1)
            exit(0)

        if not visit[nrx][nry][nbx][nby]:
            q.append((nrx,nry,nbx,nby,cost+1))
            visit[nrx][nry][nbx][nby]=True

print(-1)