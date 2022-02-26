import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
 
distance = [INF]*(n+1)

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))   

start = 1

def dijkstra(start):
    q=[]

    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

max_node = 0 # 정답 노드
max_distance = 0 # 정답 노드까지 최단거리
result = [] # 정답 노드와 거리가 같은 노드들

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))

#BFS로도 풀수 있다 왜냐면 간선의 비용이 모두 1이므로 즉 간선의 비용이
#특정 값으로 고정되어있으므로