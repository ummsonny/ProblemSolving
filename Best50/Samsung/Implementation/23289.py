from collections import deque
n,m,k = map(int, input().split())

heater = [] # 온풍기
investigate = [] # 조사해야하는 칸

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if 0<graph[i][j]<5: # 온풍기라면
            heater.append((i,j,graph[i][j]))
        elif graph[i][j]==5:
            investigate.append((i,j))
graph = [[0]*m for _ in range(n)] # 가장 처음은 온도가 0이므로

w = int(input())
wall = [[[] for _ in range(m)] for _ in range(n)]
for _ in range(w):
    x,y,t = map(int, input().split())
    wall[x-1][y-1].append(t)

heaterdir = {}
heaterdir[1] = [(-1,1),(0,1),(1,1)] # 동쪽 바라봄
heaterdir[2] = [(x,-y) for x,y in heaterdir[1]] # 서쪽 바라봄
heaterdir[3] = [(-y,x) for x,y in heaterdir[1]] # 북쪽
heaterdir[4] = [(-x,y) for x,y in heaterdir[3]] # 남쪽

def checkwallnorth(x,y,i):

    # 왼쪽
    if i==0:
        if not wall[x][y-1]:
            return True
    # 위쪽
    elif i==1:
        if 0 not in wall[x][y]:
            return True
    # 오른쪽
    else:
        if 1 not in wall[x][y]:
            if 0 not in wall[x][y+1]:
                return True

    return False


def checkwalleast(x, y, i):
    # 위쪽
    if i == 0:
        if 0 not in wall[x][y]:
            if 1 not in wall[x-1][y]:
                return True
    # 옆쪽
    elif i == 1:
        if 1 not in wall[x][y]:
            return True
    # 아래쪽
    else:
        if not wall[x+1][y]:
            return True

    return False

def checkwallsouth(x, y, i):
    # 왼쪽
    if i == 0:
        if 1 not in wall[x][y-1]:
            if 0 not in wall[x+1][y-1]:
                return True
    # 아래쪽
    elif i == 1:
        if 0 not in wall[x+1][y]:
            return True
    # 오른쪽
    else:
        if 1 not in wall[x][y]:
            if 0 not in wall[x+1][y+1]:
                return True


    return False
def checkwallwest(x, y, i):
    # 위쪽
    if i == 0:
        if 0 not in wall[x][y]:
            if 1 not in wall[x-1][y-1]:
                return True
    # 왼쪽
    elif i == 1:
        if 1 not in wall[x][y-1]:
            return True
    # 아래쪽
    else:
        if 0 not in wall[x+1][y]:
            if 1 not in wall[x+1][y-1]:
                return True

    return False

def wind(x,y,d):
    cx,cy = x+heaterdir[d][1][0],y+heaterdir[d][1][1]

    # if not(0<=cx<n and 0<=cy<m): 이건 고려안해도됨 ! 문제의 "제한" 부분에서 온풍기 바람이 나오는 방향에 있는 칸은 항상 존재한다 했으므로
    #     return

    visit = [[0]*m for _ in range(n)]
    q = deque([(cx,cy,5)])
    graph[cx][cy]+=5
    visit[cx][cy]=1

    while q:
        x,y,cost = q.popleft()

        if cost==1:
            break

        for i,(dx,dy) in enumerate(heaterdir[d]):
            nx,ny = x+dx,y+dy

            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0:
                #만약 벽이 있다면
                if d==1:
                    if not checkwalleast(x,y,i):
                        continue
                elif d==2:
                    if not checkwallwest(x,y,i):
                        continue
                elif d==3:
                    if not checkwallnorth(x,y,i):
                        continue
                else:
                    if not checkwallsouth(x,y,i):
                        continue

                q.append((nx,ny,cost-1))
                graph[nx][ny]+=(cost-1)
                visit[nx][ny]=1

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def control():
    temp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                copyvalue = graph[i][j]

                for d in range(4):
                    nx,ny = i+dx[d],j+dy[d]
                    if 0<=nx<n and 0<=ny<m and graph[i][j]>graph[nx][ny]:
                        # 만약 벽이 있다면
                        if d == 0 and 0 in wall[i][j]: continue
                        elif d == 1 and 1 in wall[i][j]: continue
                        elif d == 2 and 0 in wall[nx][ny]: continue
                        elif d == 3 and 1 in wall[nx][ny]: continue

                        temp[nx][ny] += (graph[i][j]-graph[nx][ny])//4
                        copyvalue-=(graph[i][j]-graph[nx][ny])//4
                temp[i][j] += copyvalue

    return temp

