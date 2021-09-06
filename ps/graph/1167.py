import sys
from collections import deque
read = sys.stdin.readline

V = int(read())
graph=[[] for i in range(V+1)]

for i in range(V):
    inp_list = list(map(int, read().split()[:-1]))
    length = len(inp_list)
    for i in range(1,length//2+1):
        graph[inp_list[0]].append([inp_list[2*i-1],inp_list[2*i]])# 원래 graph[inp_list[2*i-1]].append([inp_list[0],inp_list[2*i]])해줘야 할 것 같지만 
                                                                    #입력에서 다 처리 해주게 입력이 들어오므로 한 줄만 했다. 2 4 4/ 4 2 4 바바 어차피 해주자나

def bfs(start):
    visited = [-1]*(V+1)#방문여부 배열을 체크 및 거리 계산 2가지 용도로 동시에 쓸것이다.
    que = deque()
    que.append(start)
    visited[start]=0
    max_dis = [0,0]#0인덱스는 정점, 1은 거리 
    while(que):
        node = que.popleft()
        for e, w in graph[node]:#1차원 배열도 원소값만큼 이렇게 e,w따로 받을 수 있다.
            if visited[e]==-1:
                visited[e]=visited[node]+w
                que.append(e)
                if max_dis[1]<visited[e]:
                    max_dis = e, visited[e]
    return max_dis

ans1 = bfs(1)
ans2 = bfs(ans1[0])
print(ans2[1])
#1. 푸는 아이디어
#2. visited의 2가지 동시 활용성 --> 체크 및 거리계산
#3. 1차원 배열도 a,b=[2,3] 이런식으로 튜플처럼 한번에 a,b에 값 할당 가능