# 이 풀이는 몰고기가 이동할 때 4*4배열을 다 탐색하는 시간을 줄이기 위해
# fish라는 배열을 따로 생성함 -> 근데 그렇게 시간단축에 효과 있는지는 모르겟당
# 탐색할때 상태를 항상 따로 저장해둬야한다!!!!!
graph = [[0 for _ in range(4)] for _ in range(4)] # 번호
fish = [[] for _ in range(17)] # 물고기 위치 및 방향 저장
for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(4):
        graph[i][j] = arr[2*j]
        fish[arr[2*j]] = [i,j,arr[2*j+1]-1]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]


def turn_left(direction):
    return (direction+1)%8

answer = -1
def dfs(shx,shy,graph,fish,ate):
    global answer

    temp = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            temp[i][j] = graph[i][j]

    femp = [[] for _ in range(17)]
    for i in range(1,17):
        femp[i] = [fish[i][0], fish[i][1], fish[i][2]]

    # 상어가 먹어
    ate += temp[shx][shy]
    shd = femp[temp[shx][shy]][2]
    femp[temp[shx][shy]][2] = -1
    temp[shx][shy]=0


    # 물고기 이동
    for i in range(1,17):
        cx,cy,cd = femp[i] #물고기
        if cd>-1:
            for _ in range(8):
                nx,ny = cx+dx[cd],cy+dy[cd]
                # 만약 경계를 벗어나거나 상어있다면
                if not(0<=nx<4 and 0<=ny<4) or (nx==shx and ny==shy):
                    cd = turn_left(cd)
                    continue
                #만약 빈칸
                if temp[nx][ny]==0:
                    temp[cx][cy],temp[nx][ny]=temp[nx][ny],temp[cx][cy]
                    femp[temp[nx][ny]]=[nx,ny,cd]
                #만약 다른 물고기
                else:
                    temp[cx][cy], temp[nx][ny] = temp[nx][ny], temp[cx][cy]
                    femp[temp[nx][ny]] = [nx, ny, cd]
                    femp[temp[cx][cy]][0],femp[temp[cx][cy]][1] = cx,cy
                break

    # 종료조건
    candidate = []
    while True:
        nx,ny = shx+dx[shd], shy+dy[shd]
        if not(0<=nx<4 and 0<=ny<4):
            break
        if temp[nx][ny]>0:
            candidate.append((nx,ny))
        shx,shy = nx,ny

    if len(candidate)<=0:
        answer = max(answer,ate)
        return
    else:
        for a,b in candidate:
            dfs(a,b,temp,femp,ate)


dfs(0,0,graph,fish,0)
print(answer)

# 여기 밑에 굉장히 중요한 개념이 있다.
graph = [[[]for _ in range(4)] for _ in range(4)]
fish = [[] for _ in range(17)]
for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(4):
        graph[i][j] = [arr[2*j],arr[2*j+1]-1]
        fish[arr[2*j]]=[i,j]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def changedir(d):
    return (d+1)%8

def fishmove(sx,sy,graph,fish):

    for idx in range(1,17):
        if fish[idx]:
            cx,cy = fish[idx]
            d = graph[cx][cy][1]
            for _ in range(8):
                nx,ny = cx+dx[d],cy+dy[d]
                if not(0<=nx<4 and 0<=ny<4):
                    d=changedir(d)
                    continue
                if sx==nx and sy==ny:
                    d=changedir(d)
                    continue
                graph[cx][cy][1]=d
                graph[cx][cy],graph[nx][ny]=graph[nx][ny],graph[cx][cy]

                # 만약 물고기가 있는 칸이라면
                if graph[cx][cy]:
                    fish[graph[cx][cy][0]] = [cx, cy]
                # 만약 물고기가 없는 칸이라면-> 암것도 안해도됨

                fish[graph[nx][ny][0]] = [nx,ny]
                break


def sharkmove(sx,sy,sd,temp):
    candi = []
    while True:
        nx,ny = sx+dx[sd],sy+dy[sd]
        if not(0<=nx<4 and 0<=ny<4):
            break
        if temp[nx][ny]:
            candi.append((nx,ny))
        sx,sy=nx,ny
    return candi

answer = -1
def dfs(sx,sy,eat,graph,fish):
    global answer

    temp = [[[] for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            if graph[a][b]:
                temp[a][b]=[graph[a][b][0],graph[a][b][1]] # temp[a][b]=graph[a][b] 안됨! graph[a][b]가 배열이라 같은 주소값을 참고함
    fishtemp = [[] for _ in range(17)]
    for idx in range(1,17):
        if fish[idx]:
            fishtemp[idx]=[fish[idx][0],fish[idx][1]] # 여기도 4줄 위에랑 같은 이유로 이렇게 복사해줘야함

    eat+=temp[sx][sy][0]
    sd = temp[sx][sy][1]
    fishtemp[temp[sx][sy][0]]=[]
    temp[sx][sy]=[]

    fishmove(sx,sy,temp,fishtemp)
    candidiate = sharkmove(sx,sy,sd,temp)

    if not candidiate:
        answer = max(answer,eat)
        return

    for a,b in candidiate:
        dfs(a,b,eat,temp,fishtemp)

dfs(0,0,0,graph,fish)
print(answer)