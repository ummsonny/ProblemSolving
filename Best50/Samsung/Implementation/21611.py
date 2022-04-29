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
