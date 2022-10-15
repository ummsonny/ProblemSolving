n,k = map(int, input().split())
bottle = list(map(int, input().split()))

def rot90(graph):
    n = len(graph)
    m = len(graph[0])
    new_graph = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_graph[j][n-1-i] = graph[i][j]

    return new_graph
def rot180(graph):
    n = len(graph)
    m = len(graph[0])
    new_graph = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_graph[n-1-i][m-1-j] = graph[i][j]

    return new_graph

def first(graph):
    candi=[]
    stand = int(1e9)

    for idx,value in enumerate(graph):
        if graph[idx]<stand:
            candi=[idx]
            stand=graph[idx]
        elif graph[idx]==stand:
            candi.append(idx)

    for idx in candi:
        graph[idx]+=1

def second(graph):
    new_graph = []
    # 첫단계
    new_graph.append([graph[0]])
    new_graph.append(graph[1:])

    # 두번째 단계
    new_graph[0]=[new_graph[1][0],new_graph[0][0]]
    new_graph[1]=new_graph[1][1:]

    # 세번째 이후
    a = len(new_graph)
    c = 2
    b = len(new_graph[1])-c
    while a<=b:
        temp = []
        # temp rot90(new_graph[:][:c]) # 이건 안된다. 이걸 할라면 numpy만 된다. 근데 삼성은 안댐
        for z in range(a):
            temp.append(new_graph[z][:c])
        temp = rot90(temp)
        temp.append(new_graph[-1][c:])
        new_graph=temp

        a,c = c+1,a
        b = b-c

    for i in range(a-1):
        new_graph[i]+=([0]*b)

    return new_graph,a,b+c

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def third(graph,n,m):

    temp = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                copyvalue = graph[i][j]
                for d in range(4):
                    nx,ny = i+dx[d],j+dy[d]
                    if 0<=nx<n and 0<=ny<m and graph[nx][ny] and graph[i][j]>graph[nx][ny]:
                        diff = (graph[i][j] - graph[nx][ny])//5
                        if diff > 0:
                            temp[nx][ny]+=diff
                            copyvalue-=diff
                temp[i][j]+=copyvalue

    return temp
def fourth(graph,n,m):
    new_bottle = []

    for j in range(m):
        for i in range(n-1,-1,-1):
            if graph[i][j]:
                new_bottle.append(graph[i][j])

    return new_bottle
def fifth(graph):

    # 첫뻔째
    length = len(graph)
    new_graph = []
    new_graph.append(graph[:length//2][::-1])
    new_graph.append(graph[length//2:])

    # 두번째
    # temp = rot180(new_graph[:][:length//4]) # 이건 안된다. 이걸 할라면 numpy만 된다. 근데 삼성은 안댐
    temp = [new_graph[0][:length//4],new_graph[1][:length//4]]
    temp = rot180(temp)
    temp.append(new_graph[0][length//4:])
    temp.append(new_graph[1][length//4:])

    return temp, 4, length//4

answer=0
while True:
    answer+=1
    first(bottle)
    bottle,n,m = second(bottle)
    bottle = third(bottle,n,m)
    bottle = fourth(bottle,n,m)

    bottle,n,m = fifth(bottle)
    bottle = third(bottle,n,m)
    bottle = fourth(bottle,n,m)

    if max(bottle)-min(bottle)<=k:
        print(answer)
        break




# 다른 풀이인데 그냥 별 차이 없다
def rot90(n, m, graph):
    new_graph = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_graph[j][n - 1 - i] = graph[i][j]
    return new_graph


def stackbowl(n, bowl):
    # 첫 단계
    graph = [[bowl[0]]] + [bowl[1:]]

    # 두 번째 단계부터
    a, b = 2, 1
    c = n - a
    while a <= c:
        temp = []
        for i in range(a):
            temp.append(graph[i][:b])
        temp = rot90(a, b, temp)
        temp.append(graph[-1][b:])
        graph = temp

        a, b, c = b + 1, a, c - a

    for i in range(a - 1):
        graph[i] += ([0] * c)

    return graph, a, b + c


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def control(n, m, bowl):
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if bowl[i][j]:
                copyvalue = bowl[i][j]
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and 0 < bowl[nx][ny] < bowl[i][j]:
                        value = (bowl[i][j] - bowl[nx][ny]) // 5
                        if value:
                            temp[nx][ny] += value
                            copyvalue -= value
                temp[i][j] += copyvalue

    return temp


def makeflat(n, m, bowl):
    temp = []
    for j in range(m):
        for i in range(n - 1, -1, -1):
            if bowl[i][j]:
                temp.append(bowl[i][j])

    return temp


def rot180(n, m, graph):
    new_graph = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_graph[n - 1 - i][m - 1 - j] = graph[i][j]

    return new_graph


def jub(bowl):
    # 첫번째
    bowl = [bowl[:n // 2][::-1], bowl[n // 2:]]

    # 두 번째
    temp = [bowl[0][:n // 4], bowl[1][:n // 4]]
    temp = rot180(2, n // 4, temp)
    temp.append(bowl[0][n // 4:])
    temp.append(bowl[1][n // 4:])

    return temp


answer = 0
n, k = map(int, input().split())
bowl = list(map(int, input().split()))
while True:

    answer += 1

    # 가장작은 어항들에 물고기 1마리씩 넣는다.
    plus = []
    value = int(1e9)
    for i in range(n):
        if bowl[i] < value:
            plus = [i]
            value = bowl[i]
        elif bowl[i] == value:
            plus.append(i)
    for idx in plus:
        bowl[idx] += 1

    # 어항을 90도씩 돌려서 쌓는다
    bowl, a, b = stackbowl(n, bowl)

    # 물고기수 조절
    bowl = control(a, b, bowl)

    # 어항을 일렬로 놓는다.
    bowl = makeflat(a, b, bowl)

    # 2번 접는다! 180도!회전
    bowl = jub(bowl)

    # 물고기수 조절
    bowl = control(4, n // 4, bowl)

    # 어항을 일렬로 놓는다.
    bowl = makeflat(4, n // 4, bowl)

    # 어항에 최대값과 최솟값이 <= k 일때까지 정리한 회수 구한다.
    if max(bowl) - min(bowl) <= k:
        print(answer)
        break