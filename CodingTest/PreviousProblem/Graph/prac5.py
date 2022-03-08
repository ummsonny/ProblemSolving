from collections import deque
from itertools import cycle

for tc in range(int(input())):
    n = int(input())

    indegree = [0]*(n+1)
    graph = [[False]*(n+1) for _ in range(n+1)]

    data = list(map(int, input().split()))

    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]]=True
            indegree[data[j]]+=1
    
    m = int(input())
    for i in range(m):
        a,b = map(int, input().split())

        if graph[a][b]:
            graph[a][b]=False
            graph[b][a]=True
            indegree[a]+=1
            indegree[b]-=1
        else:
            graph[a][b]=True
            graph[b][a]=False
            indegree[a]-=1
            indegree[b]+=1

    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)

    certain = True
    cycle = False


    # 정확히 n번 즉, 노드 개수만큼 반복 
    # 왜냐면 사이클과 2번 나타나는 경우를 찾아내기 위해서
    # 한번 반복동안 큐에는 1개의 노드만이 존재해야한다.
    for i in range(n): 
        if len(q)==0:
            cycle = True
            break
        if len(q)>=2:
            certain=False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j]-=1

                if indegree[j]==0:
                    q.append(j)

        
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i,end=" ")
        print()