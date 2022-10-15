from collections import deque

n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(start_x,start_y,group_color,rainbow_list): #시작노드는 일반

    q = deque([(start_x, start_y)])
    visit[start_x][start_y] = group_color

    count = 1
    rainbow_count = 0

    while q:

        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0 and graph[nx][ny] != -1:
                if graph[nx][ny] == graph[start_x][start_y]:
                    q.append((nx,ny))
                    visit[nx][ny] = group_color
                    count+=1
                elif graph[nx][ny] == 0:
                    q.append((nx,ny))
                    visit[nx][ny] = group_color
                    count+=1
                    rainbow_count+=1
                    rainbow_list.append((nx,ny))

    for a,b in rainbow_list:
        visit[a][b]=0

    return count, rainbow_count

'''
1. 이 global_rainbow_list가 핵심 --> https://www.acmicpc.net/board/view/74924
위 링크처럼 무지개 가 겹치는 경우도 처리 해줘야 하므로 
'''
global_rainbow_list = []
def find_block():
    global max_leader, global_rainbow_list

    color = 1
    for i in range(n):
        for j in range(n):
            if graph[i][j]>=1 and visit[i][j]==0:

                rainbow_list = []
                color+=1 #그룹 식별별
                a,b = bfs(i,j,color,rainbow_list) #그룹 1개 생성

                '''
                2. 여기 조건문 핵심 
                if ~~:
                elif A:
                    if ~~~: # A가 조건이 맞아서 여기 if문이 실행 되는데 여기 if문이 거짓이라 elif A를 나가게 되도 elif B로 가지 않는다!!!! 그래서 if-else가 아닌 if-if로 코드 작성함
                elif B
                '''
                if max_leader[1]<a:
                    max_leader = [(i,j),a,b]
                    global_rainbow_list = rainbow_list
                if max_leader[1]==a:
                    if max_leader[2]<b:
                        max_leader = [(i,j),a,b]
                        global_rainbow_list = rainbow_list
                if max_leader[1]==a and max_leader[2] == b:
                    if max_leader[0][0]<i:
                        max_leader = [(i, j), a, b]
                        global_rainbow_list = rainbow_list
                    elif max_leader[0][0]==i:
                        if max_leader[0][1]<j:
                            max_leader = [(i, j), a, b]
                            global_rainbow_list = rainbow_list

def remove_block(x,y):

    graph[x][y] = -10

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n:
            if visit[max_leader[0][0]][max_leader[0][1]]==visit[nx][ny] or (nx,ny) in global_rainbow_list:
                if graph[nx][ny] >= 0:
                    remove_block(nx,ny)

#중력 작용
def do_gravity(): #graph를 밑에서 수정해줘야 나중에 또 안만난다.

    for i in range(n-2,-1,-1):
        for j in range(n):
            if graph[i][j] >-1:
                r = i

                while True:
                    if 0<=r+1<n and graph[r+1][j]==-10:
                        graph[r+1][j] = graph[r][j]
                        graph[r][j]= -10
                        r+=1
                    else:
                        break
# 반시계 회전 함수
def rot90(a):
    new_a = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_a[n-1-j][i] = a[i][j]
    return new_a

score = 0
while True:

    visit = [[0] * n for _ in range(n)]
    max_leader = [(-1, -1), -1, -1]

    find_block()
    if max_leader[1]<2:
        print(score)
        break
    remove_block(max_leader[0][0], max_leader[0][1])
    score += max_leader[1]**2
    do_gravity()
    graph = rot90(graph)
    do_gravity()

# 내 풀이 1
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, color, group, visit):
    visit[x][y] = 1
    group.append((x, y))

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < n and 0 <= ny < n):
            continue
        if visit[nx][ny] == -1:
            if graph[nx][ny] == 0 or graph[nx][ny] == color:  # 무지개 블록 or 일반블록
                dfs(nx, ny, color, group, visit)


def findgroup():
    # 그룹을 찾기 -> 즉 글로벌 변수들이 필요하다
    blocks = []  # 그룹 블록들
    block_cnt = 0  # 그룹 블록 개수
    rainbowblock = -1  # 무지개 블록 개수
    sx, sy = -1, -1  # 기준 블록 좌표

    for i in range(n):
        for j in range(n):
            visit = [[-1] * n for _ in range(n)] # 만약 같은 0(무지개)를 다른 일반 블록이 동시에 접근할 수 도 있으므로

            if graph[i][j] > 0 and visit[i][j] == -1:
                flag = False

