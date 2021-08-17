def dfs(v):
    visit[v]=1
    for i in range(1,n+1):
        if g[v][i]==1 and visit[i]==0:
            dfs(i)

n, m = map(int, input().split())

g = [[0]*(n+1) for i in range(n+1)]#인덱스 0은 그냥 0으로 무시하여 그래프 그림
visit = [0]*(n+1)
for i in range(m):
    x,y = map(int, input().split())
    g[x][y]=1
    g[y][x]=1

count=0

for i in range(1,n+1):
    if visit[i]!=1:
        dfs(i);
        count+=1

print(count)