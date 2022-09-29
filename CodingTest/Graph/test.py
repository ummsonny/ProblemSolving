def find_parent(parent,a):

    if parent[a]!=a:
        parent[a]=find_parent(parent,parent[a])
    return parent[a]

def union_find(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m = map(int, input().split())

parent = [0]*(n+1)
for i in range(1,n):
    parent[i] = i

edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()

answer = 0
last = 0
for cost,a,b in edges:
    if find_parent(parent,a) != find_parent(parent,b):
        union_find(parent,a,b)
        answer+=cost
        last = cost

print(answer-last)


