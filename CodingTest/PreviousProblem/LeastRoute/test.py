import heapq
INF = int(1e9)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

distance = [INF]*(n+1)
distance[1] = 0

q = []
heapq.heappush(q,(0,1))

while q:

    cost,now = heapq.heappop(q)

    if cost>distance[now]:
        continue

    for node in graph[now]:
        dist = cost+node[1]
        if dist<distance[node[0]]:
            distance[node[0]]=dist
            heapq.heappush(q,(dist,node[0]))

cost = -1
answer = -1
result = []
for i in range(1,n+1):
    if cost<distance[i]:
        answer = i
        cost = distance[i]
        result = [i]
    elif cost == distance[i]:
        result.append(i)

print(answer,cost,len(result))