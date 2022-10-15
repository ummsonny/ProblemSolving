dx = [-1,1,0,0]
dy = [0,0,1,-1]
def grow_tree(graph):
    new_graph = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j]<0:
                new_graph[i][j]=graph[i][j]
            elif graph[i][j]>0:
                count_tree = 0
                empty = []
                for d in range(4):
                    ni = i+dx[d]
                    nj = j+dy[d]
                    if 0<=ni<n and 0<=nj<n and graph[ni][nj]>0:
                        count_tree+=1
                    elif 0<=ni<n and 0<=nj<n and graph[ni][nj]==0:
                        empty.append((ni,nj))
                graph[i][j]+=count_tree

                new_graph[i][j]=graph[i][j]
                count_empty = len(empty)
                if count_empty>0:
                    spread = new_graph[i][j]//count_empty
                    for x,y in empty:
                        new_graph[x][y]+=spread

    return new_graph

dxx = [-1,-1,1,1]
dyy = [-1,1,-1,1]
def find(graph):
    max_x,max_y,max_sum = -1,-1,-1e9

    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0:
                sum = graph[x][y]
                for i in range(4):
                    for kk in range(1,k+1):
                        nx = x+(dxx[i]*kk)
                        ny = y+(dyy[i]*kk)
                        if 0<=nx<n and 0<=ny<n:
                            if graph[nx][ny]<=0: #벽, 빈칸(걍 빈칸 or 제초제)
                                break
                            elif graph[nx][ny]>0:
                                sum+=graph[nx][ny]
                if max_sum<sum:
                    max_sum=sum
                    max_x,max_y = x,y
    return max_x, max_y,max_sum

def sani(graph):
    global answer

    #제초체 년수 감소
    for i in range(n):
        for j in range(n):
            if -10<=graph[i][j]<0:
                graph[i][j] +=1

    #최대 경우 박멸 임시 저장
    x,y,sum = find(graph)
    # print(x,y)

    # 삼성은 이렇게 갱신이 안 될 경우 즉, 이런 반례를 꼭 넣는다.

    # 방법 1
    # if x==-1 and y==-1:
    #     return

    # 방법 2
    if sum<=0:
        return


    temp = [(x,y)]
    answer+=graph[x][y]
    for i in range(4):
        for kk in range(1, k + 1):
            nx = x + (dxx[i] * kk)
            ny = y + (dyy[i] * kk)
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == -11: # 벽만날때
                    break
                elif -10<=graph[nx][ny]<=0: # 빈칸(걍 빈킨 or 제초제) 있는 칸은 또 뿌릴 수 있다.
                    temp.append((nx, ny))
                    break
                elif graph[nx][ny]>0: # 나무 있는 칸
                    temp.append((nx, ny))
                    answer += graph[nx][ny]

    # 박멸!
    for x,y in temp:
        graph[x][y] = -c


n,m,k,c = map(int, input().split()) # 박멸 진행 년수, 확산, 제초제 남아있는

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j]==-1:
            graph[i][j]=-11 # 벽을 -11로 하자

answer = 0
for i in range(1,m+1):
    # 성장 및 번식
    graph = grow_tree(graph)

    # 박멸멸
    sani(graph)

print(answer)

# 밑에 풀이가 훠얼씬 깔금
n,m,k,c = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
sani = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def growtree():
    for i in range(n):
        for j in range(n):
            if graph[i][j]>0:
                for d in range(4):
                    nx,ny = i+dx[d], j+dy[d]
                    if 0<=nx<n and 0<=ny<n and graph[nx][ny]>0:
                        graph[i][j]+=1

def maketree():
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j]>0:
                candi = []
                for d in range(4):
                    nx,ny = i+dx[d],j+dy[d]
                    if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0 and sani[nx][ny]==0:
                        candi.append((nx,ny))
                cnt = len(candi)
                if cnt:
                    value = graph[i][j]//cnt
                    for x,y in candi:
                        temp[x][y]+=value


    for i in range(n):
        for j in range(n):
            if temp[i][j]:
                graph[i][j]+=temp[i][j]

def removesani():
    for i in range(n):
        for j in range(n):
            if sani[i][j]:
                sani[i][j]-=1

dxs = [-1,-1,1,1]
dys = [-1,1,-1,1]
def dosani():
    global answer

    # 제초제 뿌릴 칸 찾기
    globalcnt = -1
    gx,gy = -1,-1
    for i in range(n):
        for j in range(n):
            if graph[i][j]>0:
                cnt = graph[i][j]
                for d in range(4):
                    for step in range(1,k+1):
                        nx,ny = i+dxs[d]*step,j+dys[d]*step
                        if not (0<=nx<n and 0<=ny<n) or graph[nx][ny]==0 or graph[nx][ny]==-1:
                            break
                        if graph[nx][ny]>0:
                            cnt+=graph[nx][ny]

                if globalcnt<cnt:
                    globalcnt=cnt
                    gx,gy = i,j

    # "행이 작은 순서대로, 만약 행이 같은 경우에는 열이 작은 칸에 제초제를 뿌리게 됩니다." 조건을 살펴보자
    # 위에 말은 왜 주었을까? 만약 모든 칸에 나무가 없다면 어디다가 뿌려야할까 -> (0,0)
    if globalcnt==-1: # 갱신 된적이 없으니 즉, 나무가 없음! -> 가장 우선순위가 높은 (0,0)에 뿌렷!
        sani[0][0]=c
        answer+=0 # -> 이건 없어도 되지만 이해를 위해

    else:
        # 찾았으면 제초제 뿌리자!
        sani[gx][gy]=c
        graph[gx][gy]=0
        for d in range(4):
            for step in range(1,k+1):
                nx,ny = gx+dxs[d]*step, gy+dys[d]*step
                if not(0<=nx<n and 0<=ny<n):
                    break
                if graph[nx][ny]==-1 or graph[nx][ny]==0:
                    sani[nx][ny]=c
                    break
                sani[nx][ny]=c
                graph[nx][ny]=0

        answer+=globalcnt


answer = 0
for _ in range(m):

    # 나무의 성장
    growtree()

    # 나무의 번식
    maketree()

    #제초제 감소
    removesani()

    #제초제 뿌리자!
    dosani()

print(answer)
