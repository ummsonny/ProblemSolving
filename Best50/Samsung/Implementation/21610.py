from copy import deepcopy
n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

cloud = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]] #구름

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

for _ in range(m):
    d, s = map(int, input().split())

    #움직이자
    for place in cloud:
        place[0] = (place[0] + dx[d-1]*s)%n
        place[1] = (place[1] + dy[d-1]*s)%n

    visit = [[0]*n for _ in range(n)] #시간초과 단축 효과
    #비내리자
    for place in cloud:
        graph[place[0]][place[1]]+=1
        visit[place[0]][place[1]]=1

    #대각선 검사하자
    for place in cloud:
        count = 0
        for i in range(4): #1,3,5,7
            if not(0<=place[0]+dx[i*2+1]<n and 0<=place[1]+dy[i*2+1]<n):
                continue
            if graph[place[0]+dx[i*2+1]][place[1]+dy[i*2+1]] !=0:
                count +=1

        graph[place[0]][place[1]] += count

    cloud = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]>=2 and visit[i][j] == 0:
                cloud.append([i,j])
                graph[i][j] -=2

    '''
    cloud_copy = deepcopy(cloud) 시간 초과
    cloud = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]>=2:
                if [i,j] not in cloud_copy: 시간초가 원인
                    cloud.append([i,j])
                    graph[i][j] -=2
    
    '''

summary = 0
for i in range(n):
    for j in range(n):
        summary+=graph[i][j]

print(summary)