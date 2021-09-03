#트리는 그래프이다. 
# 나의 궁금점 : 그럼 트리를 딕션너리로 구현할지, 그래프처럼 배열 혹은 연결리스트로 구현할지 기준이 뭐징?
# 내 생각 : 1991처럼 자식이 명시되어있으면 딕션너리, 여기 문제처럼 아니면 배열/연결리스트?
import sys
from collections import deque
read = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    while(queue):
        q = queue.popleft()
        for node in tree[q]:
            parent[node]=q
            queue.append(node)
            tree[node].remove(q) #visited써서 해도되지만 트리는 일반적인 그래프와 달리 bfs시에 다시 위로 갈일이 없기 때문에 가능한 코드. 또한 그래프를 다시 쓸일 없기 때문에 가능하다.
N = int(read())

tree=[[] for _ in range(N+1)]#그래프
parent=[0]*(N+1)#부모

for i in range(N-1):
    a,b = map(int,read().split())
    tree[a].append(b)
    tree[b].append(a)
bfs(1)
for i in parent[2:]:# 슬라이싱 꿀팁!
    print(i)


