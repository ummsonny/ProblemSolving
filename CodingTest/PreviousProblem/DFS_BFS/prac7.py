from collections import deque

n, l, r = map(int, input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def process(x, y, index):
    united = []
    united.append((x,y))

    q = deque()
    q.append((x,y))
    union[x][y] = index # 현재 연합 번호 할당
    summary = graph[x][y] # 현재 연합 인구수
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n  and 0<=ny<n and union[nx][ny]==-1:
                if l<=abs(graph[x][y]-graph[nx][ny]) <= r:
                    q.append((nx,ny))
                    union[nx][ny]=index
                    summary+=graph[nx][ny]
                    count+=1
                    united.append((nx,ny))

    for i,j in united:
        graph[i][j]=summary//count

total_count=0

while True:
    union = [[-1]*n for _ in range(n)]
    index=0
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1:
                process(i,j,index)
                index+=1

    if index == n*n: # 진짜 계에에에속 조건 만족할때까지 돌아야 하므로
        break
    total_count +=1

print(total_count)
