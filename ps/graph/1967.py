import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int, read().split())
    graph[a].append([b,c]) #1167의 입력형식과 달라서 내가 두번 다 해준 것이다.
    graph[b].append([a,c])


def bfs(start):
    visited=[-1]*(N+1)
    que = deque()
    que.append(start)
    visited[start]=0
    max_dist = [0,0]
    while(que):
        node = que.popleft()
        for e,w in graph[node]:
            if visited[e]==-1:
                visited[e]=visited[node]+w
                que.append(e)
                if max_dist[1]<visited[e]:
                    max_dist = e,visited[e]
    return max_dist

node, dist = bfs(1)
node, dist = bfs(node)
print(dist)

