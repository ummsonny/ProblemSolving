from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)] # n+1 조심

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

visited = [-1]*(n+1)
visited[x]=0

# q = deque(x)
# q.append(x) 대신에
q = deque([x])

while q:
    now = q.popleft()

    for next_node in graph[now]:
        if visited[next_node] == -1:
            visited[next_node]=visited[now]+1 #거리 갱신 스킬
            q.append(next_node)

check = False
for i in range(1,n+1):
    if visited[i]==k:
        print(i)
        check=True

if check == False:
    print(-1)


# 내 풀이
from collections import deque

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

visited = [-1 for _ in range(n+1)]

answer = []
def bfs(start):
    
    q = deque()
    q.append(start)
    visited[start]=0

    while q:

        current = q.popleft()
        if visited[current]==k:
            answer.append(current)
        if visited[current]==k+1:
            break

        for i in graph[current]:
            if visited[i]==-1:
                visited[i]=visited[current]+1
                q.append(i)

bfs(x)
if answer:
    for element in sorted(answer):
        print(element)
else:
    print(-1)

