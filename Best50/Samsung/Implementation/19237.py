n,m,k = map(int, input().split())
shark = []
traceback = [[[-1,0] for _ in range(n)] for _ in range(n)] # 상어번호, 냄새
for i in range(n):
    shark.append(list(map(int,input().split())))
    for j in range(n):
        if shark[i][j]>0:
            traceback[i][j] = [shark[i][j],k]

# 1,2,3,4 위 아래 왼쪽 오른쪽
sdirect = [-1]+list(map(lambda x : int(x)-1, input().split()))
spriority = [[]]

for _ in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(lambda x : int(x)-1, input().split())))
    spriority.append(temp)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 상어이동
def move():
    sharkvisit = [-1]*(m+1) # 이동했는데 또 이동하면 안됨으로
    for i in range(n):
        for j in range(n):
            if shark[i][j]>0 and sharkvisit[shark[i][j]]==-1:
                snum = shark[i][j] # 이것도 잘했다
                flag = False
                for d in spriority[snum][sdirect[snum]]:
                    nx,ny = i+dx[d],j+dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if traceback[nx][ny][1] == 0: # 아무 냄새가 없다면
                            # 만약 다른상어가 이미 있다면
                            if shark[nx][ny]>0:
                                if snum<shark[nx][ny]:
                                    shark[nx][ny]=snum
                                shark[i][j]=0
                            # 아무것도 없다면
                            else:
                                shark[nx][ny],shark[i][j] = shark[i][j],shark[nx][ny]

                            sdirect[snum] = d
                            flag = True
                            break

                if not flag: # 내 냄새가 있는 곳으로 가자
                    for d in spriority[shark[i][j]][sdirect[shark[i][j]]]:
                        nx,ny = i+dx[d], j+dy[d]
                        if 0<=nx<n and 0<=ny<n:
                            if traceback[nx][ny][0]==shark[i][j]:
                                shark[nx][ny],shark[i][j] = shark[i][j], shark[nx][ny]
                                sdirect[snum]=d
                                break
                sharkvisit[snum]=1
# 상어 냄새 뿌리기 및 냄새 한단계 없어지기
def smell():
    for i in range(n):
        for j in range(n):
            if shark[i][j]>0:
                traceback[i][j][0],traceback[i][j][1] = shark[i][j],k
            elif traceback[i][j][1]>0:
                traceback[i][j][1]-=1

# 1번 상어만 남아있는지 체크
def check():
    for i in range(n):
        for j in range(n):
            if shark[i][j]>1:
                return False
    return True

time = 0
while True:
    time+=1
    move()
    smell()
    if check():
        print(time)
        break

    if time>=1000:
        print(-1)
        break

# 다른 내 풀이
n,m,k = map(int, input().split())
smell = [[[] for _ in range(n)] for _ in range(n)]
shark=[]
for i in range(n):
    shark.append(list(map(int, input().split())))
    for j in range(n):
        if shark[i][j]:
            smell[i][j]=[shark[i][j],k] #상어번호, 냄새 시간

sharkdirection = [0]+list(map(lambda x : int(x)-1, input().split()))
priority = [[]]
for _ in range(m):
    temp=[]
    for _ in range(4):
        temp.append(list(map(lambda x : int(x)-1, input().split())))
    priority.append(temp)


dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 상어 움직임
def sharkmove():
    sharkvisit = [0]*(m+1)
    for x in range(n):
        for y in range(n):
            if shark[x][y] and not sharkvisit[shark[x][y]]:
                sharkvisit[shark[x][y]] = 1
                snum = shark[x][y]
                flag = False
                for d in priority[shark[x][y]][sharkdirection[shark[x][y]]]:
                    nx,ny = x+dx[d],y+dy[d]
                    if not(0<=nx<n and 0<=ny<n): continue

                    # 먼저 냄새가 없는 칸을 탐색(다른 상어가 있는지 체크)
                    if not smell[nx][ny]:
                        if shark[nx][ny]:
                            shark[nx][ny] = min(shark[nx][ny],shark[x][y])
                        else:
                            shark[nx][ny] = shark[x][y]
                        shark[x][y]=0

                        sharkdirection[snum] = d
                        flag = True
                        break
                # 다 냄새가 있다면 내 냄새가 있는 칸 탐색
                if not flag:
                    for d in priority[shark[x][y]][sharkdirection[shark[x][y]]]:
                        nx, ny = x + dx[d], y + dy[d]
                        if not (0 <= nx < n and 0 <= ny < n): continue
                        if smell[nx][ny][0]==shark[x][y]:
                            shark[nx][ny], shark[x][y] = shark[x][y], shark[nx][ny]
                            sharkdirection[shark[nx][ny]] = d
                            break
# 냄새시간 감소
def minussmell():
    for i in range(n):
        for j in range(n):
            if not smell[i][j]:
                continue
            if smell[i][j][1]>1:
                smell[i][j][1]-=1
            elif smell[i][j][1]==1:
                smell[i][j]=[]

# 냄새 뿌림
def diffuse():
    for i in range(n):
        for j in range(n):
            if shark[i][j]:
                smell[i][j]=[shark[i][j],k]

def check():

    for i in range(n):
        for j in range(n):
            if shark[i][j]>1:
                return False

    return True

answer = 0
while True:
    answer+=1
    # print(answer)
    sharkmove()
    # for s in shark:
    #     print(s)
    # print()
    minussmell()
    # for s in smell:
    #     print(s)
    # print()
    diffuse()
    # for s in smell:
    #     print(s)
    # print()
    if check():
        print(answer)
        break
    if answer>=1000:
        print(-1)
        break