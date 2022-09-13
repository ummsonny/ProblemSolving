# 코딩테스트 노트

## 상하좌우
1. 
```python
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
``` 
2. 
```python
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1,),(1,2),(-1,2),(-2,1)]

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
```
3. 뒤로가기

```python
# + 대신에 - 를 한다.
nx = x - dx[i]
ny = y - dy[i]
```

---
## 리스트

1. 리스트 각 요소 빨리 바꾸기
```python
#1.
array = listmap(int, input().split()))
#2.활용
list(map(lambda x:'(' if x==')' else ')',p[1:i]))
```

2. 요소가 배열인 2차원 배열 선언
```python
1. graph = [[[]]*n for _ in range(n)] --> 이건 요소의 주소값이 복사되어서 갱신 되면 한 행이 다 갱신 되므로 주의!!! 나중에 요소값 초기화 할때 ex) graph[i][j] = [1,3]처럼 배열로 초기화 해야함
2. graph = [[[] for _ in range(n)] for _ in range(n)]
```

---
## 변수의 범위
- 파이썬은 **함수** 안에만 지역변수임 **while이나 for문**에서는 global변수쓰는거임
```python
x=2
while True: 

    #node, s, x, y = (1,1,1,1)
    x =1
    break

print(x)

a = 10  # 전역변수
def func(): 
    a = 20 # 지역변수 
    print(f"2. {a}") 
    return a + 100 # 여기서의 a는 바로위 지역변수 a

print(f"1. {a}") 
print(f"3. {func()}") # func() 함수가 호출되고 끝나면 func() 내부 지역변수가 살았다가 사라짐
```
- **리스트**는 global선언 없이 **함수** 안에서 접근 및 수정 등이 가능함
    - 어떤 deepcopy()처럼 전체를 **재할당** 할때에는 global선언 해줘야함

---
## 재귀함수
- 재귀함수 안에서 불필요한 연산하지말자! 만약 재귀함 수 밖에서 할 수 있다면 밖에서 하자 -> 시간초과 우려가 있다.

```python
# 불필요한 연산
def dfs(x,y,united):
    global people, country

    visited[x][y]=1
    united.append((x,y))

    people += graph[x][y]# ***
    country +=1# ***


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
            if l<=abs(graph[x][y]-graph[nx][ny])<=r:

                dfs(nx,ny,united)

# 권장
def dfs(x,y,united):

    visited[x][y]=1
    united.append((x,y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
            if l<=abs(graph[x][y]-graph[nx][ny])<=r:

                dfs(nx,ny,united)

```

---
## 배열 회전하기

- 시계방향 90도회전
```python

# 배열 전체
def right_rot90(a):#시계방향 90도 회전
    n = len(a) # 행
    m = len(a[0]) # 열
    new_a = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_a[j][n-1-i] = a[i][j]
    return new_a

# 배열 일부분 - 20058 참고
    temp = [[0]*(2**n) for _ in range(2**n)]
    k = 2**L # 회전할 배열 크기
    for i in range(0,2**n,k):
        for j in range(0,2**n,k):
            #회전규칙 적용
            for x in range(k):
                for y in range(k):
                    temp[i+y][j+k-1-x] = graph[i+x][j+y] # 회전 규칙 적용 + 평행이동
    graph = temp
```
- 반시계방향 90도 회전
```python
def left_rot90(a):#반시계방향 90도 회전
    n = len(a) # 행
    m = len(a[0]) # 열
    new_a = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_a[m-1-j][i] = a[i][j]
    return new_a
```

---
## max, min 값 초기화
1. 통상적으로 max = -1e9, min = 1e9 이렇게 잡는다.
    - 하지만 이 경우는 항상 max, min 값이 **변한다**는 가정이 있어야 한다.
2. 20058번 문제처럼 안 변하는 경우가 있다면 1번같이 하면 안된다.
    - 이 경우는 max는 **나올 수 있는** 최소의 값으로, min은 **나올 수 있는** 최대의 값으로 잡아줘야한다.
---
## List, Set, Dict 자료형에 따른 시간 복잡도!
### [Reference](https://2dowon.netlify.app/python/data-type-big-o/) 꼭 참고해라!