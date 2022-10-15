from collections import deque
n,k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

horses = [[[] for _ in range(n)] for _ in range(n)]
horse_list = [[] for _ in range(10)]
for num in range(k):
    x,y,d = map(int, input().split())
    horse_list[num]=[x-1,y-1,d-1]
    horses[x-1][y-1].append(num)

def chang_direction(d):
    if d==0:
        return 1
    elif d==1:
        return 0
    elif d==2:
        return 3
    else:
        return 2
turn = 0
while True:

    turn +=1

    for i in range(10):
        if not horse_list[i]: continue

        # i번 말 위치 찾기
        x,y,d = horse_list[i]
        idx = horses[x][y].index(i)

        nx,ny = x+dx[d],y+dy[d]
        # 벗어나는 경우 or 파란색
        if not(0<=nx<n and 0<=ny<n) or graph[nx][ny]==2:
            # 방향 바꿔
            horse_list[i][2] = chang_direction(horse_list[i][2])
            d = horse_list[i][2]
            nx,ny = x+dx[d],y+dy[d]

            if not(0<=nx<n and 0<=ny<n) or graph[nx][ny] == 2: continue

        # 흰색
        if graph[nx][ny]==0:
            temp = horses[x][y][idx:]

        # 빨간
        elif graph[nx][ny]==1:
            temp = horses[x][y][idx:][::-1]

        horses[nx][ny] += temp
        for num in temp:
            horse_list[num][0], horse_list[num][1] = nx, ny
        horses[x][y] = horses[x][y][:idx]

        if len(horses[nx][ny])>=4: # 이 부분이 핵심이다! 이동하고 바로 길이검사를 해야한다.
            print(turn)
            exit(0)

        if turn > 1000:
            print(-1)
            exit(0)

# 밑에는 딱 말의 갯수만큼 확인하게 코드를 짜서 더 빠르다
n,k = map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

horse = [[] for _ in range(11)]
chess = [[[] for _ in range(n)] for _ in range(n)]
for num in range(1,k+1):
    x,y,d = map(int, input().split())
    horse[num]=[x-1,y-1,d-1]
    chess[x-1][y-1].append(num)

def changedirection(d):
    if d==0:
        return 1
    elif d==1:
        return 0
    elif d==2:
        return 3
    elif d==3:
        return 2

dx = [0,0,-1,1]
dy = [1,-1,0,0]
def move(num):
    cx,cy,d = horse[num]
    nx,ny = cx+dx[d],cy+dy[d]

    # 파란색 혹은 벗어난다면:
    if not(0<=nx<n and 0<=ny<n) or graph[nx][ny]==2:
        d = changedirection(d)
        horse[num][2]=d
        nx,ny = cx+dx[d],cy+dy[d]
        if not(0<=nx<n and 0<=ny<n) or graph[nx][ny]==2:
            return False

    idx = chess[cx][cy].index(num)
    for element in chess[cx][cy][idx:]:
        horse[element][0], horse[element][1] = nx, ny

    # 흰색
    if graph[nx][ny]==0:
        chess[nx][ny]+=chess[cx][cy][idx:]

    # 빨간색
    elif graph[nx][ny]==1:
        chess[nx][ny]+=chess[cx][cy][idx:][::-1]

    chess[cx][cy] = chess[cx][cy][:idx]

    if len(chess[nx][ny])>=4:
        return True
    else:
        return False

step=0
while True:
    step+=1

    # 말 이동!
    for num in range(1,k+1):
        if move(num):
            print(step)
            exit(0)

    if step>1000:
        print(-1)
        exit(0)