n,m = map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))
clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

ox = [-1,-1,1,1]
oy = [-1,1,-1,1]

for _ in range(m):
    d,s = map(int, input().split())
    #이동
    for cloud in clouds:
        cloud[0],cloud[1] = (cloud[0]+dx[d-1]*s)%n, (cloud[1]+dy[d-1]*s)%n

    #비 내림
    visit = [[0]*n for _ in range(n)]
    for cloud in clouds:
        graph[cloud[0]][cloud[1]]+=1
        visit[cloud[0]][cloud[1]]=1

    #물복사 버그
    for cloud in clouds:
        for i in range(4):
            nx,ny = cloud[0]+ox[i],cloud[1]+oy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]>0:
                graph[cloud[0]][cloud[1]]+=1

    #구름 생김
    clouds=[]
    for i in range(n):
        for j in range(n):
            if graph[i][j]>=2 and visit[i][j]==0:
                clouds.append([i,j])
                graph[i][j]-=2

answer = 0
for i in range(n):
    for j in range(n):
        answer += graph[i][j]
print(answer)
