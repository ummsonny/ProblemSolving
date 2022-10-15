# 내 풀이 -> 다른 풀이 참고해서 꼭 풀어바 : DFS들어가면서 바로바로 계산해버리는 풀이
from collections import deque
n = int(input())
game = []
for _ in range(n):
    game.append(list(map(int, input().split())))

# 동남서북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def movedetail(i,j,d,assemble,graph):

    while True:
        ni, nj = i + dx[d], j + dy[d]
        if 0 <= ni < n and 0 <= nj < n:
            if graph[ni][nj] == 0:  # 빈공간
                graph[ni][nj], graph[i][j] = graph[i][j], graph[ni][nj]
                i,j = ni,nj
            elif graph[ni][nj] == graph[i][j] and assemble[ni][nj] == -1:  # 같은 놈 만나
                graph[ni][nj], graph[i][j] = graph[ni][nj] * 2, 0
                assemble[ni][nj] = 1
                break
            else: # (같은 놈인데 이미 합쳐진 놈) OR (다른 놈)
                break
        else:
            break

def move(cmd,temp):

    for d in cmd:
        assemble = [[-1] * n for _ in range(n)]
        # 동쪽으로 움직영
        if d==0:
            for i in range(n):
                for j in range(n-1,-1,-1):
                    if temp[i][j]:
                        movedetail(i,j,d,assemble,temp)

        # 남쪽으로 움직영
        elif d==1:
            for i in range(n-1,-1,-1):
                for j in range(n):
                    if temp[i][j]:
                        movedetail(i,j,d,assemble,temp)
        # 서쪽으로 움직영
        elif d==2:
            for i in range(n):
                for j in range(n):
                    if temp[i][j]:
                        movedetail(i,j,d,assemble,temp)
        # 북쪽으로 움직영
        elif d==3:
            for i in range(n):
                for j in range(n):
                    if temp[i][j]:
                        movedetail(i,j,d,assemble,temp)


answer = -1
def dfs(count,cmd): # 동서남북 방향이 순서가 있으므로 중복순열로 해야함
    global answer

    if count==5:
        # 원본 건들지말자
        temp = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                temp[i][j]=game[i][j]

        move(cmd,temp)
        maxv = -1
        for a in range(n):
            for b in range(n):
                maxv = max(maxv,temp[a][b])
        answer = max(maxv,answer)
        return

    # 동 남 서 북
    for d in range(4):
        dfs(count+1,cmd+[d])

dfs(0,[])
print(answer)

# 밑의 moveblock()함수 안의 로직이 위에 보다 더 좋다
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def moveblock(d,cx,cy,temp,visit):

    while True:
        nx, ny = cx + dx[d], cy + dy[d]
        if not(0<=nx<n and 0<=ny<n):
            break
        if temp[nx][ny]==temp[cx][cy] and not visit[nx][ny]:
            temp[nx][ny] = temp[nx][ny] * 2
            visit[nx][ny]=1
            temp[cx][cy] = 0
            break
        elif not temp[nx][ny]:
            temp[nx][ny], temp[cx][cy] = temp[cx][cy], temp[nx][ny]
            cx, cy = nx, ny
        else:
            break


def movedetail(d,temp):
    visit = [[0]*n for _ in range(n)]
    if d==0: # 상
        for j in range(n):
            for i in range(n):
                if temp[i][j]:
                    moveblock(d,i,j,temp,visit)
    elif d==1: # 하
        for j in range(n):
            for i in range(n-1,-1,-1):
                if temp[i][j]:
                    moveblock(d, i, j, temp, visit)
    elif d==2: # 좌
        for i in range(n):
            for j in range(n):
                if temp[i][j]:
                    moveblock(d, i, j, temp, visit)
    elif d==3: # 우
        for i in range(n):
            for j in range(n-1,-1,-1):
                if temp[i][j]:
                    moveblock(d, i, j, temp, visit)

def moveblocks(candi):

    temp = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            temp[x][y]=graph[x][y]

    for d in candi:
        movedetail(d,temp)

    value = 0
    for a in range(n):
        for b in range(n):
            if temp[a][b]>value:
                value=temp[a][b]

    return value

answer = 0
def dfs(count,candi):
    global answer

    if count==5:
        answer = max(answer,moveblocks(candi))
        return

    for i in range(4):
        dfs(count+1,candi+[i])

dfs(0,[])
print(answer)