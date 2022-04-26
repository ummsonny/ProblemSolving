n,m,x,y,k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

command = list(map(lambda x: int(x)-1, input().split()))

dice = [0,0,0,0,0,0] #주사위 현 상태

# 맵 위에서 주사위 위치
curx,cury = x,y
# 주사위 이동방향
dx = [0,0,-1,1] #동서남북
dy = [1,-1,0,0]

def move(direction):
    if direction == 0: #오른쪽으로 굴려
        dice[4], dice[1], dice[5], dice[3] = dice[3], dice[4],dice[1],dice[5]
    elif direction == 1: #좌로 굴려
        dice[4], dice[1], dice[5], dice[3] = dice[1], dice[5], dice[3], dice[4]
    elif direction == 2: #아래로 굴러
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif direction == 3: #위로 굴러
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]

for com in command:
    curx, cury = curx + dx[com], cury + dy[com]
    if not(0<=curx<n and 0<=cury<m):
        curx, cury = curx - dx[com], cury - dy[com]
        continue

    move(com)
    if graph[curx][cury] == 0:
        graph[curx][cury] = dice[3]
    else:
        dice[3] = graph[curx][cury]
        graph[curx][cury]=0

    print(dice[1])