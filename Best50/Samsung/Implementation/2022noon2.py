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
                count_empty = 0
                for d in range(4):
                    ni = i+dx[d]
                    nj = j+dy[d]
                    if 0<=ni<n and 0<=nj<n and graph[ni][nj]>0:
                        count_tree+=1
                    elif 0<=ni<n and 0<=nj<n and graph[ni][nj]==0:
                        empty.append((ni,nj))
                        count_empty+=1
                graph[i][j]+=count_tree

                new_graph[i][j]=graph[i][j]
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
                            # if graph[nx][ny]==-11 or graph[nx][ny]==0:
                            if graph[nx][ny]<=0:
                                break
                            if graph[nx][ny]>0:
                                sum+=graph[nx][ny]
                if max_sum<sum:
                    max_sum=sum
                    max_x,max_y = x,y
    return max_x, max_y

def sani(graph):
    global answer
    #제초체 년수 감소
    for i in range(n):
        for j in range(n):
            if -10<=graph[i][j]<0:
                graph[i][j] +=1
    #최대 경우 박멸
    x,y = find(graph)
    print(x,y)
    if x==-1 and y==-1:
        return
    answer+=graph[x][y]
    graph[x][y]=-c
    for i in range(4):
        for kk in range(1, k + 1):
            nx = x + (dxx[i] * kk)
            ny = y + (dyy[i] * kk)
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny]==0:
                    graph[nx][ny]=-c
                    break
                elif graph[nx][ny]<0:
                    break
                elif graph[nx][ny]>0:
                    answer += graph[nx][ny]
                    graph[nx][ny]=-c

    return x,y

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
    # for g in graph:
    #     print(g)
    # print(i)
    # 박멸멸
    sani(graph)
    for g in graph:
        print(g)
    print(i)

print(answer)
