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