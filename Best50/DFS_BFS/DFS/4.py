# 다음에 풀때는 bfs + set자료구조 사용해서 풀어봐라!
# 이거 백트래킹 문제임

dx = [-1,1,0,0]
dy = [0,0,-1,1]
alpa_can = [0]*26 # set자료구조 쓰는 거랑 같음

def dfs(x,y,cnt):
    global answer

    flag = False

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<r and 0<=ny<c and visit[nx][ny]==-1:
            if not alpa_can[ord(graph[nx][ny])-65]:

                flag = True
                visit[nx][ny]=1
                alpa_can[ord(graph[nx][ny])-65]=1
                dfs(nx,ny,cnt+1)
                visit[nx][ny]=-1
                alpa_can[ord(graph[nx][ny])-65]=0

    if not flag:
        answer = max(answer, cnt)


r,c = map(int, input().split())

graph = []

for _ in range(r):
    graph.append(list(input()))

visit = [[-1]*c for _ in range(r)]
answer = 0

visit[0][0]=1
alpa_can[ord(graph[0][0])-65]=1
dfs(0,0,1)
visit[0][0]=-1
alpa_can[ord(graph[0][0])-65]=0

print(answer)