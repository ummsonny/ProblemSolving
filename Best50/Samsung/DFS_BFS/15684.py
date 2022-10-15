# import sys
# input = sys.stdin.readline
n,m,h = map(int, input().split())

graph = [[0]*n for _ in range(h)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1][b-1]=1

def check():

    for j in range(n):
        k = j
        for i in range(h):
            #왼쪽
            if graph[i][k]==1:
                k+=1
            elif k-1>=0 and graph[i][k-1]==1:
                k-=1
        if k!=j:
            return False
    return True

def dfs(sx,sy,cnt):
    global answer

    # 여기 위치는 시간초과 난다. dfs 즉, 스택에 함수가 쌓이는걸 최대한 줄여야한다(cnt>3부분). 그래서 밑으로 가야함
    # 또한 i번 출발이 i번으로 끝나는 경우가 cnt == 3 일때까지 "안되는 경우"가 "되는 경우"보다 많으므로
    # answer<=cnt보다 cnt>3에 걸리는 경우가 많다. 그래서 cnt>3고려해서 1개라도 함수가 더 들어가는 걸 막아야해서
    # 밑에 두줄 주석코드는 여기 말고 밑으로 가야한다.
    # if cnt > 3 or answer<=cnt:
    #     return

    if check():
        answer = min(answer, cnt)
        return

    if cnt == 3 or answer<=cnt:
        return

    for i in range(sx,h):
        sy = sy if i==sx else 0
        for j in range(sy,n-1):

            if graph[i][j]==0 and graph[i][j+1]==0:
                if j>0 and graph[i][j-1]==1:
                    continue
                graph[i][j] = 1
                dfs(sx,sy+2,cnt+1)
                graph[i][j] = 0


answer = 1e9
dfs(0,0,0)
if answer == 1e9:
    print(-1)
else:
    print(answer)



