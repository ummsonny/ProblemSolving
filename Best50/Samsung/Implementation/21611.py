from collections import deque
n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

shark_x,shark_y = (n+1)//2-1,(n+1)//2-1
#상하좌우 --> 상어
dx = [-1,1,0,0]
dy = [0,0,-1,1]

order_pos = []# 나선형을 일렬로 나열!!!!
direction = 0
#좌하우상
ddx = [0,1,0,-1]
ddy = [-1,0,1,0]
def make_order():
    global direction
    curx = shark_x
    cury = shark_y
    order_pos.append((curx,cury))
    step = 1
    while True:
        for _ in range(2):
            for _ in range(step):
                curx+=ddx[direction]
                cury+=ddy[direction]
                if not (0 <= curx < n and 0 <= cury < n): return
                order_pos.append((curx,cury))
            direction = (direction+1)%4
        step+=1

def papyun(d,s):
    for i in range(1,s+1):
        nx = shark_x + dx[d]*i
        ny = shark_y + dy[d]*i
        graph[nx][ny]=0

def move_ball():
    zero_list = deque()
    for x,y in order_pos:
        if x==shark_x and y==shark_y: continue
        if graph[x][y]==0:
            zero_list.append((x,y))
        if graph[x][y]!=0 and zero_list:
            nx,ny = zero_list.popleft()
            graph[nx][ny] = graph[x][y]
            graph[x][y]=0
            zero_list.append((x,y))

def bump_ball():

    while True:
        flag = False
        tmp_ball = []
        cnt = 0
        ball_number = -1
        for x,y in order_pos:
            if x==shark_x and y==shark_y: continue
            # if graph[x][y]==0: https://www.acmicpc.net/board/view/88720
            #     break

            if ball_number == graph[x][y]: #같다면
                cnt+=1
                tmp_ball.append((x,y))
            else:
                if cnt>=4:
                    flag = True
                    result(cnt,ball_number)
                    while tmp_ball:
                        i,j = tmp_ball.pop()
                        graph[i][j]=0
                    ball_number=-1
                    cnt=0
                else:
                    ball_number = graph[x][y]
                    cnt=1
                    tmp_ball = [(x,y)]
        # 구슬 이동
        move_ball()
        if not flag:
            return

def make_group():
    tmp_ball=[]
    cnt=0
    ball_number=-1
    for x,y in order_pos:
        if x==shark_x and y==shark_y: continue

        if ball_number == graph[x][y]: #같다면
            cnt+=1
        else:
            tmp_ball.append(cnt)
            tmp_ball.append(ball_number)
            ball_number = graph[x][y]
            cnt = 1
    return tmp_ball[2:]


one_bump, two_bump, three_bump = 0,0,0
def result(cnt,number):
    global one_bump, two_bump, three_bump
    if number == 1:
        one_bump+=cnt
    elif number == 2:
        two_bump+=cnt
    elif number == 3:
        three_bump+=cnt

#나선형을 직선화!
make_order()
for _ in range(m):
    d,s = map(int, input().split())
    d = d-1

    #파편
    papyun(d,s)

    #구슬 이동
    move_ball()

    #구슬 폭파 및 이동
    bump_ball()

    #그룹만들기
    number_ball = make_group()

    for x,y in order_pos:
        if x==shark_x and y == shark_y: continue
        if number_ball:
            graph[x][y] = number_ball.pop(0)

print(1*one_bump+2*two_bump+3*three_bump)


