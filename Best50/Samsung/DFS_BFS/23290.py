from collections import deque
from copy import deepcopy

m,s = map(int, input().split())
#물고기(방향) 및 상어
graph = [[[] for _ in range(4)] for _ in range(4)]
#물고기 냄새 초!
smell = [[0]*4 for _ in range(4)]
#물고기 저장
fishes = deque()
for _ in range(m):
    fishes.append(list(map(int, input().split())))
fdx = [0,-1,-1,-1,0,1,1,1]
fdy = [-1,-1,0,1,1,1,0,-1]

#상어 저장
sx,sy = map(int, input().split())
sx,sy = sx-1,sy-1 # 인덱스 조심해라 진짜
sdx = [-1,0,1,0]
sdy = [0,-1,0,1]

def move_fish():
    for fish in fishes:
        flag = False
        x,y,d = fish[0]-1,fish[1]-1,fish[2]-1 #인덱스 조심해라 진짜
        for i in range(8):
            nx = x + fdx[(d-i)%8]
            ny = y + fdy[(d-i)%8]
            # if x==1 and y==3 and d == 1: print(nx,ny,smell[nx][ny])
            if 0<=nx<4 and 0<=ny<4 and smell[nx][ny]==0 and (nx!=sx or ny!=sy):
                graph[nx][ny].append((d-i)%8)
                flag=True
                break
        if flag:
            continue
        else:
            graph[x][y].append((d))

def move_shark(x,y,count):
    global max_ate,max_ate_fishes,sx,sy

    if count == 3:
        eat = sum(list(map(lambda k:len(graph[k[0]][k[1]]), ate_fishes)))
        if max_ate<eat:
            max_ate = eat
            sx,sy = x,y #3번 움직였을때 들어온 매개변수 x,y가 상어의 마지막 위치다!!!!!!
            max_ate_fishes = deepcopy(ate_fishes)# 조심해라 진짜
        return

    for i in range(4):
        nx = x + sdx[i]
        ny = y + sdy[i]

        if 0<=nx<4 and 0<=ny<4: #예를 들어 '상하상' 도 되자낭
            if visit[nx][ny]==0:
                ate_fishes.append((nx,ny))
                visit[nx][ny]=1
                move_shark(nx,ny,count+1)
                ate_fishes.pop()
                visit[nx][ny]=0
            else:
                move_shark(nx,ny,count+1)



def remove_fish():

    for x,y in max_ate_fishes:
        if graph[x][y]:
            graph[x][y] = []
            smell[x][y] = 3


def remove_smell():
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j]-=1

def copy_fishes():
    for i in range(4):
        for j in range(4):
            if len(graph[i][j])!=0:
                while graph[i][j]:
                    fishes.append((i+1,j+1,graph[i][j].pop()+1))

for _ in range(s):
    move_fish()
    #밑에 세줄은 함수 들어갈때마다 초기화 해줘야하므로 여기 있어야 한다.
    ate_fishes = []
    max_ate = -1  # 일단 해보자
    max_ate_fishes = []

    visit = [[0] * 4 for _ in range(4)]
    #visit[sx][sy] = 1 이거 해도되고 안해도 됨 -->?(확실치않음) 왜냐면 '상하좌','하상좌',... 즉, 모든 경우에 3번만에 상어가 다시 출발지점으로 돌아오는 일은 없기때문이다.
    move_shark(sx,sy,0)

    remove_fish()
    remove_smell()
    copy_fishes()


answer = len(fishes)
print(answer)

# 또 다른 내 풀이
from collections import deque

m, s = map(int, input().split())
graph = [[[] for _ in range(4)] for _ in range(4)]  # 물고기 정보
smell = [[0] * 4 for _ in range(4)]

for _ in range(m):
    x, y, d = map(int, input().split())
    graph[x - 1][y - 1].append(d - 1)
sharkx, sharky = map(lambda x: int(x) - 1, input().split())

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


def changedirection(d):
    return (d - 1) % 8


def movefish():
    temp = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            if graph[i][j]:
                for d in graph[i][j]:
                    flag = False
                    for _ in range(8):
                        nx, ny = i + dx[d], j + dy[d]
                        if not (0 <= nx < 4 and 0 <= ny < 4):
                            d = changedirection(d)
                            continue
                        if nx == sharkx and ny == sharky:
                            d = changedirection(d)
                            continue
                        if smell[nx][ny]:
                            d = changedirection(d)
                            continue
                        temp[nx][ny].append(d)
                        flag = True
                        break

                    if not flag:
                        temp[i][j].append(d)

    return temp


def movefish2():  # d 처리하는 부분이 movefish보다 좀더 직관적이다

    temp = [[[] for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            if graph[i][j]:
                for d in graph[i][j]:
                    flag = False
                    for k in range(8):
                        nx, ny = i + dx[(d - k) % 8], j + dy[(d - k) % 8]
                        if not (0 <= nx < 4 and 0 <= ny < 4):
                            continue
                        if nx == sharkx and ny == sharky:
                            continue
                        if smell[nx][ny]:
                            continue
                        temp[nx][ny].append((d - k) % 8)
                        flag = True
                        break

                    if not flag:
                        temp[i][j].append(d)

    return temp


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def moveshark(x, y, count, eat, candi):
    global result, result_candi, sharkx, sharky

    if count == 3:
        if result < eat:
            result = eat
            result_candi = candi
            sharkx, sharky = x, y  # 3번 움직였을때 들어온 매개변수 x,y가 상어의 마지막 위치다!!!!!!
        return

    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if not ate[nx][ny]:
                ate[nx][ny] = 1
                moveshark(nx, ny, count + 1, eat + len(graph[nx][ny]), candi + [(nx, ny)])
                ate[nx][ny] = 0
            else:
                moveshark(nx, ny, count + 1, eat, candi + [(nx, ny)])


for _ in range(s):

    # 복제
    fish = deque([])
    for a in range(4):
        for b in range(4):
            if graph[a][b]:
                for d in graph[a][b]:
                    fish.append((a, b, d))

    # 물고기 이동
    graph = movefish2()

    # 상어 이동
    result = -1  # 상어가 물고기를 못먹고 이동만 할 수도 있자나
    result_candi = []
    ate = [[0] * 4 for _ in range(4)]
    moveshark(sharkx, sharky, 0, 0, [])

    # 위에 moveshark()의 종료조건에서 이미 처리해줫다
    # 근데 아래 방법이 시간은 더 빠르다
    # sharkx,sharky = result_candi[-1][0],result_candi[-1][1]

    # 냄새 사라짐
    for a in range(4):
        for b in range(4):
            if smell[a][b]:
                smell[a][b] -= 1
    # 냄새 살포
    for x, y in result_candi:
        if graph[x][y]:
            graph[x][y] = []
            smell[x][y] = 2  # 여기를 3으로하고 # 냄새 사라짐과 위치 바꿔도 된다.

    # 복제 완료
    for a, b, d in fish:
        graph[a][b].append(d)

    # for g in graph:
    #     print(g)
    # print(sharkx,sharky)

answer = 0
for x in range(4):
    for y in range(4):
        answer += len(graph[x][y])
print(answer)