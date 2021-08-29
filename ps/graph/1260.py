def dfs(v):
    print(v, end=' ')
    visit[v]=1
    for i in range(1,n+1):
        if g[v][i]==1 and visit[i]==0:
            dfs(i)

#bfs시에 일반 리스트 말고 deque를 이용해서 구현해라 그게 훨씬 빠르다.
def bfs(v): #왜 visit[v]=1이아니라 0이냐면 위에 bfs에서 다 방문뒤 visit의 모든 원소가 1이 되었고 이 visit리스트를 그대로 쓰므로 이제는 0을 visit라고 하자
    queue = [v] #그냥 리스트 대신 dequeue써도 된다. 그럼 12줄에서 pop(0)이 아니라 popleft()쓸 수 있다.
    visit[v]=0 #큐에 들어갈때 이미 visit 체크가 되어잇어야 함. 팝 할때 체크하는 것이 아님@
    while(queue):
        q = queue.pop(0)
        print(q, end = ' ')
        for i in range(1, n+1):
            if g[q][i]==1 and visit[i]==1:
                queue.append(i)
                visit[i]=0

n, m, v = map(int, input().split())

g = [[0]*(n+1) for i in range(n+1)]#인덱스 0은 그냥 0으로 무시하여 그래프 그림
visit = [0]*(n+1)
for i in range(m):
    x,y = map(int, input().split())
    g[x][y]=1
    g[y][x]=1

dfs(v)
print()
bfs(v)