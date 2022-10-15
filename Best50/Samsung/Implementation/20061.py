#반례 https://www.acmicpc.net/board/view/93335

green = [[0]*4 for _ in range(6)]
blue = [[0]*6 for _ in range(4)]


n = int(input())

def moveblock(t,x,y):
    if t == 1:
        # 초록색
        gx,gy = 0,y
        while True:
            nx,ny = gx+1,gy
            if nx>=6 or green[nx][ny]==1:
                green[gx][gy]=1
                break
            else:
                gx,gy = nx,ny
        #파란색
        bx,by = x,0
        while True:
            nx,ny = bx,by+1
            if ny>=6 or blue[nx][ny]==1:
                blue[bx][by]=1
                break
            else:
                bx,by = nx,ny
    elif t==2:
        # 초록색
        gx,gy = 0,y
        while True:
            nx,ny = gx+1,gy
            if nx>=6 or green[nx][ny]==1 or green[nx][ny+1]==1:
                green[gx][gy],green[gx][gy+1]=1,1
                break
            else:
                gx,gy, = nx,ny
        bx,by = x,0
        #파란색
        while True:
            nx,ny = bx,by+1
            if ny>=5 or blue[nx][ny+1]==1:
                blue[bx][by],blue[bx][by+1]=1,1
                break
            else:
                bx,by = nx,ny

    else:
        # 초록색
        gx,gy = 0,y
        while True:
            nx,ny = gx+1,gy
            if nx>=5 or green[nx+1][ny]==1:
                green[gx][gy],green[gx+1][gy]=1,1
                break
            else:
                gx,gy = nx,ny
        bx,by = x,0
        # 파란색
        while True:
            nx,ny = bx,by+1
            if ny>=6 or blue[nx][ny]==1 or blue[nx+1][ny]==1:
                blue[bx][by],blue[bx+1][by]=1,1
                break
            else:
                bx,by = nx,ny

def removegreentile(i):
    for idx in range(i,0,-1):
        for k in range(4):
            green[idx][k] = green[idx-1][k]
    for k in range(4):
        green[0][k]=0

def removebluetile(j):
    for idx in range(j,0,-1):
        for k in range(4):
            blue[k][idx] = blue[k][idx-1]
    for k in range(4):
        blue[k][0]=0

def removetile():
    count = 0
    # 초록색
    for i in range(2,6): # 이렇게 해야 위에 링크걸어둔 첫번째 예외 잡을 수 있다.
        cnt = 0
        for j in range(4):
            if green[i][j]==1:
                cnt+=1
        if cnt == 4:
            removegreentile(i)
            count+=1

    # 파란색
    for j in range(2,6): # 이렇게 해야 위에 링크걸어둔 첫번째 예외 잡을 수 있다.
        cnt = 0
        for i in range(4):
            if blue[i][j]==1:
                cnt+=1
        if cnt == 4:
            removebluetile(j)
            count+=1

    return count

def check():
    #초록색
    cnt=0
    for i in range(2):
        if 1 in green[i]:
            cnt+=1
    for _ in range(cnt): # 연한부분에 블록이 있는 줄만큼 이동해야하므로 -> 위 반례 2번
        removegreentile(5)

    #파란색
    cnt = 0
    for j in range(2):
        for i in range(4):
            if blue[i][j]==1:
                cnt+=1
                break
    for _ in range(cnt): # 연한부분에 블록이 있는 줄만큼 이동해야하므로 -> 위 반례 2번
        removebluetile(5)


answer = 0
for p in range(n):
    t,x,y = map(int, input().split())


    # 먼저 이동
    moveblock(t,x,y)
    # print(p,1)
    # for g in green:
    #     print(g)
    # for b in blue:
    #     print(b)


    # 가득찬 경우 제외
    answer += removetile()
    # print(p,2)
    # for g in green:
    #     print(g)
    # for b in blue:
    #     print(b)

    # 연한 블록 확인
    check()
    # print(p,3)
    # for g in green:
    #     print(g)
    # for b in blue:
    #     print(b)

