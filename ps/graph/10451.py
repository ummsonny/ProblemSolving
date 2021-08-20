import sys
sys.setrecursionlimit(10**6)#재귀가 깊으면 런타임 에러 발생함 ㅜㅜ https://www.acmicpc.net/help/rte/RecursionError
# ******방향 그래프는 2차원이 아니라 1차원으로 그릴 수 있다.!!!!!!!!!!****존나중요
def dfs(v):
    visit[v]=1
    w = graph[v]
    if visit[w]==0:
        dfs(w)
            
n = int(input())

for i in range(n):
    m = int(sys.stdin.readline())
    graph = [0]+list(map(int, sys.stdin.readline().split())) #inp.insert(0,0)하면 시간초과 난다.
    visit = [0]*(m+1)

    count=0

    for i in range(1,m+1):
        if not visit[i]:
            dfs(i)
            count+=1

    print(count)
