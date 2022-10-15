r,c,m = map(int, input().split())
board = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x,y,s,d,z = map(int, input().split())
    board[x-1][y-1]=[s,d-1,z]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def changedirection(d):
    if d==0:
        return 1
    elif d==1:
        return 0
    elif d==2:
        return 3
    else:
        return 2
def move(temp,i,j,s,d,z): # pypy3로만 통과하는 코드

    step = 1
    x,y = i,j
    while step<=s:
        nx,ny = x+dx[d],y+dy[d]
        if not(0<=nx<r and 0<=ny<c):
            d = changedirection(d)
            nx,ny = x+dx[d], y+dy[d]
        x,y = nx,ny
        step += 1

    if temp[x][y]:
        if temp[x][y][2]<z:
            temp[x][y]=[s,d,z]
    else:
        temp[x][y]=[s,d,z]

# def move2(temp,i,j,s,d,z):
#     nx,ny = i,j
#
#     if d//2: # 우좌
#         nx = (nx+dx[d]*s)%(2*c-2)
#
answer = 0
king = -1
while True:
    # 낚시왕 한 칸 이동
    king+=1
    # print(king)
    # for b in board:
    #     print(b)
    # print()
    if king>=c:
        break

    # 상어 먹어
    for i in range(r):
        if board[i][king]:
            answer += board[i][king][2]
            board[i][king]=[]
            break
    # for b in board:
    #     print(b)
    # print()
    # 상어 이동
    temp = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j]:
                s,d,z = board[i][j]
                move(temp,i,j,s,d,z)
    board = temp
    # for b in board:
    #     print(b)
    # print('====')
print(answer)

# 위에보다 개선은 됏지만 여전히 pypy로만 돌아간다. python3 20%에서 시간초과 발생
r,c,m = map(int, input().split())
graph = [[0 for _ in range(c)] for _ in range(r)]
shark = [[]]
for num in range(1,m+1):
    x,y,s,d,z = map(int, input().split())
    graph[x-1][y-1]=num
    if d<3: # 위아래
        shark.append([x-1,y-1,s%(2*r-2),d-1,z]) # 다시 같은 상태가 될때(2*r-2)까지로 %해준다.
    else: #좌우
        shark.append([x-1,y-1,s%(2*c-2),d-1,z]) # 다시 같은 상태가 될때(2*c-2)까지로 %해준다.
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def changedirection(d):
    if d==0:
        return 1
    elif d==1:
        return 0
    elif d==2:
        return 3
    elif d==3:
        return 2

def sharkmove(num):
    cx,cy,cs,cd,cz = shark[num]

    if cd<2: # 위아래로 움직이는 상어임
        for _ in range(cs):
            nx,ny = cx+dx[cd],cy+dy[cd]
            if not(0<=nx<r):
                cd = changedirection(cd)
                nx,ny = cx+dx[cd],cy+dy[cd]
            cx,cy = nx,ny
    else: # 좌우로 움직이는 상어임
        for _ in range(cs):
            nx,ny = cx+dx[cd],cy+dy[cd]
            if not(0<=ny<c):
                cd = changedirection(cd)
                nx,ny = cx+dx[cd],cy+dy[cd]
            cx,cy = nx,ny

    return cx,cy,cd



def move():
    temp = [[0 for _ in range(c)] for _ in range(r)] # 이렇게 안해주면 if graph[a][b]에서 같은 숫자의 상어가 또 걸릴 수 있다.
    for a in range(r):
        for b in range(c):
            if graph[a][b]:
                num = graph[a][b]
                nx,ny,nd = sharkmove(num)
                if not temp[nx][ny]: # 아무 것도 없다면
                    shark[num][0],shark[num][1],shark[num][3] = nx,ny,nd
                    temp[nx][ny]=num
                elif shark[num][-1]>shark[temp[nx][ny]][-1]: # 나보다 작은 상어가 있다면
                    shark[num][0],shark[num][1],shark[num][3] = nx,ny,nd
                    temp[nx][ny]=num
                # 나보다 큰 상어가 있다면 -> 암것도 안해도된다.


    return temp

answer = 0
hunter = 0
while hunter<c:
    # print('asdfasdf')
    # for g in graph:
    #     print(g)
    # print()
    # 사냥!
    for i in range(r):
        if graph[i][hunter]:
            answer+=shark[graph[i][hunter]][-1]
            # print(shark[graph[i][hunter]][-1])
            graph[i][hunter]=0
            break
    # for g in graph:
    #     print(g)
    # print()
    # 상어 이동
    graph = move()
    # for g in graph:
    #     print(g)
    # print()
    hunter+=1

print(answer)