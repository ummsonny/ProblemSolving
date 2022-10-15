from collections import deque
n,m,fuel = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

taxi = list(map(lambda x : int(x)-1, input().split()))

customer = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b,c,d = map(int, input().split())
    customer[a-1][b-1] = [(c-1,d-1),0]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# bfs로 거리 구해
def bfs(x,y):
    distance = [[-1]*n for _ in range(n)]

    q = deque()
    distance[x][y]=0
    q.append((x,y))

    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx,ny = cx+dx[i], cy+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
                if distance[nx][ny]==-1:
                    distance[nx][ny]=distance[cx][cy]+1
                    q.append((nx,ny))

    return distance
# 손님을 찾는다.
def choice(distance):

    cost = int(1e9)
    cx,cy = -1,-1
    for i in range(n):
        for j in range(n):
            if customer[i][j] and not customer[i][j][1]and distance[i][j]>=0:
                if cost>distance[i][j]:
                    cost = distance[i][j]
                    cx,cy = i,j
    if cx==-1 and cy==-1:
        return (-1,-1)

    customer[cx][cy][1]=1
    return (cx,cy)
# 손님 데리러 간다. -> 단 연료 충분한지 확인
def take(start,distance):
    global fuel, taxi
    cost = distance[start[0]][start[1]]

    if cost>fuel or cost<0: # 연료가 부족하거나 벽때문에 아예 승객을 데리러 갈 수 없을 때
        return False
    else:
        fuel-=cost
        taxi = [start[0],start[1]]
        return True

# 손님 태워서 목적지로 간다. -> 단, 연료 충분한지 확인
def drop(dest,distance):
    global fuel, taxi
    cost = distance[dest[0]][dest[1]]
    if cost>fuel:
        return False
    else:
        fuel+=cost # 연료 소비와 충전을 한꺼번에
        taxi = [dest[0],dest[1]]
        return True


for _ in range(m):
    # 출발점까지 가기
    distance = bfs(taxi[0],taxi[1])
    start = choice(distance)
    if start[0]==-1 and start[1]==-1: # 만약 손님에게 갈 수 없다면
        print(-1)
        exit(0)
    if not take(start, distance):
        print(-1)
        exit(0)

    # 목적지까지 가기
    distance = bfs(taxi[0],taxi[1])
    dest = customer[start[0]][start[1]][0]
    if distance[dest[0]][dest[1]]==-1: # 만약 목적지에 도달할 수 없다면(목적지가 벽으로 둘러쌓여있다.)
        print(-1)
        exit(0)
    if not drop(dest,distance):
        print(-1)
        exit(0)

print(fuel)

# 밑에 풀이가 더 깔끔
from collections import deque
n,m, fuel = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j]:
            graph[i][j]=-1

taxix,taxiy = map(lambda x: int(x)-1, input().split())
customer = [()]
for num in range(1,m+1):
    a,b,c,d = map(int,input().split())
    customer.append(((a-1,b-1),(c-1,d-1)))
    graph[a-1][b-1]=num

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 태우러 갈 손님 고르기
def distance(x,y,visit):
    q = deque([(x,y)])
    visit[x][y]=0

    while q:
        cx,cy = q.popleft()
        for d in range(4):
            nx,ny = cx+dx[d],cy+dy[d]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==-1:
                if graph[nx][ny]!=-1:
                    q.append((nx,ny))
                    visit[nx][ny]=visit[cx][cy]+1


def checkcustomer():
    visit = [[-1]*n for _ in range(n)] # 거리기 때문에 -1로 초기화하는것이 좋다
    distance(taxix,taxiy,visit)

    cx,cy,dist = -1,-1,int(1e9)
    for a in range(n):
        for b in range(n):
            if graph[a][b]>0 and 0<=visit[a][b]<dist:
                cx,cy,dist = a,b,visit[a][b]

    return cx,cy,dist

left = m #남은 손님 체크
while True:

    if not left:
        print(fuel)
        break

    #  손님 태우러 가기
    nx,ny,cost = checkcustomer()
    if fuel<cost:
        print(-1)
        break

    customer_num = graph[nx][ny]
    graph[nx][ny]=0
    taxix,taxiy = nx,ny
    fuel-=cost

    # 목적지로 가기
    visit = [[-1] * n for _ in range(n)]  # 거리기 때문에 -1로 초기화하는것이 좋다
    distance(taxix, taxiy,visit)

    # 목적지로 갈 수 없다면
    i, j = customer[customer_num][1]
    if visit[i][j] == -1:
        print(-1)
        break
    # 연료가 바닥난다면
    if fuel < visit[i][j]:
        print(-1)
        break

    fuel+=visit[i][j] #연료 빼고 충전 한번에 하기
    taxix,taxiy=i,j


    left-=1