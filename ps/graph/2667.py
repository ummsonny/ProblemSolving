import sys

def dfs(x,y):
    visit[x][y]=1
    global house
    house+=1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if graph[nx][ny]==1 and visit[nx][ny]==0:
            dfs(nx,ny)

n = int(input())
visit = [[0]*n for _ in range(n)]
graph = [[0]*n for _ in range(n)]

for i in range(n):
    line = sys.stdin.readline().strip()
    for j,v in enumerate(line):
        graph[i][j]=int(v)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
#여기까지 문제 풀이를 위한 초기화 과정

home_count=[]#단지별로 집 수
house=0
for i in range(n):
    for j in range(n):
        if visit[i][j]==0 and graph[i][j]==1:
            dfs(i,j)
            home_count.append(house)
            house=0

print(len(home_count)) #굳이 단지수 따로 변수 할당할 필요 없이 그냥 길이 구하면 되자나
for i in sorted(home_count):
    print(i)

        