def minus():
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                if not i or not j or i==n-1 or j==m-1:
                    graph[i][j]-=1

answer = 0
while True:

    for x,y,d in heater:
        wind(x,y,d)

    graph = control()
    minus()

    answer+=1
    if answer>100:
        print(101)
        break

    flag = True
    for x,y in investigate:
        if graph[x][y]<k:
            flag = False

    if flag:
        print(answer)
        break

# 밑에 코드가 더 이해하기 쉽고 빠르다
from collections import deque

n, m, k = map(int, input().split())
graph = []
heater = []
investigate = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if 1 <= graph[i][j] <= 4:
            heater.append((i, j, graph[i][j] - 1))
        elif graph[i][j] == 5:
            investigate.append((i, j))
graph = [[0] * m for _ in range(n)]

wall = [[[] for _ in range(m)] for _ in range(n)]
w = int(input())
for _ in range(w):
    x, y, t = map(int, input().split())
    wall[x - 1][y - 1].append(t)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def nextnode(x, y, d):
    arr = []

    if d == 0:
        if 0 <= y + 1 < m:
            if 0 <= x - 1 < n:
                if 0 not in wall[x][y] and 1 not in wall[x - 1][y]:
                    arr.append((x - 1, y + 1))

            if 1 not in wall[x][y]:
                arr.append((x, y + 1))

            if 0 <= x + 1 < n:
                if not wall[x + 1][y]:
                    arr.append((x + 1, y + 1))
    elif d == 1:
        if 0 <= y - 1 < m:
            if 0 <= x - 1 < n:
                if 0 not in wall[x][y] and 1 not in wall[x - 1][y - 1]:
                    arr.append((x - 1, y - 1))

            if 1 not in wall[x][y - 1]:
                arr.append((x, y - 1))

            if 0 <= x + 1 < n:
                if 0 not in wall[x + 1][y] and 1 not in wall[x + 1][y - 1]:
                    arr.append((x + 1, y - 1))

    elif d == 2:
        if 0 <= x - 1 < n:
            if 0 <= y - 1 < m:
                if not wall[x][y - 1]:
                    arr.append((x - 1, y - 1))

            if 0 not in wall[x][y]:
                arr.append((x - 1, y))

            if 0 <= y + 1 < m:
                if 0 not in wall[x][y + 1] and 1 not in wall[x][y]:
                    arr.append((x - 1, y + 1))
    elif d == 3:
        if 0 <= x + 1 < n:

            if 0 <= y - 1 < m:
                if 0 not in wall[x + 1][y - 1] and 1 not in wall[x][y - 1]:
                    arr.append((x + 1, y - 1))

            if 0 not in wall[x + 1][y]:
                arr.append((x + 1, y))

            if 0 <= y + 1 < m:
                if 0 not in wall[x + 1][y + 1] and 1 not in wall[x][y]:
                    arr.append((x + 1, y + 1))

    return arr


def wind(x, y, d):
    visit = [[0] * m for _ in range(n)]
    sx, sy = x + dx[d], y + dy[d]

    q = deque([(sx, sy, 5)])
    visit[sx][sy] = 1
    graph[sx][sy] += 5

    while q:
        cx, cy, cost = q.popleft()

        if cost <= 1:
            break

        for nx, ny in nextnode(cx, cy, d):
            if not visit[nx][ny]:
                q.append((nx, ny, cost - 1))
                visit[nx][ny] = 1
                graph[nx][ny] += (cost - 1)


def control():
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                copy = graph[i][j]
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and graph[i][j] > graph[nx][ny]:
                        if d == 0 and 1 in wall[i][j]:
                            continue
                        elif d == 1 and 1 in wall[nx][ny]:
                            continue
                        elif d == 2 and 0 in wall[i][j]:
                            continue
                        elif d == 3 and 0 in wall[nx][ny]:
                            continue
                        value = (graph[i][j] - graph[nx][ny]) // 4
                        temp[nx][ny] += value
                        copy -= value
                temp[i][j] += copy
    return temp


def remove():
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    graph[i][j] -= 1


answer = 0
while True:

    # 바람 나옴
    for x, y, d in heater:
        wind(x, y, d)

    # 온도 조절
    graph = control()

    # 바깥칸 온도 1씩 감소
    remove()

    # 초콜릿 먹음
    answer += 1
    if answer > 100:
        print(101)
        break

    # 조사
    flag = False
    for x, y in investigate:
        if graph[x][y] < k:
            flag = True
            break

    if not flag:
        print(answer)
        break