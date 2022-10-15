from collections import deque

n, m, k = map(int, input().split())

teamboard = [[-1] * n for _ in range(n)]  # 팀 구별
team = [deque([]) for _ in range(m)]  # 팀 좌표
graph = [] # 전체 그래프
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def findteam(x, y, teamcount): # 나중에 bfs로 해봐

    if graph[x][y]==3:
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and 2 <= graph[nx][ny] <= 3 and visit[nx][ny] == -1:
            if graph[x][y]==1:
                if graph[nx][ny]==2:
                    team[teamcount].append([nx, ny])
                    visit[nx][ny] = 1
                    teamboard[nx][ny] = teamcount
                    findteam(nx, ny, teamcount)
            else:
                team[teamcount].append([nx, ny])
                visit[nx][ny] = 1
                teamboard[nx][ny] = teamcount
                findteam(nx,ny,teamcount)

# 팀 위치 구하기
visit = [[-1] * n for _ in range(n)]
teamcount = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            visit[i][j]=1
            teamboard[i][j]=teamcount
            team[teamcount].append([i, j])
            findteam(i, j, teamcount)
            teamcount += 1

# for t in team:
#     print(t)
# for tb in teamboard:
#     print(tb)

answer = 0
for z in range(k):

    # 1단계 - 한칸 식 이동하기
    for i in range(m):
        #print(i,'32r32r')
        for d in range(4):
            nx, ny = team[i][0][0] + dx[d], team[i][0][1] + dy[d]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] in [3,4]:
                #print(team[i][0][1],team[i][0][2],nx,ny)
                # 먼저 team변환
                # 그다음 그래프 변환
                graph[team[i][0][0]][team[i][0][1]] = 2 # 머리는 이제 두번째 위치로

                team[i].appendleft([nx, ny]) # 머리 삽입
                graph[nx][ny] = 1
                teamboard[nx][ny]=i

                x,y = team[i].pop() #꼬리 빼기
                if graph[x][y]==3:
                    graph[x][y] = 4
                    teamboard[x][y]=-1

                graph[team[i][-1][0]][team[i][-1][1]] = 3 # 새로운 꼬리

                break

    # 2단계 - 공 던지기
    z = z % (4 * n)
    # 왼쪽
    if z < n:
        #print('left')
        #print(z)
        i = z
        for j in range(n):
            if teamboard[i][j] >= 0:  # 맞았다.
                # 공획득
                # print(i, j)
                for idx, value in enumerate(team[teamboard[i][j]]):
                    if value[0] == i and value[1] == j:
                        answer += (idx + 1) ** 2
                        break
                        #print(idx+1)
                # 대가리 바꿔
                team[teamboard[i][j]].reverse()
                graph[team[teamboard[i][j]][0][0]][team[teamboard[i][j]][0][1]] = 1
                graph[team[teamboard[i][j]][-1][0]][team[teamboard[i][j]][-1][1]] = 3
                break
    # 아래쪽
    elif z < 2 * n:
        #print('bellow')
        z = z % n
        #print(z)
        j = z
        for i in range(n - 1, -1, -1):
            if teamboard[i][j] >= 0:  # 맞았고 아직 팀 만난 적 없다.
                # 공획득
                for idx, value in enumerate(team[teamboard[i][j]]):
                    if value[0] == i and value[1] == j:
                        answer += (idx + 1) ** 2
                        break
                        #print(idx+1)
                # 대가리 바꿔
                team[teamboard[i][j]].reverse()
                graph[team[teamboard[i][j]][0][0]][team[teamboard[i][j]][0][1]] = 1
                graph[team[teamboard[i][j]][-1][0]][team[teamboard[i][j]][-1][1]] = 3
                break
    # 오른쪽
    elif z < 3 * n:
        #print('rigft')
        z = n - 1 - (z % n)
        #print(z)
        i = z
        for j in range(n - 1, -1, -1):
            if teamboard[i][j] >= 0:  # 맞았고 아직 팀 만난 적 없다.
                # 공획득
                for idx, value in enumerate(team[teamboard[i][j]]):
                    if value[0] == i and value[1] == j:
                        answer += (idx + 1) ** 2
                        break
                        #print(idx+1)
                # 대가리 바꿔
                team[teamboard[i][j]].reverse()
                graph[team[teamboard[i][j]][0][0]][team[teamboard[i][j]][0][1]] = 1
                graph[team[teamboard[i][j]][-1][0]][team[teamboard[i][j]][-1][1]] = 3
                break
    # 위쪽
    elif z < 4 * n:
        #print('up')
        z = n - 1 - (z % n)
        #print(z)
        j = z
        for i in range(n):
            if teamboard[i][j] >= 0:  # 맞았고 아직 팀 만난 적 없다.
                # 공획득
                for idx, value in enumerate(team[teamboard[i][j]]):
                    if value[0] == i and value[1] == j:
                        answer += (idx + 1) ** 2
                        break
                        #print(idx+1)
                # 대가리 바꿔
                team[teamboard[i][j]].reverse()
                graph[team[teamboard[i][j]][0][0]][team[teamboard[i][j]][0][1]] = 1
                graph[team[teamboard[i][j]][-1][0]][team[teamboard[i][j]][-1][1]] = 3
                break
    # print(answer)


    # for g in graph:
    #     print(g)
    # for t in team:
    #     print(t)
    # print()

