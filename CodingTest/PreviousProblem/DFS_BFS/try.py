import sys
sys.setrecursionlimit(10000)
n,l,r = map(int, input().split())

graph = []
visit = []
count = 0

country = 0
people = 0
people_list=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    # global country, people

    visit[x][y]=1
    # country+=1
    # people+=graph[x][y]
    people_list.append((x,y))

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
            if l<=abs(graph[x][y]-graph[nx][ny])<=r:
                dfs(nx,ny)

answer=0
while True:
    visit = [[0]*n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            country = 0
            people = 0
            people_list=[]
            if visit[i][j]==0:
                dfs(i,j)
                count+=1

                if len(people_list)>1:
                    for x,y in people_list:
                        country+=1
                        people+=graph[x][y]
                    avg = people//country
                    for x,y in people_list:
                        graph[x][y]=avg
    if count == n*n:
        break
    else:
        answer+=1
print(answer)