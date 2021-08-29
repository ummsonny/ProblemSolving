import sys
from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs():
    global days 
    while(queue):
        q = queue.popleft()
        for i in range(4):
            ny = q[0]+dy[i]
            nx = q[1]+dx[i]

            if 0<=ny<h and 0<=nx<w and graph[ny][nx]==0: #조건문 위치가 중요하다 graph[ny][nx]가 처음에 있다면 out of index 에러 뜰 수도 있다.
                queue.append((ny,nx))
                graph[ny][nx]=graph[q[0]][q[1]]+1#**************bfs에서 깊이를 나타내는 방법!!!!!!!!!!!!!!!!!!!!!

w,h = map(int, sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
queue=deque()

for j in range(h):
    for i in range(w):
        if graph[j][i]==1:
            queue.append((j,i))

bfs()
maxCnt=0

for i in graph:
    if 0 in i:
        print(-1)
        exit(0) #자바나 C의 return 대신 파이썬은 exit(0)을 쓴다.
    if maxCnt<max(i):
        maxCnt=max(i)

print(maxCnt-1)
# for i in graph:
#     print(i)