def find_parent(parent, a):
    if parent[a]!=a:
        parent[a]=find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n = int(input())
parent = [0] * (n+1)
for i in range(n):
    parent[i]=i

edges = []
result = 0

x = []
y = []
z = []

for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))


x.sort()
y.sort()
z.sort()

for i in range(n-1):
    #비용순으로 정렬하기 위해 튜플의 첫 번째 원소는 비용이다.
    edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))

edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent, a,b)
        result+=cost

print(result)


#x축 기준으로만 생각했을 때 오름차순으로 x좌표를 정렬하면 이게 곧 최소 신장트리이다. (y,z도 마찬가지)
    #-->1개의 직선(x축)위에 점들이 존재하니까 당연히 최소신장트리이다.
# n(n-1)/2 간선은 너무 많으므로 고려할 간선의 개수를 줄이기 위해 x,y,z 각각을 기준으로 최소신장트리를 만든다.
    #이렇게 하면 일단 최종 트리의 최소 비용 간선 후보가 될 수 있는 간선의 후보군을 3개(x축, y축, z축 기준) 만들 수 있다.


#간선의 비용이 min(|x1-x2|, |y1-y2|, |z1-z2|)이므로 각 간선들을 
    # |x1-x2| 또는 |y1-y2| 또는 |z1-z2| 를 가짐을 기억하자.
    # 그래서 일단 x좌표, y좌표, z좌표 값 각각의 기준으로 최소 신장트리를 만든다.

# 1. x좌표, y좌표, z좌표 값 각각의 기준으로 최소 신장트리를 만든다. 
# 2. 생성된 3가지 최소 신장트리를 합친다. (비용, 노드a, 노드b)라고 하면 
    # (11, 4, 3) (5, 4, 4)처럼 겹칠 수도 있다. union연산에 의해서 중복되도 상관없다. 
    # 같은 집합이라면 고려 안하고 오름차순으로 정렬하니까 짧은 놈이 선택된다.
# 3. 합체된 신장트리를 가지고 크루스칼 알고리즘을 돌린다.