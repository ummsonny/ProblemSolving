# 좀더 예쁜 풀이
import sys
sys.setrecursionlimit(10**4)
n,q = map(int, input().split())
graph = []

for _ in range(2**n):
    graph.append(list(map(int, input().split())))

step = list(map(int, input().split()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for L in step:

    # 1. 회전하기
    new_array = [[0] * (2 ** n) for _ in range(2 ** n)]
    for i in range(0, 2 ** n, 2 ** L):
        for j in range(0, 2 ** n, 2 ** L):
            # 회전 규칙 적용!
            for i2 in range(2 ** L):
                for j2 in range(2 ** L):
                    new_array[i + j2][j + 2 ** L - i2 - 1] = graph[i + i2][j + j2]

    candidate = []
    for i in range(2**n):
        for j in range(2**n):
            if new_array[i][j]<=0:
                continue
            count = 0
            for d in range(4):
                nx = i+dx[d]
                ny = j+dy[d]
                if (0<=nx<2**n and 0<=ny<2**n):
                    if new_array[nx][ny]>0:
                        count+=1
            if count<3:
                candidate.append((i,j))
    for x,y in candidate:
        new_array[x][y]-=1

    graph = new_array #이거해줘야해.....

visit = [[0]*(2**n) for _ in range(2**n)]
total = 0
def dfs(x,y):
    global total, group_total

    visit[x][y]=1
    total += new_array[x][y]
    group_total+=1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n and new_array[nx][ny]>0:
            if visit[nx][ny]==0:
                dfs(nx,ny)

max_group = 0 # 이거 -1e9로 하면 안된다. 만약 얼음이 하나도 없는 경우라면? 답이 0이 되야지 -1e9가 되면 안됨

for i in range(2**n):
    for j in range(2**n):
        if visit[i][j]==0 and graph[i][j]>=1:
            group_total = 0
            dfs(i,j)
            max_group = max(max_group, group_total)
print(total)
print(max_group)

#내풀이1
import sys
sys.setrecursionlimit(10**4)
n,q = map(int,input().split())
graph = []
for _ in range(2**n):
    graph.append(list(map(int, input().split())))

cmd = list(map(int, input().split()))

# 회전
for L in cmd:
    temp = [[0]*(2**n) for _ in range(2**n)]
    k = 2**L
    for i in range(0,2**n,k):
        for j in range(0,2**n,k):
            for x in range(k):
                for y in range(k):
                    temp[i+y][j+k-1-x] = graph[i+x][j+y]
    graph = temp

    # 얼음 녹이기
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    temp = [[0]*(2**n) for _ in range(2**n)]
    for i in range(2**n):
        for j in range(2**n):

            if graph[i][j]<=0:
                continue

            cnt = 0
            for d in range(4):
                ni,nj = i+dx[d],j+dy[d]
                if 0<=ni<2**n and 0<=nj<2**n and graph[ni][nj]>0:
                    cnt+=1
            if cnt<3:
                temp[i][j]=graph[i][j]-1
            else:
                temp[i][j]=graph[i][j]
    graph=temp

# 얼음 수 구하기
answer1=0
for i in range(2**n):
    for j in range(2**n):
        if graph[i][j]!=0:
            answer1+=graph[i][j]

# 큰 얼음 구하기
visit = [[0]*(2**n) for _ in range(2**n)]
def dfs(x,y):
    global count
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<2**n and 0<=ny<2**n and graph[nx][ny]!=0:
            if visit[nx][ny]==0:
                visit[nx][ny]=1
                count+=1
                dfs(nx,ny)

answer2 = 0 # 이거 -1e9로 하면 안된다. 만약 얼음이 하나도 없는 경우라면? 답이 0이 되야지 -1e9가 되면 안됨
for a in range(2**n):
    for b in range(2**n):
        if graph[a][b]>0 and visit[a][b]==0:
            visit[a][b]=1
            count = 1
            dfs(a,b)
            answer2 = max(answer2,count)

print(answer1)
print(answer2)
#내풀이2
'''
import sys
sys.setrecursionlimit(10**4)
n,q = map(int, input().split())
graph = []

for _ in range(2**n):
    graph.append(list(map(int, input().split())))

step = list(map(int, input().split()))

def turn_90(array):
    n = len(array)
    m = len(array[0])
    new_array = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_array[j][n-i-1] = array[i][j]

    return new_array

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for L in step:

    bin = []
    for i in range(0,2**n,2**L):
        for j in range(0,2**n,2**L):
            #bin = [] #여기가 새로운 메모리 공간을 계속 할당하기때문에 메모리 초과 난다.
            for k in range(2**L):
                bin.append(graph[i+k][j:j+2**L])

            bin = turn_90(bin)
            for k in range(2**L):
                graph[i+k][j:j+2**L] = bin[k]
            bin.clear()



    candidate = []
    for i in range(2**n):
        for j in range(2**n):
            count = 0
            for d in range(4):
                nx = i+dx[d]
                ny = j+dy[d]
                if (0<=nx<2**n and 0<=ny<2**n):
                    if graph[nx][ny]>0:
                        count+=1
            if count<3:
                candidate.append((i,j))
    for x,y in candidate:
        graph[x][y]-=1
visit = [[0]*(2**n) for _ in range(2**n)]
total = 0
def dfs(x,y):
    global total, group_total

    visit[x][y]=1
    total += graph[x][y]
    group_total+=1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n and graph[nx][ny]>=1:
            if visit[nx][ny]==0:
                dfs(nx,ny)

max_group = 0

for i in range(2**n):
    for j in range(2**n):
        if visit[i][j]==0 and graph[i][j]>=1:
            group_total =0
            dfs(i,j)
            max_group = max(max_group, group_total)
print(total)
print(max_group)
'''