print(answer)

# 내풀이 2 : 1보다 훨씬 낫다 ========================================================
from collections import deque
n,m,k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
team = [[-1]*n for _ in range(n)]
teaminfo = []
def maketeaminfo(x,y,teamnum,info):

    q = deque([(x,y)])
    team[x][y]=teamnum
    info.append((x,y))

    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx,ny = cx+dx[i],cy+dy[i]
            if 0<=nx<n and 0<=ny<n and team[nx][ny]==-1:
                if graph[cx][cy]==1:
                    if graph[nx][ny]==2:
                        q.append((nx,ny))
                        team[nx][ny]=teamnum
                        info.append((nx, ny))
                else:
                    if graph[nx][ny]!=4 and graph[nx][ny]!=0:
                        q.append((nx,ny))
                        team[nx][ny]=teamnum
                        info.append((nx, ny))

def maketeam():
    teamnum = -1
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1:
                info = []
                teamnum+=1
                maketeaminfo(i,j,teamnum,info)
                teaminfo.append(deque(info))
maketeam()

def move():
    for i in range(m):
        fx,fy = teaminfo[i][0] # 머리!

        for d in range(4):
            nx,ny = fx+dx[d],fy+dy[d]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==4: # 머리가 이동하려는 칸에 철로가 있을때
                    lx, ly = teaminfo[i].pop()  # 꼬리 뺌
                    # graph변경
                    graph[nx][ny],graph[fx][fy],graph[lx][ly] = 1,2,4
                    graph[teaminfo[i][-1][0]][teaminfo[i][-1][1]]=3
                    # team 변경
                    team[nx][ny],team[lx][ly]=i,-1
                    # teaminfo 변경
                    teaminfo[i].appendleft((nx,ny))
                    break

                elif graph[nx][ny]==3: # 머리가 이동하려는 칸에 꼬리가 있을때
                    teaminfo[i].pop()  # 꼬리 뺌
                    # graph변경
                    lx,ly = teaminfo[i][-1]
                    graph[nx][ny],graph[fx][fy],graph[lx][ly] = 1,2,3
                    # team 변경 -> 할꺼없다
                    # teaminfo 변경
                    teaminfo[i].appendleft((nx,ny))
                    break
def doreverse(teamnum):

    # graph변경
    fx,fy = teaminfo[teamnum][0]
    lx,ly = teaminfo[teamnum][-1]
    graph[fx][fy],graph[lx][ly]=3,1
    # team변경 -> 필요없음
    # teaminfo 변경
    teaminfo[teamnum].reverse() # ********  deque는 [::-1]안댐! -> .reverse()해야함!&그리고 reverse()는 원본건드림


