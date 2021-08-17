def bfs(v): # 0는 흰색, 1은 검은색
    queue = [v] 
    visit[v]=0#시작점은 흰색
    while(queue):
        q = queue.pop(0)
        for i in g[q]:
            if visit[i]==-1:
                queue.append(i)
                visit[i]=(0 if visit[q]==1 else 1)
            elif visit[i]==visit[q]:
                return False
    return True

k = int(input())
for i in range(k):
    flag = True
    n, m = map(int, input().split())

    g = [[] for i in range(n+1)]
    visit = [-1]*(n+1)
    for i in range(m):
        x,y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)

    for i in range(1,n+1):
        if visit[i]==-1:
            if not bfs(i):
                print("NO")
                flag = False
                break       
    if flag:
        print("YES")
    
#교훈 : 그래프 표현시 행렬표현법은 연결리스트 표현법보다 메모리를 더 마니 먹는다.
