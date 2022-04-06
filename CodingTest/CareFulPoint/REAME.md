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