def throw(step):
    global answer

    step%=(4*n)

    if step<n:
        for j in range(n):
            if team[step][j]>-1:
                idx = teaminfo[team[step][j]].index((step,j))
                answer+=((idx+1)**2)
                #뒤집기
                doreverse(team[step][j])
                break
    elif step<2*n:
        step%=n
        for i in range(n-1,-1,-1):
            if team[i][step]>-1:
                idx = teaminfo[team[i][step]].index((i,step))
                answer += ((idx + 1) ** 2)
                #뒤집기
                doreverse(team[i][step])
                break
    elif step<3*n:
        step %= n
        step = n-1-step
        for j in range(n-1,-1,-1):
            if team[step][j]>-1:
                idx = teaminfo[team[step][j]].index((step,j))
                answer+=((idx+1)**2)
                #뒤집기
                doreverse(team[step][j])
                break
    elif step<4*n:
        step%=n
        step = n-1-step
        for i in range(n):
            if team[i][step]>-1:
                idx = teaminfo[team[i][step]].index((i,step))
                answer += ((idx + 1) ** 2)
                #뒤집기
                doreverse(team[i][step])
                break

answer = 0
for step in range(k):
    # 모든 팀이 한칸 움직인다.
    move()
    # 공을 던진다.
    throw(step)

print(answer)

# 타인 풀이===========================================================
from collections import deque, defaultdict

# 보드 크기, 팀 개수, 라운드 수
n, m, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

score_dict = defaultdict(lambda: 0)

# 우, 상, 좌, 하
# 공 날라오는 방향에 맞췄음
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 팀 번호로 구성된 보드
team_board = [[0 for _ in range(n)] for _ in range(n)]
team_num = 1
# 키값은 팀 번호, 맨 처음이 머리사람, 마지막이 꼬리사람
team_dict = defaultdict(lambda: [])
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            visited = set()
            deq = deque()
            deq.append([i, j])
            while deq:
                x, y = deq.popleft()
                if (x, y) not in visited:
                    visited.add((x, y))
                    team_board[x][y] = team_num
                    team_dict[team_num].append((x, y))

                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[x][y] == 1:
                                if board[nx][ny] == 2:
                                    deq.append([nx, ny])
                            else:
                                if board[nx][ny] in (2, 3):
                                    deq.append([nx, ny])
            team_num += 1

# for i in team_board:
#     print(i)
# for i in team_dict:
#     print(i, team_dict[i])


def move():
    for key in team_dict:
        sx, sy = team_dict[key][0]
        for d in range(4):
            nx, ny = sx + dx[d], sy + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] != 0 and (nx, ny) != team_dict[key][1]:
                    team_dict[key].insert(0, (nx, ny))
                    rx, ry = team_dict[key].pop()
                    team_board[rx][ry] = 0
                    team_board[nx][ny] = key
                    break


def ball_shoot(r):
    x, y, d = get_ball_pos(r)
    while True:
        if not (0 <= x < n and 0 <= y < n):
            return
        if team_board[x][y] != 0:
            team_num = team_board[x][y]
            team_calc(x, y, team_num)
            return
        x, y = x + dx[d], y + dy[d]


# 우, 상, 좌, 하
# 라운드에 따라 처음 공이 발사될 위치 및 방향 지정
def get_ball_pos(r):
    r = r % (n * 4)
    d = r // n
    offset = r % n
    x, y = -1, -1
    if d == 0:
        x, y = 0, 0
    elif d == 1:
        x, y = n - 1, 0
    elif d == 2:
        x, y = n - 1, n - 1
    elif d == 3:
        x, y = 0, n - 1
    x, y = x + dx[d - 1] * offset, y + dy[d - 1] * offset
    return x, y, d


# 공이 맞은 인원이 속한 팀의 리스트를 반대로 바꾸고 점수 갱신
def team_calc(x, y, t):
    idx = team_dict[t].index((x, y)) + 1
    score_dict[t] += idx ** 2
    team_dict[t] = team_dict[t][::-1]


for r in range(k):
    # for i in team_dict:
    #     print(i, team_dict[i])
    # print()
    move()

    ball_shoot(r)

answer = 0
for i in score_dict:
    answer += score_dict[i]

print(answer)