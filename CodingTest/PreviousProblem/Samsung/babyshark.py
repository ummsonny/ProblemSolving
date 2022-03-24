from collections import deque
INF = 1e9
n = int(input())

graph=[]

for _ in range(n):
    graph.append(list(map(int, input().split())))


now_size = 2
now_x, now_y = 0,0

for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            now_x, now_y = i, j
            graph[now_x][now_y]=0 # 처음 아기 상어 위치에는 아무것도 없다고 해 그래야지 그 부분 탐색가능하지

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 최단 거리 구하기
def bfs():

    dist = [[-1] * n for _ in range(n)] # bfs할때마다 최단거리 계산해야 하니까 

    q = deque([(now_x,now_y)])
    dist[now_x][now_y]=0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if dist[nx][ny]==-1 and graph[nx][ny]<=now_size:
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx,ny))

    return dist

# 최단 거리 테이블 주어졌을 때, 먹을 물고기 찾는 함수
def find(dist):
    x,y=0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j]!=-1 and 1<=graph[i][j]<now_size:
                if graph[i][j]<min_dist:
                    x,y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x,y,min_dist

result = 0 # 최종 답안
ate = 0 # 현재 크기에서 먹은 양

while True:
    value = find(bfs())

    if value == None:
        print(result)
        break

    else:
        now_x, now_y = value[0], value[1]
        result += value[2]

        graph[now_x][now_y]=0
        ate +=1 

        if ate>=now_size:
            now_size+=1
            ate=0

