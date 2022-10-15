n = int(input()) # 반드시 홀수
masterpic = []
for _ in range(n):
    masterpic.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def group(x,y,groupid,groupcolor):
    global cnt

    visit[x][y]=groupcolor
    cnt+=1

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and visit[nx][ny]==-1:
            if masterpic[nx][ny]==groupid:
                group(nx,ny,groupid,groupcolor)

def findbyun(candi):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j]==candi[0][0]:
                for d in range(4):
                    nx,ny = i+dx[d],j+dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if visit[nx][ny]==candi[1][0]:
                            cnt+=1
    return cnt
''' 내 풀이
def makescore(start,count):
    global score
    if count == 2:
        byun = findbyun(candi)
        score += ((candi[0][2]+candi[1][2])*candi[0][1]*candi[1][1]*byun)
        return

    for i in range(start,length):
        candi.append((i,info[i][0],info[i][1])) # 그룹 번호, 숫자, 개수
        makescore(i+1,count+1)
        candi.pop()
'''
# 답지 풀이!! 변이 2번 중복되서 계산 됨을 생각!
def makescore2():
    global score

    cnt=0
    for i in range(n):
        for j in range(n):
            for d in range(4):
                nx,ny = i+dx[d], j+dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if visit[i][j]!=visit[nx][ny]:
                        a = info[visit[i][j]][1]+info[visit[nx][ny]][1]
                        b = info[visit[i][j]][0]
                        c = info[visit[nx][ny]][0]
                        cnt += (a*b*c)
    score += cnt//2

def dorotate():
    new_graph = [[0]*n for _ in range(n)]
    # 십자가 반시계
    for j in range(n):# 가로
        new_graph[n-1-j][n//2]=masterpic[n//2][j]
    for i in range(n):# 세로
        new_graph[n-1-n//2][i]=masterpic[i][n//2]
    # 나머지 시계
    temp = [(0,0),(0,n//2+1),(n//2+1,0),(n//2+1,n//2+1)]
    for a,b in temp:
        for i in range(n//2):
            for j in range(n//2):
                new_graph[a+j][b+n//2-1-i] = masterpic[a+i][b+j]

    return new_graph

score = 0
for _ in range(4):

    # 1. 그룹 정보 만들기
    info = []  # (숫자, 속한 칸의 수)
    visit = [[-1]*n for _ in range(n)]
    groupcolor=-1 # 그룹 구별
    for i in range(n):
        for j in range(n):
            if visit[i][j]==-1:
                groupcolor+=1
                cnt = 0

                group(i,j,masterpic[i][j],groupcolor)

                info.append((masterpic[i][j],cnt))

    # 2. dfs로 그룹 2가지 뽑아내서 예술점수 구하기

    # 내 풀이
    # 이 풀이는 조합인데 변을 공유하지 않는 그룹끼리도 계산하므로 시간이 오래걸린다.
    # 변을 공유하지 않는 그룹끼리는 계산할 필요가 없다.
    #candi, length = [],len(info)
    #makescore(0,0)

    # 답안풀이
    makescore2()


    # 회전
    masterpic = dorotate()

print(score)

# 그냥 한 번 더 풀어본 풀이 회전하는 함수의 경우는 위에가 훠얼씬 좋다!!!!
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def makegroup(i,j,color,groupnum):
    global count

    group[i][j]=groupnum
    count+=1

    for d in range(4):
        nx,ny = i+dx[d],j+dy[d]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==color and group[nx][ny]==-1:
            makegroup(nx,ny,color,groupnum)
def makevalue():
    result = 0

    for i in range(n):
        for j in range(n):
            for d in range(4):
                nx,ny = i+dx[d],j+dy[d]
                if 0<=nx<n and 0<=ny<n and group[nx][ny]!=group[i][j]:
                    a = groupinfo[group[i][j]][0]+groupinfo[group[nx][ny]][0]
                    b,c = groupinfo[group[i][j]][1],groupinfo[group[nx][ny]][1]
                    result +=(a*b*c)

    return result//2

def rotate():
    new_graph = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i==n//2 or j==n//2:
                new_graph[n-1-j][i] = graph[i][j]

    # 십자가 이외에 시계방향 회전!
    for a in range(0,n,n//2+1):
        for b in range(0,n,n//2+1):
            for i in range(n//2):
                for j in range(n//2):
                    new_graph[a+j][b+n//2-1-i] = graph[a+i][b+j]

    return new_graph
answer = 0
for step in range(4):

    # 조화로움 값 구하기
    # 1. 각 그룹 정보 구하기
    group = [[-1] * n for _ in range(n)]
    groupinfo = [] # (속한 칸의수, 이루고 있는 숫자 값)
    groupnum = -1

    for i in range(n):
        for j in range(n):
            if group[i][j]==-1:
                count = 0
                groupnum+=1
                makegroup(i,j,graph[i][j],groupnum)
                groupinfo.append((count,graph[i][j]))

    # 2. 조화로움 계산하기
    answer+=makevalue()

    # 3회전 이후 예술점수만 계산하고 프로그램 종료해야지
    if step == 3: break

    # 회전하기
    graph = rotate()

print(answer)