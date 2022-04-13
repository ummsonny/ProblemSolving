# Prac7

우선순위 1. 재귀함수 안에서 불필요한 연산하지말자! 만약 재귀함 수 밖에서 할 수 있다면 밖에서 하자 -> 시간초과 우려가 있다.
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

우선순위 2. 다시 안봐도 되는 불필요한 부분은 보지말자!!! --> 시간 감소 가능

```python

if len(united) > 1:
                result +=1
                #flag=True
                summary = 0
                for a,b in united:
                   summary+=graph[a][b]
                #united_people = people//country
                length = len(united)
                avg = summary//length
                for a,b in united:
                    graph[a][b] = avg #united_people

```
---

우선순위 3. for a,b in node:
```python
for node in united: # 쓰지마!
    graph[node[0]][node[1]] = avg

for a,b in united: # 권장
    graph[a][b] = avg
```

---

우선순위 4. 3번에서 result를 써도 안봐도 되는 부분은 안봐서 통과했는데 result도 '+'연산을 하기때문에 시간 잡아먹음 그래서 flag를 쓰면 더 괜춘

