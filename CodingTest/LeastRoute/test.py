import heapq

n,m,c = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))

distance = [int(1e9)]*(n+1)
distance[c]=0

q = []
heapq.heappush(q,(0,c))

while q:
    dist,now = heapq.heappop(q)

    if dist>distance[now]:
        continue

    for i in graph[now]:

        cost = dist+i[1]

        if cost<distance[i[0]]:
            distance[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))

cnt = 0
time = 0
for node in distance:
    if 0<node<int(1e9):
        cnt+=1
        time = max(time,node)

print(cnt,time)