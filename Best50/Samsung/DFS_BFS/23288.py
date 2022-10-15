from collections import deque
n,m,k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def change(dice,d):

    # 북쪽
    if d==0:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]
    # 동쪽
    elif d==1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]

    # 남쪽
    elif d==2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]
    # 서쪽
    elif d==3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def score(x,y,value,visit):

    q=deque([(x,y)])
    visit[x][y]=1
    cnt = 1

    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx,ny = cx+dx[i],cy+dy[i]
            if 0<=nx<n and 0<=ny<m and value == graph[nx][ny]:
                if visit[nx][ny]==-1:
                    visit[nx][ny]=1
                    q.append((nx,ny))
                    cnt+=1

    return cnt


cx,cy,d=0,0,1 #주사위 위치 및 방향
dice = [1,2,3,4,5,6]
answer = 0
for _ in range(k):

    #주사위 이동
    nx,ny = cx+dx[d],cy+dy[d]
    if 0<=nx<n and 0<=ny<m:
        cx,cy = nx,ny
        change(dice,d)
    else:
        cx,cy = cx-dx[d],cy-dy[d]
        d=(d+2)%4
        change(dice,d)

    # 점수 획득
    visit = [[-1]*m for _ in range(n)]
    cnt = score(cx,cy,graph[cx][cy],visit)
    answer+=graph[cx][cy]*cnt

    #이동방향 결정
    if dice[5]>graph[cx][cy]:
        d=(d+1)%4
    elif dice[5]<graph[cx][cy]:
        d=(d-1)%4

print(answer)

# 밑에보다 위에가 더 깔끔
from collections import deque

n,m,k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dice = [2,1,5,6,4,3] #주사위 현 상태

# 맵 위에서 주사위 위치
curx,cury = 0,0
# 주사위 이동방향
dx = [0,1,0,-1] #동남서북
dy = [1,0,-1,0]

def move(direction):
    if direction == 0: #오른쪽으로 굴려
        dice[4], dice[1], dice[5], dice[3] = dice[3], dice[4],dice[1],dice[5]
    elif direction == 1: #아래로 굴려
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif direction == 2: #좌로 굴러
        dice[4], dice[1], dice[5], dice[3] = dice[1], dice[5], dice[3], dice[4]
    elif direction == 3: #위로 굴러
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]


ddx = [-1, 1, 0, 0]
ddy = [0, 0, 1, -1]
def bfs(x, y):
    count = 1

    visit = [[0] * m for _ in range(n)]
    q = deque([(x, y)])
    visit[x][y] = 1

    while q:

        next_x, next_y = q.popleft()

        for j in range(4):
            nx = next_x + dx[j]
            ny = next_y + dy[j]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if graph[nx][ny] == graph[x][y]:
                    q.append((nx, ny))
                    visit[nx][ny] = 1
                    count += 1

    return count

direction = 0
score = 0

for i in range(k):
    nx = curx + dx[direction]
    ny = cury + dy[direction]

    if 0<=nx<n and 0<=ny<m:
        curx, cury = nx, ny
        move(direction)
        score += bfs(curx,cury)*graph[curx][cury]
        if dice[3]>graph[curx][cury]:
            direction = (direction+1)%4
        elif dice[3]<graph[curx][cury]:
            direction = (direction-1) % 4
    else:
        direction=(direction+2)%4 # direction = -direction 이거 아니야!!!!
        curx = curx + dx[direction]
        cury = cury + dy[direction]
        move(direction)
        score+=bfs(curx,cury)*graph[curx][cury]
        if dice[3]>graph[curx][cury]:
            direction = (direction+1)%4
        elif dice[3]<graph[curx][cury]:
            direction = (direction-1) % 4

print(score)