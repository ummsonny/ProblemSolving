# Graph

## 들어가기 전

### 그래프란
- 노드와 간선으로 이루어진 자료구조
- 알고리즘 문제를 접했을 때 '서로 다른 개체(혹은 개체)가 연결되어 있다'는 것을 보면 가장 먼저 그래프 알고리즘을 떠올려!
    - ex)여러 개의 도시가 연결되어 있다.

### 트리자료구조
- 그래프 자료구조의 일종

||그래프|트리
|---|---|---|
|방향성|방향 그래프 혹은 무방향 그래프|방향 그래프|
|순환성|순환 및 비순환|비순환|
|루트 노드 존재 여부|없음|존재|
|노드간 관계성|부모와 자식 관계 없음|부모와 자식 관계|
|모델의 종류|네트워크 모델|계층 모델|

### 인접행렬 VS 인접 리스트
- 노드의 개수 V, 간선의 개수 E 일때

||인접 행렬|인접 리스트
|---|---|---|
|메모리|O(V^2)|O(E)
|속도(간선의 비용 파악)|O(1)|O(V)
|알고리즘|플로이드 워셜|다익스트라|
- 최단경로 문제풀이 Tip
    - 노드의 개수가 적다 -> 플로이드
    - 노드와 간선이 많다 -> 다익스트라
---
## 서로소 집합
### what?
- **공통 원소가 없는** 두 집합

### 서로소 집합 자료구조
- **서로소** 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
- 번호가 작은 원소가 부모 노드가 되도록 구현하는 경우가 많으므로 이것을 따른다
- 부모 테이블을 가지고 있다
- find,union 이 2개 연산으로 조작한다.
    - find : 특정한 원소가 속한 집합을 알려주는 연산
    ```python
    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    ```
    - union : 2개 집합을 하나로 합치는 연산
    ```python
    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    ```
### 서로소 집합 알고리즘의 시간 복잡도
- 책 참고
### 서로소 집합을 활용한 사이클 판별
- 서로소 집합은 **무방향** 그래프 내에서 사이클을 판별할 수 있다. 
- **방향** 그래프에서의 사이클 여부는 DFS를 이용하여 판별가능 But 책에서는 안 다룸
- How?
    1. 각 간선을 확인하며 두 노드의 루트 노드를 확인
        - 루트 노드가 서로 다르다면 union연산 수행
        - 같다면 사이클 발생!!
    2. 그래프에 포함 되어 있는 **모든** 간선에 대하여 1번 과정 반복
```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
```
---
## 신장 트리
### what?
- 하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
- 최소 신장 트리 : 최소 비용으로 만든 신장트리
- 최소 신장 트리는 일종의 트리 자료구조
    - 최종적으로 신장 트리에 포함되는 간선의 개수 =  노드의 개수 -1 
### how?
- 크루스칼 알고리즘
    - 최소 비용으로 만들 수 있는 신장트리를 찾는 알고리즘
- 크루스칼 알고리즘 메커니즘
    1. 모든 간선에 대해서 정렬 수행
    2. 가장 비용이 적은 간선부터 집합에 포함(단, 사이클을 발생시키는 간선의 경우는 포함X)
```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
```
### 시간 복잡도
- O(ElogE)
    - E는 간선의 개수
    - 크루스칼 알고리즘에서 시간이 가장 오래 걸리는 부분은 간선 정렬 부분 -> 이부분만 복잡도 계산시 고려
    - union, find와 같은 서로소 집합 알고리즘의 시간 복잡도는 정렬 알고리즘보다 시간 복잡도가 작으므로 무시한다.
---
## 위상 정렬
### what?
- **방향** 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
- Ex) '선수과목을 고려한 학습 순서 설정'
- 즉, 그래프상에서 **선후 관계**가 있다면, 위상 정렬을 수행하여 모든 선후 관계를 지키는 전체 순서를 계산할 수 있다.
### how?
- 메커니즘
    1. 진입차수가 0인 노드를 큐에 넣는다.
    2. 큐가 빌 때까지 다음의 과정을 반복한다.
        1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
        2. 새로게 진입차수가 0이 된 노드를 큐에 넣는다.
- 중요!
    - 모든 원소 방문하기 전 즉, 큐에서 원소가 V번 추출되기 전에 큐가 비어버리면 사이클이 발생한 것!
    - 이유 : 사이클이 존재하는 경우 사이클에 포함되어 있는 원소 중에서 어떠한 원소도 큐에 들어가지 못하기 때문!
```python
from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # 진입 차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()
```
### 시간 복잡도
- O(V+E)
    - 노드와 간선을 모두 확인하기 때문이다.