# 다른 내 풀이
from collections import deque
n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
graph[n//2][n//2]=4 # 상어

def makeroute():
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    route = []
    cx,cy = n//2,n//2
    d,step = 0,1
    while True:
        for _ in range(step):
            route.append((cx,cy))
            cx,cy = cx+dx[d],cy+dy[d]

        if not(0<=cx<n and 0<=cy<n):
            break

        d = (d+1)%4
        if d==0 or d==2:
            step+=1

    return route[1:]


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def sharkbomb(d,s):

    cx,cy = n//2,n//2
    for step in range(1,s+1):
        cx,cy = cx+dx[d], cy+dy[d]
        graph[cx][cy]=0

def moveball(): # 여기가 핵심

    zero_list = deque()
    for x,y in route:
        if graph[x][y]==0:
            zero_list.append((x,y))
        elif graph[x][y]!=0 and zero_list:
            nx,ny = zero_list.popleft()
            graph[nx][ny],graph[x][y] = graph[x][y],0
            zero_list.append((x,y))

def ballbomb():
    global first, second, third

    global_bomb_list = []
    bomb_list = []
    cnt = 0
    color = 0
    for x,y in route:

        if graph[x][y]!=color:
            if cnt>=4:
                global_bomb_list+=bomb_list
            bomb_list = [(x,y)]
            cnt=1
            color = graph[x][y]

        else:
            bomb_list.append((x,y))
            cnt+=1

        if not graph[x][y]:
            break

    if not global_bomb_list:
        return False

    for x,y in global_bomb_list:
        if graph[x][y]==1:
            first+=1
        elif graph[x][y]==2:
            second+=1
        elif graph[x][y]==3:
            third+=1
        graph[x][y]=0

    return True

def changeball():

    change_list = deque([])
    cnt = 0
    color = 0
    for x,y in route:

        if graph[x][y]!=color:
            if color:
                change_list += [cnt,color]
            cnt=1
            color = graph[x][y]
        else:
            cnt+=1

        if not graph[x][y]:
            break

    for x,y in route:
        if change_list:
            graph[x][y]=change_list.popleft()



first,second,third = 0,0,0
for _ in range(m):
    d,s = map(int, input().split())
    route = makeroute()


    # 상어가 구슬 파괴
    sharkbomb(d-1,s)

    # 구슬 이동
    moveball()

    while True:
        # 구슬 폭발 ...
        if not ballbomb():
            break
        # 구슬 이동
        moveball()

    # 구슬 변화
    changeball()

print(first + 2*second + 3*third)


# 위에 2번째 풀이랑 다른건 없지만 정답(answer)를 배열로 만들어서 폭발 구슬 개수를 구할때 시간을 좀더 단축했다.
# 배열로 함으로써 폭발한 구슬개수 구할때 조건문을 쓰지 않아도 된다.
from collections import deque

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
graph[n//2][n//2]=-1

def makeroute():
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    sx, sy = n // 2, n // 2
    d,step = 0,1

    route = []
    while True:
        for _ in range(step):
            sx,sy = sx+dx[d],sy+dy[d]
            route.append((sx,sy))

        if not(0<=sx<n and 0<=sy<n):
            break

        d = (d+1)%4
        if d == 0 or d==2:
            step+=1

    return route[:-1]

def sharkbomb(d,s):
    x,y = n//2,n//2
    for _ in range(s):
        x,y = x+dx[d],y+dy[d]
        graph[x][y]=0

def moveball():
    q = deque([])
    for x,y in route:
        if graph[x][y]==0:
            q.append((x,y))
        elif graph[x][y] and q:
            nx,ny = q.popleft()
            graph[x][y],graph[nx][ny]=graph[nx][ny],graph[x][y]
            q.append((x,y))

def ballbomb():
    global_list = []
    count = 0
    standard = 0
    bomb_list = []
    for x,y in route:
        if graph[x][y]!=standard:
            if count>=4:
                global_list+=bomb_list
            count=1
            standard=graph[x][y]
            bomb_list=[(x,y)]
        else:
            bomb_list.append((x,y))
            count+=1

    if not global_list:
        return False

    for x,y in global_list:
        answer[graph[x][y]]+=1
        graph[x][y]=0

    return True
def changeballs():
    temp = [[0]*n for _ in range(n)]
    temp[n//2][n//2]=-1

    candidate = []
    count=0
    standard = 0
    for x,y in route:
        if graph[x][y]!=standard:
            candidate+=[count,standard]
            count=1
            standard=graph[x][y]
        else:
            count+=1

    candidate = candidate[2:]
    for x,y in route:
        if candidate:
            value = candidate.pop(0)
            graph[x][y]=value

route = makeroute()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = [0,0,0,0]
for _ in range(m):
    d,s = map(int, input().split())
    sharkbomb(d-1,s)
    moveball()
    while True:
        if not ballbomb():
            break
        moveball()
    changeballs()
print(answer[1]+2*answer[2]+3*answer[3])