import sys
sys.setrecursionlimit(10**6) #재귀가 깊으면 런타임 에러 발생함 ㅜㅜ https://www.acmicpc.net/help/rte/RecursionError

#반드시 team의 마지막 학생은 team의 첫 학생을 지목해야한다는 것
# ******방향 그래프는 2차원이 아니라 1차원으로 그릴 수 있다.!!!!!!!!!!****존나중요
def dfs(v):
    global ans
    visit[v]=1
    traced.append(v)

    w = graph[v]
    if visit[w]==1:
        if w in traced:
            ans+=traced[traced.index(w):]
    else:
        dfs(w)


n = int(sys.stdin.readline())
for i in range(n):

    m = int(sys.stdin.readline())
    graph = [0]+list(map(int, sys.stdin.readline().split()))
    visit = [0]*(m+1)

    ans = [] #사이클에 속한 사람 담을 리스트

    for i in range(1,m+1):
        if visit[i]==0:
            traced = [] #탐색 경로 상의 학생 담을 리스트
            dfs(i)
    
    print(m-len(ans))



    