# 최단경로
- 코테에서는 최단 경로를 모두 출력하는 문제보다 단순히 최단 거리를 출력하도록 요구하는 문제가 많이 출제됨
---
## 알고리즘
- 다익스트라
- 플로이드 워셜
- 벨만 포드

## 다익스트라
- 1:N
- 동작방법
    1. 출발 노드를 설정
    2. 최단 거리 테이블을 초기화
    3. **방문하지 않은 노드** 중에서 최단 거리가 가장 짧은 노드를 선택
    4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
    5. 3번,4번 반복
- 특징
    - 양방향 그래프도 가능 But 음의 가중치는 안됨
    - 동작 방법3 에서 한 번 선택된 노드는 최단거리가 감소하지 않는다. 즉, 다익스트라는 **한 단계**당 하나의 노드에 대한 최단 거리를 확실히 찾는다.
        - 그래서 마지막 노드에 대해서는 확인할 필요가 없긴 하다.

- 시간 복잡도
    - O(ElogV) (V : 노드 개수, E : 간선 개수)
    - 이유는 책참고
- 구현 팁
    1. 1차원 최단 거리 테이블을 **INF = int(1e9)**로 초기화 한다.
    2. import heapq -> 파이썬은 최소힙이 기본
        - 튜플(거리, 노드)
    3. 우선 순위 큐를 이용하므로 그냥 꺼내면 된다.
        - 힙에서 꺼낸 뒤에 해당 노드를 **이미 처리한 적이 있다면 무시**
        - **더 짧은 경로를 찾은 노드**들은 다시 우선순위에 넣는다.
```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```
---
## 플로이드 워셜 알고리즘
- N : N
- 동작방법
    - 'A에서 B로 가는 최소 비용'과 'A에서 K를 거쳐 B로 가는 비용' 중 더 작은 값으로 갱신
    - 즉, '바로 이동하는 거리'가 '특정한 노드를 거쳐서 이동하는 거리'보다 더 많은 비용을 가진다면 이를 더 짧은 것으로 갱신하겠다는 다이나믹 프로그래밍!

- 특징
    - 양방향 그래프도 가능

- 시간 복잡도
    - O(N^3)
- 구현 팁
    - 2차원 최단 거리 테이블을 **INF = int(1e9)**로 초기화 한다.
        - 단 우하향 대각선은 모두 0으로 초기화
```python
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()
```

