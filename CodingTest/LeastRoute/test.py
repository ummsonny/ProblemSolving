import heapq
t = int(input())


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def die(x,y):
    q = []
    heapq.heappush(q,(graph[x][y],(x,y)))
    distance[x][y]=graph[x][y]

    while q:

        dist,now = heapq.heappop(q)

        if dist>distance[now[0]][now[1]]:
            continue

        for i in range(4):
            nx,ny = now[0]+dx[i], now[1]+dy[i]

            if not(0<=nx<n and 0<=ny<n):
                continue
            cost = dist+graph[nx][ny]
            if distance[nx][ny]>cost:
                distance[nx][ny]=cost
                heapq.heappush(q,(cost,(nx,ny)))

for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    distance = [[int(1e9)]*n for _ in range(n)]
    die(0,0)
    print(distance[n-1][n-1])