print(answer)
cnt = 0
for i in range(6):
    for j in range(4):
        if green[i][j]==1:
            cnt+=1
for j in range(6):
    for i in range(4):
        if blue[i][j]==1:
            cnt+=1
print(cnt)

# print('완료')
# for g in green:
#     print(g)
# for b in blue:
#     print(b)


# 밑에 풀이가 뭔가 가독성이 좋다.
green = [[0]*4 for _ in range(6)]
blue = [[0]*6 for _ in range(4)]

def moveblockgreen(t,y):

    cx,cy = 0,y
    if t==1:
        while True:
            nx,ny = cx+1,cy
            if nx>=6:
                green[cx][cy]=1
                break
            if green[nx][ny]:
                green[cx][cy]=1
                break
            cx,cy = nx,ny
    elif t==2:
        while True:
            nx,ny = cx+1,cy
            if nx>=6:
                green[cx][cy],green[cx][cy+1]=1,1
                break
            if green[nx][ny] or green[nx][ny+1]:
                green[cx][cy],green[cx][cy+1]=1,1
                break
            cx,cy = nx,ny
    elif t==3:
        while True:
            nx,ny = cx+1,cy
            if nx>=5:
                green[cx][cy],green[cx+1][cy]=1,1
                break
            if green[nx+1][ny]:
                green[cx][cy], green[cx+1][cy] = 1, 1
                break
            cx,cy = nx,ny

def moveblockblue(t,x):

    cx,cy = x,0
    if t==1:
        while True:
            nx,ny = cx,cy+1
            if ny>=6:
                blue[cx][cy]=1
                break
            if blue[nx][ny]:
                blue[cx][cy]=1
                break
            cx,cy = nx,ny
    elif t==2:
        while True:
            nx,ny = cx,cy+1
            if ny>=5:
                blue[cx][cy],blue[cx][cy+1]=1,1
                break
            if blue[nx][ny+1]:
                blue[cx][cy],blue[cx][cy+1]=1,1
                break
            cx,cy = nx,ny
    elif t==3:
        while True:
            nx,ny = cx,cy+1
            if ny>=6:
                blue[cx][cy],blue[cx+1][cy]=1,1
                break
            if blue[nx][ny] or blue[nx+1][ny]:
                blue[cx][cy], blue[cx+1][cy] = 1, 1
                break
            cx,cy = nx,ny
def removegreentile(x):
    for i in range(x,0,-1):
        for d in range(4):
            green[i][d]=green[i-1][d]
    for d in range(4):
        green[0][d]=0
def removebluetile(y):
    for j in range(y,0,-1):
        for d in range(4):
            blue[d][j]=blue[d][j-1]
    for d in range(4):
        blue[d][0]=0
n = int(input())
answer = 0
for _ in range(n):

    t,x,y = map(int, input().split())
    moveblockgreen(t,y)
    moveblockblue(t,x)

    # 먼저 초록색 타일 부분 처리
    for i in range(2,6):
        if green[i][0] and green[i][1] and green[i][2] and green[i][3]:
            removegreentile(i)
            answer+=1

    for i in range(0,2):
        if green[i][0] or green[i][1] or green[i][2] or green[i][3]:
            removegreentile(5)

    # 그 다음 파란색 타일 부분 처리
    for j in range(2,6):
        if blue[0][j] and blue[1][j] and blue[2][j] and blue[3][j]:
            removebluetile(j)
            answer+=1

    for j in range(0,2):
        if blue[0][j] or blue[1][j] or blue[2][j] or blue[3][j]:
            removebluetile(5)

print(answer)
answer2=0
for i in range(2,6):
    for j in range(4):
        if green[i][j]:
            answer2+=1
for i in range(4):
    for j in range(2,6):
        if blue[i][j]:
            answer2+=1
print(answer2)
