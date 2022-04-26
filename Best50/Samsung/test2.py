from collections import deque
n,m = map(int, input().split())
graph = []
virus = []
left = 0 # 모든 칸에 빈칸에 바이러스를 퍼뜨릴 수 있는지

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i,j))
        if graph[i][j] == 0:
            left +=1

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(arr, leftArea):

    visit = [[-1]*n for _ in range(n)]
    q = deque(list(map(lambda k: (k[0],k[1],0), arr)))

    for x,y,z in q:
        visit[x][y] = 2

    while q:

        a,b,time = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=1:
                if visit[nx][ny] == -1:
                    q.append((nx,ny,time+1))
                    visit[nx][ny] = 2
                    if graph[nx][ny]==0: #비활성 바이러스도 그냥 길일 뿐이다. 단지 leftArea만 감소 안할 뿐
                        leftArea-=1 #여기가 핵심!!!!

            if leftArea==0:
                return time+1

    return 1e9


lenth = len(virus)
arr = []

answer = 1e9
def dfs(start,count):
    global answer

    if count == m:
        answer = min(answer, bfs(arr,left))

    for i in range(start,lenth):
        arr.append((virus[i][0],virus[i][1]))
        dfs(i+1, count+1)
        arr.pop()


dfs(0,0)
if left == 0: #애초에 빈칸이 없을 수도 있으니까
    print(0)
elif answer==1e9:
    print(-1)
else:
    print(answer)