# DFS_BFS

## 그래프의 표현방식 2가지
### 인접 행렬
- 2차원 배열로 그래프의 연결 관계를 표현
- **연결되지 않은 노드끼리는 INF로!**
### 인접 리스트
- 2차원 연결 리스트로 그래프의 연결 관계를 표현하는 방식
### 둘의 차이
- 메모리 측면
    - 행렬 - 노드 개수가 많을수록 비효율적
    - 리스트 - 연결된 정보만 저장하므로 효율적 
- 노드 검색 속도 측면
    - 행렬 - 인덱스로 찾으므로 빠르다
    - 리스트 - 연결리스트이므로 검색 속도가 느리다
---
## DFS알고리즘
### 설명
- 깊이 우선 탐색, 깊은 부분을 우선적으로 탐색
- 스택 자료구조 사용 --> 재귀
- 가끔씩 문제조건 혹은 관례상으로 작은 번호부터 처리(하지만 순서상관없음)
### **시간복잡도**
- 무방향 그래프
    - 데이터 개수N, 간선 <= N 이므로, O(N)의 탐색 시간이 걸린다. 
- 방향 그래프
    - 노드 N, 간선 M 이라면 O(N+M)
### 기본 코드
```python
# 연결리스트 방법
def dfs(graph, v, visited):

    visited[v]=True
    print(v, end=' ')

    for i in graph[v]:
        if (not visited[v]) and "장애물이 아니라면":
            dfs(graph, i, visited)

# 그래프 방법
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def dfs(graph, x,y, visited): # visited말고 graph상에 바로 표현해도 된다.

    visited[x][y]=True
    print(v, end=' ')

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and "장애물이 아니라면":
            if graph[nx][ny] == 1:
                dfs(graph, x, y, visited)
```
<br/>

## BFS알고리즘
### 설명
- 너비 우선 탐색, **가까운** 노드부터 탐색하는 알고리즘
- 큐 자료구조 사용 -> deque 라이브러리
- **노드 사이 거리가 1이라면 최단거리 구할 수 있다**
### **시간복잡도**
- 무방향 그래프
    - 데이터 개수N, 간선 <= N 이므로, O(N)의 탐색 시간이 걸린다. 
- 방향 그래프
    - 노드 N, 간선 M 이라면 O(N+M)
- **일반적인 경우 실제 수행시간은 DFS보다 좋다.** -> 코테에서도 BFS를 먼저 고려하자
### 기본 코드
```python
#연결 리스트 방법
from collections import deque

def bfs(graph, start, visited):
    
    queue = deque([start])
    visited[start]=True

    while queue:

        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if (not visited[v]) and "장애물이 아니라면":
                queue.append(i)
                visited[i]=True # 큐에 들어가 있을 때 방문이 된 상태여야 한다.

#그래프 방법
def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 X and 장애물 X 라면
            if 0<=nx<n and 0<=ny<n and "장애물이 아니라면":
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록 중요***********
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1 # 방문체크도 동시에 된다.
                    queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

```
---
## **그래프의형태**
- 전형적인 그래프
    - 행렬 & 리스트 둘다 가능
- 1차원 배열 또는 2차원 배열
    - 2차원 배열에서의 탐색 문제 -> 전형적인 그래프 형태로 바꿔서 생각!
    - 리스트는 너무 힘들다. 행렬로 가능
- **코테에서 탐색 문제 만나면 전형적인 그래프 형태로 표현한 다음 풀이!**

---

## 실전 문제 풀이 팁
### DFS&BFS 공통점
- 확장 상태(노드)의 후보를 만들어라 
- visited가 있어야 한다.
    - 똑같은 상황이 존재하지 않는다면 visited가 없어도 된다. 하지만 대부분이 있다.
### DFS&BFS 차이점
- DFS
    - 종료 조건
    - 상황 복구 방법
        1. 특정 상태(노드)의 상황을 담고 있어야 다시 돌아왔을때 상황이 같다. 즉 나만의 상태가 필요하다!
    그래서 매개변수로 넘겨준다. 그리고 그 매개변수를 담을 지역변수가 존재한다.
        2.  dfs후에 복구 시키는 코드 넣는다.
- BFS
    - 상태(노드)의 최단 거리를 구할 수 있다.