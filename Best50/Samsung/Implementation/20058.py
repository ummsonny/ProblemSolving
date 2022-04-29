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

max_group = 0

for i in range(2**n):
    for j in range(2**n):
        if visit[i][j]==0 and graph[i][j]>=1:
            group_total = 0
            dfs(i,j)
            max_group = max(max_group, group_total)
print(total)
print(max_group)

#내풀이
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