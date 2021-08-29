import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs():
    while(queue):
        q = queue.popleft()
        for i in range(4):
            ny = q[0]+dy[i]
            nx = q[1]+dx[i]
            if 0<=nx<w and 0<=ny<h and g[ny][nx]=='1':
                queue.append([ny,nx])
                g[ny][nx]=int(g[q[0]][q[1]])+1


read = sys.stdin.readline
h,w = map(int, read().split())
g=[list(read()) for _ in range(h)] #문자열 리스트로 바꾸어 줄때 그냥 list함수 쓰면됨 단, 마지막에 \n들어감 여기서 \n은 있어도되고 없어도 됨 어차피

queue = deque()
queue.append([0,0])
g[0][0]=1 #****방문한 곳을 정수형으로 만드는 것이 곧 방문했다는 의미이다.***** 13줄에서 어차미 문자 '1'를 검사하기때문이다.

bfs()

# for i in g:
#     print(i)
print(g[h-1][w-1])