#=================================================================
                # 아래 세가지 변수 구하는 과정 -> 위 글로벌 변수들과 비교하기 위해서는 같은 종류의 지역 변수가 필요하다.
                group = []  # 그룹 블록들
                rainbowcnt = 0  # 무지개 블록 개수
                cx, cy = n, n  # 기준 블록 좌표

                dfs(i, j, graph[i][j], group, visit)
                length = len(group)
                if length < 2: continue

                # 무지개 블록이랑 기준 좌표 구하기
                for a, b in group:
                    if graph[a][b] == 0:
                        rainbowcnt += 1
                    else:
                        if cx > a:
                            cx, cy = a, b
                        elif cx == a:
                            if cy > b:
                                cx, cy = a, b
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==

                if length > block_cnt:  # 만약 더 큰 블록이라면
                    flag = True

                elif length == block_cnt:  # 만약 같다면

                    if rainbowblock < rainbowcnt:
                        flag = True
                    elif rainbowblock == rainbowcnt:
                        if sx < cx:
                            flag = True
                        elif sx == cx:
                            if sy < cy:
                                flag = True
                if flag:
                    blocks = group
                    block_cnt = length
                    rainbowblock = rainbowcnt
                    sx, sy = cx, cy
    return blocks,block_cnt


def gravity(graph):
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if graph[i][j] >= 0:  # 검은색 블록이 아니라면
                ni, nj = i, j
                while True:
                    ni, nj = ni + 1, nj
                    if ni >= n or graph[ni][nj] >= -1:  # 경계 나가거나 다른블록 만나면
                        ni, nj = ni - 1, nj
                        break
                graph[ni][nj], graph[i][j] = graph[i][j], graph[ni][nj]


def turn_left(graph):
    n = len(graph)
    m = len(graph[0])
    new_graph = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_graph[m - j - 1][i] = graph[i][j]
    return new_graph


answer = 0
while True:
    candidate,length = findgroup()

    if length < 2:
        print(answer)
        exit(0)

    answer += length ** 2  # 점수 획득
    for a, b in candidate:
        graph[a][b] = -2  # 빈칸

    # 중력
    gravity(graph)
    # 회전
    graph = turn_left(graph)
    # 중력
    gravity(graph)

#내 풀이 2 : 풀이 1이랑 별 차이 없다
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def makegroup(x,y,color,visit,blocks):
    visit[x][y]=1
    blocks.append((x,y))

    for d in range(4):
        nx,ny = x+dx[d],y+dy[d]
        if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
            if graph[nx][ny]==0 or graph[nx][ny]==color:
                makegroup(nx,ny,color,visit,blocks)


def findgroup():
    standardgroup = []
    scount = 0
    srainbow = 0
    sblockx,sblocky = -1,-1

    for i in range(n):
        for j in range(n):
            if graph[i][j]>0:
                visit = [[0]*n for _ in range(n)]
                blocks = []
                makegroup(i,j,graph[i][j],visit,blocks)

                if len(blocks)<2: continue

                # 블록 그룹 정보 만들기
                count=0
                rainbow=0
                blockx,blocky = int(1e9),int(1e9)
                for x,y in blocks:
                    count+=1
                    if graph[x][y]==0:
                        rainbow+=1
                    else:
                        if x<blockx:
                            blockx,blocky = x,y
                        elif x==blockx:
                            if y<blocky:
                                blockx,blocky=x,y

                # 글로벌 블록 그룹 찾기
                flag = False
                if scount<count:
                    flag = True
                elif scount==count:
                    if srainbow<rainbow:
                        flag = True
                    elif srainbow==rainbow:
                        if sblockx<blockx:
                            flag = True
                        elif sblockx==blockx:
                            if sblocky<blocky:
                                flag = True
                if flag:
                    standardgroup = blocks
                    scount = count
                    srainbow = rainbow
                    sblockx, sblocky = blockx,blocky

    return standardgroup,scount

def removeblocks(group,count):
    global answer
    for x,y in group:
        graph[x][y]=-10
    answer += count**2

def gravity():
    for i in range(n-1,-1,-1):
        for j in range(n):
            if graph[i][j]>-1:
                cx,cy = i,j
                while True:
                    nx,ny = cx+1,cy
                    if nx>=n:
                        graph[cx][cy],graph[i][j]=graph[i][j],graph[cx][cy]
                        break
                    if graph[nx][ny]!=-10:
                        graph[cx][cy],graph[i][j]=graph[i][j],graph[cx][cy]
                        break
                    cx,cy = nx,ny
def rotate(graph):
    new_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[n-1-j][i] = graph[i][j]
    return new_graph

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
while True:
    arr,cnt = findgroup()

    if not cnt:
        print(answer)
        break

    removeblocks(arr,cnt)
    gravity()
    graph = rotate(graph)
    gravity()