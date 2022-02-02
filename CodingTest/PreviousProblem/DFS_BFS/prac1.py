from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(n):
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
